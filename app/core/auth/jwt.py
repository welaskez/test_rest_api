from datetime import datetime, timedelta, timezone

import jwt

from core.config import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.jwt.private_key_path.read_text(),
    algorithm: str = settings.jwt.algorithm,
    expire_minutes: int = settings.jwt.access_token_expire_minutes,
) -> str:
    to_encode = payload.copy()
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(exp=expire, iat=now)
    return jwt.encode(payload=to_encode, key=private_key, algorithm=algorithm)


def decode_jwt(
    token: str,
    public_key: str = settings.jwt.public_key_path.read_text(),
    algorithm: str = settings.jwt.algorithm,
):
    return jwt.decode(jwt=token, key=public_key, algorithms=[algorithm])
