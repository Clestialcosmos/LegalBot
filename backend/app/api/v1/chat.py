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
    """
    Main LegalBot Chat Endpoint.
    """

    try:

        result = chat(request.message)

        sources = []

        if "sources" in result:

            sources = result["sources"]

        elif "documents" in result:

            seen = set()

            for doc in result["documents"]:

                source = {
                    "source": doc.metadata.get(
                        "source",
                        "Unknown Document",
                    ),
                    "page": doc.metadata.get(
                        "page",
                        "-",
                    ),
                }

                key = (
                    source["source"],
                    source["page"],
                )

                if key not in seen:
                    seen.add(key)
                    sources.append(source)

        return APIResponse(
            success=True,
            message="Response generated successfully",
            data={
                "answer": result.get("answer", ""),
                "sources": sources,
                "language": result.get(
                    "language",
                    "en",
                ),
            },
        )

    except Exception as exc:

        logger.exception(
            "Chat endpoint failed: %s",
            exc,
        )

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error",
        )