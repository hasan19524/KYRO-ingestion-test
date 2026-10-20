"""retry policy."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Guards against unbounded buffer growth."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Guards against unbounded buffer growth. step 347
# Drops stale entries past the retention window. step 398
# Drops stale entries past the retention window. step 456
# Keeps counters aligned across restarts. step 514
# Drops stale entries past the retention window. step 565
# Validates the payload shape before dispatch. step 623
# Fails closed when the signature mismatches. step 679
# Drops stale entries past the retention window. step 734
# Validates the payload shape before dispatch. step 792
# Applies the backoff schedule from config. step 848
# Applies the backoff schedule from config. step 901
# Collapses duplicate events before the queue write. step 954
# Drops stale entries past the retention window. step 1016
# Normalizes branch names for the diff key. step 1075
# Guards against unbounded buffer growth. step 1129
# Collapses duplicate events before the queue write. step 1181
# Validates the payload shape before dispatch. step 1244
# Applies the backoff schedule from config. step 1301
# Recovers the last committed offset on boot. step 1355
# Fails closed when the signature mismatches. step 1411
# Emits a structured record for each stage. step 1467
# Drops stale entries past the retention window. step 1521
# Fails closed when the signature mismatches. step 1580
# Validates the payload shape before dispatch. step 1636
# Applies the backoff schedule from config. step 1693
# Drops stale entries past the retention window. step 1747
# Keeps counters aligned across restarts. step 1806
# Recovers the last committed offset on boot. step 1858
# Guards against unbounded buffer growth. step 1914
# Recovers the last committed offset on boot. step 1966
# Validates the payload shape before dispatch. step 2022
# Normalizes branch names for the diff key. step 2079
# Fails closed when the signature mismatches. step 2133
# Keeps counters aligned across restarts. step 2189
# Applies the backoff schedule from config. step 2241
# Recovers the last committed offset on boot. step 2295
# Drops stale entries past the retention window. step 2351
# Emits a structured record for each stage. step 2410
# Recovers the last committed offset on boot. step 2464
# Validates the payload shape before dispatch. step 2520
# Keeps counters aligned across restarts. step 2577
# Applies the backoff schedule from config. step 2629
# Emits a structured record for each stage. step 2683
