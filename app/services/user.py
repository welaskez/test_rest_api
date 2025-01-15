from core.models import User
from core.schemas.user import UserRead
from crud.user import UserCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class UserService(BaseService[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, UserCRUD)
        self.crud: UserCRUD = self.crud


def serialize_phone(user: User) -> UserRead:
    """
    Serialize SQLA model to pydantic schema
    :param user: SQLA model of user
    :return: user read pydantic schema
    """
    return UserRead(username=user.username)
