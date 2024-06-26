from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean

from genie_datastores.postgres.consts.orm_consts import CASES_TABLE_ID
from genie_datastores.postgres.models import BaseORMModel


class CaseProgress(BaseORMModel):
    __tablename__ = "cases_progress"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    case_id = Column(String, ForeignKey(CASES_TABLE_ID), nullable=False)
    has_exception = Column(Boolean, nullable=False, default=False)
    status = Column(String, nullable=False)  # TODO: Rename to `stage`
    time_took = Column(Float, nullable=False)
    exception_details = Column(String)
