from pydantic import BaseModel


class TokenInfo(BaseModel):
    sub: str
    exp: int
    iat: int


class TokenRead(BaseModel):
    access: str
