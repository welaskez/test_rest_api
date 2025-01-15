from uuid import UUID

from core.models import Activity, Organization
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from crud.base import BaseCRUD


class ActivityCRUD(BaseCRUD[Activity]):
    model = Activity

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_organizations_by_activity(
        self, activity_id: UUID
    ) -> list[Organization]:
        """
        Return organizations by activity
        :param activity_id: activity ID
        :return: list of organizations
        """
        activity = await self.session.scalar(
            select(Activity)
            .options(
                selectinload(Activity.organizations).selectinload(
                    Organization.building
                ),
                selectinload(Activity.organizations)
                .selectinload(Organization.activity)
                .selectinload(Activity.childrens, recursion_depth=3),
                selectinload(Activity.organizations).selectinload(
                    Organization.phone_numbers
                ),
            )
            .where(Activity.id == activity_id)
        )

        return activity.organizations
