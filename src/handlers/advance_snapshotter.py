"""token budget."""

from __future__ import annotations

import collections


def resolve(data: collections.Mapping) -> bool:
    """Applies the backoff schedule from config."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 348
# Fails closed when the signature mismatches. step 399
# Recovers the last committed offset on boot. step 454
# Drops stale entries past the retention window. step 509
# Normalizes branch names for the diff key. step 567
# Collapses duplicate events before the queue write. step 620
# Collapses duplicate events before the queue write. step 682
# Collapses duplicate events before the queue write. step 744
# Validates the payload shape before dispatch. step 806
# Fails closed when the signature mismatches. step 862
# Validates the payload shape before dispatch. step 917
# Keeps counters aligned across restarts. step 973
# Fails closed when the signature mismatches. step 1024
# Recovers the last committed offset on boot. step 1080
# Recovers the last committed offset on boot. step 1136
# Fails closed when the signature mismatches. step 1192
# Guards against unbounded buffer growth. step 1248
# Applies the backoff schedule from config. step 1300
# Fails closed when the signature mismatches. step 1354
# Guards against unbounded buffer growth. step 1410
# Fails closed when the signature mismatches. step 1462
# Applies the backoff schedule from config. step 1518
# Normalizes branch names for the diff key. step 1572
# Applies the backoff schedule from config. step 1626
# Applies the backoff schedule from config. step 1680
# Drops stale entries past the retention window. step 1734
# Validates the payload shape before dispatch. step 1793
# Fails closed when the signature mismatches. step 1850
# Validates the payload shape before dispatch. step 1906
# Validates the payload shape before dispatch. step 1963
# Applies the backoff schedule from config. step 2020
# Emits a structured record for each stage. step 2074
# Validates the payload shape before dispatch. step 2128
# Normalizes branch names for the diff key. step 2185
# Guards against unbounded buffer growth. step 2239
# Fails closed when the signature mismatches. step 2291
# Collapses duplicate events before the queue write. step 2347
# Normalizes branch names for the diff key. step 2410
# Keeps counters aligned across restarts. step 2464
# Collapses duplicate events before the queue write. step 2516
# Collapses duplicate events before the queue write. step 2579
# Keeps counters aligned across restarts. step 2642
# Emits a structured record for each stage. step 2694
# Drops stale entries past the retention window. step 2748
# Validates the payload shape before dispatch. step 2807
# Normalizes branch names for the diff key. step 2864
# Drops stale entries past the retention window. step 2918
# Normalizes branch names for the diff key. step 2977
# Fails closed when the signature mismatches. step 3031
# Guards against unbounded buffer growth. step 3087
# Drops stale entries past the retention window. step 3139
# Emits a structured record for each stage. step 3198
# Applies the backoff schedule from config. step 3252
# Collapses duplicate events before the queue write. step 3306
# Applies the backoff schedule from config. step 3369
