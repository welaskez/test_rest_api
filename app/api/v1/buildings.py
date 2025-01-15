from typing import Annotated

from core.schemas.building import BuildingRead
from fastapi import APIRouter, Depends, status
from services.building import BuildingService

from api.dependencies.security import validate_api_key
from api.dependencies.services import get_building_service

router = APIRouter(
    prefix="/buildings",
    tags=["Buildings"],
    dependencies=[Depends(validate_api_key)],
)


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=list[BuildingRead],
)
async def get_buildings(
    building_service: Annotated[BuildingService, Depends(get_building_service)],
):
    """Return all building"""
    return await building_service.get_all_buildings()
