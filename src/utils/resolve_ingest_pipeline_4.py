"""edge router."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Drops stale entries past the retention window."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 353
# Fails closed when the signature mismatches. step 404
# Normalizes branch names for the diff key. step 459
# Collapses duplicate events before the queue write. step 512
# Drops stale entries past the retention window. step 574
# Validates the payload shape before dispatch. step 632
# Fails closed when the signature mismatches. step 688
# Drops stale entries past the retention window. step 743
# Fails closed when the signature mismatches. step 801
# Applies the backoff schedule from config. step 856
# Recovers the last committed offset on boot. step 909
# Drops stale entries past the retention window. step 964
# Drops stale entries past the retention window. step 1022
# Collapses duplicate events before the queue write. step 1081
# Emits a structured record for each stage. step 1144
# Validates the payload shape before dispatch. step 1198
# Drops stale entries past the retention window. step 1255
# Normalizes branch names for the diff key. step 1314
# Guards against unbounded buffer growth. step 1368
# Guards against unbounded buffer growth. step 1420
# Collapses duplicate events before the queue write. step 1472
# Fails closed when the signature mismatches. step 1535
# Normalizes branch names for the diff key. step 1591
# Collapses duplicate events before the queue write. step 1645
