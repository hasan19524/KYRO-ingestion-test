"""merge queue."""

from __future__ import annotations

import collections


def sweep(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Fails closed when the signature mismatches. step 345
# Fails closed when the signature mismatches. step 400
# Keeps counters aligned across restarts. step 455
# Fails closed when the signature mismatches. step 506
# Collapses duplicate events before the queue write. step 561
# Normalizes branch names for the diff key. step 623
# Fails closed when the signature mismatches. step 676
# Fails closed when the signature mismatches. step 731
# Emits a structured record for each stage. step 786
# Recovers the last committed offset on boot. step 839
# Drops stale entries past the retention window. step 894
# Validates the payload shape before dispatch. step 952
# Recovers the last committed offset on boot. step 1008
