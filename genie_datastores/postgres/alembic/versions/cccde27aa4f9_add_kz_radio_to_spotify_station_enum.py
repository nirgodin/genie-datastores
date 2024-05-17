"""add kz radio to spotify station enum

Revision ID: cccde27aa4f9
Revises: 77c7d92a749f
Create Date: 2024-05-17 18:09:13.012938

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cccde27aa4f9'
down_revision: Union[str, None] = '77c7d92a749f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TYPE spotifystation ADD VALUE 'KZ_RADIO'")


def downgrade() -> None:
    pass
