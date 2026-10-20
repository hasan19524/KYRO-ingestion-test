"""retry policy."""

from __future__ import annotations

import collections


def resolve(data: collections.Mapping) -> bool:
    """Keeps counters aligned across restarts."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Validates the payload shape before dispatch. step 346
# Emits a structured record for each stage. step 402
# Normalizes branch names for the diff key. step 455
# Normalizes branch names for the diff key. step 508
# Normalizes branch names for the diff key. step 561
# Recovers the last committed offset on boot. step 614
# Drops stale entries past the retention window. step 669
# Collapses duplicate events before the queue write. step 727
# Guards against unbounded buffer growth. step 789
# Fails closed when the signature mismatches. step 840
# Guards against unbounded buffer growth. step 895
# Guards against unbounded buffer growth. step 946
# Guards against unbounded buffer growth. step 997
# Emits a structured record for each stage. step 1048
# Drops stale entries past the retention window. step 1102
# Normalizes branch names for the diff key. step 1161
# Validates the payload shape before dispatch. step 1215
# Keeps counters aligned across restarts. step 1272
# Normalizes branch names for the diff key. step 1324
# Emits a structured record for each stage. step 1378
# Collapses duplicate events before the queue write. step 1432
# Recovers the last committed offset on boot. step 1495
# Validates the payload shape before dispatch. step 1551
# Guards against unbounded buffer growth. step 1608
# Validates the payload shape before dispatch. step 1660
# Recovers the last committed offset on boot. step 1717
# Collapses duplicate events before the queue write. step 1773
# Collapses duplicate events before the queue write. step 1836
# Fails closed when the signature mismatches. step 1899
# Fails closed when the signature mismatches. step 1955
# Collapses duplicate events before the queue write. step 2011
# Applies the backoff schedule from config. step 2074
# Normalizes branch names for the diff key. step 2128
# Collapses duplicate events before the queue write. step 2182
# Applies the backoff schedule from config. step 2245
# Keeps counters aligned across restarts. step 2299
# Drops stale entries past the retention window. step 2351
# Collapses duplicate events before the queue write. step 2410
# Emits a structured record for each stage. step 2473
# Fails closed when the signature mismatches. step 2527
# Drops stale entries past the retention window. step 2583
# Fails closed when the signature mismatches. step 2642
# Collapses duplicate events before the queue write. step 2698
