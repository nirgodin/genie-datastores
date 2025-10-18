from sqlalchemy import Column, String, ForeignKey

from genie_datastores.postgres.consts.orm_consts import CURATORS_TABLE_ID, CURATORS_COLLECTIONS_TABLE
from genie_datastores.postgres.models import BaseORMModel


class CuratorCollection(BaseORMModel):
    __tablename__ = CURATORS_COLLECTIONS_TABLE

    id = Column(String, primary_key=True, nullable=False)
    curator_id = Column(String, ForeignKey(CURATORS_TABLE_ID), nullable=False)
    title = Column(String)
    description = Column(String)
    comment = Column(String)
