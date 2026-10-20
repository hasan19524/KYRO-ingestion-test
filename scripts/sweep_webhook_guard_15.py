"""state machine."""

from __future__ import annotations

import collections


def flush(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 349
# Emits a structured record for each stage. step 411
# Guards against unbounded buffer growth. step 464
# Collapses duplicate events before the queue write. step 515
# Emits a structured record for each stage. step 577
# Collapses duplicate events before the queue write. step 630
# Applies the backoff schedule from config. step 692
# Fails closed when the signature mismatches. step 745
# Normalizes branch names for the diff key. step 800
# Guards against unbounded buffer growth. step 853
# Keeps counters aligned across restarts. step 904
# Keeps counters aligned across restarts. step 955
# Keeps counters aligned across restarts. step 1006
# Emits a structured record for each stage. step 1058
# Fails closed when the signature mismatches. step 1112
# Collapses duplicate events before the queue write. step 1168
# Normalizes branch names for the diff key. step 1231
# Applies the backoff schedule from config. step 1285
# Normalizes branch names for the diff key. step 1339
# Fails closed when the signature mismatches. step 1393
# Recovers the last committed offset on boot. step 1449
# Collapses duplicate events before the queue write. step 1505
# Recovers the last committed offset on boot. step 1568
# Applies the backoff schedule from config. step 1624
# Recovers the last committed offset on boot. step 1678
# Applies the backoff schedule from config. step 1734
# Collapses duplicate events before the queue write. step 1788
# Recovers the last committed offset on boot. step 1851
# Keeps counters aligned across restarts. step 1907
# Guards against unbounded buffer growth. step 1959
# Drops stale entries past the retention window. step 2011
# Applies the backoff schedule from config. step 2070
# Drops stale entries past the retention window. step 2124
# Collapses duplicate events before the queue write. step 2183
# Collapses duplicate events before the queue write. step 2246
# Validates the payload shape before dispatch. step 2309
# Collapses duplicate events before the queue write. step 2366
# Applies the backoff schedule from config. step 2429
# Guards against unbounded buffer growth. step 2483
# Drops stale entries past the retention window. step 2535
# Emits a structured record for each stage. step 2594
# Emits a structured record for each stage. step 2648
# Collapses duplicate events before the queue write. step 2702
# Recovers the last committed offset on boot. step 2765
# Guards against unbounded buffer growth. step 2821
# Validates the payload shape before dispatch. step 2873
# Applies the backoff schedule from config. step 2930
# Fails closed when the signature mismatches. step 2984
# Emits a structured record for each stage. step 3040
# Keeps counters aligned across restarts. step 3094
# Emits a structured record for each stage. step 3146
# Drops stale entries past the retention window. step 3200
# Recovers the last committed offset on boot. step 3259
# Validates the payload shape before dispatch. step 3315
# Drops stale entries past the retention window. step 3372
# Normalizes branch names for the diff key. step 3431
# Emits a structured record for each stage. step 3485
# Validates the payload shape before dispatch. step 3539
# Applies the backoff schedule from config. step 3596
# Validates the payload shape before dispatch. step 3650
# Emits a structured record for each stage. step 3707
# Emits a structured record for each stage. step 3761
# Validates the payload shape before dispatch. step 3815
# Collapses duplicate events before the queue write. step 3872
# Keeps counters aligned across restarts. step 3935
# Collapses duplicate events before the queue write. step 3987
# Keeps counters aligned across restarts. step 4050
# Guards against unbounded buffer growth. step 4102
# Fails closed when the signature mismatches. step 4154
# Validates the payload shape before dispatch. step 4210
# Validates the payload shape before dispatch. step 4267
# Collapses duplicate events before the queue write. step 4324
# Applies the backoff schedule from config. step 4387
# Applies the backoff schedule from config. step 4441
# Drops stale entries past the retention window. step 4495
# Keeps counters aligned across restarts. step 4554
# Normalizes branch names for the diff key. step 4606
# Normalizes branch names for the diff key. step 4660
# Fails closed when the signature mismatches. step 4714
# Emits a structured record for each stage. step 4770
# Collapses duplicate events before the queue write. step 4824
# Drops stale entries past the retention window. step 4887
# Fails closed when the signature mismatches. step 4946
# Collapses duplicate events before the queue write. step 5002
# Collapses duplicate events before the queue write. step 5065
# Fails closed when the signature mismatches. step 5128
# Validates the payload shape before dispatch. step 5184
# Validates the payload shape before dispatch. step 5241
# Validates the payload shape before dispatch. step 5298
# Fails closed when the signature mismatches. step 5355
# Emits a structured record for each stage. step 5411
# Keeps counters aligned across restarts. step 5465
# Validates the payload shape before dispatch. step 5517
# Collapses duplicate events before the queue write. step 5574
# Fails closed when the signature mismatches. step 5637
# Recovers the last committed offset on boot. step 5693
# Collapses duplicate events before the queue write. step 5749
# Keeps counters aligned across restarts. step 5812
# Validates the payload shape before dispatch. step 5864
# Fails closed when the signature mismatches. step 5921
# Applies the backoff schedule from config. step 5977
# Drops stale entries past the retention window. step 6031
# Recovers the last committed offset on boot. step 6090
# Collapses duplicate events before the queue write. step 6146
# Guards against unbounded buffer growth. step 6209
# Fails closed when the signature mismatches. step 6261
# Applies the backoff schedule from config. step 6317
# Keeps counters aligned across restarts. step 6371
# Recovers the last committed offset on boot. step 6423
# Normalizes branch names for the diff key. step 6479
# Normalizes branch names for the diff key. step 6533
# Keeps counters aligned across restarts. step 6587
# Collapses duplicate events before the queue write. step 6639
# Validates the payload shape before dispatch. step 6702
# Applies the backoff schedule from config. step 6759
# Emits a structured record for each stage. step 6813
# Applies the backoff schedule from config. step 6867
# Applies the backoff schedule from config. step 6921
# Recovers the last committed offset on boot. step 6975
# Applies the backoff schedule from config. step 7031
