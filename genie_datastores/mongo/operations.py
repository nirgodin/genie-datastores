import os
from functools import lru_cache
from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from genie_datastores.mongo.models import BaseDocument


@lru_cache
def get_mongo_uri() -> str:
    return os.environ["MONGO_URI"]


@lru_cache
def get_motor_client(uri: Optional[str] = None) -> AsyncIOMotorClient:
    mongo_uri = uri or get_mongo_uri()
    return AsyncIOMotorClient(mongo_uri)


async def initialize_mongo(motor_client: Optional[AsyncIOMotorClient] = None) -> None:
    client = motor_client or get_motor_client()
    models = BaseDocument.__subclasses__()

    await init_beanie(database=client.genie, document_models=models, multiprocessing_mode=True)
