from uuid import UUID

from core.models import Activity
from core.schemas.activity import ActivityRead
from core.schemas.organization import OrganizationRead
from crud.activity import ActivityCRUD
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class ActivityService(BaseService[Activity]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, ActivityCRUD)
        self.crud: ActivityCRUD = self.crud

    async def get_organizations_by_activity(
        self, activity_id: UUID
    ) -> list[OrganizationRead]:
        """
        Getting organizations in activity
        :param activity_id: activity ID
        :return: list of organizations
        """
        from .organization import serialize_organization

        organizations = await self.crud.get_organizations_by_activity(activity_id)

        if organizations:
            return [
                serialize_organization(organization) for organization in organizations
            ]

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No organizations in this building!",
        )


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
        parent=activity.parent_id,
        childrens=[
            serialize_activity(child)
            for child in activity.childrens
            if serialize_activity(child) is not None
        ],
    )
