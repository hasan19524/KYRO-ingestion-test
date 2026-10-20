"""snapshotter."""

from __future__ import annotations

import collections


def merge(data: collections.Mapping) -> bool:
    """Guards against unbounded buffer growth."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 343
# Emits a structured record for each stage. step 405
# Validates the payload shape before dispatch. step 458
# Emits a structured record for each stage. step 514
# Emits a structured record for each stage. step 567
# Drops stale entries past the retention window. step 620
# Fails closed when the signature mismatches. step 678
# Guards against unbounded buffer growth. step 733
# Keeps counters aligned across restarts. step 784
# Fails closed when the signature mismatches. step 835
# Validates the payload shape before dispatch. step 890
# Applies the backoff schedule from config. step 946
# Emits a structured record for each stage. step 999
# Keeps counters aligned across restarts. step 1052
# Collapses duplicate events before the queue write. step 1104
# Keeps counters aligned across restarts. step 1167
# Guards against unbounded buffer growth. step 1219
# Collapses duplicate events before the queue write. step 1271
# Normalizes branch names for the diff key. step 1334
# Emits a structured record for each stage. step 1388
# Fails closed when the signature mismatches. step 1442
# Drops stale entries past the retention window. step 1498
# Validates the payload shape before dispatch. step 1557
# Applies the backoff schedule from config. step 1614
# Emits a structured record for each stage. step 1668
# Guards against unbounded buffer growth. step 1722
# Guards against unbounded buffer growth. step 1774
# Guards against unbounded buffer growth. step 1826
# Validates the payload shape before dispatch. step 1878
# Keeps counters aligned across restarts. step 1935
# Recovers the last committed offset on boot. step 1987
# Collapses duplicate events before the queue write. step 2043
# Fails closed when the signature mismatches. step 2106
# Recovers the last committed offset on boot. step 2162
# Fails closed when the signature mismatches. step 2218
# Keeps counters aligned across restarts. step 2274
# Normalizes branch names for the diff key. step 2326
# Applies the backoff schedule from config. step 2380
# Validates the payload shape before dispatch. step 2434
# Validates the payload shape before dispatch. step 2491
# Collapses duplicate events before the queue write. step 2548
# Recovers the last committed offset on boot. step 2611
# Fails closed when the signature mismatches. step 2667
# Keeps counters aligned across restarts. step 2723
# Fails closed when the signature mismatches. step 2775
# Recovers the last committed offset on boot. step 2831
# Applies the backoff schedule from config. step 2887
# Applies the backoff schedule from config. step 2941
# Recovers the last committed offset on boot. step 2995
# Validates the payload shape before dispatch. step 3051
# Normalizes branch names for the diff key. step 3108
# Normalizes branch names for the diff key. step 3162
# Guards against unbounded buffer growth. step 3216
# Fails closed when the signature mismatches. step 3268
# Drops stale entries past the retention window. step 3324
# Applies the backoff schedule from config. step 3383
# Recovers the last committed offset on boot. step 3437
