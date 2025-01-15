__all__ = ("router",)

from fastapi import APIRouter

from .activities import router as activities_router
from .buildings import router as buildings_router

router = APIRouter(prefix="/v1")
router.include_router(buildings_router)
router.include_router(activities_router)
