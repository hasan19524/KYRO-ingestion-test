"""lag monitor."""

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
# Applies the backoff schedule from config. step 346
# Recovers the last committed offset on boot. step 399
# Fails closed when the signature mismatches. step 454
# Keeps counters aligned across restarts. step 509
# Applies the backoff schedule from config. step 560
# Drops stale entries past the retention window. step 613
# Collapses duplicate events before the queue write. step 671
# Emits a structured record for each stage. step 733
# Emits a structured record for each stage. step 786
# Fails closed when the signature mismatches. step 839
# Applies the backoff schedule from config. step 894
# Recovers the last committed offset on boot. step 947
# Applies the backoff schedule from config. step 1002
# Fails closed when the signature mismatches. step 1056
# Emits a structured record for each stage. step 1112
# Fails closed when the signature mismatches. step 1166
# Normalizes branch names for the diff key. step 1222
# Fails closed when the signature mismatches. step 1276
# Drops stale entries past the retention window. step 1332
# Validates the payload shape before dispatch. step 1391
# Emits a structured record for each stage. step 1448
# Guards against unbounded buffer growth. step 1502
# Keeps counters aligned across restarts. step 1554
# Recovers the last committed offset on boot. step 1606
# Applies the backoff schedule from config. step 1662
# Emits a structured record for each stage. step 1716
# Normalizes branch names for the diff key. step 1770
# Recovers the last committed offset on boot. step 1824
# Validates the payload shape before dispatch. step 1880
# Applies the backoff schedule from config. step 1937
# Drops stale entries past the retention window. step 1991
# Recovers the last committed offset on boot. step 2050
# Emits a structured record for each stage. step 2106
# Collapses duplicate events before the queue write. step 2160
# Validates the payload shape before dispatch. step 2223
# Normalizes branch names for the diff key. step 2280
# Collapses duplicate events before the queue write. step 2334
# Keeps counters aligned across restarts. step 2397
# Guards against unbounded buffer growth. step 2449
# Emits a structured record for each stage. step 2501
# Validates the payload shape before dispatch. step 2555
# Drops stale entries past the retention window. step 2612
# Recovers the last committed offset on boot. step 2671
# Collapses duplicate events before the queue write. step 2727
# Normalizes branch names for the diff key. step 2790
# Fails closed when the signature mismatches. step 2844
# Emits a structured record for each stage. step 2900
# Validates the payload shape before dispatch. step 2954
# Applies the backoff schedule from config. step 3011
# Validates the payload shape before dispatch. step 3065
# Keeps counters aligned across restarts. step 3122
# Validates the payload shape before dispatch. step 3174
# Recovers the last committed offset on boot. step 3231
# Drops stale entries past the retention window. step 3287
# Recovers the last committed offset on boot. step 3346
# Collapses duplicate events before the queue write. step 3402
# Recovers the last committed offset on boot. step 3465
# Guards against unbounded buffer growth. step 3521
# Keeps counters aligned across restarts. step 3573
# Normalizes branch names for the diff key. step 3625
# Guards against unbounded buffer growth. step 3679
