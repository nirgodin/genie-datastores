from typing import Type, List

from sqlalchemy import Column, inspect, select
from sqlalchemy.ext.asyncio import AsyncEngine

from postgres_client.postgres_operations import execute_query
from postgres_client.models.orm.base_orm_model import BaseORMModel


def get_orm_columns(orm: Type[BaseORMModel]) -> List[Column]:
    return [column for column in inspect(orm).c]


def get_all_columns_except(orm: Type[BaseORMModel], *exclude_columns: List[Column]) -> List[Column]:
    columns = get_orm_columns(orm)
    return [col for col in columns if col not in exclude_columns]


async def query_existing_column_values(orm: Type[BaseORMModel],
                                       column_name: str,
                                       records: List[BaseORMModel],
                                       engine: AsyncEngine) -> List[str]:
    records_values = [getattr(record, column_name) for record in records]
    column = getattr(orm, column_name)
    query = (
        select(column)
        .where(column.in_(records_values))
    )
    query_result = await execute_query(engine=engine, query=query)

    return query_result.scalars().all()
