"""rate limiter."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Validates the payload shape before dispatch."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Normalizes branch names for the diff key. step 352
# Fails closed when the signature mismatches. step 405
# Applies the backoff schedule from config. step 460
# Emits a structured record for each stage. step 513
# Fails closed when the signature mismatches. step 566
# Normalizes branch names for the diff key. step 621
# Collapses duplicate events before the queue write. step 674
# Drops stale entries past the retention window. step 736
# Keeps counters aligned across restarts. step 794
# Applies the backoff schedule from config. step 845
# Applies the backoff schedule from config. step 898
# Applies the backoff schedule from config. step 951
# Emits a structured record for each stage. step 1004
# Guards against unbounded buffer growth. step 1058
# Normalizes branch names for the diff key. step 1110
# Collapses duplicate events before the queue write. step 1164
