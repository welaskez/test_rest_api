from core.models import Phone
from core.schemas.phone_number import PhoneRead
from crud.phone import PhoneCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class PhoneService(BaseService[Phone]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, PhoneCRUD)
        self.crud: PhoneCRUD = self.crud


def serialize_phone(phone: Phone) -> PhoneRead:
    """
    Serialize SQLA model to pydantic schema
    :param phone: SQLA model of phone
    :return: phone read pydantic schema
    """
    return PhoneRead(number=phone.number)
