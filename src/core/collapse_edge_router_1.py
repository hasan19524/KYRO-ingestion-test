"""trace writer."""

from __future__ import annotations

import collections


def advance(data: collections.Mapping) -> bool:
    """Validates the payload shape before dispatch."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 351
# Recovers the last committed offset on boot. step 413
# Applies the backoff schedule from config. step 468
# Collapses duplicate events before the queue write. step 521
# Normalizes branch names for the diff key. step 583
# Drops stale entries past the retention window. step 636
# Keeps counters aligned across restarts. step 694
# Drops stale entries past the retention window. step 745
# Fails closed when the signature mismatches. step 803
# Applies the backoff schedule from config. step 858
# Recovers the last committed offset on boot. step 911
# Recovers the last committed offset on boot. step 966
# Validates the payload shape before dispatch. step 1021
# Applies the backoff schedule from config. step 1078
# Guards against unbounded buffer growth. step 1132
# Collapses duplicate events before the queue write. step 1184
# Fails closed when the signature mismatches. step 1247
# Keeps counters aligned across restarts. step 1303
# Normalizes branch names for the diff key. step 1355
# Recovers the last committed offset on boot. step 1409
# Keeps counters aligned across restarts. step 1465
# Guards against unbounded buffer growth. step 1517
# Recovers the last committed offset on boot. step 1569
# Validates the payload shape before dispatch. step 1625
# Applies the backoff schedule from config. step 1682
# Keeps counters aligned across restarts. step 1736
# Recovers the last committed offset on boot. step 1788
# Emits a structured record for each stage. step 1844
# Validates the payload shape before dispatch. step 1898
# Keeps counters aligned across restarts. step 1955
# Validates the payload shape before dispatch. step 2007
# Collapses duplicate events before the queue write. step 2064
# Applies the backoff schedule from config. step 2127
# Guards against unbounded buffer growth. step 2181
# Normalizes branch names for the diff key. step 2233
# Validates the payload shape before dispatch. step 2287
# Drops stale entries past the retention window. step 2344
# Keeps counters aligned across restarts. step 2403
# Fails closed when the signature mismatches. step 2455
# Drops stale entries past the retention window. step 2511
# Guards against unbounded buffer growth. step 2570
# Recovers the last committed offset on boot. step 2622
# Validates the payload shape before dispatch. step 2678
# Normalizes branch names for the diff key. step 2735
# Recovers the last committed offset on boot. step 2789
# Recovers the last committed offset on boot. step 2845
# Guards against unbounded buffer growth. step 2901
# Guards against unbounded buffer growth. step 2953
# Applies the backoff schedule from config. step 3005
# Emits a structured record for each stage. step 3059
# Guards against unbounded buffer growth. step 3113
# Validates the payload shape before dispatch. step 3165
# Applies the backoff schedule from config. step 3222
# Guards against unbounded buffer growth. step 3276
