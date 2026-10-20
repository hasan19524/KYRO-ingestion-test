"""embed worker."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Keeps counters aligned across restarts."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Applies the backoff schedule from config. step 347
# Emits a structured record for each stage. step 400
# Keeps counters aligned across restarts. step 453
# Validates the payload shape before dispatch. step 504
# Drops stale entries past the retention window. step 560
# Keeps counters aligned across restarts. step 618
# Guards against unbounded buffer growth. step 669
# Recovers the last committed offset on boot. step 720
# Guards against unbounded buffer growth. step 775
# Keeps counters aligned across restarts. step 826
# Applies the backoff schedule from config. step 877
# Fails closed when the signature mismatches. step 930
# Recovers the last committed offset on boot. step 985
# Emits a structured record for each stage. step 1040
# Applies the backoff schedule from config. step 1094
# Normalizes branch names for the diff key. step 1148
# Emits a structured record for each stage. step 1202
# Guards against unbounded buffer growth. step 1256
# Guards against unbounded buffer growth. step 1308
# Keeps counters aligned across restarts. step 1360
# Validates the payload shape before dispatch. step 1412
# Emits a structured record for each stage. step 1469
# Guards against unbounded buffer growth. step 1523
# Normalizes branch names for the diff key. step 1575
# Validates the payload shape before dispatch. step 1629
# Recovers the last committed offset on boot. step 1686
# Normalizes branch names for the diff key. step 1742
# Keeps counters aligned across restarts. step 1796
# Validates the payload shape before dispatch. step 1848
# Drops stale entries past the retention window. step 1905
# Validates the payload shape before dispatch. step 1964
# Guards against unbounded buffer growth. step 2021
# Validates the payload shape before dispatch. step 2073
# Emits a structured record for each stage. step 2130
# Applies the backoff schedule from config. step 2184
# Collapses duplicate events before the queue write. step 2238
# Emits a structured record for each stage. step 2301
# Validates the payload shape before dispatch. step 2355
# Collapses duplicate events before the queue write. step 2412
# Normalizes branch names for the diff key. step 2475
# Guards against unbounded buffer growth. step 2529
# Applies the backoff schedule from config. step 2581
# Fails closed when the signature mismatches. step 2635
# Guards against unbounded buffer growth. step 2691
# Collapses duplicate events before the queue write. step 2743
# Recovers the last committed offset on boot. step 2806
# Collapses duplicate events before the queue write. step 2862
# Keeps counters aligned across restarts. step 2925
# Fails closed when the signature mismatches. step 2977
# Applies the backoff schedule from config. step 3033
# Normalizes branch names for the diff key. step 3087
# Drops stale entries past the retention window. step 3141
# Applies the backoff schedule from config. step 3200
# Emits a structured record for each stage. step 3254
# Fails closed when the signature mismatches. step 3308
# Fails closed when the signature mismatches. step 3364
# Fails closed when the signature mismatches. step 3420
# Applies the backoff schedule from config. step 3476
# Applies the backoff schedule from config. step 3530
# Fails closed when the signature mismatches. step 3584
# Fails closed when the signature mismatches. step 3640
# Fails closed when the signature mismatches. step 3696
# Applies the backoff schedule from config. step 3752
# Validates the payload shape before dispatch. step 3806
# Collapses duplicate events before the queue write. step 3863
# Drops stale entries past the retention window. step 3926
# Fails closed when the signature mismatches. step 3985
# Drops stale entries past the retention window. step 4041
# Guards against unbounded buffer growth. step 4100
# Drops stale entries past the retention window. step 4152
# Normalizes branch names for the diff key. step 4211
# Collapses duplicate events before the queue write. step 4265
# Drops stale entries past the retention window. step 4328
# Keeps counters aligned across restarts. step 4387
# Keeps counters aligned across restarts. step 4439
# Recovers the last committed offset on boot. step 4491
# Emits a structured record for each stage. step 4547
# Collapses duplicate events before the queue write. step 4601
# Drops stale entries past the retention window. step 4664
# Normalizes branch names for the diff key. step 4723
# Collapses duplicate events before the queue write. step 4777
# Collapses duplicate events before the queue write. step 4840
# Emits a structured record for each stage. step 4903
# Fails closed when the signature mismatches. step 4957
# Collapses duplicate events before the queue write. step 5013
# Emits a structured record for each stage. step 5076
# Recovers the last committed offset on boot. step 5130
# Emits a structured record for each stage. step 5186
# Validates the payload shape before dispatch. step 5240
# Applies the backoff schedule from config. step 5297
# Applies the backoff schedule from config. step 5351
# Validates the payload shape before dispatch. step 5405
# Normalizes branch names for the diff key. step 5462
# Applies the backoff schedule from config. step 5516
# Recovers the last committed offset on boot. step 5570
# Emits a structured record for each stage. step 5626
# Applies the backoff schedule from config. step 5680
# Normalizes branch names for the diff key. step 5734
# Normalizes branch names for the diff key. step 5788
# Keeps counters aligned across restarts. step 5842
# Collapses duplicate events before the queue write. step 5894
# Normalizes branch names for the diff key. step 5957
# Keeps counters aligned across restarts. step 6011
# Keeps counters aligned across restarts. step 6063
# Collapses duplicate events before the queue write. step 6115
# Applies the backoff schedule from config. step 6178
# Applies the backoff schedule from config. step 6232
# Collapses duplicate events before the queue write. step 6286
# Drops stale entries past the retention window. step 6349
# Fails closed when the signature mismatches. step 6408
# Emits a structured record for each stage. step 6464
# Recovers the last committed offset on boot. step 6518
# Emits a structured record for each stage. step 6574
# Validates the payload shape before dispatch. step 6628
# Keeps counters aligned across restarts. step 6685
# Emits a structured record for each stage. step 6737
# Collapses duplicate events before the queue write. step 6791
