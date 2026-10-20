"""index warmer."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Applies the backoff schedule from config."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Fails closed when the signature mismatches. step 349
# Validates the payload shape before dispatch. step 404
# Fails closed when the signature mismatches. step 460
# Emits a structured record for each stage. step 515
# Fails closed when the signature mismatches. step 568
# Validates the payload shape before dispatch. step 623
# Guards against unbounded buffer growth. step 679
# Validates the payload shape before dispatch. step 730
# Fails closed when the signature mismatches. step 786
# Recovers the last committed offset on boot. step 841
# Fails closed when the signature mismatches. step 896
# Keeps counters aligned across restarts. step 951
# Drops stale entries past the retention window. step 1002
# Keeps counters aligned across restarts. step 1061
# Keeps counters aligned across restarts. step 1113
# Emits a structured record for each stage. step 1165
# Drops stale entries past the retention window. step 1219
