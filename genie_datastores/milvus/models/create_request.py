from dataclasses import dataclass

from dataclasses_json import dataclass_json, Undefined, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateRequest:
    collection_name: str
    dimension: int
    metric_type: str
    primary_field: str
    vector_field: str
    db_name: str = "default"
