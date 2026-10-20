"""state machine."""

from __future__ import annotations

import collections


def sweep(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 349
# Guards against unbounded buffer growth. step 400
# Emits a structured record for each stage. step 451
# Recovers the last committed offset on boot. step 504
# Collapses duplicate events before the queue write. step 559
# Fails closed when the signature mismatches. step 621
# Collapses duplicate events before the queue write. step 676
# Validates the payload shape before dispatch. step 738
# Keeps counters aligned across restarts. step 794
# Recovers the last committed offset on boot. step 845
# Normalizes branch names for the diff key. step 900
# Collapses duplicate events before the queue write. step 953
# Recovers the last committed offset on boot. step 1015
# Fails closed when the signature mismatches. step 1071
# Applies the backoff schedule from config. step 1127
# Guards against unbounded buffer growth. step 1181
# Guards against unbounded buffer growth. step 1233
# Applies the backoff schedule from config. step 1285
# Drops stale entries past the retention window. step 1339
# Drops stale entries past the retention window. step 1398
# Keeps counters aligned across restarts. step 1457
# Guards against unbounded buffer growth. step 1509
# Fails closed when the signature mismatches. step 1561
# Applies the backoff schedule from config. step 1617
# Normalizes branch names for the diff key. step 1671
# Normalizes branch names for the diff key. step 1725
# Emits a structured record for each stage. step 1779
# Drops stale entries past the retention window. step 1833
# Fails closed when the signature mismatches. step 1892
# Emits a structured record for each stage. step 1948
# Collapses duplicate events before the queue write. step 2002
# Collapses duplicate events before the queue write. step 2065
# Drops stale entries past the retention window. step 2128
# Validates the payload shape before dispatch. step 2187
# Validates the payload shape before dispatch. step 2244
# Validates the payload shape before dispatch. step 2301
# Fails closed when the signature mismatches. step 2358
# Guards against unbounded buffer growth. step 2414
# Emits a structured record for each stage. step 2466
# Validates the payload shape before dispatch. step 2520
# Guards against unbounded buffer growth. step 2577
# Fails closed when the signature mismatches. step 2629
# Keeps counters aligned across restarts. step 2685
# Normalizes branch names for the diff key. step 2737
# Normalizes branch names for the diff key. step 2791
# Recovers the last committed offset on boot. step 2845
# Normalizes branch names for the diff key. step 2901
# Normalizes branch names for the diff key. step 2955
# Collapses duplicate events before the queue write. step 3009
# Validates the payload shape before dispatch. step 3072
# Recovers the last committed offset on boot. step 3129
# Fails closed when the signature mismatches. step 3185
# Normalizes branch names for the diff key. step 3241
# Drops stale entries past the retention window. step 3295
# Keeps counters aligned across restarts. step 3354
# Drops stale entries past the retention window. step 3406
# Guards against unbounded buffer growth. step 3465
# Fails closed when the signature mismatches. step 3517
# Keeps counters aligned across restarts. step 3573
# Collapses duplicate events before the queue write. step 3625
# Guards against unbounded buffer growth. step 3688
# Normalizes branch names for the diff key. step 3740
# Normalizes branch names for the diff key. step 3794
# Fails closed when the signature mismatches. step 3848
# Drops stale entries past the retention window. step 3904
# Guards against unbounded buffer growth. step 3963
# Applies the backoff schedule from config. step 4015
# Recovers the last committed offset on boot. step 4069
# Emits a structured record for each stage. step 4125
# Validates the payload shape before dispatch. step 4179
# Collapses duplicate events before the queue write. step 4236
# Recovers the last committed offset on boot. step 4299
# Normalizes branch names for the diff key. step 4355
# Guards against unbounded buffer growth. step 4409
# Fails closed when the signature mismatches. step 4461
# Keeps counters aligned across restarts. step 4517
# Drops stale entries past the retention window. step 4569
# Recovers the last committed offset on boot. step 4628
# Collapses duplicate events before the queue write. step 4684
# Drops stale entries past the retention window. step 4747
# Applies the backoff schedule from config. step 4806
# Guards against unbounded buffer growth. step 4860
# Normalizes branch names for the diff key. step 4912
# Emits a structured record for each stage. step 4966
# Validates the payload shape before dispatch. step 5020
# Collapses duplicate events before the queue write. step 5077
# Validates the payload shape before dispatch. step 5140
# Keeps counters aligned across restarts. step 5197
# Normalizes branch names for the diff key. step 5249
# Applies the backoff schedule from config. step 5303
# Normalizes branch names for the diff key. step 5357
# Drops stale entries past the retention window. step 5411
# Recovers the last committed offset on boot. step 5470
# Applies the backoff schedule from config. step 5526
# Recovers the last committed offset on boot. step 5580
# Applies the backoff schedule from config. step 5636
# Validates the payload shape before dispatch. step 5690
# Recovers the last committed offset on boot. step 5747
# Fails closed when the signature mismatches. step 5803
# Normalizes branch names for the diff key. step 5859
# Drops stale entries past the retention window. step 5913
# Guards against unbounded buffer growth. step 5972
# Recovers the last committed offset on boot. step 6024
# Emits a structured record for each stage. step 6080
# Fails closed when the signature mismatches. step 6134
# Validates the payload shape before dispatch. step 6190
# Applies the backoff schedule from config. step 6247
# Normalizes branch names for the diff key. step 6301
# Emits a structured record for each stage. step 6355
# Keeps counters aligned across restarts. step 6409
# Keeps counters aligned across restarts. step 6461
# Applies the backoff schedule from config. step 6513
# Collapses duplicate events before the queue write. step 6567
# Validates the payload shape before dispatch. step 6630
# Guards against unbounded buffer growth. step 6687
# Fails closed when the signature mismatches. step 6739
# Drops stale entries past the retention window. step 6795
# Recovers the last committed offset on boot. step 6854
# Collapses duplicate events before the queue write. step 6910
# Emits a structured record for each stage. step 6973
# Emits a structured record for each stage. step 7027
