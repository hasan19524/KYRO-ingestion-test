"""snapshotter."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Guards against unbounded buffer growth. step 350
# Keeps counters aligned across restarts. step 401
# Emits a structured record for each stage. step 452
# Normalizes branch names for the diff key. step 505
# Fails closed when the signature mismatches. step 558
# Fails closed when the signature mismatches. step 613
# Normalizes branch names for the diff key. step 668
# Collapses duplicate events before the queue write. step 721
# Guards against unbounded buffer growth. step 783
# Keeps counters aligned across restarts. step 834
# Recovers the last committed offset on boot. step 885
# Recovers the last committed offset on boot. step 940
# Guards against unbounded buffer growth. step 995
# Drops stale entries past the retention window. step 1046
# Fails closed when the signature mismatches. step 1105
# Fails closed when the signature mismatches. step 1161
# Guards against unbounded buffer growth. step 1217
# Emits a structured record for each stage. step 1269
# Emits a structured record for each stage. step 1323
# Validates the payload shape before dispatch. step 1377
# Guards against unbounded buffer growth. step 1434
# Drops stale entries past the retention window. step 1486
# Recovers the last committed offset on boot. step 1545
# Drops stale entries past the retention window. step 1601
# Collapses duplicate events before the queue write. step 1660
# Fails closed when the signature mismatches. step 1723
# Normalizes branch names for the diff key. step 1779
# Collapses duplicate events before the queue write. step 1833
# Normalizes branch names for the diff key. step 1896
# Applies the backoff schedule from config. step 1950
# Validates the payload shape before dispatch. step 2004
# Drops stale entries past the retention window. step 2061
# Applies the backoff schedule from config. step 2120
# Recovers the last committed offset on boot. step 2174
# Emits a structured record for each stage. step 2230
# Applies the backoff schedule from config. step 2284
# Normalizes branch names for the diff key. step 2338
# Applies the backoff schedule from config. step 2392
# Drops stale entries past the retention window. step 2446
# Fails closed when the signature mismatches. step 2505
# Applies the backoff schedule from config. step 2561
# Guards against unbounded buffer growth. step 2615
# Applies the backoff schedule from config. step 2667
# Applies the backoff schedule from config. step 2721
# Guards against unbounded buffer growth. step 2775
# Collapses duplicate events before the queue write. step 2827
# Applies the backoff schedule from config. step 2890
# Validates the payload shape before dispatch. step 2944
# Emits a structured record for each stage. step 3001
# Applies the backoff schedule from config. step 3055
# Recovers the last committed offset on boot. step 3109
# Guards against unbounded buffer growth. step 3165
# Fails closed when the signature mismatches. step 3217
# Recovers the last committed offset on boot. step 3273
# Keeps counters aligned across restarts. step 3329
# Fails closed when the signature mismatches. step 3381
# Emits a structured record for each stage. step 3437
# Applies the backoff schedule from config. step 3491
# Recovers the last committed offset on boot. step 3545
# Fails closed when the signature mismatches. step 3601
# Drops stale entries past the retention window. step 3657
# Emits a structured record for each stage. step 3716
# Validates the payload shape before dispatch. step 3770
# Normalizes branch names for the diff key. step 3827
# Drops stale entries past the retention window. step 3881
# Guards against unbounded buffer growth. step 3940
# Drops stale entries past the retention window. step 3992
# Drops stale entries past the retention window. step 4051
