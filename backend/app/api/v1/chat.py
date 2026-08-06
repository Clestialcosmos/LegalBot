import logging

from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest
from app.schemas.response import APIResponse
from app.services.chat_service import chat

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

    try:

        result = chat(request.message)

        return APIResponse(
            success=True,
            message="Response generated successfully",
            data={
                "answer": result.get("answer", ""),
                "sources": result.get("sources", []),
                "language": result.get("language", "en"),
            },
        )

    except Exception as exc:

        logger.exception(exc)

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )