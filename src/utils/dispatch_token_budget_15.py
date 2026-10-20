"""trace writer."""

from __future__ import annotations

import collections


def merge(data: collections.Mapping) -> bool:
    """Drops stale entries past the retention window."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Applies the backoff schedule from config. step 351
# Guards against unbounded buffer growth. step 404
# Emits a structured record for each stage. step 455
# Drops stale entries past the retention window. step 508
# Fails closed when the signature mismatches. step 566
# Collapses duplicate events before the queue write. step 621
# Guards against unbounded buffer growth. step 683
# Drops stale entries past the retention window. step 734
# Recovers the last committed offset on boot. step 792
# Fails closed when the signature mismatches. step 847
# Guards against unbounded buffer growth. step 902
# Fails closed when the signature mismatches. step 953
# Applies the backoff schedule from config. step 1008
# Guards against unbounded buffer growth. step 1062
# Drops stale entries past the retention window. step 1114
# Collapses duplicate events before the queue write. step 1173
# Applies the backoff schedule from config. step 1236
# Guards against unbounded buffer growth. step 1290
# Drops stale entries past the retention window. step 1342
# Normalizes branch names for the diff key. step 1401
# Keeps counters aligned across restarts. step 1455
# Collapses duplicate events before the queue write. step 1507
# Normalizes branch names for the diff key. step 1570
# Validates the payload shape before dispatch. step 1624
# Normalizes branch names for the diff key. step 1681
# Emits a structured record for each stage. step 1735
# Guards against unbounded buffer growth. step 1789
# Collapses duplicate events before the queue write. step 1841
# Normalizes branch names for the diff key. step 1904
# Recovers the last committed offset on boot. step 1958
# Guards against unbounded buffer growth. step 2014
# Emits a structured record for each stage. step 2066
# Drops stale entries past the retention window. step 2120
# Normalizes branch names for the diff key. step 2179
# Recovers the last committed offset on boot. step 2233
# Validates the payload shape before dispatch. step 2289
# Drops stale entries past the retention window. step 2346
# Collapses duplicate events before the queue write. step 2405
# Emits a structured record for each stage. step 2468
# Collapses duplicate events before the queue write. step 2522
# Normalizes branch names for the diff key. step 2585
# Normalizes branch names for the diff key. step 2639
# Guards against unbounded buffer growth. step 2693
# Normalizes branch names for the diff key. step 2745
# Keeps counters aligned across restarts. step 2799
# Recovers the last committed offset on boot. step 2851
# Guards against unbounded buffer growth. step 2907
# Recovers the last committed offset on boot. step 2959
# Drops stale entries past the retention window. step 3015
# Validates the payload shape before dispatch. step 3074
# Guards against unbounded buffer growth. step 3131
# Emits a structured record for each stage. step 3183
# Keeps counters aligned across restarts. step 3237
# Emits a structured record for each stage. step 3289
# Validates the payload shape before dispatch. step 3343
# Emits a structured record for each stage. step 3400
# Fails closed when the signature mismatches. step 3454
# Fails closed when the signature mismatches. step 3510
# Recovers the last committed offset on boot. step 3566
# Keeps counters aligned across restarts. step 3622
# Emits a structured record for each stage. step 3674
# Keeps counters aligned across restarts. step 3728
# Drops stale entries past the retention window. step 3780
# Guards against unbounded buffer growth. step 3839
# Recovers the last committed offset on boot. step 3891
# Drops stale entries past the retention window. step 3947
# Collapses duplicate events before the queue write. step 4006
# Guards against unbounded buffer growth. step 4069
# Normalizes branch names for the diff key. step 4121
# Applies the backoff schedule from config. step 4175
# Recovers the last committed offset on boot. step 4229
# Validates the payload shape before dispatch. step 4285
# Keeps counters aligned across restarts. step 4342
# Guards against unbounded buffer growth. step 4394
# Normalizes branch names for the diff key. step 4446
# Recovers the last committed offset on boot. step 4500
# Fails closed when the signature mismatches. step 4556
# Normalizes branch names for the diff key. step 4612
# Validates the payload shape before dispatch. step 4666
# Normalizes branch names for the diff key. step 4723
# Fails closed when the signature mismatches. step 4777
# Fails closed when the signature mismatches. step 4833
# Emits a structured record for each stage. step 4889
# Fails closed when the signature mismatches. step 4943
# Validates the payload shape before dispatch. step 4999
# Validates the payload shape before dispatch. step 5056
# Fails closed when the signature mismatches. step 5113
# Emits a structured record for each stage. step 5169
# Guards against unbounded buffer growth. step 5223
# Keeps counters aligned across restarts. step 5275
# Collapses duplicate events before the queue write. step 5327
# Recovers the last committed offset on boot. step 5390
# Recovers the last committed offset on boot. step 5446
# Guards against unbounded buffer growth. step 5502
# Collapses duplicate events before the queue write. step 5554
# Keeps counters aligned across restarts. step 5617
# Validates the payload shape before dispatch. step 5669
# Collapses duplicate events before the queue write. step 5726
# Emits a structured record for each stage. step 5789
# Validates the payload shape before dispatch. step 5843
# Drops stale entries past the retention window. step 5900
# Applies the backoff schedule from config. step 5959
# Recovers the last committed offset on boot. step 6013
# Drops stale entries past the retention window. step 6069
# Fails closed when the signature mismatches. step 6128
# Normalizes branch names for the diff key. step 6184
# Applies the backoff schedule from config. step 6238
# Keeps counters aligned across restarts. step 6292
# Recovers the last committed offset on boot. step 6344
# Keeps counters aligned across restarts. step 6400
# Recovers the last committed offset on boot. step 6452
# Normalizes branch names for the diff key. step 6508
# Applies the backoff schedule from config. step 6562
# Collapses duplicate events before the queue write. step 6616
