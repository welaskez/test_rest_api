import secrets

import bcrypt
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="token")


def generate_static_token(length: int = 32) -> str:
    return secrets.token_urlsafe(length)


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password)
