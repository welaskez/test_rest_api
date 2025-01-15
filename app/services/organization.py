from uuid import UUID

from core.models import Organization
from core.schemas.organization import OrganizationFiltersQueryParams, OrganizationRead
from crud.organization import OrganizationCRUD
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from services.activity import serialize_activity

from .base import BaseService
from .building import serialize_building
from .phone import serialize_phone


class OrganizationService(BaseService[Organization]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, OrganizationCRUD)
        self.crud: OrganizationCRUD = self.crud

    async def get_organization_by_name(self, name: str) -> OrganizationRead:
        """
        Getting organization by name
        :param name: org name
        :return: organization read schema or http exception
        """
        organization = await self.crud.get_loaded_organization_by_expression(
            Organization.name == name
        )

        if organization:
            return serialize_organization(organization)

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
        )

    async def get_organization_by_id(
        self, organization_id: UUID | str
    ) -> OrganizationRead:
        """
        Getting organization by id
        :param organization_id: org id
        :return: organization read schema or http exception
        """
        organization = await self.crud.get_loaded_organization_by_expression(
            Organization.id == organization_id
        )
        if organization:
            return serialize_organization(organization)

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
        )

    async def get_filtered_organizations(
        self, filters: OrganizationFiltersQueryParams
    ) -> list[OrganizationRead]:
        """
        Getting organizations by rect area or circular area
        :param filters: filters
        :return: list of organizations
        """
        organizations = []

        if filters.center_latitude and filters.center_longitude and filters.radius:
            organizations = await self.crud.get_organizations_in_circular_area(
                filters.center_latitude,
                filters.center_longitude,
                filters.radius,
            )

        if (
            filters.min_latitude
            and filters.max_latitude
            and filters.min_longitude
            and filters.max_longitude
        ):
            organizations = await self.crud.get_organizations_in_rect_area(
                filters.min_latitude,
                filters.max_latitude,
                filters.min_longitude,
                filters.max_longitude,
            )

        if organizations:
            return [
                serialize_organization(organization) for organization in organizations
            ]

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No organizations found for this filter!",
        )


def serialize_organization(organization: Organization) -> OrganizationRead:
    """
    Serialize SQLA model to pydantic schema
    :param organization: SQLA model of organization
    :return: organization read pydantic schema
    """
    return OrganizationRead(
        name=organization.name,
        building=serialize_building(organization.building),
        activity=serialize_activity(organization.activity),
        phone_numbers=[serialize_phone(phone) for phone in organization.phone_numbers],
    )
