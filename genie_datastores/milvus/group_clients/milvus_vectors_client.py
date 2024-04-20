from typing import List

from genie_common.clients import BaseWebClient

from genie_datastores.milvus.consts import COLLECTION_NAME, DATA
from genie_datastores.milvus.models import QueryRequest, SearchRequest


class MilvusVectorsClient(BaseWebClient):
    async def insert(self, collection_name: str, records: List[dict]) -> None:
        payload = {
            COLLECTION_NAME: collection_name,
            DATA: records
        }
        await self._post(route="insert", payload=payload)

    async def query(self, request: QueryRequest):
        response = await self._post(
            route="query",
            payload=request.to_dict()
        )
        return response[DATA]

    async def search(self, request: SearchRequest):
        response = await self._post(
            route="search",
            payload=request.to_dict()
        )
        return response[DATA]

    @property
    def _route(self) -> str:
        return "v1/vector"
