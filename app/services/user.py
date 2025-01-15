from core.auth.jwt import encode_jwt
from core.auth.utils import hash_password, validate_password
from core.models import User
from core.schemas.auth import TokenRead
from core.schemas.user import UserCreate, UserUpdate
from crud.user import UserCRUD
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class UserService(BaseService[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, UserCRUD)
        self.crud: UserCRUD = self.crud

    async def auth(self, form_data: OAuth2PasswordRequestForm) -> TokenRead:
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

        access_token = encode_jwt(payload={"sub": form_data.username})

        await self.crud.create(
            UserCreate(
                username=form_data.username,
                password=password.decode(),
                api_key=access_token,
            )
        )

        return TokenRead(access=access_token)

    async def refresh(self, form_data: OAuth2PasswordRequestForm) -> TokenRead:
        """
        refresh token for existing user
        :param form_data: form_data
        :return: token
        """
        user = await self.crud.get_one_by_expression(
            User.username == form_data.username
        )

        if user:
            try:
                validate_password(
                    password=form_data.password,
                    hashed_password=user.password.encode(),
                )
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Username or password invalid!",
                )

            access_token = encode_jwt(payload={"sub": form_data.username})

            await self.crud.update(user, UserUpdate(api_key=access_token))

            return TokenRead(access=access_token)

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not exists",
        )
