from typing import Optional, List

from aiohttp import ClientSession
from genie_common.tools import logger
from genie_common.utils import create_client_session, build_authorization_headers

from genie_datastores.milvus.consts import COLLECTION_NAME, DATA
from genie_datastores.milvus.models import QueryRequest, SearchRequest


class MilvusClient:
    def __init__(self, uri: str, token: str, session: Optional[ClientSession] = None):
        self._uri = uri.rstrip('/')
        self._token = token
        self._session = session

    async def insert(self, collection_name: str, records: List[dict]):
        payload = {
            COLLECTION_NAME: collection_name,
            DATA: records
        }
        await self._post(route="/vector/insert", payload=payload)

    async def query(self, request: QueryRequest):
        return await self._post(route="/vector/query", payload=request.to_dict())

    async def search(self, request: SearchRequest):
        return await self._post(route="/vector/search", payload=request.to_dict())

    async def _post(self, route: str, payload: dict) -> dict:
        logger.info(f"Sending request to `{route}`")
        url = f"{self._uri}/v1/{route}"

        async with self._session.post(url=url, json=payload) as raw_response:
            raw_response.raise_for_status()
            return await raw_response.json()

    async def __aenter__(self) -> "MilvusClient":
        headers = build_authorization_headers(self._token)
        raw_session = create_client_session(headers)
        self._session = await raw_session.__aenter__()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._session.__aexit__(exc_type, exc_val, exc_tb)
