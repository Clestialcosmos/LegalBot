from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.chat import router as chat_router

# Main API Router
api_router = APIRouter()

# Health Check Routes
api_router.include_router(
    health_router,
)

# Chat API Routes
api_router.include_router(
    chat_router,
)