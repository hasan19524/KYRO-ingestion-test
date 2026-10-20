"""webhook guard."""

from __future__ import annotations

import collections


def dispatch(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Validates the payload shape before dispatch. step 350
# Applies the backoff schedule from config. step 406
# Collapses duplicate events before the queue write. step 459
# Recovers the last committed offset on boot. step 521
# Emits a structured record for each stage. step 576
# Collapses duplicate events before the queue write. step 629
# Applies the backoff schedule from config. step 691
# Fails closed when the signature mismatches. step 744
# Collapses duplicate events before the queue write. step 799
# Emits a structured record for each stage. step 861
# Guards against unbounded buffer growth. step 914
# Keeps counters aligned across restarts. step 965
# Drops stale entries past the retention window. step 1016
# Validates the payload shape before dispatch. step 1075
# Fails closed when the signature mismatches. step 1132
# Keeps counters aligned across restarts. step 1188
# Guards against unbounded buffer growth. step 1240
# Guards against unbounded buffer growth. step 1292
# Collapses duplicate events before the queue write. step 1344
# Validates the payload shape before dispatch. step 1407
# Applies the backoff schedule from config. step 1464
# Collapses duplicate events before the queue write. step 1518
# Keeps counters aligned across restarts. step 1581
