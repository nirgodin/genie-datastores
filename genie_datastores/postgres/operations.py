import os
from functools import lru_cache
from typing import List, Union

from sqlalchemy.dialects.postgresql import insert, Insert
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import Select, Update
from sqlalchemy.sql.elements import TextClause

from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel, Base


async def insert_records(engine: AsyncEngine, records: List[BaseORMModel]) -> None:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            session.add_all(records)


async def insert_records_ignoring_conflicts(engine: AsyncEngine, records: List[BaseORMModel]) -> None:
    values = [record.to_dict() for record in records]
    query = (
        insert(type(records[0]))
        .values(values)
        .on_conflict_do_nothing()
    )

    await execute_query(engine, query)


async def execute_query(engine: AsyncEngine, query: Union[Select, Update, TextClause, Insert]) -> Result:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            return await session.execute(query)


async def create_all_tables(engine: AsyncEngine) -> None:
    print("Starting to create all schema tables")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_all_tables(engine: AsyncEngine) -> None:
    print("Starting to drop all schema tables")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@lru_cache
def get_database_url() -> str:
    return os.environ["DATABASE_URL"]


@lru_cache
def get_database_engine() -> AsyncEngine:
    return create_async_engine(get_database_url())
