from uuid import UUID

from core.models import Organization
from core.schemas.building import BuildingRead
from core.schemas.organization import OrganizationFiltersQueryParams, OrganizationRead
from core.schemas.phone_number import PhoneRead
from crud.organization import OrganizationCRUD
from fastapi import HTTPException, status
from sqlalchemy import ColumnExpressionArgument
from sqlalchemy.ext.asyncio import AsyncSession

from services.activity import serialize_activity

from .base import BaseService


class OrganizationService(BaseService[Organization]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, OrganizationCRUD)
        self.crud: OrganizationCRUD = self.crud

    async def _get_organization_by_expression(
        self, expression: ColumnExpressionArgument, many: bool = False
    ) -> OrganizationRead | list[OrganizationRead]:
        """
        Getting organization by expression with business logic
        :param expression: 'where' expression
        :param many: if true return list of organizations else one org
        :return: organization read pydantic schema or http exception
        """
        organization = await self.crud.get_loaded_organizations_by_expression(
            expression, many
        )
        if organization:
            if many:
                return [serialize_organization(org) for org in organization]
            else:
                return serialize_organization(organization)

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
        )

    async def get_organizations_by_building_id(
        self, building_id: UUID
    ) -> list[OrganizationRead]:
        """
        Getting organizations by building
        :param building_id: building id
        :return: organization read schema or http exception
        """
        return await self._get_organization_by_expression(
            Organization.building_id == building_id, many=True
        )

    async def get_organizations_by_activity_id(
        self, activity_id: UUID
    ) -> list[OrganizationRead]:
        """
        Getting organizations by activity
        :param activity_id: activity id
        :return: organization read schema or http exception
        """
        return await self._get_organization_by_expression(
            Organization.activity_id == activity_id, many=True
        )

    async def get_organization_by_name(self, name: str) -> OrganizationRead:
        """
        Getting organization by name
        :param name: org name
        :return: organization read schema or http exception
        """
        return await self._get_organization_by_expression(Organization.name == name)

    async def get_organization_by_id(
        self, organization_id: UUID | str
    ) -> OrganizationRead:
        """
        Getting organization by id
        :param organization_id: org id
        :return: organization read schema or http exception
        """
        return await self._get_organization_by_expression(
            Organization.id == organization_id
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

        if filters.building_id:
            organizations = await self.get_organizations_by_building_id(
                filters.building_id
            )

        if filters.activity_id:
            organizations = await self.get_organizations_by_activity_id(
                filters.activity_id
            )

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
        building=BuildingRead.model_validate(organization.building),
        activity=serialize_activity(organization.activity),
        phone_numbers=[
            PhoneRead(number=phone.number) for phone in organization.phone_numbers
        ],
    )
