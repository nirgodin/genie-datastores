"""populate artists table

Revision ID: dd27cfbdbab4
Revises: 0aaea7e78166
Create Date: 2023-12-19 14:55:22.196148

"""
import asyncio
from typing import Sequence, Union

import nest_asyncio
from alembic import op
import sqlalchemy as sa
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncEngine
from tools.data_chunks_generator import DataChunksGenerator

from tqdm import tqdm

from genie_datastores.postgres.models import SpotifyArtist, Artist
from genie_datastores.postgres.operations import get_database_engine, execute_query, insert_records

# revision identifiers, used by Alembic.
revision: str = 'dd27cfbdbab4'
down_revision: Union[str, None] = '0aaea7e78166'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


async def create_ids_records() -> None:
    QUERY_COLUMNS = [
        SpotifyArtist.id,
        SpotifyArtist.birth_date,
        SpotifyArtist.death_date,
        SpotifyArtist.gender,
        SpotifyArtist.gender_source,
        SpotifyArtist.is_israeli,
        SpotifyArtist.is_lgbtq,
        SpotifyArtist.primary_genre
    ]

    engine = get_database_engine()
    query = select(*QUERY_COLUMNS)
    query_result = await execute_query(engine=engine, query=query)
    raw_records = [dict(res._mapping) for res in query_result.all()]
    records = [Artist(**record) for record in raw_records]
    chunks = list(DataChunksGenerator(max_chunks_number=None).generate_data_chunks(records, None))

    with tqdm(total=len(chunks)) as progress_bar:
        for chunk in chunks:
            await insert_records(engine=engine, records=chunk)
            progress_bar.update(1)


def upgrade() -> None:
    loop = asyncio.get_event_loop()
    nest_asyncio.apply(loop)
    loop.run_until_complete(create_ids_records())


def downgrade() -> None:
    pass
