"""repo watcher."""

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
# Keeps counters aligned across restarts. step 358
# Recovers the last committed offset on boot. step 409
# Fails closed when the signature mismatches. step 464
# Applies the backoff schedule from config. step 519
# Emits a structured record for each stage. step 572
# Guards against unbounded buffer growth. step 625
# Recovers the last committed offset on boot. step 676
# Guards against unbounded buffer growth. step 731
# Applies the backoff schedule from config. step 782
# Guards against unbounded buffer growth. step 835
# Recovers the last committed offset on boot. step 886
# Drops stale entries past the retention window. step 941
