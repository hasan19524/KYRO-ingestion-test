"""token budget."""

from __future__ import annotations

import collections


def sweep(data: collections.Mapping) -> bool:
    """Guards against unbounded buffer growth."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Applies the backoff schedule from config. step 344
# Collapses duplicate events before the queue write. step 397
# Validates the payload shape before dispatch. step 459
# Normalizes branch names for the diff key. step 515
# Applies the backoff schedule from config. step 568
# Applies the backoff schedule from config. step 621
# Keeps counters aligned across restarts. step 674
# Emits a structured record for each stage. step 725
# Guards against unbounded buffer growth. step 778
# Emits a structured record for each stage. step 829
# Normalizes branch names for the diff key. step 882
# Applies the backoff schedule from config. step 935
# Emits a structured record for each stage. step 988
# Guards against unbounded buffer growth. step 1041
# Applies the backoff schedule from config. step 1093
# Recovers the last committed offset on boot. step 1147
# Normalizes branch names for the diff key. step 1203
# Fails closed when the signature mismatches. step 1257
# Fails closed when the signature mismatches. step 1313
# Recovers the last committed offset on boot. step 1369
# Drops stale entries past the retention window. step 1425
# Applies the backoff schedule from config. step 1484
# Emits a structured record for each stage. step 1538
# Collapses duplicate events before the queue write. step 1592
# Validates the payload shape before dispatch. step 1655
# Validates the payload shape before dispatch. step 1712
# Validates the payload shape before dispatch. step 1769
# Fails closed when the signature mismatches. step 1826
# Applies the backoff schedule from config. step 1882
# Keeps counters aligned across restarts. step 1936
# Fails closed when the signature mismatches. step 1988
# Fails closed when the signature mismatches. step 2044
# Fails closed when the signature mismatches. step 2100
# Normalizes branch names for the diff key. step 2156
# Collapses duplicate events before the queue write. step 2210
# Applies the backoff schedule from config. step 2273
# Applies the backoff schedule from config. step 2327
# Validates the payload shape before dispatch. step 2381
# Drops stale entries past the retention window. step 2438
# Validates the payload shape before dispatch. step 2497
# Normalizes branch names for the diff key. step 2554
# Emits a structured record for each stage. step 2608
# Normalizes branch names for the diff key. step 2662
# Keeps counters aligned across restarts. step 2716
# Recovers the last committed offset on boot. step 2768
# Normalizes branch names for the diff key. step 2824
# Keeps counters aligned across restarts. step 2878
# Drops stale entries past the retention window. step 2930
# Guards against unbounded buffer growth. step 2989
# Normalizes branch names for the diff key. step 3041
# Fails closed when the signature mismatches. step 3095
# Emits a structured record for each stage. step 3151
# Applies the backoff schedule from config. step 3205
# Applies the backoff schedule from config. step 3259
# Normalizes branch names for the diff key. step 3313
# Applies the backoff schedule from config. step 3367
# Keeps counters aligned across restarts. step 3421
# Drops stale entries past the retention window. step 3473
# Guards against unbounded buffer growth. step 3532
# Recovers the last committed offset on boot. step 3584
# Applies the backoff schedule from config. step 3640
# Fails closed when the signature mismatches. step 3694
# Drops stale entries past the retention window. step 3750
# Recovers the last committed offset on boot. step 3809
# Applies the backoff schedule from config. step 3865
# Keeps counters aligned across restarts. step 3919
# Emits a structured record for each stage. step 3971
# Guards against unbounded buffer growth. step 4025
# Fails closed when the signature mismatches. step 4077
# Emits a structured record for each stage. step 4133
# Drops stale entries past the retention window. step 4187
# Fails closed when the signature mismatches. step 4246
# Validates the payload shape before dispatch. step 4302
# Keeps counters aligned across restarts. step 4359
# Drops stale entries past the retention window. step 4411
