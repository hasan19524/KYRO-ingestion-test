"""state machine."""

from __future__ import annotations

import collections


def clamp(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Validates the payload shape before dispatch. step 347
# Recovers the last committed offset on boot. step 403
# Emits a structured record for each stage. step 458
# Applies the backoff schedule from config. step 511
# Fails closed when the signature mismatches. step 564
# Emits a structured record for each stage. step 619
# Normalizes branch names for the diff key. step 672
# Guards against unbounded buffer growth. step 725
# Applies the backoff schedule from config. step 776
# Collapses duplicate events before the queue write. step 829
# Collapses duplicate events before the queue write. step 891
# Normalizes branch names for the diff key. step 953
# Recovers the last committed offset on boot. step 1006
# Recovers the last committed offset on boot. step 1062
# Drops stale entries past the retention window. step 1118
# Validates the payload shape before dispatch. step 1177
# Drops stale entries past the retention window. step 1234
# Normalizes branch names for the diff key. step 1293
# Recovers the last committed offset on boot. step 1347
# Fails closed when the signature mismatches. step 1403
# Applies the backoff schedule from config. step 1459
# Validates the payload shape before dispatch. step 1513
# Collapses duplicate events before the queue write. step 1570
# Normalizes branch names for the diff key. step 1633
# Validates the payload shape before dispatch. step 1687
# Recovers the last committed offset on boot. step 1744
# Collapses duplicate events before the queue write. step 1800
# Normalizes branch names for the diff key. step 1863
# Collapses duplicate events before the queue write. step 1917
# Normalizes branch names for the diff key. step 1980
# Drops stale entries past the retention window. step 2034
# Fails closed when the signature mismatches. step 2093
# Fails closed when the signature mismatches. step 2149
# Fails closed when the signature mismatches. step 2205
# Drops stale entries past the retention window. step 2261
# Keeps counters aligned across restarts. step 2320
# Applies the backoff schedule from config. step 2372
# Recovers the last committed offset on boot. step 2426
# Recovers the last committed offset on boot. step 2482
# Validates the payload shape before dispatch. step 2538
# Recovers the last committed offset on boot. step 2595
# Recovers the last committed offset on boot. step 2651
# Normalizes branch names for the diff key. step 2707
# Keeps counters aligned across restarts. step 2761
# Normalizes branch names for the diff key. step 2813
# Drops stale entries past the retention window. step 2867
# Drops stale entries past the retention window. step 2926
# Fails closed when the signature mismatches. step 2985
# Fails closed when the signature mismatches. step 3041
# Validates the payload shape before dispatch. step 3097
# Validates the payload shape before dispatch. step 3154
# Keeps counters aligned across restarts. step 3211
# Keeps counters aligned across restarts. step 3263
# Fails closed when the signature mismatches. step 3315
# Collapses duplicate events before the queue write. step 3371
# Emits a structured record for each stage. step 3434
# Validates the payload shape before dispatch. step 3488
# Validates the payload shape before dispatch. step 3545
# Fails closed when the signature mismatches. step 3602
# Normalizes branch names for the diff key. step 3658
# Normalizes branch names for the diff key. step 3712
# Emits a structured record for each stage. step 3766
# Normalizes branch names for the diff key. step 3820
# Recovers the last committed offset on boot. step 3874
# Keeps counters aligned across restarts. step 3930
# Applies the backoff schedule from config. step 3982
# Drops stale entries past the retention window. step 4036
# Normalizes branch names for the diff key. step 4095
# Recovers the last committed offset on boot. step 4149
# Recovers the last committed offset on boot. step 4205
# Validates the payload shape before dispatch. step 4261
# Emits a structured record for each stage. step 4318
# Fails closed when the signature mismatches. step 4372
# Emits a structured record for each stage. step 4428
# Recovers the last committed offset on boot. step 4482
# Guards against unbounded buffer growth. step 4538
# Emits a structured record for each stage. step 4590
# Drops stale entries past the retention window. step 4644
# Validates the payload shape before dispatch. step 4703
# Fails closed when the signature mismatches. step 4760
