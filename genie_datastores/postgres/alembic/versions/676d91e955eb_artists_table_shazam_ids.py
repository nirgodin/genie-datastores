"""artists table shazam ids

Revision ID: 676d91e955eb
Revises: dd27cfbdbab4
Create Date: 2023-12-19 15:11:38.892004

"""
import asyncio
from typing import Sequence, Union

import nest_asyncio
from alembic import op
import sqlalchemy as sa
from sqlalchemy import select
from tools.data_chunks_generator import DataChunksGenerator
from tqdm import tqdm

from genie_datastores.postgres.models import TrackIDMapping, Artist
from genie_datastores.postgres.operations import get_database_engine, execute_query
from genie_datastores.postgres.utils import update_by_mapping

# revision identifiers, used by Alembic.
revision: str = '676d91e955eb'
down_revision: Union[str, None] = 'dd27cfbdbab4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


async def map_shazam_ids():
    engine = get_database_engine()
    query = select(TrackIDMapping.id, TrackIDMapping.shazam_id)
    query_result = await execute_query(engine=engine, query=query)
    records = query_result.all()
    chunks = list(DataChunksGenerator().generate_data_chunks(records, None))

    with tqdm(total=len(chunks)) as progress_bar:
        for chunk in chunks:
            mapping = dict(chunk)
            await update_by_mapping(
                engine=engine,
                mapping=mapping,
                orm=Artist,
                key_column=Artist.id,
                value_column=Artist.shazam_id
            )
            progress_bar.update(1)


def upgrade() -> None:
    loop = asyncio.get_event_loop()
    nest_asyncio.apply(loop)
    loop.run_until_complete(map_shazam_ids())


def downgrade() -> None:
    pass
