import logging

from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.schemas.response import APIResponse

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="",
    tags=["Chat"],
)


@router.post(
    "/chat",
    response_model=APIResponse,
)
async def chat_endpoint(
    request: ChatRequest,
):

    logger.info("==== CHAT ENDPOINT HIT ====")

    logger.info("Message: %s", request.message)

    # Temporary static response
    result = {
        "answer": "Chat service bypass successful",
        "sources": [],
        "language": "en",
    }

    return APIResponse(
        success=True,
        message="Response generated successfully",
        data={
            "answer": result["answer"],
            "sources": result["sources"],
            "language": result["language"],
        },
    )