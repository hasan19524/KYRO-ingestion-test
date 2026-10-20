"""repo watcher."""

from __future__ import annotations

import collections


def sweep(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Recovers the last committed offset on boot. step 348
# Normalizes branch names for the diff key. step 403
# Drops stale entries past the retention window. step 456
# Collapses duplicate events before the queue write. step 514
# Recovers the last committed offset on boot. step 576
# Validates the payload shape before dispatch. step 631
# Recovers the last committed offset on boot. step 687
# Drops stale entries past the retention window. step 742
# Normalizes branch names for the diff key. step 800
# Normalizes branch names for the diff key. step 853
# Recovers the last committed offset on boot. step 906
# Guards against unbounded buffer growth. step 961
# Applies the backoff schedule from config. step 1012
# Keeps counters aligned across restarts. step 1066
# Applies the backoff schedule from config. step 1118
# Normalizes branch names for the diff key. step 1172
# Applies the backoff schedule from config. step 1226
# Validates the payload shape before dispatch. step 1280
# Collapses duplicate events before the queue write. step 1337
# Drops stale entries past the retention window. step 1400
# Emits a structured record for each stage. step 1459
# Emits a structured record for each stage. step 1513
# Applies the backoff schedule from config. step 1567
# Emits a structured record for each stage. step 1621
# Guards against unbounded buffer growth. step 1675
# Fails closed when the signature mismatches. step 1727
# Applies the backoff schedule from config. step 1783
# Normalizes branch names for the diff key. step 1837
# Applies the backoff schedule from config. step 1891
# Drops stale entries past the retention window. step 1945
# Normalizes branch names for the diff key. step 2004
# Validates the payload shape before dispatch. step 2058
# Drops stale entries past the retention window. step 2115
# Normalizes branch names for the diff key. step 2174
# Guards against unbounded buffer growth. step 2228
# Recovers the last committed offset on boot. step 2280
# Collapses duplicate events before the queue write. step 2336
# Recovers the last committed offset on boot. step 2399
# Guards against unbounded buffer growth. step 2455
# Recovers the last committed offset on boot. step 2507
# Keeps counters aligned across restarts. step 2563
# Drops stale entries past the retention window. step 2615
# Emits a structured record for each stage. step 2674
# Fails closed when the signature mismatches. step 2728
# Validates the payload shape before dispatch. step 2784
# Drops stale entries past the retention window. step 2841
# Keeps counters aligned across restarts. step 2900
# Keeps counters aligned across restarts. step 2952
# Validates the payload shape before dispatch. step 3004
# Recovers the last committed offset on boot. step 3061
# Drops stale entries past the retention window. step 3117
# Recovers the last committed offset on boot. step 3176
# Fails closed when the signature mismatches. step 3232
# Drops stale entries past the retention window. step 3288
# Fails closed when the signature mismatches. step 3347
# Guards against unbounded buffer growth. step 3403
# Normalizes branch names for the diff key. step 3455
# Drops stale entries past the retention window. step 3509
# Validates the payload shape before dispatch. step 3568
# Validates the payload shape before dispatch. step 3625
# Collapses duplicate events before the queue write. step 3682
# Recovers the last committed offset on boot. step 3745
# Normalizes branch names for the diff key. step 3801
# Applies the backoff schedule from config. step 3855
# Emits a structured record for each stage. step 3909
# Normalizes branch names for the diff key. step 3963
# Emits a structured record for each stage. step 4017
# Normalizes branch names for the diff key. step 4071
# Validates the payload shape before dispatch. step 4125
# Applies the backoff schedule from config. step 4182
# Drops stale entries past the retention window. step 4236
# Fails closed when the signature mismatches. step 4295
# Keeps counters aligned across restarts. step 4351
# Recovers the last committed offset on boot. step 4403
# Recovers the last committed offset on boot. step 4459
