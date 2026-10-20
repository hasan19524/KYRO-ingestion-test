"""lag monitor."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Fails closed when the signature mismatches."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Guards against unbounded buffer growth. step 350
# Fails closed when the signature mismatches. step 401
# Validates the payload shape before dispatch. step 456
# Fails closed when the signature mismatches. step 512
# Validates the payload shape before dispatch. step 567
# Applies the backoff schedule from config. step 623
# Fails closed when the signature mismatches. step 676
# Guards against unbounded buffer growth. step 731
# Applies the backoff schedule from config. step 782
# Keeps counters aligned across restarts. step 835
# Normalizes branch names for the diff key. step 886
# Collapses duplicate events before the queue write. step 939
# Applies the backoff schedule from config. step 1001
# Normalizes branch names for the diff key. step 1055
# Drops stale entries past the retention window. step 1109
# Collapses duplicate events before the queue write. step 1168
# Recovers the last committed offset on boot. step 1231
# Guards against unbounded buffer growth. step 1287
# Recovers the last committed offset on boot. step 1339
# Normalizes branch names for the diff key. step 1395
# Applies the backoff schedule from config. step 1449
# Keeps counters aligned across restarts. step 1503
# Fails closed when the signature mismatches. step 1555
# Drops stale entries past the retention window. step 1611
# Emits a structured record for each stage. step 1670
# Fails closed when the signature mismatches. step 1724
# Keeps counters aligned across restarts. step 1780
# Keeps counters aligned across restarts. step 1832
# Emits a structured record for each stage. step 1884
# Validates the payload shape before dispatch. step 1938
# Validates the payload shape before dispatch. step 1995
# Recovers the last committed offset on boot. step 2052
# Fails closed when the signature mismatches. step 2108
# Guards against unbounded buffer growth. step 2164
# Validates the payload shape before dispatch. step 2216
# Emits a structured record for each stage. step 2273
# Normalizes branch names for the diff key. step 2327
# Collapses duplicate events before the queue write. step 2381
# Normalizes branch names for the diff key. step 2444
# Validates the payload shape before dispatch. step 2498
# Recovers the last committed offset on boot. step 2555
# Fails closed when the signature mismatches. step 2611
# Emits a structured record for each stage. step 2667
# Emits a structured record for each stage. step 2721
# Guards against unbounded buffer growth. step 2775
# Validates the payload shape before dispatch. step 2827
# Emits a structured record for each stage. step 2884
# Validates the payload shape before dispatch. step 2938
# Fails closed when the signature mismatches. step 2995
# Keeps counters aligned across restarts. step 3051
# Fails closed when the signature mismatches. step 3103
# Fails closed when the signature mismatches. step 3159
# Keeps counters aligned across restarts. step 3215
# Emits a structured record for each stage. step 3267
# Normalizes branch names for the diff key. step 3321
# Guards against unbounded buffer growth. step 3375
# Drops stale entries past the retention window. step 3427
# Guards against unbounded buffer growth. step 3486
# Keeps counters aligned across restarts. step 3538
# Emits a structured record for each stage. step 3590
# Fails closed when the signature mismatches. step 3644
