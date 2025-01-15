from uuid import UUID

from pydantic import BaseModel, Field

from .activity import ActivityRead
from .building import BuildingRead
from .phone_number import PhoneRead


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
    phone_numbers: list[PhoneRead]


class OrganizationFiltersQueryParams(BaseModel):
    center_latitude: float | None = Field(
        description="Latitude of the center for radius search", default=None
    )
    center_longitude: float | None = Field(
        description="Longitude of the center for radius search", default=None
    )
    radius: float | None = Field(
        description="Radius (in kilometers) for search around the center", default=None
    )
    min_latitude: float | None = Field(
        description="Minimum latitude for rectangular search", default=None
    )
    max_latitude: float | None = Field(
        description="Maximum latitude for rectangular search", default=None
    )
    min_longitude: float | None = Field(
        description="Minimum longitude for rectangular search", default=None
    )
    max_longitude: float | None = Field(
        description="Maximum longitude for rectangular search", default=None
    )
