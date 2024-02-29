from sqlalchemy import String, Column, Enum

from genie_datastores.postgres.consts.orm_consts import CASES_TABLE
from genie_datastores.postgres.models import BaseORMModel
from genie_datastores.postgres.models.enum.playlist_endpoint import PlaylistEndpoint


class Case(BaseORMModel):
    __tablename__ = CASES_TABLE

    id = Column(String, primary_key=True, nullable=False)
    endpoint = Column(Enum(PlaylistEndpoint), nullable=False)
