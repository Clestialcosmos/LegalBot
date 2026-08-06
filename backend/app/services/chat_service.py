import logging

from app.services.rag_service import RAGService

logger = logging.getLogger(__name__)

# Lazy initialization
rag_service = None


def get_rag_service():
    global rag_service

    if rag_service is None:
        logger.info("Creating RAG Service...")
        rag_service = RAGService()

    return rag_service


def chat(message: str):
    """
    Main chat service.
    """

    try:

        if not message or not message.strip():

            return {
                "answer": "Please enter a legal question.",
                "documents": [],
                "sources": [],
                "language": "en",
                "original_query": "",
            }

        logger.info("Received query: %s", message)

        response = get_rag_service().ask(message.strip())

        logger.info("Response generated successfully.")

        return response

    except Exception as exc:

        logger.exception("Chat Service Error: %s", exc)

        return {
            "answer": (
                "Something went wrong while processing your request. "
                "Please try again."
            ),
            "documents": [],
            "sources": [],
            "language": "en",
            "original_query": message,
        }