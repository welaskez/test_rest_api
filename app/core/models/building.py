from typing import TYPE_CHECKING

from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin

if TYPE_CHECKING:
    from .organization import Organization


class Building(Base, UuidPkMixin, CreatedAtMixin, UpdatedAtMixin):
    county: Mapped[str]
    region: Mapped[str]
    city: Mapped[str]
    district: Mapped[str | None]
    micro_district_or_street: Mapped[str]
    number: Mapped[int]
    postal_code: Mapped[int]
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)

    organizations: Mapped[list["Organization"]] = relationship(
        back_populates="building"
    )
