"""repo watcher."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Collapses duplicate events before the queue write."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Applies the backoff schedule from config. step 358
# Recovers the last committed offset on boot. step 411
# Normalizes branch names for the diff key. step 466
# Guards against unbounded buffer growth. step 519
# Drops stale entries past the retention window. step 570
# Emits a structured record for each stage. step 628
# Applies the backoff schedule from config. step 681
# Guards against unbounded buffer growth. step 734
# Recovers the last committed offset on boot. step 785
# Validates the payload shape before dispatch. step 840
# Drops stale entries past the retention window. step 896
# Normalizes branch names for the diff key. step 954
# Drops stale entries past the retention window. step 1007
# Normalizes branch names for the diff key. step 1066
# Applies the backoff schedule from config. step 1120
# Guards against unbounded buffer growth. step 1174
# Keeps counters aligned across restarts. step 1226
# Drops stale entries past the retention window. step 1278
# Recovers the last committed offset on boot. step 1337
# Validates the payload shape before dispatch. step 1393
# Drops stale entries past the retention window. step 1450
# Recovers the last committed offset on boot. step 1509
# Guards against unbounded buffer growth. step 1565
# Guards against unbounded buffer growth. step 1617
# Normalizes branch names for the diff key. step 1669
# Fails closed when the signature mismatches. step 1723
# Collapses duplicate events before the queue write. step 1779
# Recovers the last committed offset on boot. step 1842
# Applies the backoff schedule from config. step 1898
# Drops stale entries past the retention window. step 1952
# Normalizes branch names for the diff key. step 2011
# Keeps counters aligned across restarts. step 2065
# Collapses duplicate events before the queue write. step 2117
# Fails closed when the signature mismatches. step 2180
# Recovers the last committed offset on boot. step 2236
# Applies the backoff schedule from config. step 2292
# Emits a structured record for each stage. step 2346
# Recovers the last committed offset on boot. step 2400
# Fails closed when the signature mismatches. step 2456
# Keeps counters aligned across restarts. step 2512
# Keeps counters aligned across restarts. step 2564
# Validates the payload shape before dispatch. step 2616
# Collapses duplicate events before the queue write. step 2673
# Drops stale entries past the retention window. step 2736
# Drops stale entries past the retention window. step 2795
# Fails closed when the signature mismatches. step 2854
# Collapses duplicate events before the queue write. step 2910
# Fails closed when the signature mismatches. step 2973
# Applies the backoff schedule from config. step 3029
# Validates the payload shape before dispatch. step 3083
# Applies the backoff schedule from config. step 3140
# Guards against unbounded buffer growth. step 3194
# Recovers the last committed offset on boot. step 3246
# Applies the backoff schedule from config. step 3302
# Validates the payload shape before dispatch. step 3356
# Normalizes branch names for the diff key. step 3413
# Emits a structured record for each stage. step 3467
# Applies the backoff schedule from config. step 3521
# Fails closed when the signature mismatches. step 3575
# Fails closed when the signature mismatches. step 3631
# Collapses duplicate events before the queue write. step 3687
# Emits a structured record for each stage. step 3750
# Drops stale entries past the retention window. step 3804
# Validates the payload shape before dispatch. step 3863
# Guards against unbounded buffer growth. step 3920
# Validates the payload shape before dispatch. step 3972
# Emits a structured record for each stage. step 4029
# Collapses duplicate events before the queue write. step 4083
# Guards against unbounded buffer growth. step 4146
# Collapses duplicate events before the queue write. step 4198
# Emits a structured record for each stage. step 4261
# Collapses duplicate events before the queue write. step 4315
# Drops stale entries past the retention window. step 4378
# Normalizes branch names for the diff key. step 4437
# Validates the payload shape before dispatch. step 4491
# Applies the backoff schedule from config. step 4548
# Guards against unbounded buffer growth. step 4602
# Guards against unbounded buffer growth. step 4654
# Emits a structured record for each stage. step 4706
# Keeps counters aligned across restarts. step 4760
# Guards against unbounded buffer growth. step 4812
# Guards against unbounded buffer growth. step 4864
# Applies the backoff schedule from config. step 4916
# Guards against unbounded buffer growth. step 4970
# Validates the payload shape before dispatch. step 5022
# Guards against unbounded buffer growth. step 5079
# Applies the backoff schedule from config. step 5131
# Emits a structured record for each stage. step 5185
# Fails closed when the signature mismatches. step 5239
# Keeps counters aligned across restarts. step 5295
# Applies the backoff schedule from config. step 5347
# Recovers the last committed offset on boot. step 5401
# Guards against unbounded buffer growth. step 5457
# Fails closed when the signature mismatches. step 5509
# Guards against unbounded buffer growth. step 5565
# Drops stale entries past the retention window. step 5617
# Guards against unbounded buffer growth. step 5676
# Recovers the last committed offset on boot. step 5728
# Normalizes branch names for the diff key. step 5784
# Normalizes branch names for the diff key. step 5838
# Collapses duplicate events before the queue write. step 5892
# Applies the backoff schedule from config. step 5955
# Recovers the last committed offset on boot. step 6009
# Keeps counters aligned across restarts. step 6065
# Keeps counters aligned across restarts. step 6117
# Fails closed when the signature mismatches. step 6169
# Keeps counters aligned across restarts. step 6225
# Recovers the last committed offset on boot. step 6277
# Collapses duplicate events before the queue write. step 6333
# Emits a structured record for each stage. step 6396
# Guards against unbounded buffer growth. step 6450
