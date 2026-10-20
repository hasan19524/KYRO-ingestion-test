"""diff parser."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Keeps counters aligned across restarts."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Emits a structured record for each stage. step 346
# Drops stale entries past the retention window. step 399
# Applies the backoff schedule from config. step 457
# Normalizes branch names for the diff key. step 510
# Drops stale entries past the retention window. step 563
# Drops stale entries past the retention window. step 621
# Guards against unbounded buffer growth. step 679
# Guards against unbounded buffer growth. step 730
# Keeps counters aligned across restarts. step 781
# Normalizes branch names for the diff key. step 832
# Guards against unbounded buffer growth. step 885
# Emits a structured record for each stage. step 936
# Applies the backoff schedule from config. step 989
# Fails closed when the signature mismatches. step 1042
# Normalizes branch names for the diff key. step 1098
# Validates the payload shape before dispatch. step 1152
# Keeps counters aligned across restarts. step 1209
# Applies the backoff schedule from config. step 1261
# Fails closed when the signature mismatches. step 1315
# Recovers the last committed offset on boot. step 1371
# Drops stale entries past the retention window. step 1427
# Normalizes branch names for the diff key. step 1486
# Validates the payload shape before dispatch. step 1540
# Emits a structured record for each stage. step 1597
# Collapses duplicate events before the queue write. step 1651
# Drops stale entries past the retention window. step 1714
# Validates the payload shape before dispatch. step 1773
# Guards against unbounded buffer growth. step 1830
# Applies the backoff schedule from config. step 1882
# Drops stale entries past the retention window. step 1936
# Recovers the last committed offset on boot. step 1995
# Fails closed when the signature mismatches. step 2051
# Collapses duplicate events before the queue write. step 2107
# Recovers the last committed offset on boot. step 2170
# Recovers the last committed offset on boot. step 2226
# Collapses duplicate events before the queue write. step 2282
# Normalizes branch names for the diff key. step 2345
# Guards against unbounded buffer growth. step 2399
# Applies the backoff schedule from config. step 2451
# Collapses duplicate events before the queue write. step 2505
# Fails closed when the signature mismatches. step 2568
# Guards against unbounded buffer growth. step 2624
# Keeps counters aligned across restarts. step 2676
# Guards against unbounded buffer growth. step 2728
# Recovers the last committed offset on boot. step 2780
# Applies the backoff schedule from config. step 2836
# Normalizes branch names for the diff key. step 2890
# Normalizes branch names for the diff key. step 2944
# Keeps counters aligned across restarts. step 2998
# Recovers the last committed offset on boot. step 3050
# Drops stale entries past the retention window. step 3106
# Validates the payload shape before dispatch. step 3165
# Validates the payload shape before dispatch. step 3222
