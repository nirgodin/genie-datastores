"""add spotify charts to charts enum

Revision ID: e5e3c2044a6f
Revises: 8935d4b04386
Create Date: 2024-01-12 17:06:07.228481

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from genie_datastores.postgres.models import Chart

# revision identifiers, used by Alembic.
revision: str = 'e5e3c2044a6f'
down_revision: Union[str, None] = '8935d4b04386'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    for option in [Chart.SPOTIFY_DAILY_ISRAELI, Chart.SPOTIFY_DAILY_INTERNATIONAL]:
        op.execute(sa.text(f"ALTER TYPE chart ADD value '{option.name}'"))


def downgrade() -> None:
    pass
