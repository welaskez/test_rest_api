from typing import Annotated

import bcrypt
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from jwt import DecodeError, ExpiredSignatureError
from pydantic import ValidationError

from core.auth.jwt import decode_jwt
from core.schemas.auth import TokenInfo

api_key_header = APIKeyHeader(name="token")


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password)


def validate_jwt_token(token: Annotated[str, Depends(api_key_header)]) -> TokenInfo:
    invalid_token_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Token is Invalid!",
    )
    try:
        token_info = TokenInfo.model_validate(decode_jwt(token=token))
    except ValidationError:
        raise invalid_token_exception
    except DecodeError:
        raise invalid_token_exception
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token is expired!",
        )

    return token_info
