"""change number type to string in building table

Revision ID: 788ac66ff6ba
Revises: aeeac8d8ec11
Create Date: 2025-01-15 02:30:41.320151

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "788ac66ff6ba"
down_revision: Union[str, None] = "aeeac8d8ec11"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "buildings",
        "number",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "buildings",
        "number",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
