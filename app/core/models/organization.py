from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin


class Organization(Base, UuidPkMixin, CreatedAtMixin, UpdatedAtMixin):
    name: Mapped[str] = mapped_column(unique=True)
    building_id: Mapped[UUID] = mapped_column(ForeignKey("buildings.id"))
    activity_id: Mapped[UUID] = mapped_column(ForeignKey("activities.id"))

    def __str__(self):
        return self.name
