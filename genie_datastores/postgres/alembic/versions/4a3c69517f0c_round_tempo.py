"""round tempo

Revision ID: 4a3c69517f0c
Revises: edce136d56b9
Create Date: 2023-11-11 12:09:16.742524

"""
import asyncio
from typing import Sequence, Union

import nest_asyncio
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

from genie_datastores.postgres.models import AudioFeatures
from genie_datastores.postgres.operations import execute_query, get_database_engine

# revision identifiers, used by Alembic.
revision: str = '4a3c69517f0c'
down_revision: Union[str, None] = 'edce136d56b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    engine = get_database_engine()
    query = text(f"update audio_features set {AudioFeatures.tempo.key} = round({AudioFeatures.tempo.key})")
    loop = asyncio.get_event_loop()
    nest_asyncio.apply(loop)
    loop.run_until_complete(execute_query(engine, query))


def downgrade() -> None:
    pass
