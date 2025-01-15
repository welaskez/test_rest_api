from core.models import Building
from crud.building import BuildingCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class BuildingService(BaseService[Building]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, BuildingCRUD)
        self.crud: BuildingCRUD = self.crud
