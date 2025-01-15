from core.models import User
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD


class UserCRUD(BaseCRUD[User]):
    model = User

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
