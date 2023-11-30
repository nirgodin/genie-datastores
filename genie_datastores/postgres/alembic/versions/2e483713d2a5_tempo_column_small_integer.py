"""tempo column small integer

Revision ID: 2e483713d2a5
Revises: 4a3c69517f0c
Create Date: 2023-11-11 12:22:18.119231

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e483713d2a5'
down_revision: Union[str, None] = '4a3c69517f0c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('audio_features', 'tempo',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.SmallInteger(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('audio_features', 'tempo',
               existing_type=sa.SmallInteger(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    # ### end Alembic commands ###
