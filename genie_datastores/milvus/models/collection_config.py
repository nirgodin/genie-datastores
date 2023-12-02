from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json
from pymilvus import FieldSchema, Collection, CollectionSchema, DataType

from genie_datastores.milvus.models.index_params import IndexParams


@dataclass_json
@dataclass
class CollectionConfig:
    name: str
    fields: List[FieldSchema]
    index_params: IndexParams = IndexParams()
    description: str = ""

    def __post_init__(self):
        self.embeddings_field = self._extract_embeddings_field()

    def build(self) -> Collection:
        return Collection(
            name=self.name,
            schema=CollectionSchema(self.fields, self.description)
        )

    def _extract_embeddings_field(self) -> FieldSchema:
        for field in self.fields:
            if field.dtype == DataType.FLOAT_VECTOR:
                return field

        raise ValueError("Did not find any embeddings field")
