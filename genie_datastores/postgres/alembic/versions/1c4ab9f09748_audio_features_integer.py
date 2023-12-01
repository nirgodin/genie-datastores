"""audio features integer

Revision ID: 1c4ab9f09748
Revises: 198984bd0e84
Create Date: 2023-11-11 11:26:17.291746

"""
import asyncio
from typing import Sequence, Union

import nest_asyncio
from alembic import op
import sqlalchemy as sa
from sqlalchemy import select, update, func, text

from genie_datastores.postgres.models import AudioFeatures
from genie_datastores.postgres.operations import execute_query, get_database_engine

# revision identifiers, used by Alembic.
revision: str = '1c4ab9f09748'
down_revision: Union[str, None] = '198984bd0e84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


MULTIPLY_COLUMNS = [
    AudioFeatures.acousticness,
    AudioFeatures.danceability,
    AudioFeatures.energy,
    AudioFeatures.instrumentalness,
    AudioFeatures.liveness,
    AudioFeatures.speechiness,
    AudioFeatures.valence
]


def upgrade() -> None:
    engine = get_database_engine()

    for column in MULTIPLY_COLUMNS:
        query = text(f"update audio_features set {column.key} = round({column.key} * 100)")
        loop = asyncio.get_event_loop()
        nest_asyncio.apply(loop)
        loop.run_until_complete(execute_query(engine, query))


def downgrade() -> None:
    pass
