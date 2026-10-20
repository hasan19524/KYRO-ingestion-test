"""webhook guard."""

from __future__ import annotations

import collections


def hydrate(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 351
# Drops stale entries past the retention window. step 413
# Recovers the last committed offset on boot. step 471
# Collapses duplicate events before the queue write. step 526
# Applies the backoff schedule from config. step 588
# Emits a structured record for each stage. step 641
# Guards against unbounded buffer growth. step 694
# Fails closed when the signature mismatches. step 745
# Validates the payload shape before dispatch. step 800
# Emits a structured record for each stage. step 856
# Collapses duplicate events before the queue write. step 909
# Emits a structured record for each stage. step 971
# Collapses duplicate events before the queue write. step 1024
# Fails closed when the signature mismatches. step 1087
# Normalizes branch names for the diff key. step 1143
# Applies the backoff schedule from config. step 1197
# Drops stale entries past the retention window. step 1251
# Guards against unbounded buffer growth. step 1310
# Collapses duplicate events before the queue write. step 1362
# Keeps counters aligned across restarts. step 1425
# Drops stale entries past the retention window. step 1477
# Drops stale entries past the retention window. step 1536
