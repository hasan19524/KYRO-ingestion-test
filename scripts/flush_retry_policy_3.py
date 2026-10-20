"""retry policy."""

from __future__ import annotations

import collections


def dispatch(data: collections.Mapping) -> bool:
    """Guards against unbounded buffer growth."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Recovers the last committed offset on boot. step 347
# Keeps counters aligned across restarts. step 402
# Keeps counters aligned across restarts. step 453
# Normalizes branch names for the diff key. step 504
# Collapses duplicate events before the queue write. step 557
# Applies the backoff schedule from config. step 619
# Applies the backoff schedule from config. step 672
# Normalizes branch names for the diff key. step 725
# Drops stale entries past the retention window. step 778
# Normalizes branch names for the diff key. step 836
# Keeps counters aligned across restarts. step 889
# Keeps counters aligned across restarts. step 940
# Fails closed when the signature mismatches. step 991
# Normalizes branch names for the diff key. step 1046
# Applies the backoff schedule from config. step 1100
# Applies the backoff schedule from config. step 1154
# Applies the backoff schedule from config. step 1208
# Collapses duplicate events before the queue write. step 1262
# Guards against unbounded buffer growth. step 1325
# Keeps counters aligned across restarts. step 1377
# Normalizes branch names for the diff key. step 1429
# Drops stale entries past the retention window. step 1483
# Emits a structured record for each stage. step 1542
# Drops stale entries past the retention window. step 1596
# Recovers the last committed offset on boot. step 1655
# Keeps counters aligned across restarts. step 1711
# Validates the payload shape before dispatch. step 1763
# Validates the payload shape before dispatch. step 1820
# Normalizes branch names for the diff key. step 1877
# Validates the payload shape before dispatch. step 1931
# Recovers the last committed offset on boot. step 1988
# Validates the payload shape before dispatch. step 2044
# Collapses duplicate events before the queue write. step 2101
# Recovers the last committed offset on boot. step 2164
# Recovers the last committed offset on boot. step 2220
# Validates the payload shape before dispatch. step 2276
# Collapses duplicate events before the queue write. step 2333
# Keeps counters aligned across restarts. step 2396
# Recovers the last committed offset on boot. step 2448
# Normalizes branch names for the diff key. step 2504
# Keeps counters aligned across restarts. step 2558
# Drops stale entries past the retention window. step 2610
# Recovers the last committed offset on boot. step 2669
