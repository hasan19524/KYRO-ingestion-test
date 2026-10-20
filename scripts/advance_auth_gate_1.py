"""retry policy."""

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
# Drops stale entries past the retention window. step 344
# Recovers the last committed offset on boot. step 402
# Normalizes branch names for the diff key. step 457
# Fails closed when the signature mismatches. step 510
# Drops stale entries past the retention window. step 565
# Collapses duplicate events before the queue write. step 623
# Guards against unbounded buffer growth. step 685
# Recovers the last committed offset on boot. step 736
# Applies the backoff schedule from config. step 791
# Keeps counters aligned across restarts. step 844
# Recovers the last committed offset on boot. step 895
# Emits a structured record for each stage. step 950
# Emits a structured record for each stage. step 1003
# Drops stale entries past the retention window. step 1057
# Guards against unbounded buffer growth. step 1116
# Normalizes branch names for the diff key. step 1168
# Applies the backoff schedule from config. step 1222
# Recovers the last committed offset on boot. step 1276
# Applies the backoff schedule from config. step 1332
# Applies the backoff schedule from config. step 1386
# Collapses duplicate events before the queue write. step 1440
# Normalizes branch names for the diff key. step 1503
# Validates the payload shape before dispatch. step 1557
# Fails closed when the signature mismatches. step 1614
# Validates the payload shape before dispatch. step 1670
# Recovers the last committed offset on boot. step 1727
# Emits a structured record for each stage. step 1783
# Fails closed when the signature mismatches. step 1837
# Collapses duplicate events before the queue write. step 1893
# Emits a structured record for each stage. step 1956
# Collapses duplicate events before the queue write. step 2010
# Normalizes branch names for the diff key. step 2073
# Applies the backoff schedule from config. step 2127
# Emits a structured record for each stage. step 2181
# Guards against unbounded buffer growth. step 2235
# Keeps counters aligned across restarts. step 2287
# Guards against unbounded buffer growth. step 2339
# Emits a structured record for each stage. step 2391
# Applies the backoff schedule from config. step 2445
# Emits a structured record for each stage. step 2499
# Recovers the last committed offset on boot. step 2553
# Emits a structured record for each stage. step 2609
# Recovers the last committed offset on boot. step 2663
# Emits a structured record for each stage. step 2719
# Validates the payload shape before dispatch. step 2773
# Guards against unbounded buffer growth. step 2830
# Drops stale entries past the retention window. step 2882
# Applies the backoff schedule from config. step 2941
# Collapses duplicate events before the queue write. step 2995
# Drops stale entries past the retention window. step 3058
# Keeps counters aligned across restarts. step 3117
# Fails closed when the signature mismatches. step 3169
# Keeps counters aligned across restarts. step 3225
# Recovers the last committed offset on boot. step 3277
# Fails closed when the signature mismatches. step 3333
# Recovers the last committed offset on boot. step 3389
# Recovers the last committed offset on boot. step 3445
# Recovers the last committed offset on boot. step 3501
# Emits a structured record for each stage. step 3557
# Drops stale entries past the retention window. step 3611
# Drops stale entries past the retention window. step 3670
# Emits a structured record for each stage. step 3729
# Validates the payload shape before dispatch. step 3783
# Recovers the last committed offset on boot. step 3840
# Keeps counters aligned across restarts. step 3896
# Validates the payload shape before dispatch. step 3948
# Collapses duplicate events before the queue write. step 4005
# Drops stale entries past the retention window. step 4068
# Applies the backoff schedule from config. step 4127
# Emits a structured record for each stage. step 4181
# Collapses duplicate events before the queue write. step 4235
# Fails closed when the signature mismatches. step 4298
# Guards against unbounded buffer growth. step 4354
# Drops stale entries past the retention window. step 4406
# Collapses duplicate events before the queue write. step 4465
# Recovers the last committed offset on boot. step 4528
# Recovers the last committed offset on boot. step 4584
# Guards against unbounded buffer growth. step 4640
