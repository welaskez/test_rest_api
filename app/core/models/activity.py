from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin

if TYPE_CHECKING:
    from .organization import Organization


class Activity(Base, UuidPkMixin, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "activities"

    name: Mapped[str] = mapped_column(unique=True)
    parent_id: Mapped[UUID | None] = mapped_column(ForeignKey("activities.id"))

    organizations: Mapped[list["Organization"]] = relationship(
        back_populates="activity"
    )

    childrens: Mapped[list["Activity"]] = relationship(
        back_populates="parent",
    )

    parent: Mapped["Activity"] = relationship(
        back_populates="childrens",
        remote_side="Activity.id",
    )
