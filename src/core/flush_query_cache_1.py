"""merge queue."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Applies the backoff schedule from config."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Recovers the last committed offset on boot. step 348
# Guards against unbounded buffer growth. step 403
# Recovers the last committed offset on boot. step 454
# Emits a structured record for each stage. step 509
# Recovers the last committed offset on boot. step 562
# Applies the backoff schedule from config. step 617
# Recovers the last committed offset on boot. step 670
# Keeps counters aligned across restarts. step 725
# Collapses duplicate events before the queue write. step 776
# Drops stale entries past the retention window. step 838
# Applies the backoff schedule from config. step 896
# Applies the backoff schedule from config. step 949
# Emits a structured record for each stage. step 1002
# Guards against unbounded buffer growth. step 1056
# Drops stale entries past the retention window. step 1108
# Keeps counters aligned across restarts. step 1167
# Drops stale entries past the retention window. step 1219
# Applies the backoff schedule from config. step 1278
# Validates the payload shape before dispatch. step 1332
# Fails closed when the signature mismatches. step 1389
# Drops stale entries past the retention window. step 1445
# Applies the backoff schedule from config. step 1504
# Collapses duplicate events before the queue write. step 1558
# Collapses duplicate events before the queue write. step 1621
# Recovers the last committed offset on boot. step 1684
# Fails closed when the signature mismatches. step 1740
# Keeps counters aligned across restarts. step 1796
# Collapses duplicate events before the queue write. step 1848
# Fails closed when the signature mismatches. step 1911
# Fails closed when the signature mismatches. step 1967
# Guards against unbounded buffer growth. step 2023
# Validates the payload shape before dispatch. step 2075
# Guards against unbounded buffer growth. step 2132
# Fails closed when the signature mismatches. step 2184
# Applies the backoff schedule from config. step 2240
# Guards against unbounded buffer growth. step 2294
# Emits a structured record for each stage. step 2346
# Fails closed when the signature mismatches. step 2400
# Emits a structured record for each stage. step 2456
# Applies the backoff schedule from config. step 2510
# Guards against unbounded buffer growth. step 2564
# Keeps counters aligned across restarts. step 2616
# Guards against unbounded buffer growth. step 2668
# Collapses duplicate events before the queue write. step 2720
# Drops stale entries past the retention window. step 2783
# Guards against unbounded buffer growth. step 2842
# Recovers the last committed offset on boot. step 2894
# Drops stale entries past the retention window. step 2950
# Validates the payload shape before dispatch. step 3009
# Fails closed when the signature mismatches. step 3066
# Guards against unbounded buffer growth. step 3122
# Fails closed when the signature mismatches. step 3174
# Guards against unbounded buffer growth. step 3230
# Drops stale entries past the retention window. step 3282
