from functools import lru_cache
import logging
import re
from langchain_community.vectorstores import FAISS

from app.rag.embeddings import get_embedding_model
from app.rag.query_processor import processor
from app.rag.domain_router import router

logger = logging.getLogger(__name__)

DEFAULT_DB_PATH = "data/vector_db"


@lru_cache(maxsize=1)
def load_vector_store(path: str = DEFAULT_DB_PATH):
    """
    Load the FAISS vector database only once and cache it.
    """

    logger.info("Loading FAISS vector database...")

    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        folder_path=path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True,
    )

    logger.info("FAISS vector database loaded successfully.")

    return vector_store


def retrieve_documents(
    query: str,
    k: int = 5,
    fetch_k: int = 20,
):
    """
    Retrieve relevant documents using query preprocessing,
    domain detection and MMR search.
    """

    if not query or not query.strip():
        return []

    # -------------------------
    # Query Processing
    # -------------------------

    processed_query = processor.process(query)

    detected_domain = router.detect(processed_query)

    logger.info("Original Query : %s", query)
    logger.info("Processed Query: %s", processed_query)
    logger.info("Detected Domain: %s", detected_domain)

    vector_store = load_vector_store()

    try:

        if re.search(r"(article|section)\s+\d+[a-zA-Z]*", processed_query.lower()):

            logger.info("Legal reference detected → Using similarity search")

            documents = vector_store.similarity_search(
                query=processed_query,
                k=fetch_k,
            )

        else:

            documents = vector_store.max_marginal_relevance_search(
                query=processed_query,
                k=fetch_k,
                fetch_k=max(fetch_k * 2, 20),
            )

        # -------------------------
        # Domain Filtering
        # -------------------------

        if detected_domain != "general":

            filtered = []

            for doc in documents:

                metadata = doc.metadata or {}

                domain = str(
                    metadata.get("domain", "")
                ).lower()

                if domain == detected_domain:
                    filtered.append(doc)

            if filtered:
                documents = filtered

        return documents[:k]

    except Exception as exc:

        logger.exception("MMR retrieval failed: %s", exc)

        try:

            logger.warning(
                "Falling back to similarity search..."
            )

            return vector_store.similarity_search(
                query=processed_query,
                k=k,
            )

        except Exception as inner_exc:

            logger.exception(
                "Similarity search also failed: %s",
                inner_exc,
            )

            return []