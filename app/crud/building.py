from uuid import UUID

from core.models import Activity, Building, Organization
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from crud.base import BaseCRUD


class BuildingCRUD(BaseCRUD[Building]):
    model = Building

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_organizations_by_building(
        self, building_id: UUID
    ) -> list[Organization]:
        """
        Return organizations by building
        :param building_id: building ID
        :return: list of organizations
        """
        building = await self.session.scalar(
            select(Building)
            .options(
                selectinload(Building.organizations).selectinload(
                    Organization.building
                ),
                selectinload(Building.organizations)
                .selectinload(Organization.activity)
                .selectinload(Activity.childrens, recursion_depth=3),
                selectinload(Building.organizations).selectinload(
                    Organization.phone_numbers
                ),
            )
            .where(Building.id == building_id)
        )

        return building.organizations
