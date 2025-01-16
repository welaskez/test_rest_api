from typing import Annotated

from core.schemas.activity import ActivityRead
from fastapi import APIRouter, Depends, status
from services.activity import ActivityService

from api.dependencies.security import validate_api_key
from api.dependencies.services import get_activity_service

router = APIRouter(
    prefix="/activities",
    tags=["Activities"],
    dependencies=[Depends(validate_api_key)],
)


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=list[ActivityRead],
)
async def get_activities(
    activity_service: Annotated[ActivityService, Depends(get_activity_service)],
):
    """Return all activities"""
    return await activity_service.get_all_activities()
