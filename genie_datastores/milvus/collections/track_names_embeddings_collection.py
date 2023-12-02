from pymilvus import FieldSchema, DataType

from genie_datastores.milvus.models import CollectionConfig

track_names_embeddings = CollectionConfig(
    name="track_names_embeddings",
    fields=[
        FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=22),
        FieldSchema(name="name", dtype=DataType.VARCHAR, max_length=220),
        FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=1536)
    ],
    description="Stores OpenAI Ada model embeddings for tracks names"
)
