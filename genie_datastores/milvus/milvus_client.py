from typing import Optional

from aiohttp import ClientSession
from genie_common.clients.utils import build_authorization_headers, create_client_session

from genie_datastores.milvus.group_clients import MilvusCollectionsClient, MilvusVectorsClient


class MilvusClient:
    def __init__(self,
                 uri: str,
                 token: Optional[str] = None,
                 session: Optional[ClientSession] = None,
                 wrap_exceptions: bool = True,
                 collections: Optional[MilvusCollectionsClient] = None,
                 vectors: Optional[MilvusVectorsClient] = None):
        self._uri = uri
        self._token = token
        self._session = session
        self._wrap_exceptions = wrap_exceptions
        self.collections = collections
        self.vectors = vectors

    async def __aenter__(self) -> "MilvusClient":
        await self._initialize_session()
        if self.collections is None:
            self.collections = MilvusCollectionsClient(
                base_url=self._uri,
                session=self._session,
                wrap_exceptions=self._wrap_exceptions
            )

        if self.vectors is None:
            self.vectors = MilvusVectorsClient(
                base_url=self._uri,
                session=self._session,
                wrap_exceptions=self._wrap_exceptions
            )

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._session.__aexit__(exc_type, exc_val, exc_tb)
        self.vectors = None
        self.collections = None

    async def _initialize_session(self) -> None:
        if self._session is None:
            headers = None if self._token is None else build_authorization_headers(self._token)
            raw_session = create_client_session(headers)
            self._session = await raw_session.__aenter__()
