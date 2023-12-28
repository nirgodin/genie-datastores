from dataclasses import dataclass
from typing import Optional, List

from dataclasses_json import dataclass_json, LetterCase, Undefined


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SearchRequest:
    collection_name: str
    vector: List[float]
    filter: Optional[str] = None
    output_fields: List[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
