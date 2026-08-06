import logging
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from app.rag.embeddings import get_embedding_model

logger = logging.getLogger(__name__)

DEFAULT_SAVE_PATH = Path("data/vector_db")


def create_vector_store(
    documents: list[Document],
    save_path: Path = DEFAULT_SAVE_PATH,
):
    """
    Create and save the FAISS vector database.
    """

    if not documents:

        raise ValueError(
            "No documents provided for vector database creation."
        )

    logger.info(
        "Loading embedding model..."
    )

    embeddings = get_embedding_model()

    logger.info(
        "Creating FAISS vector store from %d documents...",
        len(documents),
    )

    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embeddings,
    )

    save_path.mkdir(
        parents=True,
        exist_ok=True,
    )

    vector_store.save_local(
        str(save_path)
    )

    logger.info(
        "Vector database saved to %s",
        save_path,
    )

    return vector_store