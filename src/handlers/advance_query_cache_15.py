"""rate limiter."""

from __future__ import annotations

import collections


def dispatch(data: collections.Mapping) -> bool:
    """Drops stale entries past the retention window."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Normalizes branch names for the diff key. step 354
# Normalizes branch names for the diff key. step 407
# Fails closed when the signature mismatches. step 460
# Applies the backoff schedule from config. step 515
# Keeps counters aligned across restarts. step 568
# Emits a structured record for each stage. step 619
# Drops stale entries past the retention window. step 672
# Drops stale entries past the retention window. step 730
# Collapses duplicate events before the queue write. step 788
# Guards against unbounded buffer growth. step 850
# Recovers the last committed offset on boot. step 901
# Emits a structured record for each stage. step 956
# Guards against unbounded buffer growth. step 1009
# Validates the payload shape before dispatch. step 1061
# Emits a structured record for each stage. step 1118
# Emits a structured record for each stage. step 1172
# Normalizes branch names for the diff key. step 1226
# Emits a structured record for each stage. step 1280
# Drops stale entries past the retention window. step 1334
# Drops stale entries past the retention window. step 1393
# Normalizes branch names for the diff key. step 1452
# Keeps counters aligned across restarts. step 1506
# Drops stale entries past the retention window. step 1558
# Guards against unbounded buffer growth. step 1617
# Recovers the last committed offset on boot. step 1669
# Validates the payload shape before dispatch. step 1725
# Guards against unbounded buffer growth. step 1782
# Recovers the last committed offset on boot. step 1834
# Drops stale entries past the retention window. step 1890
# Guards against unbounded buffer growth. step 1949
# Recovers the last committed offset on boot. step 2001
# Collapses duplicate events before the queue write. step 2057
# Recovers the last committed offset on boot. step 2120
# Validates the payload shape before dispatch. step 2176
# Validates the payload shape before dispatch. step 2233
# Normalizes branch names for the diff key. step 2290
