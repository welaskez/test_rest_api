from typing import Generic, Type, TypeVar
from uuid import UUID

from core.models import Base
from crud.base import BaseCRUD
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T", bound=Base)

S = TypeVar("S", bound=BaseModel)


class BaseService(Generic[T]):
    def __init__(self, session: AsyncSession, crud_class: Type[BaseCRUD[T]]) -> None:
        """
        Base service class
        :param session: db session
        :param crud_class: crud class
        """
        self.session = session
        self.crud = crud_class(session)

    async def create(self, schema: S) -> T:
        """
        create new record
        :param schema: pydantic schema
        :return: model
        """
        return await self.crud.create(schema)

    async def get_by_id(self, model_id: UUID | str) -> T | None:
        """
        getting record by id
        :param model_id: record id
        :return: model or none
        """
        return await self.crud.get_by_id(model_id)

    async def get_all(self) -> list[T]:
        """
        getting all records
        :return: records
        """
        return await self.crud.get_all()

    async def update(self, model: T, schema: S) -> T:
        """
        update record
        :param model: model
        :param schema: pydantic schema
        :return: updated model
        """
        return await self.crud.update(model, schema)

    async def delete(self, model: T) -> None:
        """
        delete model
        :param model: model
        """
        await self.crud.delete(model)
