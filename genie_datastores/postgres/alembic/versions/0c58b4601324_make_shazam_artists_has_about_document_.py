"""Make shazam_artists has_about_document not nullable

Revision ID: 0c58b4601324
Revises: 7872808c91bc
Create Date: 2024-07-25 18:54:04.001967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c58b4601324'
down_revision: Union[str, None] = '7872808c91bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shazam_artists', 'has_about_document',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shazam_artists', 'has_about_document',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
