from sqlalchemy import String, Column, CheckConstraint, Enum

from genie_datastores.postgres.models import BaseORMModel, PrimaryGenre


class Genre(BaseORMModel):
    __tablename__ = "genres"

    id = Column(String, primary_key=True, nullable=False)
    primary_genre = Column(Enum(PrimaryGenre))
