"""create buildings table

Revision ID: c240d59dc133
Revises: 
Create Date: 2025-01-15 00:37:43.154289

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c240d59dc133"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "buildings",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("county", sa.String(), nullable=False),
        sa.Column("region", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("district", sa.String(), nullable=True),
        sa.Column("micro_district_or_street", sa.String(), nullable=False),
        sa.Column("number", sa.Integer(), nullable=False),
        sa.Column("postal_code", sa.Integer(), nullable=False),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_buildings")),
    )


def downgrade() -> None:
    op.drop_table("buildings")
