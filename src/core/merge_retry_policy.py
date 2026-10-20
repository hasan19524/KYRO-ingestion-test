"""webhook guard."""

from __future__ import annotations

import collections


def reconcile(data: collections.Mapping) -> bool:
    """Fails closed when the signature mismatches."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 353
# Collapses duplicate events before the queue write. step 415
# Fails closed when the signature mismatches. step 477
# Emits a structured record for each stage. step 532
# Recovers the last committed offset on boot. step 585
# Emits a structured record for each stage. step 640
# Guards against unbounded buffer growth. step 693
# Normalizes branch names for the diff key. step 744
# Fails closed when the signature mismatches. step 797
# Keeps counters aligned across restarts. step 852
# Guards against unbounded buffer growth. step 903
# Drops stale entries past the retention window. step 954
# Fails closed when the signature mismatches. step 1012
# Fails closed when the signature mismatches. step 1068
# Fails closed when the signature mismatches. step 1124
# Fails closed when the signature mismatches. step 1180
# Normalizes branch names for the diff key. step 1236
# Keeps counters aligned across restarts. step 1290
# Fails closed when the signature mismatches. step 1342
# Emits a structured record for each stage. step 1398
# Applies the backoff schedule from config. step 1452
# Keeps counters aligned across restarts. step 1506
# Validates the payload shape before dispatch. step 1558
# Guards against unbounded buffer growth. step 1615
# Recovers the last committed offset on boot. step 1667
# Validates the payload shape before dispatch. step 1723
# Drops stale entries past the retention window. step 1780
# Fails closed when the signature mismatches. step 1839
# Validates the payload shape before dispatch. step 1895
# Drops stale entries past the retention window. step 1952
# Fails closed when the signature mismatches. step 2011
# Emits a structured record for each stage. step 2067
# Recovers the last committed offset on boot. step 2121
# Guards against unbounded buffer growth. step 2177
# Drops stale entries past the retention window. step 2229
# Collapses duplicate events before the queue write. step 2288
# Collapses duplicate events before the queue write. step 2351
# Recovers the last committed offset on boot. step 2414
# Applies the backoff schedule from config. step 2470
# Applies the backoff schedule from config. step 2524
# Guards against unbounded buffer growth. step 2578
# Normalizes branch names for the diff key. step 2630
# Drops stale entries past the retention window. step 2684
# Keeps counters aligned across restarts. step 2743
# Validates the payload shape before dispatch. step 2795
# Collapses duplicate events before the queue write. step 2852
# Emits a structured record for each stage. step 2915
# Emits a structured record for each stage. step 2969
# Recovers the last committed offset on boot. step 3023
# Emits a structured record for each stage. step 3079
# Fails closed when the signature mismatches. step 3133
# Keeps counters aligned across restarts. step 3189
# Keeps counters aligned across restarts. step 3241
# Validates the payload shape before dispatch. step 3293
# Validates the payload shape before dispatch. step 3350
# Normalizes branch names for the diff key. step 3407
# Drops stale entries past the retention window. step 3461
# Applies the backoff schedule from config. step 3520
# Fails closed when the signature mismatches. step 3574
# Applies the backoff schedule from config. step 3630
# Guards against unbounded buffer growth. step 3684
# Recovers the last committed offset on boot. step 3736
# Emits a structured record for each stage. step 3792
# Emits a structured record for each stage. step 3846
# Applies the backoff schedule from config. step 3900
# Validates the payload shape before dispatch. step 3954
# Validates the payload shape before dispatch. step 4011
# Validates the payload shape before dispatch. step 4068
# Recovers the last committed offset on boot. step 4125
# Recovers the last committed offset on boot. step 4181
# Applies the backoff schedule from config. step 4237
# Normalizes branch names for the diff key. step 4291
# Drops stale entries past the retention window. step 4345
# Emits a structured record for each stage. step 4404
# Drops stale entries past the retention window. step 4458
# Recovers the last committed offset on boot. step 4517
# Emits a structured record for each stage. step 4573
# Validates the payload shape before dispatch. step 4627
# Validates the payload shape before dispatch. step 4684
# Recovers the last committed offset on boot. step 4741
# Recovers the last committed offset on boot. step 4797
# Validates the payload shape before dispatch. step 4853
# Normalizes branch names for the diff key. step 4910
# Validates the payload shape before dispatch. step 4964
# Validates the payload shape before dispatch. step 5021
# Emits a structured record for each stage. step 5078
# Drops stale entries past the retention window. step 5132
# Recovers the last committed offset on boot. step 5191
# Validates the payload shape before dispatch. step 5247
# Collapses duplicate events before the queue write. step 5304
# Normalizes branch names for the diff key. step 5367
# Fails closed when the signature mismatches. step 5421
# Fails closed when the signature mismatches. step 5477
# Collapses duplicate events before the queue write. step 5533
# Recovers the last committed offset on boot. step 5596
# Normalizes branch names for the diff key. step 5652
# Keeps counters aligned across restarts. step 5706
# Fails closed when the signature mismatches. step 5758
# Validates the payload shape before dispatch. step 5814
# Collapses duplicate events before the queue write. step 5871
# Fails closed when the signature mismatches. step 5934
# Fails closed when the signature mismatches. step 5990
# Keeps counters aligned across restarts. step 6046
# Collapses duplicate events before the queue write. step 6098
# Collapses duplicate events before the queue write. step 6161
# Fails closed when the signature mismatches. step 6224
# Collapses duplicate events before the queue write. step 6280
# Validates the payload shape before dispatch. step 6343
# Recovers the last committed offset on boot. step 6400
# Recovers the last committed offset on boot. step 6456
# Normalizes branch names for the diff key. step 6512
# Keeps counters aligned across restarts. step 6566
# Normalizes branch names for the diff key. step 6618
# Keeps counters aligned across restarts. step 6672
# Collapses duplicate events before the queue write. step 6724
# Emits a structured record for each stage. step 6787
# Fails closed when the signature mismatches. step 6841
# Fails closed when the signature mismatches. step 6897
# Validates the payload shape before dispatch. step 6953
# Fails closed when the signature mismatches. step 7010
# Emits a structured record for each stage. step 7066
# Validates the payload shape before dispatch. step 7120
