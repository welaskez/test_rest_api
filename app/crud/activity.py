from core.models import Activity
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD


class ActivityCRUD(BaseCRUD[Activity]):
    model = Activity

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
