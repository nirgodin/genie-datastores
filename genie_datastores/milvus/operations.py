import os
from functools import lru_cache


@lru_cache
def get_milvus_uri() -> str:
    return os.environ["MILVUS_URI"]


@lru_cache
def get_milvus_token() -> str:
    return os.environ["MILVUS_TOKEN"]
