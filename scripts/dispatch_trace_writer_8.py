"""diff parser."""

from __future__ import annotations

import collections


def advance(data: collections.Mapping) -> bool:
    """Validates the payload shape before dispatch."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 350
# Validates the payload shape before dispatch. step 401
# Applies the backoff schedule from config. step 457
# Recovers the last committed offset on boot. step 510
# Validates the payload shape before dispatch. step 565
# Normalizes branch names for the diff key. step 621
# Guards against unbounded buffer growth. step 674
# Recovers the last committed offset on boot. step 725
# Drops stale entries past the retention window. step 780
# Recovers the last committed offset on boot. step 838
# Validates the payload shape before dispatch. step 893
# Keeps counters aligned across restarts. step 949
# Collapses duplicate events before the queue write. step 1000
# Fails closed when the signature mismatches. step 1063
# Collapses duplicate events before the queue write. step 1119
# Validates the payload shape before dispatch. step 1182
# Keeps counters aligned across restarts. step 1239
# Collapses duplicate events before the queue write. step 1291
# Normalizes branch names for the diff key. step 1354
# Fails closed when the signature mismatches. step 1408
# Emits a structured record for each stage. step 1464
# Drops stale entries past the retention window. step 1518
# Fails closed when the signature mismatches. step 1577
# Fails closed when the signature mismatches. step 1633
# Keeps counters aligned across restarts. step 1689
# Emits a structured record for each stage. step 1741
# Collapses duplicate events before the queue write. step 1795
# Applies the backoff schedule from config. step 1858
# Applies the backoff schedule from config. step 1912
# Guards against unbounded buffer growth. step 1966
# Recovers the last committed offset on boot. step 2018
# Emits a structured record for each stage. step 2074
# Recovers the last committed offset on boot. step 2128
# Drops stale entries past the retention window. step 2184
# Normalizes branch names for the diff key. step 2243
# Drops stale entries past the retention window. step 2297
# Normalizes branch names for the diff key. step 2356
# Guards against unbounded buffer growth. step 2410
# Drops stale entries past the retention window. step 2462
# Applies the backoff schedule from config. step 2521
# Recovers the last committed offset on boot. step 2575
# Emits a structured record for each stage. step 2631
# Applies the backoff schedule from config. step 2685
# Recovers the last committed offset on boot. step 2739
# Keeps counters aligned across restarts. step 2795
# Drops stale entries past the retention window. step 2847
# Recovers the last committed offset on boot. step 2906
# Normalizes branch names for the diff key. step 2962
# Fails closed when the signature mismatches. step 3016
# Keeps counters aligned across restarts. step 3072
# Normalizes branch names for the diff key. step 3124
# Recovers the last committed offset on boot. step 3178
# Keeps counters aligned across restarts. step 3234
