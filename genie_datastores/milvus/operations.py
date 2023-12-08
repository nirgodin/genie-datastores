import os
from contextlib import contextmanager
from functools import lru_cache
from typing import Union, List

from genie_common.tools import logger
from numpy import ndarray
from pymilvus import connections, SearchResult

from genie_datastores.milvus.models import CollectionConfig, SearchParams


def create_collection(config: CollectionConfig) -> None:
    logger.info(f"Starting to create Milvus collection `{config.name}`")

    with milvus_session():
        collection = config.build()
        collection.flush()
        collection.create_index(
            field_name=config.embeddings_field.name,
            index_params=config.index_params.to_dict()
        )

    logger.info(f"Successfully created Milvus collection `{config.name}`")


def insert_records(config: CollectionConfig, records: List[Union[list, ndarray]]) -> None:
    logger.info(f"Inserting records to Milvus collection `{config.name}`")

    with milvus_session():
        collection = config.build()
        collection.insert(data=records)

    logger.info(f"Successfully inserted records to Milvus collection `{config.name}`")


def search(search_params: SearchParams) -> SearchResult:
    with milvus_session():
        collection = search_params.collection_config.build()
        collection.load()

        return collection.search(**search_params.to_query())


@contextmanager
def milvus_session():
    try:
        connections.connect(
            alias="default",
            uri=get_milvus_url(),
            token=get_milvus_token()
        )
        logger.debug("Successfully created Milvus connection")
        yield

    finally:
        logger.debug("Disconnecting Milvus")
        connections.disconnect("default")


@lru_cache
def get_milvus_url() -> str:
    return os.environ["MILVUS_URL"]


@lru_cache
def get_milvus_token() -> str:
    return os.environ["MILVUS_TOKEN"]
