from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    api_key: str


class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    api_key: str | None = None


class UserRead(BaseModel):
    username: str
