from core.models import Building
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD


class BuildingCRUD(BaseCRUD[Building]):
    model = Building

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
