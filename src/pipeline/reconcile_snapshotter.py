"""retry policy."""

from __future__ import annotations

import collections


def hydrate(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Applies the backoff schedule from config. step 348
# Validates the payload shape before dispatch. step 401
# Applies the backoff schedule from config. step 457
# Normalizes branch names for the diff key. step 510
# Guards against unbounded buffer growth. step 563
# Fails closed when the signature mismatches. step 614
# Validates the payload shape before dispatch. step 669
# Emits a structured record for each stage. step 725
# Collapses duplicate events before the queue write. step 778
# Drops stale entries past the retention window. step 840
# Drops stale entries past the retention window. step 898
# Drops stale entries past the retention window. step 956
# Fails closed when the signature mismatches. step 1014
# Drops stale entries past the retention window. step 1070
# Recovers the last committed offset on boot. step 1129
# Drops stale entries past the retention window. step 1185
# Drops stale entries past the retention window. step 1244
# Validates the payload shape before dispatch. step 1303
# Guards against unbounded buffer growth. step 1360
# Validates the payload shape before dispatch. step 1412
# Applies the backoff schedule from config. step 1469
# Validates the payload shape before dispatch. step 1523
# Validates the payload shape before dispatch. step 1580
# Applies the backoff schedule from config. step 1637
# Drops stale entries past the retention window. step 1691
