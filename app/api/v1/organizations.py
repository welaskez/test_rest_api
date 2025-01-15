from typing import Annotated
from uuid import UUID

from core.auth.utils import validate_jwt_token
from core.schemas.organization import OrganizationFiltersQueryParams, OrganizationRead
from fastapi import APIRouter, Depends, Path, Query, status
from services.organization import OrganizationService

from api.dependencies.services import get_organization_service

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
    dependencies=[Depends(validate_jwt_token)],
)


@router.get(
    path="/search/name",
    status_code=status.HTTP_200_OK,
    response_model=OrganizationRead,
)
async def get_organization_by_name(
    organization_service: Annotated[
        OrganizationService, Depends(get_organization_service)
    ],
    organization_name: Annotated[
        str,
        Query(description="Name of organization"),
    ],
):
    """Return organization by name"""
    return await organization_service.get_organization_by_name(organization_name)


@router.get(
    path="/search/location",
    status_code=status.HTTP_200_OK,
    response_model=list[OrganizationRead],
)
async def get_organizations_by_location(
    organization_service: Annotated[
        OrganizationService, Depends(get_organization_service)
    ],
    filters: Annotated[OrganizationFiltersQueryParams, Query()],
):
    """
    Returns the list of organizations located in the specified
    radius/rectangular space:
    - center_latitude, center_longitude, radius: Filter organizations within
    a circular area.
    - min_latitude, max_latitude, min_longitude, max_longitude: Filter
    organizations within a rectangular area.
    """
    return await organization_service.get_filtered_organizations(filters)


@router.get(
    path="/{organization_id}",
    status_code=status.HTTP_200_OK,
    response_model=OrganizationRead,
)
async def get_organization_by_id(
    organization_service: Annotated[
        OrganizationService, Depends(get_organization_service)
    ],
    organization_id: Annotated[
        UUID,
        Path(description="ID of organization"),
    ],
):
    """Return organization by ID"""
    return await organization_service.get_organization_by_id(organization_id)
