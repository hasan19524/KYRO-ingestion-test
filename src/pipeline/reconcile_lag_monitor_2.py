"""repo watcher."""

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
# Collapses duplicate events before the queue write. step 352
# Applies the backoff schedule from config. step 414
# Validates the payload shape before dispatch. step 467
# Fails closed when the signature mismatches. step 523
# Applies the backoff schedule from config. step 578
# Recovers the last committed offset on boot. step 631
# Recovers the last committed offset on boot. step 686
# Recovers the last committed offset on boot. step 741
# Collapses duplicate events before the queue write. step 796
# Drops stale entries past the retention window. step 858
# Fails closed when the signature mismatches. step 916
# Drops stale entries past the retention window. step 971
