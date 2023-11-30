from abc import abstractmethod

from postgres_client.models.orm.base_orm_model import BaseORMModel


class BaseSpotifyORMModel(BaseORMModel):
    __abstract__ = True

    @classmethod
    @abstractmethod
    def from_spotify_response(cls, response: dict) -> "BaseSpotifyORMModel":
        raise NotImplementedError
