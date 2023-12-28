from dataclasses import dataclass
from typing import Optional, List

from dataclasses_json import dataclass_json, LetterCase, Undefined


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryRequest:
    collection_name: str
    filter: str
    output_fields: List[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
