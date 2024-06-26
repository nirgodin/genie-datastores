"""add translations orm

Revision ID: 77c7d92a749f
Revises: 3f407bc136c9
Create Date: 2024-05-16 15:24:24.530162

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM

# revision identifiers, used by Alembic.
revision: str = '77c7d92a749f'
down_revision: Union[str, None] = '3f407bc136c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('translations',
    sa.Column('creation_date', sa.TIMESTAMP(), nullable=False),
    sa.Column('update_date', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('entity_source', ENUM('GENERAL_WIKIPEDIA', 'GENIUS', 'GOOGLE_IMAGES', 'ISRAELI_WIKIPEDIA', 'MANUAL_TAGGING', 'MUSIXMATCH', 'OPENAI', 'SHAZAM', 'SPOTIFY_EQUAL_PLAYLISTS', 'SPOTIFY_IMAGES', 'CHARTS', 'SPOTIFY', name='datasource', create_type=False), nullable=False),
    sa.Column('entity_type', sa.Enum('TRACK', 'ARTIST', name='entitytype'), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('translation', sa.String(), nullable=False),
    sa.Column('source_language', sa.String(), nullable=False),
    sa.Column('target_language', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('translations')
    # ### end Alembic commands ###
