from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin


class User(Base, UuidPkMixin, CreatedAtMixin, UpdatedAtMixin):
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(unique=True)
    api_key: Mapped[str | None]
