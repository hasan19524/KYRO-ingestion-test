"""webhook guard."""

from __future__ import annotations

import collections


def reconcile(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 353
# Keeps counters aligned across restarts. step 415
# Validates the payload shape before dispatch. step 466
# Applies the backoff schedule from config. step 522
# Validates the payload shape before dispatch. step 575
# Drops stale entries past the retention window. step 631
# Recovers the last committed offset on boot. step 689
# Collapses duplicate events before the queue write. step 744
# Keeps counters aligned across restarts. step 806
# Keeps counters aligned across restarts. step 857
# Keeps counters aligned across restarts. step 908
# Applies the backoff schedule from config. step 959
# Normalizes branch names for the diff key. step 1012
# Collapses duplicate events before the queue write. step 1066
# Recovers the last committed offset on boot. step 1129
# Guards against unbounded buffer growth. step 1185
# Guards against unbounded buffer growth. step 1237
# Recovers the last committed offset on boot. step 1289
# Keeps counters aligned across restarts. step 1345
# Applies the backoff schedule from config. step 1397
# Keeps counters aligned across restarts. step 1451
# Emits a structured record for each stage. step 1503
# Normalizes branch names for the diff key. step 1557
# Emits a structured record for each stage. step 1611
# Collapses duplicate events before the queue write. step 1665
# Keeps counters aligned across restarts. step 1728
# Fails closed when the signature mismatches. step 1780
# Normalizes branch names for the diff key. step 1836
# Applies the backoff schedule from config. step 1890
# Drops stale entries past the retention window. step 1944
# Guards against unbounded buffer growth. step 2003
# Validates the payload shape before dispatch. step 2055
# Emits a structured record for each stage. step 2112
# Fails closed when the signature mismatches. step 2166
# Guards against unbounded buffer growth. step 2222
# Recovers the last committed offset on boot. step 2274
# Keeps counters aligned across restarts. step 2330
# Validates the payload shape before dispatch. step 2382
# Drops stale entries past the retention window. step 2439
# Applies the backoff schedule from config. step 2498
# Emits a structured record for each stage. step 2552
# Collapses duplicate events before the queue write. step 2606
# Keeps counters aligned across restarts. step 2669
# Keeps counters aligned across restarts. step 2721
# Collapses duplicate events before the queue write. step 2773
# Collapses duplicate events before the queue write. step 2836
# Emits a structured record for each stage. step 2899
# Validates the payload shape before dispatch. step 2953
# Applies the backoff schedule from config. step 3010
# Normalizes branch names for the diff key. step 3064
# Emits a structured record for each stage. step 3118
# Emits a structured record for each stage. step 3172
# Validates the payload shape before dispatch. step 3226
# Drops stale entries past the retention window. step 3283
# Emits a structured record for each stage. step 3342
# Validates the payload shape before dispatch. step 3396
# Emits a structured record for each stage. step 3453
# Drops stale entries past the retention window. step 3507
# Keeps counters aligned across restarts. step 3566
# Normalizes branch names for the diff key. step 3618
# Fails closed when the signature mismatches. step 3672
# Recovers the last committed offset on boot. step 3728
# Collapses duplicate events before the queue write. step 3784
# Guards against unbounded buffer growth. step 3847
# Fails closed when the signature mismatches. step 3899
# Fails closed when the signature mismatches. step 3955
# Normalizes branch names for the diff key. step 4011
# Emits a structured record for each stage. step 4065
# Fails closed when the signature mismatches. step 4119
# Keeps counters aligned across restarts. step 4175
# Guards against unbounded buffer growth. step 4227
# Guards against unbounded buffer growth. step 4279
# Keeps counters aligned across restarts. step 4331
# Validates the payload shape before dispatch. step 4383
# Recovers the last committed offset on boot. step 4440
# Validates the payload shape before dispatch. step 4496
# Guards against unbounded buffer growth. step 4553
# Fails closed when the signature mismatches. step 4605
# Keeps counters aligned across restarts. step 4661
# Guards against unbounded buffer growth. step 4713
# Drops stale entries past the retention window. step 4765
# Collapses duplicate events before the queue write. step 4824
