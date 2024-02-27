from abc import ABC

from sqlalchemy.ext.asyncio import AsyncEngine

from genie_datastores.contract import IDatabaseInserter


class IPostgresDatabaseInserter(IDatabaseInserter, ABC):
    def __init__(self, db_engine: AsyncEngine):
        self._db_engine = db_engine
