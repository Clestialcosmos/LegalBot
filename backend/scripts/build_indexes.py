import logging
import pickle
from pathlib import Path

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.vector_store import create_vector_store
from app.rag.bm25 import BM25Retriever

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

PROCESSED_DIR = Path("data/processed")

PROCESSED_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

CHUNKS_PATH = PROCESSED_DIR / "chunks.pkl"
BM25_PATH = PROCESSED_DIR / "bm25.pkl"


def save_pickle(
    obj,
    path: Path,
):

    with open(
        path,
        "wb",
    ) as f:

        pickle.dump(
            obj,
            f,
        )


def build():

    logger.info(
        "Loading knowledge base..."
    )

    documents = load_documents()

    logger.info(
        "Loaded %d documents.",
        len(documents),
    )

    logger.info(
        "Splitting documents..."
    )

    chunks = split_documents(
        documents,
    )

    logger.info(
        "Created %d chunks.",
        len(chunks),
    )

    logger.info(
        "Saving chunks..."
    )

    save_pickle(
        chunks,
        CHUNKS_PATH,
    )

    logger.info(
        "Building BM25..."
    )

    bm25 = BM25Retriever(
        chunks,
    )

    save_pickle(
        bm25,
        BM25_PATH,
    )

    logger.info(
        "Building FAISS..."
    )

    create_vector_store(
        chunks,
    )

    logger.info(
        "================================="
    )

    logger.info(
        "Knowledge Base Built Successfully."
    )

    logger.info(
        "Chunks : %d",
        len(chunks),
    )

    logger.info(
        "================================="
    )


if __name__ == "__main__":

    build()