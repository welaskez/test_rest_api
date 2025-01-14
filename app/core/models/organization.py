from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin

if TYPE_CHECKING:
    from .activity import Activity
    from .building import Building
    from .phone import Phone


class Organization(Base, UuidPkMixin, CreatedAtMixin, UpdatedAtMixin):
    name: Mapped[str] = mapped_column(unique=True)
    building_id: Mapped[UUID] = mapped_column(ForeignKey("buildings.id"))
    activity_id: Mapped[UUID] = mapped_column(ForeignKey("activities.id"))

    building: Mapped["Building"] = relationship(back_populates="organizations")
    activity: Mapped["Activity"] = relationship(back_populates="organizations")
    phone_numbers: Mapped[list["Phone"]] = relationship(back_populates="organization")

    def __str__(self):
        return self.name
