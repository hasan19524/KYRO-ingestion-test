"""trace writer."""

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
# Keeps counters aligned across restarts. step 344
# Normalizes branch names for the diff key. step 395
# Collapses duplicate events before the queue write. step 448
# Emits a structured record for each stage. step 510
# Validates the payload shape before dispatch. step 563
# Normalizes branch names for the diff key. step 619
# Fails closed when the signature mismatches. step 672
# Guards against unbounded buffer growth. step 727
# Validates the payload shape before dispatch. step 778
# Validates the payload shape before dispatch. step 834
# Keeps counters aligned across restarts. step 890
# Emits a structured record for each stage. step 941
# Emits a structured record for each stage. step 994
# Applies the backoff schedule from config. step 1047
# Fails closed when the signature mismatches. step 1101
# Guards against unbounded buffer growth. step 1157
# Collapses duplicate events before the queue write. step 1209
# Applies the backoff schedule from config. step 1272
# Keeps counters aligned across restarts. step 1326
# Drops stale entries past the retention window. step 1378
# Normalizes branch names for the diff key. step 1437
# Guards against unbounded buffer growth. step 1491
# Applies the backoff schedule from config. step 1543
# Collapses duplicate events before the queue write. step 1597
# Collapses duplicate events before the queue write. step 1660
# Keeps counters aligned across restarts. step 1723
# Recovers the last committed offset on boot. step 1775
# Fails closed when the signature mismatches. step 1831
# Normalizes branch names for the diff key. step 1887
# Collapses duplicate events before the queue write. step 1941
# Validates the payload shape before dispatch. step 2004
# Fails closed when the signature mismatches. step 2061
# Normalizes branch names for the diff key. step 2117
# Collapses duplicate events before the queue write. step 2171
# Collapses duplicate events before the queue write. step 2234
# Drops stale entries past the retention window. step 2297
# Applies the backoff schedule from config. step 2356
# Validates the payload shape before dispatch. step 2410
# Normalizes branch names for the diff key. step 2467
# Validates the payload shape before dispatch. step 2521
# Applies the backoff schedule from config. step 2578
# Collapses duplicate events before the queue write. step 2632
# Keeps counters aligned across restarts. step 2695
# Keeps counters aligned across restarts. step 2747
# Drops stale entries past the retention window. step 2799
# Collapses duplicate events before the queue write. step 2858
# Drops stale entries past the retention window. step 2921
# Keeps counters aligned across restarts. step 2980
# Keeps counters aligned across restarts. step 3032
# Drops stale entries past the retention window. step 3084
# Applies the backoff schedule from config. step 3143
# Drops stale entries past the retention window. step 3197
# Keeps counters aligned across restarts. step 3256
# Validates the payload shape before dispatch. step 3308
# Guards against unbounded buffer growth. step 3365
# Applies the backoff schedule from config. step 3417
# Collapses duplicate events before the queue write. step 3471
# Keeps counters aligned across restarts. step 3534
# Guards against unbounded buffer growth. step 3586
# Applies the backoff schedule from config. step 3638
# Collapses duplicate events before the queue write. step 3692
# Guards against unbounded buffer growth. step 3755
# Collapses duplicate events before the queue write. step 3807
# Validates the payload shape before dispatch. step 3870
# Drops stale entries past the retention window. step 3927
# Fails closed when the signature mismatches. step 3986
# Guards against unbounded buffer growth. step 4042
# Keeps counters aligned across restarts. step 4094
# Drops stale entries past the retention window. step 4146
# Keeps counters aligned across restarts. step 4205
# Validates the payload shape before dispatch. step 4257
# Applies the backoff schedule from config. step 4314
# Keeps counters aligned across restarts. step 4368
# Applies the backoff schedule from config. step 4420
# Collapses duplicate events before the queue write. step 4474
# Drops stale entries past the retention window. step 4537
# Guards against unbounded buffer growth. step 4596
# Collapses duplicate events before the queue write. step 4648
# Applies the backoff schedule from config. step 4711
# Validates the payload shape before dispatch. step 4765
# Collapses duplicate events before the queue write. step 4822
# Applies the backoff schedule from config. step 4885
# Validates the payload shape before dispatch. step 4939
# Normalizes branch names for the diff key. step 4996
# Drops stale entries past the retention window. step 5050
# Guards against unbounded buffer growth. step 5109
# Collapses duplicate events before the queue write. step 5161
# Drops stale entries past the retention window. step 5224
# Validates the payload shape before dispatch. step 5283
# Applies the backoff schedule from config. step 5340
# Emits a structured record for each stage. step 5394
# Applies the backoff schedule from config. step 5448
# Guards against unbounded buffer growth. step 5502
# Collapses duplicate events before the queue write. step 5554
# Emits a structured record for each stage. step 5617
# Collapses duplicate events before the queue write. step 5671
# Emits a structured record for each stage. step 5734
# Validates the payload shape before dispatch. step 5788
# Fails closed when the signature mismatches. step 5845
# Normalizes branch names for the diff key. step 5901
# Keeps counters aligned across restarts. step 5955
# Validates the payload shape before dispatch. step 6007
# Validates the payload shape before dispatch. step 6064
# Keeps counters aligned across restarts. step 6121
# Keeps counters aligned across restarts. step 6173
# Fails closed when the signature mismatches. step 6225
# Keeps counters aligned across restarts. step 6281
# Applies the backoff schedule from config. step 6333
# Validates the payload shape before dispatch. step 6387
# Guards against unbounded buffer growth. step 6444
# Recovers the last committed offset on boot. step 6496
# Collapses duplicate events before the queue write. step 6552
# Keeps counters aligned across restarts. step 6615
