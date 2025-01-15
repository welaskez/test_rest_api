from core.models import Phone
from crud.phone import PhoneCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class PhoneService(BaseService[Phone]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, PhoneCRUD)
        self.crud: PhoneCRUD = self.crud
