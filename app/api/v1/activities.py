from typing import Annotated
from uuid import UUID

from core.auth.utils import validate_jwt_token
from core.schemas.organization import OrganizationRead
from fastapi import APIRouter, Depends, Path, status
from services.activity import ActivityService

from api.dependencies.services import get_activity_service

router = APIRouter(
    prefix="/activities",
    tags=["Activities"],
    dependencies=[Depends(validate_jwt_token)],
)


@router.get(
    path="/{activity_id}/organizations",
    status_code=status.HTTP_200_OK,
    response_model=list[OrganizationRead],
)
async def get_organizations_by_activity(
    activity_service: Annotated[ActivityService, Depends(get_activity_service)],
    activity_id: Annotated[UUID, Path(description="ID of activity")],
):
    """Return organizations by activity"""
    return await activity_service.get_organizations_by_activity(activity_id)
