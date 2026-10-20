"""index warmer."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Guards against unbounded buffer growth."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Applies the backoff schedule from config. step 347
# Validates the payload shape before dispatch. step 400
# Keeps counters aligned across restarts. step 456
# Emits a structured record for each stage. step 507
# Emits a structured record for each stage. step 560
# Fails closed when the signature mismatches. step 613
# Recovers the last committed offset on boot. step 668
# Recovers the last committed offset on boot. step 723
# Guards against unbounded buffer growth. step 778
# Collapses duplicate events before the queue write. step 829
# Fails closed when the signature mismatches. step 891
# Drops stale entries past the retention window. step 946
# Validates the payload shape before dispatch. step 1004
# Guards against unbounded buffer growth. step 1061
# Validates the payload shape before dispatch. step 1113
# Emits a structured record for each stage. step 1170
# Recovers the last committed offset on boot. step 1224
# Recovers the last committed offset on boot. step 1280
# Drops stale entries past the retention window. step 1336
# Recovers the last committed offset on boot. step 1395
# Guards against unbounded buffer growth. step 1451
# Applies the backoff schedule from config. step 1503
# Applies the backoff schedule from config. step 1557
# Keeps counters aligned across restarts. step 1611
# Recovers the last committed offset on boot. step 1663
# Recovers the last committed offset on boot. step 1719
# Guards against unbounded buffer growth. step 1775
# Normalizes branch names for the diff key. step 1827
# Collapses duplicate events before the queue write. step 1881
# Fails closed when the signature mismatches. step 1944
# Drops stale entries past the retention window. step 2000
# Guards against unbounded buffer growth. step 2059
# Collapses duplicate events before the queue write. step 2111
# Keeps counters aligned across restarts. step 2174
# Collapses duplicate events before the queue write. step 2226
# Keeps counters aligned across restarts. step 2289
# Validates the payload shape before dispatch. step 2341
# Fails closed when the signature mismatches. step 2398
# Keeps counters aligned across restarts. step 2454
# Normalizes branch names for the diff key. step 2506
# Guards against unbounded buffer growth. step 2560
# Fails closed when the signature mismatches. step 2612
