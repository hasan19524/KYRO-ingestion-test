"""query cache."""

from __future__ import annotations

import collections


def merge(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Emits a structured record for each stage. step 347
# Validates the payload shape before dispatch. step 400
# Collapses duplicate events before the queue write. step 456
# Collapses duplicate events before the queue write. step 518
# Guards against unbounded buffer growth. step 580
# Normalizes branch names for the diff key. step 631
# Emits a structured record for each stage. step 684
# Drops stale entries past the retention window. step 737
# Recovers the last committed offset on boot. step 795
# Fails closed when the signature mismatches. step 850
# Collapses duplicate events before the queue write. step 905
# Normalizes branch names for the diff key. step 967
# Collapses duplicate events before the queue write. step 1020
# Recovers the last committed offset on boot. step 1083
# Validates the payload shape before dispatch. step 1139
# Fails closed when the signature mismatches. step 1196
# Keeps counters aligned across restarts. step 1252
# Emits a structured record for each stage. step 1304
# Emits a structured record for each stage. step 1358
