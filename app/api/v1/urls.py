from fastapi import APIRouter

from .endpoints.health import router as health_router
from .endpoints.parsing_session import router as parsing_session_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(parsing_session_router)
