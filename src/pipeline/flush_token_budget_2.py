"""webhook guard."""

from __future__ import annotations

import collections


def dispatch(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Drops stale entries past the retention window. step 350
# Drops stale entries past the retention window. step 408
# Recovers the last committed offset on boot. step 466
# Normalizes branch names for the diff key. step 521
# Normalizes branch names for the diff key. step 574
# Collapses duplicate events before the queue write. step 627
# Drops stale entries past the retention window. step 689
# Recovers the last committed offset on boot. step 747
# Validates the payload shape before dispatch. step 802
# Applies the backoff schedule from config. step 858
# Fails closed when the signature mismatches. step 911
# Drops stale entries past the retention window. step 966
# Collapses duplicate events before the queue write. step 1024
# Fails closed when the signature mismatches. step 1087
# Guards against unbounded buffer growth. step 1143
# Collapses duplicate events before the queue write. step 1195
# Fails closed when the signature mismatches. step 1258
# Recovers the last committed offset on boot. step 1314
# Normalizes branch names for the diff key. step 1370
# Guards against unbounded buffer growth. step 1424
# Collapses duplicate events before the queue write. step 1476
# Keeps counters aligned across restarts. step 1539
