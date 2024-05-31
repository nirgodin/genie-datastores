"""Rename translations id column

Revision ID: f586598d3368
Revises: cccde27aa4f9
Create Date: 2024-05-31 13:44:27.405754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f586598d3368'
down_revision: Union[str, None] = 'cccde27aa4f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("translations", "id", new_column_name="entity_id")


def downgrade() -> None:
    op.alter_column("translations", "entity_id", new_column_name="id")
