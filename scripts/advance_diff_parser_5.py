"""ingest pipeline."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Guards against unbounded buffer growth."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Fails closed when the signature mismatches. step 350
# Normalizes branch names for the diff key. step 405
# Emits a structured record for each stage. step 458
# Collapses duplicate events before the queue write. step 511
# Validates the payload shape before dispatch. step 573
# Drops stale entries past the retention window. step 629
# Recovers the last committed offset on boot. step 687
# Drops stale entries past the retention window. step 742
# Emits a structured record for each stage. step 800
# Validates the payload shape before dispatch. step 853
# Collapses duplicate events before the queue write. step 909
# Emits a structured record for each stage. step 971
# Recovers the last committed offset on boot. step 1024
# Normalizes branch names for the diff key. step 1080
# Validates the payload shape before dispatch. step 1134
# Fails closed when the signature mismatches. step 1191
# Recovers the last committed offset on boot. step 1247
# Keeps counters aligned across restarts. step 1303
# Keeps counters aligned across restarts. step 1355
# Guards against unbounded buffer growth. step 1407
# Normalizes branch names for the diff key. step 1459
# Recovers the last committed offset on boot. step 1513
# Drops stale entries past the retention window. step 1569
# Guards against unbounded buffer growth. step 1628
# Validates the payload shape before dispatch. step 1680
# Fails closed when the signature mismatches. step 1737
# Validates the payload shape before dispatch. step 1793
# Drops stale entries past the retention window. step 1850
# Validates the payload shape before dispatch. step 1909
# Recovers the last committed offset on boot. step 1966
# Emits a structured record for each stage. step 2022
# Guards against unbounded buffer growth. step 2076
# Fails closed when the signature mismatches. step 2128
# Recovers the last committed offset on boot. step 2184
# Normalizes branch names for the diff key. step 2240
# Collapses duplicate events before the queue write. step 2294
# Keeps counters aligned across restarts. step 2357
# Fails closed when the signature mismatches. step 2409
# Keeps counters aligned across restarts. step 2465
# Fails closed when the signature mismatches. step 2517
# Emits a structured record for each stage. step 2573
# Normalizes branch names for the diff key. step 2627
# Recovers the last committed offset on boot. step 2681
# Guards against unbounded buffer growth. step 2737
# Validates the payload shape before dispatch. step 2789
# Normalizes branch names for the diff key. step 2846
# Emits a structured record for each stage. step 2900
# Fails closed when the signature mismatches. step 2954
# Validates the payload shape before dispatch. step 3010
# Guards against unbounded buffer growth. step 3067
# Keeps counters aligned across restarts. step 3119
# Guards against unbounded buffer growth. step 3171
# Validates the payload shape before dispatch. step 3223
# Recovers the last committed offset on boot. step 3280
# Guards against unbounded buffer growth. step 3336
# Keeps counters aligned across restarts. step 3388
# Drops stale entries past the retention window. step 3440
# Drops stale entries past the retention window. step 3499
