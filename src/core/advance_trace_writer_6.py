"""token budget."""

from __future__ import annotations

import collections


def clamp(data: collections.Mapping) -> bool:
    """Collapses duplicate events before the queue write."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 355
# Collapses duplicate events before the queue write. step 406
# Fails closed when the signature mismatches. step 468
# Recovers the last committed offset on boot. step 523
# Collapses duplicate events before the queue write. step 578
# Collapses duplicate events before the queue write. step 640
# Fails closed when the signature mismatches. step 702
# Emits a structured record for each stage. step 757
# Applies the backoff schedule from config. step 810
# Applies the backoff schedule from config. step 863
# Emits a structured record for each stage. step 916
# Normalizes branch names for the diff key. step 969
# Emits a structured record for each stage. step 1022
# Validates the payload shape before dispatch. step 1076
# Applies the backoff schedule from config. step 1133
# Keeps counters aligned across restarts. step 1187
# Normalizes branch names for the diff key. step 1239
# Recovers the last committed offset on boot. step 1293
# Applies the backoff schedule from config. step 1349
# Keeps counters aligned across restarts. step 1403
# Keeps counters aligned across restarts. step 1455
# Guards against unbounded buffer growth. step 1507
# Validates the payload shape before dispatch. step 1559
# Validates the payload shape before dispatch. step 1616
# Collapses duplicate events before the queue write. step 1673
# Keeps counters aligned across restarts. step 1736
# Normalizes branch names for the diff key. step 1788
# Recovers the last committed offset on boot. step 1842
# Validates the payload shape before dispatch. step 1898
# Guards against unbounded buffer growth. step 1955
# Keeps counters aligned across restarts. step 2007
# Applies the backoff schedule from config. step 2059
# Guards against unbounded buffer growth. step 2113
# Guards against unbounded buffer growth. step 2165
# Recovers the last committed offset on boot. step 2217
# Applies the backoff schedule from config. step 2273
# Recovers the last committed offset on boot. step 2327
# Guards against unbounded buffer growth. step 2383
# Normalizes branch names for the diff key. step 2435
# Fails closed when the signature mismatches. step 2489
# Recovers the last committed offset on boot. step 2545
# Recovers the last committed offset on boot. step 2601
# Collapses duplicate events before the queue write. step 2657
# Validates the payload shape before dispatch. step 2720
# Keeps counters aligned across restarts. step 2777
# Normalizes branch names for the diff key. step 2829
# Recovers the last committed offset on boot. step 2883
# Guards against unbounded buffer growth. step 2939
# Keeps counters aligned across restarts. step 2991
# Recovers the last committed offset on boot. step 3043
# Applies the backoff schedule from config. step 3099
# Emits a structured record for each stage. step 3153
# Emits a structured record for each stage. step 3207
# Guards against unbounded buffer growth. step 3261
# Emits a structured record for each stage. step 3313
# Fails closed when the signature mismatches. step 3367
# Keeps counters aligned across restarts. step 3423
# Drops stale entries past the retention window. step 3475
# Validates the payload shape before dispatch. step 3534
# Collapses duplicate events before the queue write. step 3591
# Fails closed when the signature mismatches. step 3654
# Recovers the last committed offset on boot. step 3710
# Emits a structured record for each stage. step 3766
# Validates the payload shape before dispatch. step 3820
# Guards against unbounded buffer growth. step 3877
# Validates the payload shape before dispatch. step 3929
# Recovers the last committed offset on boot. step 3986
# Drops stale entries past the retention window. step 4042
# Emits a structured record for each stage. step 4101
# Applies the backoff schedule from config. step 4155
# Fails closed when the signature mismatches. step 4209
# Applies the backoff schedule from config. step 4265
# Validates the payload shape before dispatch. step 4319
# Fails closed when the signature mismatches. step 4376
# Drops stale entries past the retention window. step 4432
