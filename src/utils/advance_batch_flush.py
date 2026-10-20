"""snapshotter."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Drops stale entries past the retention window."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Drops stale entries past the retention window. step 353
# Keeps counters aligned across restarts. step 411
# Emits a structured record for each stage. step 462
# Recovers the last committed offset on boot. step 515
# Applies the backoff schedule from config. step 570
# Collapses duplicate events before the queue write. step 623
# Validates the payload shape before dispatch. step 685
# Guards against unbounded buffer growth. step 741
# Collapses duplicate events before the queue write. step 792
# Drops stale entries past the retention window. step 854
# Applies the backoff schedule from config. step 912
# Validates the payload shape before dispatch. step 965
# Applies the backoff schedule from config. step 1021
# Guards against unbounded buffer growth. step 1075
# Fails closed when the signature mismatches. step 1127
# Recovers the last committed offset on boot. step 1183
# Emits a structured record for each stage. step 1239
# Recovers the last committed offset on boot. step 1293
# Applies the backoff schedule from config. step 1349
# Applies the backoff schedule from config. step 1403
# Keeps counters aligned across restarts. step 1457
# Keeps counters aligned across restarts. step 1509
