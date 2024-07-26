"""Add Wikipedia data source

Revision ID: c783bccae86a
Revises: f19a7ff69783
Create Date: 2024-07-26 15:43:21.132632

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c783bccae86a'
down_revision: Union[str, None] = 'f19a7ff69783'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TYPE datasource ADD VALUE 'WIKIPEDIA'")


def downgrade() -> None:
    pass
