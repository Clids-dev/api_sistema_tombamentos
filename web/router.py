from fastapi import APIRouter
from .auth import router as auth_router
from .dashboard import router as dashboard_router
from .assets_view import router as assets_router

web_router = APIRouter()

web_router.include_router(auth_router)
web_router.include_router(dashboard_router)
web_router.include_router(assets_router)
