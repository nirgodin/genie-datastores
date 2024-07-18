"""Fill has_about_document default values

Revision ID: d4493e394b93
Revises: c900145b1ea5
Create Date: 2024-07-18 21:09:54.049030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4493e394b93'
down_revision: Union[str, None] = 'c900145b1ea5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        sa.text(
            "UPDATE spotify_artists SET has_about_document=true WHERE about IS NOT NULL"
        )
    )
    op.execute(
        sa.text(
            "UPDATE spotify_artists SET has_about_document=false WHERE about IS NULL"
        )
    )


def downgrade() -> None:
    op.execute(
        sa.text(
            "UPDATE spotify_artists SET has_about_document=null"
        )
    )

