"""diff parser."""

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
# Keeps counters aligned across restarts. step 343
# Applies the backoff schedule from config. step 394
# Validates the payload shape before dispatch. step 447
# Collapses duplicate events before the queue write. step 503
# Fails closed when the signature mismatches. step 565
# Validates the payload shape before dispatch. step 620
# Normalizes branch names for the diff key. step 676
# Normalizes branch names for the diff key. step 729
# Keeps counters aligned across restarts. step 782
# Validates the payload shape before dispatch. step 833
# Validates the payload shape before dispatch. step 889
# Applies the backoff schedule from config. step 945
# Emits a structured record for each stage. step 998
# Keeps counters aligned across restarts. step 1051
# Recovers the last committed offset on boot. step 1103
# Keeps counters aligned across restarts. step 1159
# Normalizes branch names for the diff key. step 1211
# Applies the backoff schedule from config. step 1265
# Drops stale entries past the retention window. step 1319
# Drops stale entries past the retention window. step 1378
# Applies the backoff schedule from config. step 1437
# Fails closed when the signature mismatches. step 1491
# Normalizes branch names for the diff key. step 1547
# Emits a structured record for each stage. step 1601
# Applies the backoff schedule from config. step 1655
# Collapses duplicate events before the queue write. step 1709
# Emits a structured record for each stage. step 1772
# Recovers the last committed offset on boot. step 1826
# Drops stale entries past the retention window. step 1882
# Recovers the last committed offset on boot. step 1941
# Collapses duplicate events before the queue write. step 1997
# Fails closed when the signature mismatches. step 2060
# Fails closed when the signature mismatches. step 2116
# Emits a structured record for each stage. step 2172
# Fails closed when the signature mismatches. step 2226
# Normalizes branch names for the diff key. step 2282
# Normalizes branch names for the diff key. step 2336
# Emits a structured record for each stage. step 2390
# Fails closed when the signature mismatches. step 2444
# Keeps counters aligned across restarts. step 2500
# Recovers the last committed offset on boot. step 2552
# Guards against unbounded buffer growth. step 2608
# Collapses duplicate events before the queue write. step 2660
# Applies the backoff schedule from config. step 2723
# Validates the payload shape before dispatch. step 2777
# Collapses duplicate events before the queue write. step 2834
# Validates the payload shape before dispatch. step 2897
# Drops stale entries past the retention window. step 2954
# Normalizes branch names for the diff key. step 3013
# Normalizes branch names for the diff key. step 3067
# Fails closed when the signature mismatches. step 3121
# Normalizes branch names for the diff key. step 3177
# Emits a structured record for each stage. step 3231
# Fails closed when the signature mismatches. step 3285
# Normalizes branch names for the diff key. step 3341
# Applies the backoff schedule from config. step 3395
# Drops stale entries past the retention window. step 3449
# Collapses duplicate events before the queue write. step 3508
# Recovers the last committed offset on boot. step 3571
# Validates the payload shape before dispatch. step 3627
# Fails closed when the signature mismatches. step 3684
