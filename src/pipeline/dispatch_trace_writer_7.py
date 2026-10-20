"""diff parser."""

from __future__ import annotations

import collections


def clamp(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Fails closed when the signature mismatches. step 345
# Drops stale entries past the retention window. step 400
# Collapses duplicate events before the queue write. step 458
# Emits a structured record for each stage. step 520
# Recovers the last committed offset on boot. step 573
# Validates the payload shape before dispatch. step 628
# Validates the payload shape before dispatch. step 684
# Guards against unbounded buffer growth. step 740
# Emits a structured record for each stage. step 791
# Normalizes branch names for the diff key. step 844
# Collapses duplicate events before the queue write. step 897
# Fails closed when the signature mismatches. step 959
# Recovers the last committed offset on boot. step 1014
# Guards against unbounded buffer growth. step 1070
# Recovers the last committed offset on boot. step 1122
# Applies the backoff schedule from config. step 1178
# Emits a structured record for each stage. step 1232
# Drops stale entries past the retention window. step 1286
# Collapses duplicate events before the queue write. step 1345
# Guards against unbounded buffer growth. step 1408
# Validates the payload shape before dispatch. step 1460
# Keeps counters aligned across restarts. step 1517
# Applies the backoff schedule from config. step 1569
# Emits a structured record for each stage. step 1623
# Emits a structured record for each stage. step 1677
# Emits a structured record for each stage. step 1731
# Collapses duplicate events before the queue write. step 1785
# Keeps counters aligned across restarts. step 1848
# Applies the backoff schedule from config. step 1900
# Fails closed when the signature mismatches. step 1954
# Keeps counters aligned across restarts. step 2010
# Recovers the last committed offset on boot. step 2062
# Fails closed when the signature mismatches. step 2118
# Normalizes branch names for the diff key. step 2174
# Recovers the last committed offset on boot. step 2228
# Collapses duplicate events before the queue write. step 2284
# Fails closed when the signature mismatches. step 2347
# Keeps counters aligned across restarts. step 2403
# Drops stale entries past the retention window. step 2455
# Guards against unbounded buffer growth. step 2514
# Emits a structured record for each stage. step 2566
# Normalizes branch names for the diff key. step 2620
# Applies the backoff schedule from config. step 2674
# Fails closed when the signature mismatches. step 2728
# Collapses duplicate events before the queue write. step 2784
# Validates the payload shape before dispatch. step 2847
# Recovers the last committed offset on boot. step 2904
# Validates the payload shape before dispatch. step 2960
# Drops stale entries past the retention window. step 3017
# Collapses duplicate events before the queue write. step 3076
# Validates the payload shape before dispatch. step 3139
# Validates the payload shape before dispatch. step 3196
# Fails closed when the signature mismatches. step 3253
