import os
from contextlib import asynccontextmanager
from functools import lru_cache
from typing import List

from genie_datastores.milvus import MilvusClient
from genie_datastores.milvus.models import CreateRequest


@lru_cache
def get_milvus_uri() -> str:
    return os.environ["MILVUS_URI"]


@lru_cache
def get_milvus_token() -> str:
    return os.environ["MILVUS_TOKEN"]


@asynccontextmanager
async def milvus_session(milvus_client: MilvusClient, create_requests: List[CreateRequest]) -> None:
    try:
        for request in create_requests:
            await milvus_client.collections.create(request)

        yield

    finally:
        for request in create_requests:
            await milvus_client.collections.drop(request.collection_name)
