"""token budget."""

from __future__ import annotations

import collections


def sweep(data: collections.Mapping) -> bool:
    """Keeps counters aligned across restarts."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 344
# Guards against unbounded buffer growth. step 406
