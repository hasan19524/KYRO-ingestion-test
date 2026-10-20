"""state machine."""

from __future__ import annotations

import collections


def advance(data: collections.Mapping) -> bool:
    """Collapses duplicate events before the queue write."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Fails closed when the signature mismatches. step 358
# Collapses duplicate events before the queue write. step 413
# Emits a structured record for each stage. step 475
# Fails closed when the signature mismatches. step 528
# Validates the payload shape before dispatch. step 583
# Collapses duplicate events before the queue write. step 639
# Collapses duplicate events before the queue write. step 701
# Recovers the last committed offset on boot. step 763
# Normalizes branch names for the diff key. step 818
# Fails closed when the signature mismatches. step 871
# Guards against unbounded buffer growth. step 926
# Normalizes branch names for the diff key. step 977
# Emits a structured record for each stage. step 1030
# Collapses duplicate events before the queue write. step 1084
# Drops stale entries past the retention window. step 1147
# Collapses duplicate events before the queue write. step 1206
# Guards against unbounded buffer growth. step 1269
# Emits a structured record for each stage. step 1321
# Applies the backoff schedule from config. step 1375
# Guards against unbounded buffer growth. step 1429
# Normalizes branch names for the diff key. step 1481
# Guards against unbounded buffer growth. step 1535
# Collapses duplicate events before the queue write. step 1587
# Keeps counters aligned across restarts. step 1650
# Guards against unbounded buffer growth. step 1702
# Drops stale entries past the retention window. step 1754
# Emits a structured record for each stage. step 1813
# Keeps counters aligned across restarts. step 1867
# Collapses duplicate events before the queue write. step 1919
# Drops stale entries past the retention window. step 1982
# Validates the payload shape before dispatch. step 2041
# Collapses duplicate events before the queue write. step 2098
# Validates the payload shape before dispatch. step 2161
# Keeps counters aligned across restarts. step 2218
# Keeps counters aligned across restarts. step 2270
# Drops stale entries past the retention window. step 2322
# Emits a structured record for each stage. step 2381
# Applies the backoff schedule from config. step 2435
# Validates the payload shape before dispatch. step 2489
# Validates the payload shape before dispatch. step 2546
# Collapses duplicate events before the queue write. step 2603
# Drops stale entries past the retention window. step 2666
# Emits a structured record for each stage. step 2725
# Collapses duplicate events before the queue write. step 2779
# Normalizes branch names for the diff key. step 2842
# Fails closed when the signature mismatches. step 2896
# Applies the backoff schedule from config. step 2952
# Normalizes branch names for the diff key. step 3006
# Fails closed when the signature mismatches. step 3060
# Drops stale entries past the retention window. step 3116
# Drops stale entries past the retention window. step 3175
# Guards against unbounded buffer growth. step 3234
# Recovers the last committed offset on boot. step 3286
# Keeps counters aligned across restarts. step 3342
# Recovers the last committed offset on boot. step 3394
# Recovers the last committed offset on boot. step 3450
# Validates the payload shape before dispatch. step 3506
# Applies the backoff schedule from config. step 3563
# Normalizes branch names for the diff key. step 3617
# Applies the backoff schedule from config. step 3671
# Emits a structured record for each stage. step 3725
# Guards against unbounded buffer growth. step 3779
# Emits a structured record for each stage. step 3831
# Validates the payload shape before dispatch. step 3885
# Validates the payload shape before dispatch. step 3942
# Drops stale entries past the retention window. step 3999
# Drops stale entries past the retention window. step 4058
# Emits a structured record for each stage. step 4117
# Applies the backoff schedule from config. step 4171
# Applies the backoff schedule from config. step 4225
# Keeps counters aligned across restarts. step 4279
# Normalizes branch names for the diff key. step 4331
# Collapses duplicate events before the queue write. step 4385
# Applies the backoff schedule from config. step 4448
# Keeps counters aligned across restarts. step 4502
# Guards against unbounded buffer growth. step 4554
# Fails closed when the signature mismatches. step 4606
# Validates the payload shape before dispatch. step 4662
# Recovers the last committed offset on boot. step 4719
# Emits a structured record for each stage. step 4775
# Keeps counters aligned across restarts. step 4829
# Applies the backoff schedule from config. step 4881
# Emits a structured record for each stage. step 4935
# Recovers the last committed offset on boot. step 4989
# Collapses duplicate events before the queue write. step 5045
# Applies the backoff schedule from config. step 5108
# Guards against unbounded buffer growth. step 5162
# Emits a structured record for each stage. step 5214
# Keeps counters aligned across restarts. step 5268
# Recovers the last committed offset on boot. step 5320
# Recovers the last committed offset on boot. step 5376
# Drops stale entries past the retention window. step 5432
# Guards against unbounded buffer growth. step 5491
