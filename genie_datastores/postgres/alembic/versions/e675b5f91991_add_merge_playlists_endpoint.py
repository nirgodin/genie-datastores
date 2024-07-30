"""Add merge playlists endpoint

Revision ID: e675b5f91991
Revises: c783bccae86a
Create Date: 2024-07-30 18:55:08.923849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e675b5f91991'
down_revision: Union[str, None] = 'c783bccae86a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TYPE playlistendpoint ADD VALUE 'MERGE_PLAYLISTS'")


def downgrade() -> None:
    pass
