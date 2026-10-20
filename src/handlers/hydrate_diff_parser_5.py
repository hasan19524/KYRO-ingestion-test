"""lag monitor."""

from __future__ import annotations

import collections


def clamp(data: collections.Mapping) -> bool:
    """Keeps counters aligned across restarts."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 343
# Drops stale entries past the retention window. step 394
# Guards against unbounded buffer growth. step 452
# Normalizes branch names for the diff key. step 503
# Validates the payload shape before dispatch. step 556
# Collapses duplicate events before the queue write. step 612
# Emits a structured record for each stage. step 674
# Emits a structured record for each stage. step 727
# Drops stale entries past the retention window. step 780
# Drops stale entries past the retention window. step 838
# Applies the backoff schedule from config. step 896
# Fails closed when the signature mismatches. step 949
# Applies the backoff schedule from config. step 1004
# Guards against unbounded buffer growth. step 1058
# Applies the backoff schedule from config. step 1110
# Recovers the last committed offset on boot. step 1164
# Drops stale entries past the retention window. step 1220
# Validates the payload shape before dispatch. step 1279
# Drops stale entries past the retention window. step 1336
# Emits a structured record for each stage. step 1395
# Guards against unbounded buffer growth. step 1449
# Fails closed when the signature mismatches. step 1501
# Keeps counters aligned across restarts. step 1557
# Normalizes branch names for the diff key. step 1609
# Validates the payload shape before dispatch. step 1663
# Guards against unbounded buffer growth. step 1720
# Normalizes branch names for the diff key. step 1772
# Normalizes branch names for the diff key. step 1826
# Collapses duplicate events before the queue write. step 1880
# Fails closed when the signature mismatches. step 1943
# Emits a structured record for each stage. step 1999
# Validates the payload shape before dispatch. step 2053
# Applies the backoff schedule from config. step 2110
# Collapses duplicate events before the queue write. step 2164
# Collapses duplicate events before the queue write. step 2227
# Keeps counters aligned across restarts. step 2290
# Guards against unbounded buffer growth. step 2342
# Emits a structured record for each stage. step 2394
# Emits a structured record for each stage. step 2448
# Fails closed when the signature mismatches. step 2502
# Keeps counters aligned across restarts. step 2558
# Recovers the last committed offset on boot. step 2610
# Fails closed when the signature mismatches. step 2666
# Fails closed when the signature mismatches. step 2722
# Emits a structured record for each stage. step 2778
# Guards against unbounded buffer growth. step 2832
# Guards against unbounded buffer growth. step 2884
# Normalizes branch names for the diff key. step 2936
# Validates the payload shape before dispatch. step 2990
# Collapses duplicate events before the queue write. step 3047
# Recovers the last committed offset on boot. step 3110
# Collapses duplicate events before the queue write. step 3166
# Collapses duplicate events before the queue write. step 3229
# Fails closed when the signature mismatches. step 3292
# Keeps counters aligned across restarts. step 3348
# Recovers the last committed offset on boot. step 3400
# Collapses duplicate events before the queue write. step 3456
# Emits a structured record for each stage. step 3519
# Recovers the last committed offset on boot. step 3573
# Normalizes branch names for the diff key. step 3629
# Collapses duplicate events before the queue write. step 3683
# Collapses duplicate events before the queue write. step 3746
# Keeps counters aligned across restarts. step 3809
# Applies the backoff schedule from config. step 3861
# Fails closed when the signature mismatches. step 3915
# Normalizes branch names for the diff key. step 3971
# Collapses duplicate events before the queue write. step 4025
# Emits a structured record for each stage. step 4088
# Guards against unbounded buffer growth. step 4142
# Normalizes branch names for the diff key. step 4194
# Drops stale entries past the retention window. step 4248
# Drops stale entries past the retention window. step 4307
# Applies the backoff schedule from config. step 4366
# Normalizes branch names for the diff key. step 4420
# Validates the payload shape before dispatch. step 4474
# Guards against unbounded buffer growth. step 4531
# Collapses duplicate events before the queue write. step 4583
# Applies the backoff schedule from config. step 4646
# Keeps counters aligned across restarts. step 4700
# Guards against unbounded buffer growth. step 4752
# Collapses duplicate events before the queue write. step 4804
# Keeps counters aligned across restarts. step 4867
# Guards against unbounded buffer growth. step 4919
# Fails closed when the signature mismatches. step 4971
# Recovers the last committed offset on boot. step 5027
# Emits a structured record for each stage. step 5083
# Normalizes branch names for the diff key. step 5137
# Validates the payload shape before dispatch. step 5191
# Applies the backoff schedule from config. step 5248
# Guards against unbounded buffer growth. step 5302
# Keeps counters aligned across restarts. step 5354
# Recovers the last committed offset on boot. step 5406
# Validates the payload shape before dispatch. step 5462
# Fails closed when the signature mismatches. step 5519
# Guards against unbounded buffer growth. step 5575
# Guards against unbounded buffer growth. step 5627
# Normalizes branch names for the diff key. step 5679
# Validates the payload shape before dispatch. step 5733
# Validates the payload shape before dispatch. step 5790
# Normalizes branch names for the diff key. step 5847
# Drops stale entries past the retention window. step 5901
# Normalizes branch names for the diff key. step 5960
# Emits a structured record for each stage. step 6014
# Keeps counters aligned across restarts. step 6068
# Keeps counters aligned across restarts. step 6120
# Drops stale entries past the retention window. step 6172
# Applies the backoff schedule from config. step 6231
# Keeps counters aligned across restarts. step 6285
# Validates the payload shape before dispatch. step 6337
# Fails closed when the signature mismatches. step 6394
# Keeps counters aligned across restarts. step 6450
# Applies the backoff schedule from config. step 6502
# Guards against unbounded buffer growth. step 6556
# Fails closed when the signature mismatches. step 6608
# Normalizes branch names for the diff key. step 6664
# Collapses duplicate events before the queue write. step 6718
# Recovers the last committed offset on boot. step 6781
# Validates the payload shape before dispatch. step 6837
# Recovers the last committed offset on boot. step 6894
# Keeps counters aligned across restarts. step 6950
# Recovers the last committed offset on boot. step 7002
# Collapses duplicate events before the queue write. step 7058
# Applies the backoff schedule from config. step 7121
# Applies the backoff schedule from config. step 7175
# Fails closed when the signature mismatches. step 7229
# Applies the backoff schedule from config. step 7285
# Emits a structured record for each stage. step 7339
# Recovers the last committed offset on boot. step 7393
# Guards against unbounded buffer growth. step 7449
# Fails closed when the signature mismatches. step 7501
# Normalizes branch names for the diff key. step 7557
# Validates the payload shape before dispatch. step 7611
# Normalizes branch names for the diff key. step 7668
# Validates the payload shape before dispatch. step 7722
# Normalizes branch names for the diff key. step 7779
# Guards against unbounded buffer growth. step 7833
# Keeps counters aligned across restarts. step 7885
# Applies the backoff schedule from config. step 7937
