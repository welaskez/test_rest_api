from pydantic import BaseModel, ConfigDict


class BuildingCreate(BaseModel):
    county: str
    region: str
    city: str
    district: str | None = None
    micro_district_or_street: str
    number: str
    postal_code: int
    latitude: float
    longitude: float


class BuildingRead(BuildingCreate):
    model_config = ConfigDict(from_attributes=True)


class BuildingUpdate(BaseModel):
    county: str | None = None
    region: str | None = None
    city: str | None = None
    district: str | None = None
    micro_district_or_street: str | None = None
    number: str | None = None
    postal_code: int | None = None
    latitude: float | None = None
    longitude: float | None = None
