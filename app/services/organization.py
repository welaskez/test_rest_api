from uuid import UUID

from core.models import Organization
from core.schemas.organization import OrganizationRead
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
        self,
        center_latitude: float | None = None,
        center_longitude: float | None = None,
        radius: float | None = None,
        min_latitude: float | None = None,
        max_latitude: float | None = None,
        min_longitude: float | None = None,
        max_longitude: float | None = None,
    ) -> list[OrganizationRead]:
        """
        Getting organizations by rect area or circular area
        :param center_latitude: central latitude (for circular area)
        :param center_longitude: central longitude (for circular area)
        :param radius: radius (for circular area)
        :param min_latitude: minimal latitude (for rect area)
        :param max_latitude: maximal latitude (for rect area)
        :param min_longitude: minimal longitude (for rect area)
        :param max_longitude: maximal longitude (for rect area)
        :return: list of organizations
        """
        organizations = []

        if center_latitude and center_longitude and radius:
            organizations = await self.crud.get_organizations_in_circular_area(
                center_latitude,
                center_longitude,
                radius,
            )

        if min_latitude and max_latitude and min_longitude and max_longitude:
            organizations = await self.crud.get_organizations_in_rect_area(
                min_latitude,
                max_latitude,
                min_longitude,
                max_longitude,
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
