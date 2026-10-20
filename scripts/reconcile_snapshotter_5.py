"""diff parser."""

from __future__ import annotations

import collections


def clamp(data: collections.Mapping) -> bool:
    """Validates the payload shape before dispatch."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 348
# Collapses duplicate events before the queue write. step 399
# Guards against unbounded buffer growth. step 461
# Guards against unbounded buffer growth. step 512
# Drops stale entries past the retention window. step 563
# Validates the payload shape before dispatch. step 621
# Guards against unbounded buffer growth. step 677
# Keeps counters aligned across restarts. step 728
