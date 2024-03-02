"""artists table

Revision ID: 0aaea7e78166
Revises: 0f8daceba5e6
Create Date: 2023-12-19 14:50:08.998021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM


# revision identifiers, used by Alembic.
revision: str = '0aaea7e78166'
down_revision: Union[str, None] = '0f8daceba5e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('creation_date', sa.TIMESTAMP(), nullable=False),
    sa.Column('update_date', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('shazam_id', sa.String(), nullable=True),
    sa.Column('birth_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('death_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('gender', ENUM('MALE', 'FEMALE', 'BAND', 'UNKNOWN', name='gender', create_type=True), nullable=True),
    sa.Column('gender_source', ENUM('GENERAL_WIKIPEDIA', 'GENIUS', 'GOOGLE_IMAGES', 'ISRAELI_WIKIPEDIA', 'MANUAL_TAGGING', 'MUSIXMATCH', 'OPENAI', 'SHAZAM', 'SPOTIFY_EQUAL_PLAYLISTS', 'SPOTIFY_IMAGES', name='datasource', create_type=False), nullable=True),
    sa.Column('is_israeli', sa.Boolean(), nullable=True),
    sa.Column('is_lgbtq', sa.Boolean(), nullable=True),
    sa.Column('primary_genre', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('county', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['spotify_artists.id'], ),
    sa.ForeignKeyConstraint(['shazam_id'], ['shazam_artists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artists')
    # ### end Alembic commands ###
