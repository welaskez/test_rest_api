from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin

if TYPE_CHECKING:
    from .organization import Organization


class Phone(Base, UuidPkMixin, CreatedAtMixin, UpdatedAtMixin):
    number: Mapped[str]
    organization_id: Mapped[UUID] = mapped_column(ForeignKey("organizations.id"))

    organization: Mapped["Organization"] = relationship(back_populates="phone_numbers")

    def __str__(self):
        return self.number
