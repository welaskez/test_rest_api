from uuid import UUID as PYUUID
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column


class UuidPkMixin:
    """Mixin for models, adding id with uuid type"""

    id: Mapped[PYUUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )
