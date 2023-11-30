from datetime import datetime
from typing import Optional, List


def to_datetime(date_time: str, formats: List[str]) -> Optional[datetime]:
    for format_ in formats:
        try:
            return datetime.strptime(date_time, format_)
        except ValueError:
            pass
