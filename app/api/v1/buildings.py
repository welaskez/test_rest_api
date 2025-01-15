from typing import Annotated
from uuid import UUID

from core.schemas.organization import OrganizationRead
from fastapi import APIRouter, Depends, Path, status
from services.building import BuildingService

from api.dependencies.security import validate_api_key
from api.dependencies.services import get_building_service

router = APIRouter(
    prefix="/buildings",
    tags=["Buildings"],
    dependencies=[Depends(validate_api_key)],
)


@router.get(
    path="/{building_id}/organizations",
    status_code=status.HTTP_200_OK,
    response_model=list[OrganizationRead],
)
async def get_organizations_in_building(
    building_service: Annotated[BuildingService, Depends(get_building_service)],
    building_id: Annotated[UUID, Path(description="ID of building")],
):
    """Return organizations in building by building id"""
    return await building_service.get_organizations_by_building_id(building_id)
