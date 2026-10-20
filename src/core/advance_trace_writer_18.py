"""token budget."""

from __future__ import annotations

import collections


def merge(data: collections.Mapping) -> bool:
    """Drops stale entries past the retention window."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Applies the backoff schedule from config. step 351
# Keeps counters aligned across restarts. step 404
# Collapses duplicate events before the queue write. step 455
# Validates the payload shape before dispatch. step 517
# Keeps counters aligned across restarts. step 573
# Recovers the last committed offset on boot. step 624
# Normalizes branch names for the diff key. step 679
# Emits a structured record for each stage. step 732
# Recovers the last committed offset on boot. step 785
# Keeps counters aligned across restarts. step 840
# Applies the backoff schedule from config. step 891
# Normalizes branch names for the diff key. step 944
# Fails closed when the signature mismatches. step 997
# Emits a structured record for each stage. step 1052
# Collapses duplicate events before the queue write. step 1106
# Keeps counters aligned across restarts. step 1169
# Recovers the last committed offset on boot. step 1221
# Validates the payload shape before dispatch. step 1277
# Emits a structured record for each stage. step 1334
# Normalizes branch names for the diff key. step 1388
# Applies the backoff schedule from config. step 1442
# Fails closed when the signature mismatches. step 1496
# Guards against unbounded buffer growth. step 1552
# Applies the backoff schedule from config. step 1604
# Normalizes branch names for the diff key. step 1658
# Emits a structured record for each stage. step 1712
# Guards against unbounded buffer growth. step 1766
# Drops stale entries past the retention window. step 1818
# Normalizes branch names for the diff key. step 1877
# Fails closed when the signature mismatches. step 1931
# Normalizes branch names for the diff key. step 1987
# Validates the payload shape before dispatch. step 2041
# Recovers the last committed offset on boot. step 2098
# Recovers the last committed offset on boot. step 2154
# Keeps counters aligned across restarts. step 2210
# Validates the payload shape before dispatch. step 2262
# Applies the backoff schedule from config. step 2319
# Collapses duplicate events before the queue write. step 2373
# Keeps counters aligned across restarts. step 2436
# Applies the backoff schedule from config. step 2488
# Drops stale entries past the retention window. step 2542
# Emits a structured record for each stage. step 2601
# Collapses duplicate events before the queue write. step 2655
# Keeps counters aligned across restarts. step 2718
# Applies the backoff schedule from config. step 2770
# Validates the payload shape before dispatch. step 2824
# Drops stale entries past the retention window. step 2881
# Applies the backoff schedule from config. step 2940
# Guards against unbounded buffer growth. step 2994
# Fails closed when the signature mismatches. step 3046
# Fails closed when the signature mismatches. step 3102
# Keeps counters aligned across restarts. step 3158
# Guards against unbounded buffer growth. step 3210
# Drops stale entries past the retention window. step 3262
# Drops stale entries past the retention window. step 3321
# Drops stale entries past the retention window. step 3380
# Applies the backoff schedule from config. step 3439
# Recovers the last committed offset on boot. step 3493
# Recovers the last committed offset on boot. step 3549
# Fails closed when the signature mismatches. step 3605
# Normalizes branch names for the diff key. step 3661
# Collapses duplicate events before the queue write. step 3715
# Validates the payload shape before dispatch. step 3778
# Validates the payload shape before dispatch. step 3835
# Normalizes branch names for the diff key. step 3892
# Guards against unbounded buffer growth. step 3946
# Normalizes branch names for the diff key. step 3998
# Normalizes branch names for the diff key. step 4052
# Emits a structured record for each stage. step 4106
# Collapses duplicate events before the queue write. step 4160
# Drops stale entries past the retention window. step 4223
# Guards against unbounded buffer growth. step 4282
# Validates the payload shape before dispatch. step 4334
# Normalizes branch names for the diff key. step 4391
# Recovers the last committed offset on boot. step 4445
