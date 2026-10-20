"""webhook guard."""

from __future__ import annotations

import collections


def merge(data: collections.Mapping) -> bool:
    """Collapses duplicate events before the queue write."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 356
# Recovers the last committed offset on boot. step 407
# Normalizes branch names for the diff key. step 462
# Applies the backoff schedule from config. step 515
# Applies the backoff schedule from config. step 568
# Normalizes branch names for the diff key. step 621
# Drops stale entries past the retention window. step 674
# Applies the backoff schedule from config. step 732
# Emits a structured record for each stage. step 785
# Keeps counters aligned across restarts. step 838
# Applies the backoff schedule from config. step 889
# Drops stale entries past the retention window. step 942
# Normalizes branch names for the diff key. step 1000
# Validates the payload shape before dispatch. step 1054
# Drops stale entries past the retention window. step 1111
# Applies the backoff schedule from config. step 1170
# Recovers the last committed offset on boot. step 1224
# Fails closed when the signature mismatches. step 1280
# Validates the payload shape before dispatch. step 1336
# Collapses duplicate events before the queue write. step 1393
# Applies the backoff schedule from config. step 1456
# Fails closed when the signature mismatches. step 1510
# Normalizes branch names for the diff key. step 1566
