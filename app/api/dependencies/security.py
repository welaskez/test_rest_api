from typing import Annotated

from core.auth.utils import api_key_header
from core.models import User
from fastapi import Depends, HTTPException, status
from services.user import UserService

from api.dependencies.services import get_user_service


async def validate_api_key(
    api_key: Annotated[str, Depends(api_key_header)],
    user_service: Annotated[UserService, Depends(get_user_service)],
) -> User:
    """
    Dependency check if api key exists
    :param api_key: api key
    :param user_service: user service dep
    :return: user
    """
    user = await user_service.get_by_api_key(api_key)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No one user have this api key!",
        )
    return user
