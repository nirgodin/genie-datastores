"""eurovision_chart

Revision ID: f612e4ab4456
Revises: 4d49d0e91690
Create Date: 2024-02-01 19:41:48.480701

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from genie_datastores.postgres.models import Chart

# revision identifiers, used by Alembic.
revision: str = 'f612e4ab4456'
down_revision: Union[str, None] = '4d49d0e91690'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.text(f"ALTER TYPE chart ADD value '{Chart.EUROVISION.name}'"))


def downgrade() -> None:
    pass
