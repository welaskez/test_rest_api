from core.models import Activity
from core.schemas.activity import ActivityRead
from crud.activity import ActivityCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class ActivityService(BaseService[Activity]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, ActivityCRUD)
        self.crud: ActivityCRUD = self.crud

    async def get_all_activities(self) -> list[ActivityRead]:
        """
        Getting all activities
        :return: list of activity read pydantic schemas
        """
        return [
            serialize_activity(activity)
            for activity in await self.crud.get_loaded_activities()
        ]


def serialize_activity(activity: Activity) -> ActivityRead | None:
    """
    Serialize activity SQLA model to pydantic schema
    :param activity: SQLA model
    :return: activity read pydantic schema
    """
    if not activity:
        return None

    return ActivityRead(
        name=activity.name,
        parent_id=activity.parent_id,
        childrens=[
            serialize_activity(child)
            for child in activity.childrens
            if serialize_activity(child) is not None
        ],
    )
