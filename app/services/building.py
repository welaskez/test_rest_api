from core.models import Building
from core.schemas.building import BuildingRead
from crud.building import BuildingCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class BuildingService(BaseService[Building]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, BuildingCRUD)
        self.crud: BuildingCRUD = self.crud

    async def get_all_buildings(self) -> list[BuildingRead]:
        """
        Getting all buildings
        :return: list of building read pydantic schemas
        """
        return [
            BuildingRead.model_validate(building)
            for building in await self.crud.get_all()
        ]
