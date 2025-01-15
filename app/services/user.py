from core.auth.utils import generate_static_token, hash_password, validate_password
from core.models import User
from core.schemas.auth import ApiKeyResponse
from core.schemas.user import UserCreate
from crud.user import UserCRUD
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class UserService(BaseService[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, UserCRUD)
        self.crud: UserCRUD = self.crud

    async def get_by_api_key(self, api_key: str) -> User | None:
        """
        Return user by api key
        :param api_key: api key
        :return: user or none
        """
        return await self.crud.get_one_by_expression(User.api_key == api_key)

    async def register(self, form_data: OAuth2PasswordRequestForm) -> ApiKeyResponse:
        """
        authenticate new user, add him to db & return access token
        :param form_data: form data
        :return: token
        """
        user = await self.crud.get_one_by_expression(
            User.username == form_data.username
        )
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists",
            )

        password = hash_password(form_data.password)

        api_key = generate_static_token()

        await self.crud.create(
            UserCreate(
                username=form_data.username,
                password=password.decode(),
                api_key=api_key,
            )
        )

        return ApiKeyResponse(api_key=api_key)

    async def login(self, form_data: OAuth2PasswordRequestForm) -> ApiKeyResponse:
        """
        refresh token for existing user
        :param form_data: form_data
        :return: token
        """
        user = await self.crud.get_one_by_expression(
            User.username == form_data.username
        )

        invalid_passwd_exc = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password invalid!",
        )

        if user:
            try:
                is_valid = validate_password(
                    password=form_data.password,
                    hashed_password=user.password.encode(),
                )
            except ValueError:
                raise invalid_passwd_exc

            if not is_valid:
                raise invalid_passwd_exc

            return ApiKeyResponse(api_key=user.api_key)

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not exists",
        )
