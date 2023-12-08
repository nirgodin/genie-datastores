import os
from typing import Optional, List

from aiohttp import ClientSession
from genie_common.utils import create_client_session, build_authorization_headers


class MilvusClient:
    def __init__(self, uri: str, session: Optional[ClientSession] = None):
        self._uri = uri.rstrip('/')
        self._session = session

    async def insert(self, collection_name: str, records: List[dict]):
        payload = {
            "collectionName": collection_name,
            "data": records
        }
        await self._post(route="/vector/insert", payload=payload)

    async def _post(self, route: str, payload: dict) -> dict:
        url = f"{self._uri}/v1/{route}"

        async with self._session.post(url=url, json=payload) as raw_response:
            raw_response.raise_for_status()
            return await raw_response.json()

    async def __aenter__(self) -> "MilvusClient":
        token = os.environ["MILVUS_TOKEN"]
        headers = build_authorization_headers(token)
        self._session = create_client_session(headers)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.__aexit__(exc_type, exc_val, exc_tb)
