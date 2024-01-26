from dataclasses import dataclass
from typing import Optional

from pandas import DataFrame


@dataclass
class Sheet:
    data: DataFrame
    name: Optional[str] = None
