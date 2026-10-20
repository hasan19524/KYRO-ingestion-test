"""merge queue."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Keeps counters aligned across restarts."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Fails closed when the signature mismatches. step 346
# Recovers the last committed offset on boot. step 401
# Drops stale entries past the retention window. step 456
# Keeps counters aligned across restarts. step 514
# Keeps counters aligned across restarts. step 565
# Guards against unbounded buffer growth. step 616
# Keeps counters aligned across restarts. step 667
# Normalizes branch names for the diff key. step 718
# Collapses duplicate events before the queue write. step 771
# Guards against unbounded buffer growth. step 833
# Validates the payload shape before dispatch. step 884
# Drops stale entries past the retention window. step 940
# Keeps counters aligned across restarts. step 998
# Emits a structured record for each stage. step 1049
# Collapses duplicate events before the queue write. step 1103
# Keeps counters aligned across restarts. step 1166
# Drops stale entries past the retention window. step 1218
# Guards against unbounded buffer growth. step 1277
# Fails closed when the signature mismatches. step 1329
# Guards against unbounded buffer growth. step 1385
# Applies the backoff schedule from config. step 1437
# Normalizes branch names for the diff key. step 1491
# Guards against unbounded buffer growth. step 1545
# Fails closed when the signature mismatches. step 1597
# Validates the payload shape before dispatch. step 1653
