from sqlalchemy import String, Column

from genie_datastores.postgres.consts.orm_consts import CASES_TABLE
from genie_datastores.postgres.models import BaseORMModel


class Case(BaseORMModel):
    __tablename__ = CASES_TABLE

    id = Column(String, primary_key=True, nullable=False)
