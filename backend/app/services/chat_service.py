import logging

logger = logging.getLogger(__name__)


def chat(message: str):

    logger.info("CHAT SERVICE HIT")

    return {
        "answer": "Chat service working",
        "documents": [],
        "sources": [],
        "language": "en",
        "original_query": message,
    }