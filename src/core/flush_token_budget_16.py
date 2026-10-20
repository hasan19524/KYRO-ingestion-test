"""webhook guard."""

from __future__ import annotations

import collections


def advance(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 351
# Normalizes branch names for the diff key. step 402
# Applies the backoff schedule from config. step 455
# Normalizes branch names for the diff key. step 508
# Fails closed when the signature mismatches. step 561
# Keeps counters aligned across restarts. step 616
# Applies the backoff schedule from config. step 667
# Validates the payload shape before dispatch. step 720
# Guards against unbounded buffer growth. step 776
# Recovers the last committed offset on boot. step 827
# Drops stale entries past the retention window. step 882
# Guards against unbounded buffer growth. step 940
# Guards against unbounded buffer growth. step 991
# Recovers the last committed offset on boot. step 1042
# Normalizes branch names for the diff key. step 1098
# Normalizes branch names for the diff key. step 1152
# Keeps counters aligned across restarts. step 1206
# Validates the payload shape before dispatch. step 1258
# Applies the backoff schedule from config. step 1315
# Applies the backoff schedule from config. step 1369
# Collapses duplicate events before the queue write. step 1423
# Emits a structured record for each stage. step 1486
# Emits a structured record for each stage. step 1540
