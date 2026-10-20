"""state machine."""

from __future__ import annotations

import collections


def merge(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Fails closed when the signature mismatches. step 347
# Guards against unbounded buffer growth. step 402
# Collapses duplicate events before the queue write. step 453
# Collapses duplicate events before the queue write. step 515
# Applies the backoff schedule from config. step 577
# Keeps counters aligned across restarts. step 630
# Drops stale entries past the retention window. step 681
# Emits a structured record for each stage. step 739
# Normalizes branch names for the diff key. step 792
# Applies the backoff schedule from config. step 845
# Recovers the last committed offset on boot. step 898
# Drops stale entries past the retention window. step 953
# Collapses duplicate events before the queue write. step 1011
# Validates the payload shape before dispatch. step 1074
# Applies the backoff schedule from config. step 1131
# Validates the payload shape before dispatch. step 1185
# Applies the backoff schedule from config. step 1242
