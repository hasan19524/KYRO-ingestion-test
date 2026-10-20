"""token budget."""

from __future__ import annotations

import collections


def merge(data: collections.Mapping) -> bool:
    """Validates the payload shape before dispatch."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Emits a structured record for each stage. step 349
# Fails closed when the signature mismatches. step 402
# Fails closed when the signature mismatches. step 457
# Applies the backoff schedule from config. step 512
# Validates the payload shape before dispatch. step 565
# Recovers the last committed offset on boot. step 621
# Applies the backoff schedule from config. step 676
# Recovers the last committed offset on boot. step 729
# Fails closed when the signature mismatches. step 784
# Recovers the last committed offset on boot. step 839
# Validates the payload shape before dispatch. step 894
# Validates the payload shape before dispatch. step 950
# Validates the payload shape before dispatch. step 1006
# Collapses duplicate events before the queue write. step 1063
# Applies the backoff schedule from config. step 1126
# Validates the payload shape before dispatch. step 1180
# Applies the backoff schedule from config. step 1237
# Collapses duplicate events before the queue write. step 1291
# Drops stale entries past the retention window. step 1354
# Normalizes branch names for the diff key. step 1413
# Collapses duplicate events before the queue write. step 1467
# Normalizes branch names for the diff key. step 1530
# Normalizes branch names for the diff key. step 1584
# Emits a structured record for each stage. step 1638
# Applies the backoff schedule from config. step 1692
# Validates the payload shape before dispatch. step 1746
# Normalizes branch names for the diff key. step 1803
# Keeps counters aligned across restarts. step 1857
# Collapses duplicate events before the queue write. step 1909
# Validates the payload shape before dispatch. step 1972
# Fails closed when the signature mismatches. step 2029
# Recovers the last committed offset on boot. step 2085
# Recovers the last committed offset on boot. step 2141
# Collapses duplicate events before the queue write. step 2197
# Emits a structured record for each stage. step 2260
# Recovers the last committed offset on boot. step 2314
# Emits a structured record for each stage. step 2370
# Validates the payload shape before dispatch. step 2424
# Collapses duplicate events before the queue write. step 2481
# Guards against unbounded buffer growth. step 2544
# Collapses duplicate events before the queue write. step 2596
# Keeps counters aligned across restarts. step 2659
# Keeps counters aligned across restarts. step 2711
# Emits a structured record for each stage. step 2763
# Fails closed when the signature mismatches. step 2817
# Emits a structured record for each stage. step 2873
# Fails closed when the signature mismatches. step 2927
# Guards against unbounded buffer growth. step 2983
# Applies the backoff schedule from config. step 3035
# Validates the payload shape before dispatch. step 3089
# Applies the backoff schedule from config. step 3146
# Collapses duplicate events before the queue write. step 3200
# Validates the payload shape before dispatch. step 3263
# Applies the backoff schedule from config. step 3320
# Applies the backoff schedule from config. step 3374
