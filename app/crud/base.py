from typing import Generic, Type, TypeVar
from uuid import UUID

from core.models import Base
from pydantic import BaseModel
from sqlalchemy import ColumnExpressionArgument, select
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T", bound=Base)

S = TypeVar("S", bound=BaseModel)


class BaseCRUD(Generic[T]):
    model: Type[T]

    def __init__(self, session: AsyncSession) -> None:
        """
        Base CRUD class
        :param session: db session
        """
        self.session = session

    async def create(self, schema: S) -> T:
        """
        creating model
        :param schema: pydantic schema with model params
        :return: model
        """
        model = self.model(**schema.model_dump())

        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)

        return model

    async def get_by_id(self, model_id: UUID | str) -> T:
        """
        getting model by id
        :param model_id: model id
        :return: model or none
        """
        return await self.session.get(self.model, model_id)

    async def get_all(self) -> list[T]:
        """
        return all models
        :return: list of model
        """
        return list(await self.session.scalars(select(self.model)))

    async def get_one_by_expression(
        self, expression: ColumnExpressionArgument
    ) -> T | None:
        """
        return one model by expression
        :param expression: 'where' expression
        :return: model or none
        """
        return await self.session.scalar(select(self.model).where(expression))

    async def get_all_by_expression(
        self, expression: ColumnExpressionArgument
    ) -> list[T]:
        """
        return many models by expression
        :param expression: 'where' expression
        :return: model or none
        """
        return list(await self.session.scalars(select(self.model).where(expression)))

    async def update(self, model: T, schema: S) -> T:
        """
        updating model
        :param model: model
        :param schema: pydantic schema
        :return: model
        """
        for k, v in schema.model_dump(exclude_unset=True).items():
            setattr(model, k, v)

        await self.session.commit()
        await self.session.refresh(model)

        return model

    async def delete(self, model: T) -> None:
        """
        deleting model
        :param model: model
        :return: none
        """
        await self.session.delete(model)
        await self.session.commit()
