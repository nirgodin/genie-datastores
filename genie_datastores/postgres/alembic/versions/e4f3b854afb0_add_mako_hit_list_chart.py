"""Add mako hit list chart

Revision ID: e4f3b854afb0
Revises: 2a42b3f17e1a
Create Date: 2024-01-19 17:24:16.786378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from genie_datastores.postgres.models import Chart

# revision identifiers, used by Alembic.
revision: str = 'e4f3b854afb0'
down_revision: Union[str, None] = '2a42b3f17e1a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.text(f"ALTER TYPE chart ADD value '{Chart.MAKO_WEEKLY_HIT_LIST.name}'"))


def downgrade() -> None:
    pass
