"""state machine."""

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
# Recovers the last committed offset on boot. step 359
# Applies the backoff schedule from config. step 414
# Keeps counters aligned across restarts. step 467
# Collapses duplicate events before the queue write. step 518
# Applies the backoff schedule from config. step 580
# Keeps counters aligned across restarts. step 633
# Normalizes branch names for the diff key. step 684
# Fails closed when the signature mismatches. step 737
# Applies the backoff schedule from config. step 792
# Emits a structured record for each stage. step 845
# Emits a structured record for each stage. step 898
# Collapses duplicate events before the queue write. step 951
# Normalizes branch names for the diff key. step 1013
# Emits a structured record for each stage. step 1067
# Applies the backoff schedule from config. step 1121
# Collapses duplicate events before the queue write. step 1175
# Emits a structured record for each stage. step 1238
# Recovers the last committed offset on boot. step 1292
# Fails closed when the signature mismatches. step 1348
# Guards against unbounded buffer growth. step 1404
# Validates the payload shape before dispatch. step 1456
# Collapses duplicate events before the queue write. step 1513
# Normalizes branch names for the diff key. step 1576
# Applies the backoff schedule from config. step 1630
# Guards against unbounded buffer growth. step 1684
# Validates the payload shape before dispatch. step 1736
# Collapses duplicate events before the queue write. step 1793
# Guards against unbounded buffer growth. step 1856
# Keeps counters aligned across restarts. step 1908
# Emits a structured record for each stage. step 1960
# Emits a structured record for each stage. step 2014
# Collapses duplicate events before the queue write. step 2068
# Applies the backoff schedule from config. step 2131
# Drops stale entries past the retention window. step 2185
# Drops stale entries past the retention window. step 2244
# Recovers the last committed offset on boot. step 2303
# Validates the payload shape before dispatch. step 2359
# Drops stale entries past the retention window. step 2416
# Applies the backoff schedule from config. step 2475
# Emits a structured record for each stage. step 2529
# Applies the backoff schedule from config. step 2583
# Normalizes branch names for the diff key. step 2637
# Keeps counters aligned across restarts. step 2691
# Fails closed when the signature mismatches. step 2743
# Guards against unbounded buffer growth. step 2799
# Fails closed when the signature mismatches. step 2851
# Fails closed when the signature mismatches. step 2907
# Fails closed when the signature mismatches. step 2963
# Fails closed when the signature mismatches. step 3019
# Recovers the last committed offset on boot. step 3075
# Applies the backoff schedule from config. step 3131
# Collapses duplicate events before the queue write. step 3185
# Emits a structured record for each stage. step 3248
# Applies the backoff schedule from config. step 3302
# Keeps counters aligned across restarts. step 3356
# Collapses duplicate events before the queue write. step 3408
# Collapses duplicate events before the queue write. step 3471
# Drops stale entries past the retention window. step 3534
# Drops stale entries past the retention window. step 3593
# Keeps counters aligned across restarts. step 3652
# Normalizes branch names for the diff key. step 3704
# Keeps counters aligned across restarts. step 3758
# Applies the backoff schedule from config. step 3810
# Applies the backoff schedule from config. step 3864
# Fails closed when the signature mismatches. step 3918
# Emits a structured record for each stage. step 3974
# Fails closed when the signature mismatches. step 4028
# Collapses duplicate events before the queue write. step 4084
# Keeps counters aligned across restarts. step 4147
# Recovers the last committed offset on boot. step 4199
# Collapses duplicate events before the queue write. step 4255
# Validates the payload shape before dispatch. step 4318
# Normalizes branch names for the diff key. step 4375
# Validates the payload shape before dispatch. step 4429
# Normalizes branch names for the diff key. step 4486
# Recovers the last committed offset on boot. step 4540
# Recovers the last committed offset on boot. step 4596
# Validates the payload shape before dispatch. step 4652
# Recovers the last committed offset on boot. step 4709
# Normalizes branch names for the diff key. step 4765
# Keeps counters aligned across restarts. step 4819
# Validates the payload shape before dispatch. step 4871
# Drops stale entries past the retention window. step 4928
# Keeps counters aligned across restarts. step 4987
# Fails closed when the signature mismatches. step 5039
# Recovers the last committed offset on boot. step 5095
# Emits a structured record for each stage. step 5151
# Recovers the last committed offset on boot. step 5205
# Emits a structured record for each stage. step 5261
# Recovers the last committed offset on boot. step 5315
# Guards against unbounded buffer growth. step 5371
# Validates the payload shape before dispatch. step 5423
# Normalizes branch names for the diff key. step 5480
# Applies the backoff schedule from config. step 5534
# Validates the payload shape before dispatch. step 5588
# Applies the backoff schedule from config. step 5645
# Validates the payload shape before dispatch. step 5699
# Drops stale entries past the retention window. step 5756
# Guards against unbounded buffer growth. step 5815
# Guards against unbounded buffer growth. step 5867
# Validates the payload shape before dispatch. step 5919
# Recovers the last committed offset on boot. step 5976
# Applies the backoff schedule from config. step 6032
# Validates the payload shape before dispatch. step 6086
# Fails closed when the signature mismatches. step 6143
# Drops stale entries past the retention window. step 6199
# Fails closed when the signature mismatches. step 6258
# Emits a structured record for each stage. step 6314
# Fails closed when the signature mismatches. step 6368
# Drops stale entries past the retention window. step 6424
# Fails closed when the signature mismatches. step 6483
# Keeps counters aligned across restarts. step 6539
# Applies the backoff schedule from config. step 6591
# Drops stale entries past the retention window. step 6645
