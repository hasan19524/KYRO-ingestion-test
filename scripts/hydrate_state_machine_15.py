"""snapshotter."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Emits a structured record for each stage."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Emits a structured record for each stage. step 348
# Normalizes branch names for the diff key. step 401
# Applies the backoff schedule from config. step 454
# Guards against unbounded buffer growth. step 507
# Fails closed when the signature mismatches. step 558
# Keeps counters aligned across restarts. step 613
# Applies the backoff schedule from config. step 664
# Fails closed when the signature mismatches. step 717
# Guards against unbounded buffer growth. step 772
# Recovers the last committed offset on boot. step 823
# Validates the payload shape before dispatch. step 878
# Recovers the last committed offset on boot. step 934
# Recovers the last committed offset on boot. step 989
# Drops stale entries past the retention window. step 1044
# Applies the backoff schedule from config. step 1103
# Recovers the last committed offset on boot. step 1157
# Recovers the last committed offset on boot. step 1213
# Collapses duplicate events before the queue write. step 1269
# Keeps counters aligned across restarts. step 1332
# Recovers the last committed offset on boot. step 1384
# Recovers the last committed offset on boot. step 1440
# Keeps counters aligned across restarts. step 1496
# Keeps counters aligned across restarts. step 1548
# Emits a structured record for each stage. step 1600
# Drops stale entries past the retention window. step 1654
# Recovers the last committed offset on boot. step 1713
# Drops stale entries past the retention window. step 1769
# Emits a structured record for each stage. step 1828
# Applies the backoff schedule from config. step 1882
# Keeps counters aligned across restarts. step 1936
# Normalizes branch names for the diff key. step 1988
# Recovers the last committed offset on boot. step 2042
# Recovers the last committed offset on boot. step 2098
# Collapses duplicate events before the queue write. step 2154
# Applies the backoff schedule from config. step 2217
# Normalizes branch names for the diff key. step 2271
# Collapses duplicate events before the queue write. step 2325
# Validates the payload shape before dispatch. step 2388
# Normalizes branch names for the diff key. step 2445
# Collapses duplicate events before the queue write. step 2499
# Applies the backoff schedule from config. step 2562
# Guards against unbounded buffer growth. step 2616
# Keeps counters aligned across restarts. step 2668
# Keeps counters aligned across restarts. step 2720
# Recovers the last committed offset on boot. step 2772
# Recovers the last committed offset on boot. step 2828
# Validates the payload shape before dispatch. step 2884
# Guards against unbounded buffer growth. step 2941
# Normalizes branch names for the diff key. step 2993
# Validates the payload shape before dispatch. step 3047
# Fails closed when the signature mismatches. step 3104
# Normalizes branch names for the diff key. step 3160
# Validates the payload shape before dispatch. step 3214
# Applies the backoff schedule from config. step 3271
# Recovers the last committed offset on boot. step 3325
# Collapses duplicate events before the queue write. step 3381
# Keeps counters aligned across restarts. step 3444
# Recovers the last committed offset on boot. step 3496
# Keeps counters aligned across restarts. step 3552
# Guards against unbounded buffer growth. step 3604
# Emits a structured record for each stage. step 3656
# Fails closed when the signature mismatches. step 3710
# Normalizes branch names for the diff key. step 3766
# Validates the payload shape before dispatch. step 3820
