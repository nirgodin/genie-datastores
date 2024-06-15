from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncEngine

from genie_datastores.postgres.operations import create_all_tables, drop_all_tables


@asynccontextmanager
async def postgres_session(engine: AsyncEngine) -> None:
    try:
        await create_all_tables(engine)
        yield

    finally:
        await drop_all_tables(engine)
