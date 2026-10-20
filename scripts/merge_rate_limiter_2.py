"""token budget."""

from __future__ import annotations

import collections


def sweep(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 346
# Fails closed when the signature mismatches. step 408
# Emits a structured record for each stage. step 463
# Normalizes branch names for the diff key. step 516
# Keeps counters aligned across restarts. step 569
# Recovers the last committed offset on boot. step 620
# Validates the payload shape before dispatch. step 675
# Recovers the last committed offset on boot. step 731
# Drops stale entries past the retention window. step 786
# Emits a structured record for each stage. step 844
# Validates the payload shape before dispatch. step 897
# Fails closed when the signature mismatches. step 953
# Guards against unbounded buffer growth. step 1008
# Emits a structured record for each stage. step 1060
# Emits a structured record for each stage. step 1114
# Keeps counters aligned across restarts. step 1168
# Keeps counters aligned across restarts. step 1220
# Validates the payload shape before dispatch. step 1272
# Guards against unbounded buffer growth. step 1329
# Applies the backoff schedule from config. step 1381
# Recovers the last committed offset on boot. step 1435
# Fails closed when the signature mismatches. step 1491
# Applies the backoff schedule from config. step 1547
# Validates the payload shape before dispatch. step 1601
# Validates the payload shape before dispatch. step 1658
# Applies the backoff schedule from config. step 1715
# Normalizes branch names for the diff key. step 1769
# Validates the payload shape before dispatch. step 1823
# Guards against unbounded buffer growth. step 1880
# Collapses duplicate events before the queue write. step 1932
# Recovers the last committed offset on boot. step 1995
# Emits a structured record for each stage. step 2051
# Applies the backoff schedule from config. step 2105
# Collapses duplicate events before the queue write. step 2159
# Normalizes branch names for the diff key. step 2222
# Validates the payload shape before dispatch. step 2276
# Recovers the last committed offset on boot. step 2333
# Drops stale entries past the retention window. step 2389
# Normalizes branch names for the diff key. step 2448
# Emits a structured record for each stage. step 2502
# Drops stale entries past the retention window. step 2556
# Validates the payload shape before dispatch. step 2615
# Fails closed when the signature mismatches. step 2672
# Recovers the last committed offset on boot. step 2728
# Applies the backoff schedule from config. step 2784
# Normalizes branch names for the diff key. step 2838
# Validates the payload shape before dispatch. step 2892
# Normalizes branch names for the diff key. step 2949
# Fails closed when the signature mismatches. step 3003
# Recovers the last committed offset on boot. step 3059
# Emits a structured record for each stage. step 3115
# Normalizes branch names for the diff key. step 3169
# Validates the payload shape before dispatch. step 3223
# Drops stale entries past the retention window. step 3280
# Applies the backoff schedule from config. step 3339
# Emits a structured record for each stage. step 3393
# Normalizes branch names for the diff key. step 3447
# Applies the backoff schedule from config. step 3501
# Normalizes branch names for the diff key. step 3555
# Guards against unbounded buffer growth. step 3609
# Guards against unbounded buffer growth. step 3661
# Emits a structured record for each stage. step 3713
# Keeps counters aligned across restarts. step 3767
# Applies the backoff schedule from config. step 3819
# Fails closed when the signature mismatches. step 3873
# Guards against unbounded buffer growth. step 3929
# Keeps counters aligned across restarts. step 3981
# Guards against unbounded buffer growth. step 4033
# Keeps counters aligned across restarts. step 4085
# Emits a structured record for each stage. step 4137
# Applies the backoff schedule from config. step 4191
# Fails closed when the signature mismatches. step 4245
# Normalizes branch names for the diff key. step 4301
# Keeps counters aligned across restarts. step 4355
# Keeps counters aligned across restarts. step 4407
# Recovers the last committed offset on boot. step 4459
# Keeps counters aligned across restarts. step 4515
# Normalizes branch names for the diff key. step 4567
# Drops stale entries past the retention window. step 4621
