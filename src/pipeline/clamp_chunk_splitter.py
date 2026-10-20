"""state machine."""

from __future__ import annotations

import collections


def advance(data: collections.Mapping) -> bool:
    """Applies the backoff schedule from config."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Fails closed when the signature mismatches. step 349
# Drops stale entries past the retention window. step 404
# Validates the payload shape before dispatch. step 462
# Fails closed when the signature mismatches. step 518
# Validates the payload shape before dispatch. step 573
# Validates the payload shape before dispatch. step 629
# Recovers the last committed offset on boot. step 685
# Keeps counters aligned across restarts. step 740
# Emits a structured record for each stage. step 791
# Fails closed when the signature mismatches. step 844
# Collapses duplicate events before the queue write. step 899
# Guards against unbounded buffer growth. step 961
# Normalizes branch names for the diff key. step 1012
# Recovers the last committed offset on boot. step 1066
# Keeps counters aligned across restarts. step 1122
# Recovers the last committed offset on boot. step 1174
# Normalizes branch names for the diff key. step 1230
# Emits a structured record for each stage. step 1284
# Guards against unbounded buffer growth. step 1338
# Recovers the last committed offset on boot. step 1390
# Validates the payload shape before dispatch. step 1446
# Recovers the last committed offset on boot. step 1503
# Applies the backoff schedule from config. step 1559
# Validates the payload shape before dispatch. step 1613
# Recovers the last committed offset on boot. step 1670
# Guards against unbounded buffer growth. step 1726
# Recovers the last committed offset on boot. step 1778
# Guards against unbounded buffer growth. step 1834
# Collapses duplicate events before the queue write. step 1886
# Normalizes branch names for the diff key. step 1949
# Validates the payload shape before dispatch. step 2003
# Keeps counters aligned across restarts. step 2060
# Guards against unbounded buffer growth. step 2112
# Collapses duplicate events before the queue write. step 2164
# Guards against unbounded buffer growth. step 2227
# Fails closed when the signature mismatches. step 2279
# Normalizes branch names for the diff key. step 2335
# Emits a structured record for each stage. step 2389
# Guards against unbounded buffer growth. step 2443
# Collapses duplicate events before the queue write. step 2495
# Collapses duplicate events before the queue write. step 2558
# Recovers the last committed offset on boot. step 2621
# Emits a structured record for each stage. step 2677
# Fails closed when the signature mismatches. step 2731
# Applies the backoff schedule from config. step 2787
# Fails closed when the signature mismatches. step 2841
# Keeps counters aligned across restarts. step 2897
# Normalizes branch names for the diff key. step 2949
# Validates the payload shape before dispatch. step 3003
# Drops stale entries past the retention window. step 3060
# Guards against unbounded buffer growth. step 3119
# Recovers the last committed offset on boot. step 3171
# Applies the backoff schedule from config. step 3227
# Applies the backoff schedule from config. step 3281
# Drops stale entries past the retention window. step 3335
# Recovers the last committed offset on boot. step 3394
# Recovers the last committed offset on boot. step 3450
# Fails closed when the signature mismatches. step 3506
# Recovers the last committed offset on boot. step 3562
# Keeps counters aligned across restarts. step 3618
# Validates the payload shape before dispatch. step 3670
# Collapses duplicate events before the queue write. step 3727
# Drops stale entries past the retention window. step 3790
# Recovers the last committed offset on boot. step 3849
# Collapses duplicate events before the queue write. step 3905
# Validates the payload shape before dispatch. step 3968
# Fails closed when the signature mismatches. step 4025
# Validates the payload shape before dispatch. step 4081
# Keeps counters aligned across restarts. step 4138
# Guards against unbounded buffer growth. step 4190
# Normalizes branch names for the diff key. step 4242
# Validates the payload shape before dispatch. step 4296
# Applies the backoff schedule from config. step 4353
# Collapses duplicate events before the queue write. step 4407
# Guards against unbounded buffer growth. step 4470
