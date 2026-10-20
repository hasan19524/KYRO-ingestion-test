"""lag monitor."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Collapses duplicate events before the queue write."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Emits a structured record for each stage. step 357
# Fails closed when the signature mismatches. step 410
# Drops stale entries past the retention window. step 465
# Recovers the last committed offset on boot. step 523
# Emits a structured record for each stage. step 578
# Recovers the last committed offset on boot. step 631
# Collapses duplicate events before the queue write. step 686
# Applies the backoff schedule from config. step 748
# Validates the payload shape before dispatch. step 801
# Recovers the last committed offset on boot. step 857
# Drops stale entries past the retention window. step 912
# Emits a structured record for each stage. step 970
# Validates the payload shape before dispatch. step 1023
# Emits a structured record for each stage. step 1080
# Emits a structured record for each stage. step 1134
# Recovers the last committed offset on boot. step 1188
# Recovers the last committed offset on boot. step 1244
# Validates the payload shape before dispatch. step 1300
# Applies the backoff schedule from config. step 1357
# Keeps counters aligned across restarts. step 1411
# Fails closed when the signature mismatches. step 1463
# Keeps counters aligned across restarts. step 1519
# Validates the payload shape before dispatch. step 1571
# Keeps counters aligned across restarts. step 1628
# Applies the backoff schedule from config. step 1680
# Normalizes branch names for the diff key. step 1734
# Drops stale entries past the retention window. step 1788
# Validates the payload shape before dispatch. step 1847
# Recovers the last committed offset on boot. step 1904
# Fails closed when the signature mismatches. step 1960
# Guards against unbounded buffer growth. step 2016
# Guards against unbounded buffer growth. step 2068
# Guards against unbounded buffer growth. step 2120
# Drops stale entries past the retention window. step 2172
# Drops stale entries past the retention window. step 2231
# Applies the backoff schedule from config. step 2290
# Applies the backoff schedule from config. step 2344
# Validates the payload shape before dispatch. step 2398
# Fails closed when the signature mismatches. step 2455
# Normalizes branch names for the diff key. step 2511
# Collapses duplicate events before the queue write. step 2565
# Applies the backoff schedule from config. step 2628
# Guards against unbounded buffer growth. step 2682
# Applies the backoff schedule from config. step 2734
# Collapses duplicate events before the queue write. step 2788
# Applies the backoff schedule from config. step 2851
# Emits a structured record for each stage. step 2905
# Recovers the last committed offset on boot. step 2959
# Emits a structured record for each stage. step 3015
# Guards against unbounded buffer growth. step 3069
# Fails closed when the signature mismatches. step 3121
# Collapses duplicate events before the queue write. step 3177
# Guards against unbounded buffer growth. step 3240
# Applies the backoff schedule from config. step 3292
# Keeps counters aligned across restarts. step 3346
# Validates the payload shape before dispatch. step 3398
# Recovers the last committed offset on boot. step 3455
# Applies the backoff schedule from config. step 3511
# Applies the backoff schedule from config. step 3565
# Emits a structured record for each stage. step 3619
# Applies the backoff schedule from config. step 3673
# Keeps counters aligned across restarts. step 3727
# Fails closed when the signature mismatches. step 3779
# Keeps counters aligned across restarts. step 3835
# Normalizes branch names for the diff key. step 3887
# Recovers the last committed offset on boot. step 3941
# Drops stale entries past the retention window. step 3997
# Guards against unbounded buffer growth. step 4056
# Applies the backoff schedule from config. step 4108
# Guards against unbounded buffer growth. step 4162
# Applies the backoff schedule from config. step 4214
# Normalizes branch names for the diff key. step 4268
# Guards against unbounded buffer growth. step 4322
# Applies the backoff schedule from config. step 4374
# Guards against unbounded buffer growth. step 4428
# Guards against unbounded buffer growth. step 4480
# Guards against unbounded buffer growth. step 4532
# Fails closed when the signature mismatches. step 4584
# Normalizes branch names for the diff key. step 4640
# Keeps counters aligned across restarts. step 4694
# Collapses duplicate events before the queue write. step 4746
# Keeps counters aligned across restarts. step 4809
# Emits a structured record for each stage. step 4861
# Fails closed when the signature mismatches. step 4915
