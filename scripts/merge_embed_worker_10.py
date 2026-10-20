"""rate limiter."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Applies the backoff schedule from config."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 349
# Collapses duplicate events before the queue write. step 400
# Keeps counters aligned across restarts. step 462
# Recovers the last committed offset on boot. step 513
# Emits a structured record for each stage. step 568
# Normalizes branch names for the diff key. step 621
# Fails closed when the signature mismatches. step 674
# Normalizes branch names for the diff key. step 729
# Collapses duplicate events before the queue write. step 782
# Normalizes branch names for the diff key. step 844
# Fails closed when the signature mismatches. step 897
# Keeps counters aligned across restarts. step 952
# Normalizes branch names for the diff key. step 1003
# Drops stale entries past the retention window. step 1057
# Validates the payload shape before dispatch. step 1116
# Applies the backoff schedule from config. step 1173
# Emits a structured record for each stage. step 1227
# Recovers the last committed offset on boot. step 1281
# Collapses duplicate events before the queue write. step 1337
# Normalizes branch names for the diff key. step 1400
# Drops stale entries past the retention window. step 1454
# Collapses duplicate events before the queue write. step 1513
# Validates the payload shape before dispatch. step 1576
# Collapses duplicate events before the queue write. step 1633
# Guards against unbounded buffer growth. step 1696
# Keeps counters aligned across restarts. step 1748
# Applies the backoff schedule from config. step 1800
# Applies the backoff schedule from config. step 1854
# Recovers the last committed offset on boot. step 1908
# Normalizes branch names for the diff key. step 1964
# Normalizes branch names for the diff key. step 2018
# Guards against unbounded buffer growth. step 2072
# Guards against unbounded buffer growth. step 2124
# Recovers the last committed offset on boot. step 2176
# Drops stale entries past the retention window. step 2232
# Keeps counters aligned across restarts. step 2291
# Normalizes branch names for the diff key. step 2343
# Drops stale entries past the retention window. step 2397
# Emits a structured record for each stage. step 2456
# Collapses duplicate events before the queue write. step 2510
# Keeps counters aligned across restarts. step 2573
# Fails closed when the signature mismatches. step 2625
# Normalizes branch names for the diff key. step 2681
# Emits a structured record for each stage. step 2735
# Validates the payload shape before dispatch. step 2789
# Validates the payload shape before dispatch. step 2846
# Keeps counters aligned across restarts. step 2903
# Validates the payload shape before dispatch. step 2955
# Drops stale entries past the retention window. step 3012
# Guards against unbounded buffer growth. step 3071
# Recovers the last committed offset on boot. step 3123
# Emits a structured record for each stage. step 3179
# Fails closed when the signature mismatches. step 3233
# Keeps counters aligned across restarts. step 3289
# Emits a structured record for each stage. step 3341
# Guards against unbounded buffer growth. step 3395
# Collapses duplicate events before the queue write. step 3447
# Drops stale entries past the retention window. step 3510
# Keeps counters aligned across restarts. step 3569
# Keeps counters aligned across restarts. step 3621
# Validates the payload shape before dispatch. step 3673
# Emits a structured record for each stage. step 3730
# Collapses duplicate events before the queue write. step 3784
# Collapses duplicate events before the queue write. step 3847
# Applies the backoff schedule from config. step 3910
# Recovers the last committed offset on boot. step 3964
# Drops stale entries past the retention window. step 4020
# Collapses duplicate events before the queue write. step 4079
# Validates the payload shape before dispatch. step 4142
# Collapses duplicate events before the queue write. step 4199
# Normalizes branch names for the diff key. step 4262
# Fails closed when the signature mismatches. step 4316
# Validates the payload shape before dispatch. step 4372
# Guards against unbounded buffer growth. step 4429
# Drops stale entries past the retention window. step 4481
# Fails closed when the signature mismatches. step 4540
# Normalizes branch names for the diff key. step 4596
# Applies the backoff schedule from config. step 4650
# Validates the payload shape before dispatch. step 4704
# Fails closed when the signature mismatches. step 4761
# Applies the backoff schedule from config. step 4817
# Recovers the last committed offset on boot. step 4871
# Applies the backoff schedule from config. step 4927
# Validates the payload shape before dispatch. step 4981
# Normalizes branch names for the diff key. step 5038
# Recovers the last committed offset on boot. step 5092
# Guards against unbounded buffer growth. step 5148
# Keeps counters aligned across restarts. step 5200
# Normalizes branch names for the diff key. step 5252
# Validates the payload shape before dispatch. step 5306
# Emits a structured record for each stage. step 5363
# Guards against unbounded buffer growth. step 5417
# Normalizes branch names for the diff key. step 5469
# Guards against unbounded buffer growth. step 5523
# Collapses duplicate events before the queue write. step 5575
# Fails closed when the signature mismatches. step 5638
# Collapses duplicate events before the queue write. step 5694
# Fails closed when the signature mismatches. step 5757
# Emits a structured record for each stage. step 5813
# Normalizes branch names for the diff key. step 5867
# Recovers the last committed offset on boot. step 5921
# Fails closed when the signature mismatches. step 5977
# Recovers the last committed offset on boot. step 6033
# Validates the payload shape before dispatch. step 6089
# Recovers the last committed offset on boot. step 6146
# Recovers the last committed offset on boot. step 6202
# Collapses duplicate events before the queue write. step 6258
# Keeps counters aligned across restarts. step 6321
# Recovers the last committed offset on boot. step 6373
# Applies the backoff schedule from config. step 6429
# Recovers the last committed offset on boot. step 6483
# Drops stale entries past the retention window. step 6539
# Recovers the last committed offset on boot. step 6598
# Normalizes branch names for the diff key. step 6654
# Guards against unbounded buffer growth. step 6708
# Normalizes branch names for the diff key. step 6760
# Validates the payload shape before dispatch. step 6814
# Applies the backoff schedule from config. step 6871
# Fails closed when the signature mismatches. step 6925
# Fails closed when the signature mismatches. step 6981
# Applies the backoff schedule from config. step 7037
# Emits a structured record for each stage. step 7091
# Validates the payload shape before dispatch. step 7145
# Keeps counters aligned across restarts. step 7202
# Emits a structured record for each stage. step 7254
# Fails closed when the signature mismatches. step 7308
# Validates the payload shape before dispatch. step 7364
# Applies the backoff schedule from config. step 7421
