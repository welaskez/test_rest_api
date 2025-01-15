from core.models import Phone
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD


class PhoneCRUD(BaseCRUD[Phone]):
    model = Phone

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
