from typing import Type, List, Dict, Any

from sqlalchemy import Column, inspect, select, update, case
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.sql.elements import BinaryExpression

from genie_datastores.postgres.operations import execute_query
from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel


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


async def update_by_mapping(engine: AsyncEngine,
                            mapping: dict,
                            orm: Type[BaseORMModel],
                            key_column: BaseORMModel,
                            value_column: BaseORMModel) -> None:
    query = (
        update(orm)
        .where(key_column.in_(mapping.keys()))
        .values(
            {
                value_column: case(
                    mapping, value=key_column
                )
            }
        )
    )
    await execute_query(engine=engine, query=query)


async def update_by_values(engine: AsyncEngine,
                           orm: Type[BaseORMModel],
                           values: Dict[BaseORMModel, Any],
                           *conditions: BinaryExpression) -> None:
    query = update(orm).values(values)

    for condition in conditions:
        query = query.where(condition)

    await execute_query(engine=engine, query=query)


async def is_existing_value(engine: AsyncEngine, orm: Type[BaseORMModel], value: Any) -> bool:
    query = (
        select(orm)
        .where(orm == value)
        .limit(1)
    )
    query_result = await execute_query(engine=engine, query=query)
    first_result = query_result.scalars().first()

    return first_result is not None
