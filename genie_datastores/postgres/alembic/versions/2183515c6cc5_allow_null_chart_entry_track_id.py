"""Allow null chart entry track id

Revision ID: 2183515c6cc5
Revises: e4f3b854afb0
Create Date: 2024-01-27 09:15:19.206332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2183515c6cc5'
down_revision: Union[str, None] = '2a42b3f17e1a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('charts_entries', 'track_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.execute(
        sa.text(
            "ALTER TABLE charts_entries ADD constraint check_track_id_and_key_are_not_both_null CHECK "
            "(key IS NOT NULL OR track_id IS NOT NULL)"
        )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('charts_entries', 'track_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
