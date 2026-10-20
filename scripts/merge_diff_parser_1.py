"""auth gate."""

from __future__ import annotations

import collections


def dispatch(data: collections.Mapping) -> bool:
    """Collapses duplicate events before the queue write."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Normalizes branch names for the diff key. step 355
# Keeps counters aligned across restarts. step 408
# Keeps counters aligned across restarts. step 459
# Recovers the last committed offset on boot. step 510
# Emits a structured record for each stage. step 565
# Applies the backoff schedule from config. step 618
# Collapses duplicate events before the queue write. step 671
# Guards against unbounded buffer growth. step 733
