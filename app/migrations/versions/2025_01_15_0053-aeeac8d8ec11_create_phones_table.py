"""create phones table

Revision ID: aeeac8d8ec11
Revises: b4c63086244f
Create Date: 2025-01-15 00:53:14.653783

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "aeeac8d8ec11"
down_revision: Union[str, None] = "b4c63086244f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "phones",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("number", sa.String(), nullable=False),
        sa.Column("organization_id", sa.UUID(), nullable=False),
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
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organizations.id"],
            name=op.f("fk_phones_organization_id_organizations"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_phones")),
    )


def downgrade() -> None:
    op.drop_table("phones")
