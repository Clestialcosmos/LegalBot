from fastapi import APIRouter

from app.schemas.response import APIResponse

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    response_model=APIResponse
)
async def health():
    return APIResponse(
        success=True,
        message="Server is healthy",
        data={
            "service": "LegalBot",
            "version": "1.0.0"
        }
    )