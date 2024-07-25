"""Fill shazam_artists has_about_document column

Revision ID: 7872808c91bc
Revises: 9d4df5af2a02
Create Date: 2024-07-25 18:49:38.526638

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7872808c91bc'
down_revision: Union[str, None] = '9d4df5af2a02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        sa.text(
            "UPDATE shazam_artists SET has_about_document=true WHERE about IS NOT NULL"
        )
    )
    op.execute(
        sa.text(
            "UPDATE shazam_artists SET has_about_document=false WHERE about IS NULL"
        )
    )


def downgrade() -> None:
    op.execute(
        sa.text(
            "UPDATE shazam_artists SET has_about_document=null"
        )
    )
