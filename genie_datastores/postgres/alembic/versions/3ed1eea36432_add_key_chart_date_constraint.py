"""add_key_chart_date_constraint

Revision ID: 3ed1eea36432
Revises: 132a498067f4
Create Date: 2024-04-28 11:27:08.939237

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ed1eea36432'
down_revision: Union[str, None] = '132a498067f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'charts_entries', ['key', 'chart', 'date'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'charts_entries', type_='unique')
    # ### end Alembic commands ###