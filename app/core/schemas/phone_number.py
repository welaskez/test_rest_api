from uuid import UUID

from pydantic import BaseModel


class PhoneNumberCreate(BaseModel):
    number: str
    organization_id: UUID


class PhoneNumberUpdate(BaseModel):
    number: str | None = None
    organization_id: UUID | None = None


class PhoneRead(BaseModel):
    number: str
