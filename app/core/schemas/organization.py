from uuid import UUID

from pydantic import BaseModel

from .activity import ActivityRead
from .building import BuildingRead


class OrganizationCreate(BaseModel):
    name: str
    building_id: str | UUID
    activity_id: str | UUID


class OrganizationUpdate(BaseModel):
    name: str | None = None
    building_id: str | UUID | None = None
    activity_id: str | UUID | None = None


class OrganizationRead(BaseModel):
    name: str
    building: BuildingRead
    activity: ActivityRead
