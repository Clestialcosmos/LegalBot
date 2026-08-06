from fastapi import APIRouter

router = APIRouter(tags=["Chat"])

@router.post("/chat")
async def chat_endpoint():
    return {
        "success": True,
        "message": "Endpoint working",
        "data": {
            "answer": "Hello from LegalBot"
        }
    }