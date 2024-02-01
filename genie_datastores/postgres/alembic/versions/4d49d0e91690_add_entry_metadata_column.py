"""add_entry_metadata_column

Revision ID: 4d49d0e91690
Revises: bc99287abfc5
Create Date: 2024-02-01 19:38:48.068462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4d49d0e91690'
down_revision: Union[str, None] = 'bc99287abfc5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('charts_entries', sa.Column('entry_metadata', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('charts_entries', 'entry_metadata')
    # ### end Alembic commands ###
