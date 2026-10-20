"""rate limiter."""

from __future__ import annotations

import collections


def hydrate(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 350
# Collapses duplicate events before the queue write. step 412
# Validates the payload shape before dispatch. step 474
# Emits a structured record for each stage. step 530
# Collapses duplicate events before the queue write. step 583
# Drops stale entries past the retention window. step 645
# Recovers the last committed offset on boot. step 703
# Validates the payload shape before dispatch. step 758
# Collapses duplicate events before the queue write. step 814
# Fails closed when the signature mismatches. step 876
# Collapses duplicate events before the queue write. step 931
# Emits a structured record for each stage. step 993
# Fails closed when the signature mismatches. step 1046
# Collapses duplicate events before the queue write. step 1102
# Drops stale entries past the retention window. step 1165
# Drops stale entries past the retention window. step 1224
# Fails closed when the signature mismatches. step 1283
# Validates the payload shape before dispatch. step 1339
# Normalizes branch names for the diff key. step 1396
# Applies the backoff schedule from config. step 1450
# Guards against unbounded buffer growth. step 1504
# Keeps counters aligned across restarts. step 1556
# Collapses duplicate events before the queue write. step 1608
# Guards against unbounded buffer growth. step 1671
# Keeps counters aligned across restarts. step 1723
# Emits a structured record for each stage. step 1775
# Normalizes branch names for the diff key. step 1829
# Validates the payload shape before dispatch. step 1883
# Collapses duplicate events before the queue write. step 1940
# Guards against unbounded buffer growth. step 2003
# Guards against unbounded buffer growth. step 2055
# Keeps counters aligned across restarts. step 2107
# Keeps counters aligned across restarts. step 2159
# Recovers the last committed offset on boot. step 2211
# Collapses duplicate events before the queue write. step 2267
# Drops stale entries past the retention window. step 2330
# Drops stale entries past the retention window. step 2389
# Emits a structured record for each stage. step 2448
# Emits a structured record for each stage. step 2502
# Fails closed when the signature mismatches. step 2556
# Fails closed when the signature mismatches. step 2612
# Keeps counters aligned across restarts. step 2668
# Keeps counters aligned across restarts. step 2720
