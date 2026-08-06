import logging
import pickle
from functools import lru_cache
from pathlib import Path

logger = logging.getLogger(__name__)

BASE_DIR = Path("data") / "processed"

CHUNKS_PATH = BASE_DIR / "chunks.pkl"
BM25_PATH = BASE_DIR / "bm25.pkl"


def _load_pickle(path: Path):
    """
    Load a pickle file safely.
    """

    if not path.exists():
        raise FileNotFoundError(
            f"Required file not found: {path}"
        )

    try:
        with open(path, "rb") as file:
            return pickle.load(file)

    except Exception as exc:
        logger.exception(
            "Failed to load %s",
            path,
        )
        raise RuntimeError(
            f"Unable to load {path}"
        ) from exc


@lru_cache(maxsize=1)
def load_chunks():
    """
    Load document chunks once and cache them.
    """

    logger.info("Loading chunks...")

    chunks = _load_pickle(CHUNKS_PATH)

    logger.info(
        "Loaded %d chunks.",
        len(chunks),
    )

    return chunks


@lru_cache(maxsize=1)
def load_bm25():
    """
    Load BM25 index once and cache it.
    """

    logger.info("Loading BM25 index...")

    bm25 = _load_pickle(BM25_PATH)

    logger.info("BM25 index loaded successfully.")

    return bm25