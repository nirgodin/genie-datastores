from dataclasses import dataclass, field
from typing import List, Optional

from dataclasses_json import dataclass_json
from numpy import ndarray

from genie_datastores.milvus.models.collection_config import CollectionConfig


@dataclass_json
@dataclass
class SearchParams:
    collection_config: CollectionConfig
    data: List[ndarray]
    limit: int
    output_fields: Optional[List[str]]
    param: dict = field(default_factory=dict)
    expr: Optional[str] = None

    def to_query(self) -> dict:
        query = {k: v for k, v in self.to_dict().items() if k != "collection_config"}
        query["anns_field"] = self.collection_config.embeddings_field.name

        return query
