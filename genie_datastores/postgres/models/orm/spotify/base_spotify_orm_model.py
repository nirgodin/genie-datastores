from abc import abstractmethod

from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel


class BaseSpotifyORMModel(BaseORMModel):
    __abstract__ = True

    @classmethod
    @abstractmethod
    def from_spotify_response(cls, response: dict) -> "BaseSpotifyORMModel":
        raise NotImplementedError
