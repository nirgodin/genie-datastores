from typing import Optional

from genie_common.tools import logger
from motor.motor_asyncio import AsyncIOMotorClient
from testcontainers.mongodb import MongoDbContainer

from genie_datastores.mongo.operations import get_motor_client


class MongoTestkit:
    def __init__(self,
                 container: Optional[MongoDbContainer] = None,
                 image: Optional[str] = None,
                 port: Optional[int] = None):
        self.image = image or "mongo:7.0.7"
        self.port = port or 27017
        self._container = container

    def get_motor_client(self) -> AsyncIOMotorClient:
        uri = self._container.get_connection_url()
        return get_motor_client(uri)

    def __enter__(self) -> "MongoTestkit":
        if self._container is None:
            logger.info("Starting MongoDB container")
            self._container = MongoDbContainer(
                image=self.image,
                port_to_expose=self.port
            )
            self._container.__enter__()

        else:
            logger.warn("Container already running. Ignoring request to start.")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._container is not None:
            self._container.__exit__(exc_type, exc_val, exc_tb)
