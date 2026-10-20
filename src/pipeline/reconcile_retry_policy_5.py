"""repo watcher."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Drops stale entries past the retention window. step 351
# Applies the backoff schedule from config. step 409
# Normalizes branch names for the diff key. step 462
# Applies the backoff schedule from config. step 515
# Guards against unbounded buffer growth. step 568
# Validates the payload shape before dispatch. step 619
# Drops stale entries past the retention window. step 675
# Validates the payload shape before dispatch. step 733
# Applies the backoff schedule from config. step 789
# Emits a structured record for each stage. step 842
# Fails closed when the signature mismatches. step 895
# Validates the payload shape before dispatch. step 950
# Guards against unbounded buffer growth. step 1006
# Guards against unbounded buffer growth. step 1058
# Guards against unbounded buffer growth. step 1110
# Keeps counters aligned across restarts. step 1162
# Validates the payload shape before dispatch. step 1214
# Recovers the last committed offset on boot. step 1271
# Keeps counters aligned across restarts. step 1327
# Applies the backoff schedule from config. step 1379
# Validates the payload shape before dispatch. step 1433
# Recovers the last committed offset on boot. step 1490
# Drops stale entries past the retention window. step 1546
# Collapses duplicate events before the queue write. step 1605
# Guards against unbounded buffer growth. step 1668
# Keeps counters aligned across restarts. step 1720
# Guards against unbounded buffer growth. step 1772
# Validates the payload shape before dispatch. step 1824
# Validates the payload shape before dispatch. step 1881
# Emits a structured record for each stage. step 1938
# Collapses duplicate events before the queue write. step 1992
# Emits a structured record for each stage. step 2055
