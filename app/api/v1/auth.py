from typing import Annotated

from core.schemas.auth import TokenRead
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from services.user import UserService

from api.dependencies.services import get_user_service

router = APIRouter(prefix="/auth", tags=["Authentication"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")


@router.post(
    path="/",
    response_model=TokenRead,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    user_service: Annotated[UserService, Depends(get_user_service)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    """Register user, add him to db & return access token"""
    return await user_service.auth(form_data)


@router.post(
    path="/refresh",
    response_model=TokenRead,
    status_code=status.HTTP_201_CREATED,
)
async def refresh_token(
    user_service: Annotated[UserService, Depends(get_user_service)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    """Refresh user access token"""
    return await user_service.refresh(form_data)
