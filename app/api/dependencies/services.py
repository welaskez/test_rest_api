from typing import Annotated

from core.models import db_helper
from fastapi import Depends
from services.activity import ActivityService
from services.building import BuildingService
from sqlalchemy.ext.asyncio import AsyncSession


def get_building_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> BuildingService:
    return BuildingService(session)


def get_activity_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> ActivityService:
    return ActivityService(session)
