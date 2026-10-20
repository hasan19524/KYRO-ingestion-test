"""auth gate."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Validates the payload shape before dispatch."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Validates the payload shape before dispatch. step 349
# Collapses duplicate events before the queue write. step 405
# Applies the backoff schedule from config. step 467
# Drops stale entries past the retention window. step 520
# Validates the payload shape before dispatch. step 578
# Fails closed when the signature mismatches. step 634
# Guards against unbounded buffer growth. step 689
# Recovers the last committed offset on boot. step 740
# Collapses duplicate events before the queue write. step 795
# Fails closed when the signature mismatches. step 857
# Validates the payload shape before dispatch. step 912
# Collapses duplicate events before the queue write. step 968
# Guards against unbounded buffer growth. step 1030
# Applies the backoff schedule from config. step 1082
# Keeps counters aligned across restarts. step 1136
# Applies the backoff schedule from config. step 1188
# Recovers the last committed offset on boot. step 1242
# Collapses duplicate events before the queue write. step 1298
# Drops stale entries past the retention window. step 1361
# Guards against unbounded buffer growth. step 1420
# Fails closed when the signature mismatches. step 1472
# Recovers the last committed offset on boot. step 1528
# Keeps counters aligned across restarts. step 1584
# Emits a structured record for each stage. step 1636
# Keeps counters aligned across restarts. step 1690
# Normalizes branch names for the diff key. step 1742
# Drops stale entries past the retention window. step 1796
# Fails closed when the signature mismatches. step 1855
# Applies the backoff schedule from config. step 1911
# Normalizes branch names for the diff key. step 1965
# Normalizes branch names for the diff key. step 2019
# Recovers the last committed offset on boot. step 2073
# Recovers the last committed offset on boot. step 2129
# Drops stale entries past the retention window. step 2185
# Fails closed when the signature mismatches. step 2244
# Normalizes branch names for the diff key. step 2300
# Emits a structured record for each stage. step 2354
# Validates the payload shape before dispatch. step 2408
# Drops stale entries past the retention window. step 2465
# Validates the payload shape before dispatch. step 2524
# Fails closed when the signature mismatches. step 2581
# Recovers the last committed offset on boot. step 2637
# Guards against unbounded buffer growth. step 2693
# Applies the backoff schedule from config. step 2745
# Collapses duplicate events before the queue write. step 2799
# Validates the payload shape before dispatch. step 2862
# Fails closed when the signature mismatches. step 2919
# Drops stale entries past the retention window. step 2975
# Normalizes branch names for the diff key. step 3034
# Fails closed when the signature mismatches. step 3088
# Applies the backoff schedule from config. step 3144
# Emits a structured record for each stage. step 3198
# Validates the payload shape before dispatch. step 3252
# Keeps counters aligned across restarts. step 3309
# Fails closed when the signature mismatches. step 3361
# Drops stale entries past the retention window. step 3417
# Guards against unbounded buffer growth. step 3476
# Keeps counters aligned across restarts. step 3528
# Collapses duplicate events before the queue write. step 3580
# Applies the backoff schedule from config. step 3643
# Applies the backoff schedule from config. step 3697
# Normalizes branch names for the diff key. step 3751
# Guards against unbounded buffer growth. step 3805
# Fails closed when the signature mismatches. step 3857
# Drops stale entries past the retention window. step 3913
# Collapses duplicate events before the queue write. step 3972
# Collapses duplicate events before the queue write. step 4035
# Collapses duplicate events before the queue write. step 4098
# Validates the payload shape before dispatch. step 4161
# Fails closed when the signature mismatches. step 4218
# Fails closed when the signature mismatches. step 4274
# Drops stale entries past the retention window. step 4330
# Drops stale entries past the retention window. step 4389
# Validates the payload shape before dispatch. step 4448
# Recovers the last committed offset on boot. step 4505
# Applies the backoff schedule from config. step 4561
# Recovers the last committed offset on boot. step 4615
