"""translations entity columns nullable

Revision ID: d83acd20b1c3
Revises: 82a5e756e3be
Create Date: 2024-05-31 14:36:21.711838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd83acd20b1c3'
down_revision: Union[str, None] = '82a5e756e3be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('translations', 'entity_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('translations', 'entity_source',
               existing_type=postgresql.ENUM('MANUAL_TAGGING', 'OPENAI', 'ISRAELI_WIKIPEDIA', 'GENERAL_WIKIPEDIA', 'SPOTIFY_EQUAL_PLAYLISTS', 'GOOGLE_IMAGES', 'SHAZAM', 'MUSIXMATCH', 'GENIUS', 'SPOTIFY_IMAGES', 'CHARTS', 'SPOTIFY', name='datasource'),
               nullable=True)
    op.alter_column('translations', 'entity_type',
               existing_type=postgresql.ENUM('TRACK', 'ARTIST', name='entitytype'),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('translations', 'entity_type',
               existing_type=postgresql.ENUM('TRACK', 'ARTIST', name='entitytype'),
               nullable=False)
    op.alter_column('translations', 'entity_source',
               existing_type=postgresql.ENUM('MANUAL_TAGGING', 'OPENAI', 'ISRAELI_WIKIPEDIA', 'GENERAL_WIKIPEDIA', 'SPOTIFY_EQUAL_PLAYLISTS', 'GOOGLE_IMAGES', 'SHAZAM', 'MUSIXMATCH', 'GENIUS', 'SPOTIFY_IMAGES', 'CHARTS', 'SPOTIFY', name='datasource'),
               nullable=False)
    op.alter_column('translations', 'entity_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
