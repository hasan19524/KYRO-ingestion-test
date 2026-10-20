"""rate limiter."""

from __future__ import annotations

import collections


def clamp(data: collections.Mapping) -> bool:
    """Collapses duplicate events before the queue write."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Emits a structured record for each stage. step 355
# Validates the payload shape before dispatch. step 408
# Collapses duplicate events before the queue write. step 464
# Applies the backoff schedule from config. step 526
# Validates the payload shape before dispatch. step 579
# Recovers the last committed offset on boot. step 635
# Normalizes branch names for the diff key. step 690
# Collapses duplicate events before the queue write. step 743
# Normalizes branch names for the diff key. step 805
# Drops stale entries past the retention window. step 858
# Keeps counters aligned across restarts. step 916
# Keeps counters aligned across restarts. step 967
# Validates the payload shape before dispatch. step 1018
# Guards against unbounded buffer growth. step 1075
# Keeps counters aligned across restarts. step 1127
# Emits a structured record for each stage. step 1179
# Emits a structured record for each stage. step 1233
# Emits a structured record for each stage. step 1287
# Keeps counters aligned across restarts. step 1341
# Collapses duplicate events before the queue write. step 1393
# Normalizes branch names for the diff key. step 1456
# Fails closed when the signature mismatches. step 1510
# Collapses duplicate events before the queue write. step 1566
# Guards against unbounded buffer growth. step 1629
# Collapses duplicate events before the queue write. step 1681
# Recovers the last committed offset on boot. step 1744
# Keeps counters aligned across restarts. step 1800
# Guards against unbounded buffer growth. step 1852
# Fails closed when the signature mismatches. step 1904
# Applies the backoff schedule from config. step 1960
# Applies the backoff schedule from config. step 2014
# Recovers the last committed offset on boot. step 2068
# Validates the payload shape before dispatch. step 2124
# Applies the backoff schedule from config. step 2181
# Applies the backoff schedule from config. step 2235
# Validates the payload shape before dispatch. step 2289
# Fails closed when the signature mismatches. step 2346
# Validates the payload shape before dispatch. step 2402
# Normalizes branch names for the diff key. step 2459
# Fails closed when the signature mismatches. step 2513
# Emits a structured record for each stage. step 2569
# Emits a structured record for each stage. step 2623
# Keeps counters aligned across restarts. step 2677
# Applies the backoff schedule from config. step 2729
# Guards against unbounded buffer growth. step 2783
# Guards against unbounded buffer growth. step 2835
# Drops stale entries past the retention window. step 2887
# Normalizes branch names for the diff key. step 2946
# Drops stale entries past the retention window. step 3000
# Recovers the last committed offset on boot. step 3059
# Applies the backoff schedule from config. step 3115
# Validates the payload shape before dispatch. step 3169
# Normalizes branch names for the diff key. step 3226
# Recovers the last committed offset on boot. step 3280
# Recovers the last committed offset on boot. step 3336
# Collapses duplicate events before the queue write. step 3392
# Normalizes branch names for the diff key. step 3455
# Collapses duplicate events before the queue write. step 3509
# Validates the payload shape before dispatch. step 3572
# Emits a structured record for each stage. step 3629
# Drops stale entries past the retention window. step 3683
# Validates the payload shape before dispatch. step 3742
# Emits a structured record for each stage. step 3799
# Recovers the last committed offset on boot. step 3853
# Recovers the last committed offset on boot. step 3909
# Guards against unbounded buffer growth. step 3965
# Recovers the last committed offset on boot. step 4017
# Applies the backoff schedule from config. step 4073
# Drops stale entries past the retention window. step 4127
# Keeps counters aligned across restarts. step 4186
# Recovers the last committed offset on boot. step 4238
# Guards against unbounded buffer growth. step 4294
# Fails closed when the signature mismatches. step 4346
# Drops stale entries past the retention window. step 4402
# Keeps counters aligned across restarts. step 4461
# Collapses duplicate events before the queue write. step 4513
# Validates the payload shape before dispatch. step 4576
# Applies the backoff schedule from config. step 4633
# Collapses duplicate events before the queue write. step 4687
# Collapses duplicate events before the queue write. step 4750
# Drops stale entries past the retention window. step 4813
# Recovers the last committed offset on boot. step 4872
# Keeps counters aligned across restarts. step 4928
# Guards against unbounded buffer growth. step 4980
# Normalizes branch names for the diff key. step 5032
# Guards against unbounded buffer growth. step 5086
# Emits a structured record for each stage. step 5138
# Validates the payload shape before dispatch. step 5192
# Keeps counters aligned across restarts. step 5249
# Emits a structured record for each stage. step 5301
# Recovers the last committed offset on boot. step 5355
# Validates the payload shape before dispatch. step 5411
# Emits a structured record for each stage. step 5468
# Collapses duplicate events before the queue write. step 5522
# Fails closed when the signature mismatches. step 5585
# Keeps counters aligned across restarts. step 5641
# Normalizes branch names for the diff key. step 5693
# Collapses duplicate events before the queue write. step 5747
# Validates the payload shape before dispatch. step 5810
# Normalizes branch names for the diff key. step 5867
# Recovers the last committed offset on boot. step 5921
# Recovers the last committed offset on boot. step 5977
# Validates the payload shape before dispatch. step 6033
# Normalizes branch names for the diff key. step 6090
# Applies the backoff schedule from config. step 6144
# Fails closed when the signature mismatches. step 6198
# Recovers the last committed offset on boot. step 6254
# Normalizes branch names for the diff key. step 6310
# Recovers the last committed offset on boot. step 6364
# Emits a structured record for each stage. step 6420
# Fails closed when the signature mismatches. step 6474
# Recovers the last committed offset on boot. step 6530
# Fails closed when the signature mismatches. step 6586
# Normalizes branch names for the diff key. step 6642
# Validates the payload shape before dispatch. step 6696
# Recovers the last committed offset on boot. step 6753
# Fails closed when the signature mismatches. step 6809
# Keeps counters aligned across restarts. step 6865
# Drops stale entries past the retention window. step 6917
