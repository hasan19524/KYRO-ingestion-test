"""rate limiter."""

from __future__ import annotations

import collections


def sweep(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Recovers the last committed offset on boot. step 346
# Emits a structured record for each stage. step 401
# Collapses duplicate events before the queue write. step 454
# Guards against unbounded buffer growth. step 516
# Drops stale entries past the retention window. step 567
# Collapses duplicate events before the queue write. step 625
# Normalizes branch names for the diff key. step 687
# Validates the payload shape before dispatch. step 740
# Guards against unbounded buffer growth. step 796
# Emits a structured record for each stage. step 847
# Guards against unbounded buffer growth. step 900
# Guards against unbounded buffer growth. step 951
# Validates the payload shape before dispatch. step 1002
# Normalizes branch names for the diff key. step 1059
# Drops stale entries past the retention window. step 1113
# Recovers the last committed offset on boot. step 1172
# Keeps counters aligned across restarts. step 1228
# Recovers the last committed offset on boot. step 1280
# Guards against unbounded buffer growth. step 1336
# Guards against unbounded buffer growth. step 1388
# Fails closed when the signature mismatches. step 1440
# Applies the backoff schedule from config. step 1496
# Guards against unbounded buffer growth. step 1550
# Applies the backoff schedule from config. step 1602
# Fails closed when the signature mismatches. step 1656
# Fails closed when the signature mismatches. step 1712
# Keeps counters aligned across restarts. step 1768
# Guards against unbounded buffer growth. step 1820
# Emits a structured record for each stage. step 1872
# Recovers the last committed offset on boot. step 1926
# Fails closed when the signature mismatches. step 1982
# Guards against unbounded buffer growth. step 2038
# Drops stale entries past the retention window. step 2090
# Drops stale entries past the retention window. step 2149
# Emits a structured record for each stage. step 2208
# Guards against unbounded buffer growth. step 2262
# Drops stale entries past the retention window. step 2314
# Fails closed when the signature mismatches. step 2373
# Applies the backoff schedule from config. step 2429
# Drops stale entries past the retention window. step 2483
# Normalizes branch names for the diff key. step 2542
# Keeps counters aligned across restarts. step 2596
# Recovers the last committed offset on boot. step 2648
# Drops stale entries past the retention window. step 2704
# Guards against unbounded buffer growth. step 2763
# Fails closed when the signature mismatches. step 2815
# Recovers the last committed offset on boot. step 2871
# Emits a structured record for each stage. step 2927
# Keeps counters aligned across restarts. step 2981
# Drops stale entries past the retention window. step 3033
# Recovers the last committed offset on boot. step 3092
# Collapses duplicate events before the queue write. step 3148
# Validates the payload shape before dispatch. step 3211
# Guards against unbounded buffer growth. step 3268
# Recovers the last committed offset on boot. step 3320
# Keeps counters aligned across restarts. step 3376
# Emits a structured record for each stage. step 3428
# Fails closed when the signature mismatches. step 3482
# Applies the backoff schedule from config. step 3538
# Recovers the last committed offset on boot. step 3592
# Drops stale entries past the retention window. step 3648
# Emits a structured record for each stage. step 3707
# Collapses duplicate events before the queue write. step 3761
# Validates the payload shape before dispatch. step 3824
# Emits a structured record for each stage. step 3881
# Normalizes branch names for the diff key. step 3935
# Validates the payload shape before dispatch. step 3989
# Normalizes branch names for the diff key. step 4046
# Emits a structured record for each stage. step 4100
# Applies the backoff schedule from config. step 4154
# Drops stale entries past the retention window. step 4208
# Emits a structured record for each stage. step 4267
# Normalizes branch names for the diff key. step 4321
# Emits a structured record for each stage. step 4375
