from sqlalchemy import Column, String, Enum

from genie_datastores.models import DataSource
from genie_datastores.postgres.consts.orm_consts import CURATORS_TABLE
from genie_datastores.postgres.models import BaseORMModel


class Curator(BaseORMModel):
    __tablename__ = CURATORS_TABLE

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    source = Column(Enum(DataSource), nullable=False)
