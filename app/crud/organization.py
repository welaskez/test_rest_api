from core.models import Organization
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD


class OrganizationCRUD(BaseCRUD[Organization]):
    model = Organization

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
