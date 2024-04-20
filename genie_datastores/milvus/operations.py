import os
from contextlib import asynccontextmanager
from functools import lru_cache
from typing import List, Optional

from genie_datastores.milvus import MilvusClient
from genie_datastores.milvus.models import CreateRequest
from genie_datastores.milvus.utils import get_track_names_embeddings_create_request


@lru_cache
def get_milvus_uri() -> str:
    return os.environ["MILVUS_URI"]


@lru_cache
def get_milvus_token() -> str:
    return os.environ["MILVUS_TOKEN"]


@asynccontextmanager
async def milvus_session(milvus_client: MilvusClient, create_requests: Optional[List[CreateRequest]] = None) -> None:
    requests = create_requests or _get_default_create_requests()

    try:
        for request in requests:
            await milvus_client.collections.create(request)

        yield

    finally:
        for request in create_requests:
            await milvus_client.collections.drop(request.collection_name)


def _get_default_create_requests() -> List[CreateRequest]:
    return [get_track_names_embeddings_create_request()]
