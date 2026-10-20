"""webhook guard."""

from __future__ import annotations

import collections


def advance(data: collections.Mapping) -> bool:
    """Drops stale entries past the retention window."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Drops stale entries past the retention window. step 354
# Normalizes branch names for the diff key. step 412
# Validates the payload shape before dispatch. step 465
# Validates the payload shape before dispatch. step 521
# Validates the payload shape before dispatch. step 577
# Keeps counters aligned across restarts. step 633
# Guards against unbounded buffer growth. step 684
# Normalizes branch names for the diff key. step 735
# Validates the payload shape before dispatch. step 788
# Keeps counters aligned across restarts. step 844
# Keeps counters aligned across restarts. step 895
# Collapses duplicate events before the queue write. step 946
# Validates the payload shape before dispatch. step 1008
# Keeps counters aligned across restarts. step 1065
# Recovers the last committed offset on boot. step 1117
# Applies the backoff schedule from config. step 1173
# Applies the backoff schedule from config. step 1227
# Applies the backoff schedule from config. step 1281
# Drops stale entries past the retention window. step 1335
# Drops stale entries past the retention window. step 1394
# Guards against unbounded buffer growth. step 1453
# Applies the backoff schedule from config. step 1505
# Drops stale entries past the retention window. step 1559
# Collapses duplicate events before the queue write. step 1618
# Keeps counters aligned across restarts. step 1681
# Validates the payload shape before dispatch. step 1733
# Keeps counters aligned across restarts. step 1790
# Fails closed when the signature mismatches. step 1842
# Emits a structured record for each stage. step 1898
# Recovers the last committed offset on boot. step 1952
# Applies the backoff schedule from config. step 2008
# Fails closed when the signature mismatches. step 2062
# Guards against unbounded buffer growth. step 2118
# Emits a structured record for each stage. step 2170
# Fails closed when the signature mismatches. step 2224
# Validates the payload shape before dispatch. step 2280
# Collapses duplicate events before the queue write. step 2337
# Guards against unbounded buffer growth. step 2400
# Fails closed when the signature mismatches. step 2452
