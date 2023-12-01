"""spotify images datasource

Revision ID: 8c68058d20da
Revises: 0650feea2b8d
Create Date: 2023-12-01 12:07:26.371640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from genie_datastores.postgres.models import DataSource

# revision identifiers, used by Alembic.
revision: str = '8c68058d20da'
down_revision: Union[str, None] = '0650feea2b8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.text(f"ALTER TYPE datasource ADD value '{DataSource.SPOTIFY_IMAGES.name}'"))


def downgrade() -> None:
    pass
