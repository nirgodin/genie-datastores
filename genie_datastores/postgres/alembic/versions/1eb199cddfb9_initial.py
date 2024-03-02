"""Initial

Revision ID: 1eb199cddfb9
Revises: 
Create Date: 2023-11-10 10:49:37.579191

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import ENUM

# revision identifiers, used by Alembic.
revision: str = '1eb199cddfb9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'spotify_artists',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('about', sa.String(), nullable=True),
        sa.Column('facebook_name', sa.String(), nullable=True),
        sa.Column('genres', sa.ARRAY(sa.String()), nullable=True),
        sa.Column('instagram_name', sa.String(), nullable=True),
        sa.Column('twitter_name', sa.String(), nullable=True),
        sa.Column('wikipedia_language', sa.String(), nullable=True),
        sa.Column('wikipedia_name', sa.String(), nullable=True),
        sa.Column('creation_date', sa.TIMESTAMP(), nullable=False),
        sa.Column('update_date', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table(
        'spotify_albums',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('artist_id', sa.String(), nullable=False),
        sa.Column('group', sa.Enum('ALBUM', 'SINGLE', 'COMPILATION', 'APPEARS_ON', name='spotifyalbumtype'), nullable=True),
        sa.Column('label', sa.String(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('release_date', sa.TIMESTAMP(), nullable=True),
        sa.Column('total_tracks', sa.SmallInteger(), nullable=False),
        sa.Column('group', ENUM('ALBUM', 'SINGLE', 'COMPILATION', 'APPEARS_ON', name='spotifyalbumtype', create_type=False), nullable=True),
        sa.Column('creation_date', sa.TIMESTAMP(), nullable=False),
        sa.Column('update_date', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['artist_id'], ['spotify_artists.id'], ),
    )

    op.create_table(
        'spotify_tracks',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('album_id', sa.String(), nullable=True),
        sa.Column('artist_id', sa.String(), nullable=False),
        sa.Column('explicit', sa.Boolean(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('number', sa.SmallInteger(), nullable=False),
        sa.Column('release_date', sa.TIMESTAMP(), nullable=True),
        sa.Column('creation_date', sa.TIMESTAMP(), nullable=False),
        sa.Column('update_date', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['artist_id'], ['spotify_artists.id'], ),
    )

    op.create_table(
        'audio_features',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('album_id', sa.String(), nullable=True),
        sa.Column('acousticness', sa.SmallInteger(), nullable=False),
        sa.Column('danceability', sa.SmallInteger(), nullable=False),
        sa.Column('duration_ms', sa.Integer(), nullable=False),
        sa.Column('energy', sa.SmallInteger(), nullable=False),
        sa.Column('instrumentalness', sa.SmallInteger(), nullable=False),
        sa.Column('key', sa.SmallInteger(), nullable=False),
        sa.Column('liveness', sa.SmallInteger(), nullable=False),
        sa.Column('loudness', sa.Float(), nullable=True),
        sa.Column('mode', sa.Boolean(), nullable=True),
        sa.Column('speechiness', sa.SmallInteger(), nullable=False),
        sa.Column('tempo', sa.SmallInteger(), nullable=False),
        sa.Column('time_signature', sa.SmallInteger(), nullable=False),
        sa.Column('valence', sa.SmallInteger(), nullable=False),
        sa.Column('creation_date', sa.TIMESTAMP(), nullable=False),
        sa.Column('update_date', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['id'], ['spotify_tracks.id'], ),
    )

    op.create_table(
        'radio_tracks',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('track_id', sa.String(), nullable=False),
        sa.Column('added_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('artist_followers', sa.Integer(), nullable=False),
        sa.Column('artist_popularity', sa.SmallInteger(), nullable=False),
        sa.Column('popularity', sa.SmallInteger(), nullable=False),
        sa.Column('snapshot_id', sa.String(), nullable=False),
        sa.Column('station', sa.Enum('GLGLZ', 'KAN_88', 'ECO_99', 'KAN_GIMEL', 'FM_103', 'SPOTIFY_TOP_50_WEEKLY', 'SPOTIFY_TOP_50_ISRAEL_DAILY', 'SPOTIFY_TOP_50_GLOBAL_DAILY', 'SPOTIFY_VIRAL_50_ISRAEL', name='spotifystation'), nullable=False),
        sa.Column('creation_date', sa.TIMESTAMP(), nullable=False),
        sa.Column('update_date', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['track_id'], ['spotify_tracks.id'], ),
    )
    op.create_unique_constraint(None, 'radio_tracks', ['track_id', 'added_at', 'station'])

    op.create_table(
        'track_ids_mapping',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('adam_id', sa.String(), nullable=True),
        sa.Column('apple_music_id', sa.String(), nullable=True),
        sa.Column('genius_id', sa.String(), nullable=True),
        sa.Column('musixmatch_id', sa.String(), nullable=True),
        sa.Column('shazam_id', sa.String(), nullable=True),
        sa.Column('creation_date', sa.TIMESTAMP(), nullable=False),
        sa.Column('update_date', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['id'], ['spotify_tracks.id'], ),
    )

    op.create_table(
        'tracks_lyrics',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('lyrics', sa.ARRAY(sa.String()), nullable=True),
        sa.Column('lyrics_source', sa.Enum('GENERAL_WIKIPEDIA', 'GENIUS', 'GOOGLE_IMAGES', 'ISRAELI_WIKIPEDIA', 'MANUAL_TAGGING', 'MUSIXMATCH', 'OPENAI', 'SHAZAM', 'SPOTIFY_EQUAL_PLAYLISTS', 'SPOTIFY_IMAGES', 'CHARTS', 'SPOTIFY', name='datasource'), nullable=True),
        sa.Column('language', sa.String(), nullable=True),
        sa.Column('language_confidence', sa.SmallInteger(), nullable=True),
        sa.Column('number_of_words', sa.SmallInteger(), nullable=True),
        sa.Column('words_count', sa.JSON(), nullable=True),
        sa.Column('creation_date', sa.TIMESTAMP(), nullable=False),
        sa.Column('update_date', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['id'], ['spotify_tracks.id'], ),
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
