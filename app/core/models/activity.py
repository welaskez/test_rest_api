from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin


class Activity(Base, UuidPkMixin, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "activities"

    name: Mapped[str] = mapped_column(unique=True)
    parent_id: Mapped[UUID | None] = mapped_column(ForeignKey("activities.id"))
