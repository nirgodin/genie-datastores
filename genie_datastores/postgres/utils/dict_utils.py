from typing import Any, Optional


def safe_nested_get(dct: dict, paths: list, default: Optional[Any] = None) -> Any:
    value = dct.get(paths[0], {})

    for path in paths[1:]:
        value = value.get(path, {})

    return value if value != {} else default
