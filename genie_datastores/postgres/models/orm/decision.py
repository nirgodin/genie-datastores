from sqlalchemy import Column, Integer, Enum, Float, String

from genie_datastores.postgres.models import BaseORMModel, DataSource
from genie_datastores.postgres.models.enum.table import Table


class Decision(BaseORMModel):
    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    column = Column(String, nullable=False)
    source = Column(Enum(DataSource), nullable=False)
    table = Column(Enum(Table), nullable=False)
    table_id = Column(String, nullable=False)
    confidence = Column(Float)
    evidence = Column(String)
