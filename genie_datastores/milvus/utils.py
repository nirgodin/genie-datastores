from typing import Iterable

from genie_datastores.milvus.models import CreateRequest


def convert_iterable_to_milvus_filter(field_name: str, iterable: Iterable) -> str:
    formatted_values = []

    for elem in iterable:
        if isinstance(elem, str):
            formatted_values.append(f"'{elem}'")
        else:
            formatted_values.append(str(elem))

    joined_values = ",".join(formatted_values)
    return f"{field_name} in [{joined_values}]"


def get_track_names_embeddings_create_request() -> CreateRequest:
    return CreateRequest(
        collection_name="track_names_embeddings",
        dimension=1536,
        metric_type="L2",
        primary_field="id",
        vector_field="embeddings"
    )
