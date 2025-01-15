from uuid import UUID

from pydantic import BaseModel


class ActivityCreate(BaseModel):
    name: str
    parent_id: UUID | str | None


class ActivityRead(BaseModel):
    name: str
    parent: "ActivityRead"
    childrens: list["ActivityRead"]


class ActivityUpdate(BaseModel):
    name: str | None = None
    parent_id: UUID | str | None = None
