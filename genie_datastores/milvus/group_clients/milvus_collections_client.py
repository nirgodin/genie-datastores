from typing import List, Any, Dict

from genie_common.clients import BaseWebClient

from genie_datastores.milvus.consts import DATA, COLLECTION_NAME
from genie_datastores.milvus.models import CreateRequest


class MilvusCollectionsClient(BaseWebClient):
    async def create(self, request: CreateRequest) -> None:
        await self._post(
            route="create",
            payload=request.to_dict()
        )

    async def describe(self, collection_name: str) -> Dict[str, Any]:
        response = await self._get(
            route="describe",
            params={COLLECTION_NAME: collection_name}
        )
        return response[DATA]

    async def drop(self, collection_name: str) -> None:
        await self._post(
            route="drop",
            payload={COLLECTION_NAME: collection_name}
        )

    async def list(self) -> List[str]:
        response = await self._get()
        return response[DATA]

    @property
    def _route(self) -> str:
        return "v1/vector/collections"
