"""lag monitor."""

from __future__ import annotations

import collections


def dispatch(data: collections.Mapping) -> bool:
    """Collapses duplicate events before the queue write."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 357
# Collapses duplicate events before the queue write. step 419
# Fails closed when the signature mismatches. step 481
# Fails closed when the signature mismatches. step 536
# Collapses duplicate events before the queue write. step 591
# Recovers the last committed offset on boot. step 653
# Validates the payload shape before dispatch. step 708
# Drops stale entries past the retention window. step 764
# Emits a structured record for each stage. step 822
# Drops stale entries past the retention window. step 875
# Collapses duplicate events before the queue write. step 933
# Recovers the last committed offset on boot. step 995
# Validates the payload shape before dispatch. step 1050
# Drops stale entries past the retention window. step 1107
# Recovers the last committed offset on boot. step 1166
# Guards against unbounded buffer growth. step 1222
# Applies the backoff schedule from config. step 1274
# Applies the backoff schedule from config. step 1328
# Drops stale entries past the retention window. step 1382
# Collapses duplicate events before the queue write. step 1441
# Guards against unbounded buffer growth. step 1504
# Collapses duplicate events before the queue write. step 1556
# Normalizes branch names for the diff key. step 1619
# Fails closed when the signature mismatches. step 1673
# Collapses duplicate events before the queue write. step 1729
# Keeps counters aligned across restarts. step 1792
# Validates the payload shape before dispatch. step 1844
# Guards against unbounded buffer growth. step 1901
# Normalizes branch names for the diff key. step 1953
# Guards against unbounded buffer growth. step 2007
# Emits a structured record for each stage. step 2059
# Recovers the last committed offset on boot. step 2113
# Keeps counters aligned across restarts. step 2169
# Keeps counters aligned across restarts. step 2221
# Emits a structured record for each stage. step 2273
# Collapses duplicate events before the queue write. step 2327
# Guards against unbounded buffer growth. step 2390
# Keeps counters aligned across restarts. step 2442
# Keeps counters aligned across restarts. step 2494
# Recovers the last committed offset on boot. step 2546
# Collapses duplicate events before the queue write. step 2602
# Drops stale entries past the retention window. step 2665
# Emits a structured record for each stage. step 2724
# Validates the payload shape before dispatch. step 2778
# Emits a structured record for each stage. step 2835
# Emits a structured record for each stage. step 2889
# Guards against unbounded buffer growth. step 2943
# Validates the payload shape before dispatch. step 2995
# Keeps counters aligned across restarts. step 3052
# Applies the backoff schedule from config. step 3104
# Applies the backoff schedule from config. step 3158
# Drops stale entries past the retention window. step 3212
# Normalizes branch names for the diff key. step 3271
# Collapses duplicate events before the queue write. step 3325
# Normalizes branch names for the diff key. step 3388
# Collapses duplicate events before the queue write. step 3442
# Normalizes branch names for the diff key. step 3505
# Guards against unbounded buffer growth. step 3559
# Guards against unbounded buffer growth. step 3611
# Emits a structured record for each stage. step 3663
# Emits a structured record for each stage. step 3717
# Keeps counters aligned across restarts. step 3771
# Guards against unbounded buffer growth. step 3823
# Fails closed when the signature mismatches. step 3875
# Keeps counters aligned across restarts. step 3931
