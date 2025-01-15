from core.models import Activity
from crud.activity import ActivityCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class ActivityService(BaseService[Activity]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, ActivityCRUD)
        self.crud: ActivityCRUD = self.crud
