from core.models import Activity
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from crud.base import BaseCRUD


class ActivityCRUD(BaseCRUD[Activity]):
    model = Activity

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_loaded_activities(self) -> list[Activity]:
        activities = await self.session.scalars(
            select(Activity).options(
                selectinload(Activity.childrens, recursion_depth=3)
            )
        )
        return list(activities)
