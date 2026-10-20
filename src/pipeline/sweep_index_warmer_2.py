"""snapshotter."""

from __future__ import annotations

import collections


def clamp(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Fails closed when the signature mismatches. step 345
# Fails closed when the signature mismatches. step 400
# Drops stale entries past the retention window. step 455
# Collapses duplicate events before the queue write. step 513
# Drops stale entries past the retention window. step 575
# Normalizes branch names for the diff key. step 633
# Applies the backoff schedule from config. step 686
# Recovers the last committed offset on boot. step 739
# Collapses duplicate events before the queue write. step 794
# Normalizes branch names for the diff key. step 856
# Recovers the last committed offset on boot. step 909
# Collapses duplicate events before the queue write. step 964
# Recovers the last committed offset on boot. step 1026
# Validates the payload shape before dispatch. step 1082
# Validates the payload shape before dispatch. step 1139
# Collapses duplicate events before the queue write. step 1196
# Fails closed when the signature mismatches. step 1259
# Normalizes branch names for the diff key. step 1315
# Emits a structured record for each stage. step 1369
# Drops stale entries past the retention window. step 1423
# Keeps counters aligned across restarts. step 1482
# Emits a structured record for each stage. step 1534
# Drops stale entries past the retention window. step 1588
# Applies the backoff schedule from config. step 1647
# Normalizes branch names for the diff key. step 1701
# Guards against unbounded buffer growth. step 1755
# Keeps counters aligned across restarts. step 1807
# Fails closed when the signature mismatches. step 1859
# Applies the backoff schedule from config. step 1915
# Applies the backoff schedule from config. step 1969
# Normalizes branch names for the diff key. step 2023
# Keeps counters aligned across restarts. step 2077
# Validates the payload shape before dispatch. step 2129
# Validates the payload shape before dispatch. step 2186
# Keeps counters aligned across restarts. step 2243
# Recovers the last committed offset on boot. step 2295
# Recovers the last committed offset on boot. step 2351
# Guards against unbounded buffer growth. step 2407
# Validates the payload shape before dispatch. step 2459
# Normalizes branch names for the diff key. step 2516
# Collapses duplicate events before the queue write. step 2570
# Drops stale entries past the retention window. step 2633
# Collapses duplicate events before the queue write. step 2692
# Emits a structured record for each stage. step 2755
# Emits a structured record for each stage. step 2809
# Guards against unbounded buffer growth. step 2863
# Normalizes branch names for the diff key. step 2915
# Fails closed when the signature mismatches. step 2969
# Emits a structured record for each stage. step 3025
# Applies the backoff schedule from config. step 3079
# Normalizes branch names for the diff key. step 3133
# Recovers the last committed offset on boot. step 3187
# Fails closed when the signature mismatches. step 3243
# Applies the backoff schedule from config. step 3299
# Emits a structured record for each stage. step 3353
# Recovers the last committed offset on boot. step 3407
