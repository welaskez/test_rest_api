from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin


class Phone(Base, UuidPkMixin, CreatedAtMixin, UpdatedAtMixin):
    number: Mapped[str]
    organization_id: Mapped[UUID] = mapped_column(ForeignKey("organizations.id"))

    def __str__(self):
        return self.number
