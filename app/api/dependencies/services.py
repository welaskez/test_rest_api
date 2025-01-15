from typing import Annotated

from core.models import db_helper
from fastapi import Depends
from services.building import BuildingService
from sqlalchemy.ext.asyncio import AsyncSession


def get_building_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> BuildingService:
    return BuildingService(session)
