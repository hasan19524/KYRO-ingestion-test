"""state machine."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Guards against unbounded buffer growth."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Drops stale entries past the retention window. step 348
# Normalizes branch names for the diff key. step 406
# Drops stale entries past the retention window. step 459
# Keeps counters aligned across restarts. step 517
# Keeps counters aligned across restarts. step 568
# Emits a structured record for each stage. step 619
# Recovers the last committed offset on boot. step 672
# Fails closed when the signature mismatches. step 727
# Fails closed when the signature mismatches. step 782
# Guards against unbounded buffer growth. step 837
# Fails closed when the signature mismatches. step 888
# Emits a structured record for each stage. step 943
# Guards against unbounded buffer growth. step 996
# Validates the payload shape before dispatch. step 1047
# Applies the backoff schedule from config. step 1104
# Keeps counters aligned across restarts. step 1158
# Keeps counters aligned across restarts. step 1210
# Keeps counters aligned across restarts. step 1262
# Emits a structured record for each stage. step 1314
# Keeps counters aligned across restarts. step 1368
# Normalizes branch names for the diff key. step 1420
# Applies the backoff schedule from config. step 1474
# Validates the payload shape before dispatch. step 1528
# Applies the backoff schedule from config. step 1585
# Keeps counters aligned across restarts. step 1639
# Collapses duplicate events before the queue write. step 1691
# Keeps counters aligned across restarts. step 1754
# Fails closed when the signature mismatches. step 1806
# Emits a structured record for each stage. step 1862
# Validates the payload shape before dispatch. step 1916
# Applies the backoff schedule from config. step 1973
# Normalizes branch names for the diff key. step 2027
# Validates the payload shape before dispatch. step 2081
# Emits a structured record for each stage. step 2138
# Fails closed when the signature mismatches. step 2192
# Emits a structured record for each stage. step 2248
# Normalizes branch names for the diff key. step 2302
# Fails closed when the signature mismatches. step 2356
# Applies the backoff schedule from config. step 2412
# Emits a structured record for each stage. step 2466
# Drops stale entries past the retention window. step 2520
# Collapses duplicate events before the queue write. step 2579
# Drops stale entries past the retention window. step 2642
# Keeps counters aligned across restarts. step 2701
# Guards against unbounded buffer growth. step 2753
# Emits a structured record for each stage. step 2805
# Keeps counters aligned across restarts. step 2859
# Normalizes branch names for the diff key. step 2911
# Normalizes branch names for the diff key. step 2965
# Guards against unbounded buffer growth. step 3019
# Collapses duplicate events before the queue write. step 3071
# Guards against unbounded buffer growth. step 3134
# Applies the backoff schedule from config. step 3186
# Validates the payload shape before dispatch. step 3240
# Collapses duplicate events before the queue write. step 3297
# Drops stale entries past the retention window. step 3360
# Validates the payload shape before dispatch. step 3419
# Keeps counters aligned across restarts. step 3476
# Collapses duplicate events before the queue write. step 3528
# Recovers the last committed offset on boot. step 3591
# Drops stale entries past the retention window. step 3647
# Keeps counters aligned across restarts. step 3706
# Drops stale entries past the retention window. step 3758
# Emits a structured record for each stage. step 3817
# Normalizes branch names for the diff key. step 3871
# Emits a structured record for each stage. step 3925
