from uuid import UUID

from core.models import Building
from core.schemas.building import BuildingRead
from core.schemas.organization import OrganizationRead
from crud.building import BuildingCRUD
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class BuildingService(BaseService[Building]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, BuildingCRUD)
        self.crud: BuildingCRUD = self.crud

    async def get_organizations_by_building_id(
        self, building_id: UUID
    ) -> list[OrganizationRead]:
        """
        Getting organizations in building
        :param building_id: building ID
        :return: list of organizations
        """
        from .organization import serialize_organization

        organizations = await self.crud.get_organizations_by_building(building_id)

        if organizations:
            return [
                serialize_organization(organization) for organization in organizations
            ]

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No organizations in this building!",
        )


def serialize_building(building: Building) -> BuildingRead:
    """
    Serialize SQLA model to pydantic schema
    :param building: SQLA model of building
    :return: building read pydantic schema
    """
    return BuildingRead.model_validate(building)
