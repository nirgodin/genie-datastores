"""add_every_hit_chart

Revision ID: f29de397d90b
Revises: 5b23c3100284
Create Date: 2024-02-08 19:15:44.455682

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from genie_datastores.postgres.models import Chart

# revision identifiers, used by Alembic.
revision: str = 'f29de397d90b'
down_revision: Union[str, None] = '5b23c3100284'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.text(f"ALTER TYPE chart ADD value '{Chart.UK_EVERY_HIT.name}'"))


def downgrade() -> None:
    pass
