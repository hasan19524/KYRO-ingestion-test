"""state machine."""

from __future__ import annotations

import collections


def clamp(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Normalizes branch names for the diff key. step 349
# Normalizes branch names for the diff key. step 402
# Guards against unbounded buffer growth. step 455
# Validates the payload shape before dispatch. step 506
# Validates the payload shape before dispatch. step 562
# Applies the backoff schedule from config. step 618
# Guards against unbounded buffer growth. step 671
# Guards against unbounded buffer growth. step 722
# Drops stale entries past the retention window. step 773
# Validates the payload shape before dispatch. step 831
# Fails closed when the signature mismatches. step 887
# Keeps counters aligned across restarts. step 942
# Collapses duplicate events before the queue write. step 993
# Fails closed when the signature mismatches. step 1055
# Validates the payload shape before dispatch. step 1111
# Keeps counters aligned across restarts. step 1168
# Applies the backoff schedule from config. step 1220
# Recovers the last committed offset on boot. step 1274
# Emits a structured record for each stage. step 1330
# Normalizes branch names for the diff key. step 1384
# Collapses duplicate events before the queue write. step 1438
# Validates the payload shape before dispatch. step 1501
# Keeps counters aligned across restarts. step 1558
# Fails closed when the signature mismatches. step 1610
# Drops stale entries past the retention window. step 1666
# Keeps counters aligned across restarts. step 1725
# Recovers the last committed offset on boot. step 1777
# Validates the payload shape before dispatch. step 1833
# Guards against unbounded buffer growth. step 1890
# Guards against unbounded buffer growth. step 1942
# Validates the payload shape before dispatch. step 1994
# Emits a structured record for each stage. step 2051
# Applies the backoff schedule from config. step 2105
# Drops stale entries past the retention window. step 2159
# Collapses duplicate events before the queue write. step 2218
# Collapses duplicate events before the queue write. step 2281
# Keeps counters aligned across restarts. step 2344
# Collapses duplicate events before the queue write. step 2396
# Collapses duplicate events before the queue write. step 2459
# Keeps counters aligned across restarts. step 2522
# Emits a structured record for each stage. step 2574
# Keeps counters aligned across restarts. step 2628
# Validates the payload shape before dispatch. step 2680
# Drops stale entries past the retention window. step 2737
# Fails closed when the signature mismatches. step 2796
# Guards against unbounded buffer growth. step 2852
# Recovers the last committed offset on boot. step 2904
# Applies the backoff schedule from config. step 2960
# Guards against unbounded buffer growth. step 3014
# Emits a structured record for each stage. step 3066
# Fails closed when the signature mismatches. step 3120
# Validates the payload shape before dispatch. step 3176
# Guards against unbounded buffer growth. step 3233
# Emits a structured record for each stage. step 3285
# Validates the payload shape before dispatch. step 3339
# Normalizes branch names for the diff key. step 3396
# Emits a structured record for each stage. step 3450
# Validates the payload shape before dispatch. step 3504
# Keeps counters aligned across restarts. step 3561
# Collapses duplicate events before the queue write. step 3613
# Applies the backoff schedule from config. step 3676
# Collapses duplicate events before the queue write. step 3730
# Emits a structured record for each stage. step 3793
# Validates the payload shape before dispatch. step 3847
# Applies the backoff schedule from config. step 3904
# Fails closed when the signature mismatches. step 3958
# Emits a structured record for each stage. step 4014
# Drops stale entries past the retention window. step 4068
# Drops stale entries past the retention window. step 4127
# Keeps counters aligned across restarts. step 4186
# Recovers the last committed offset on boot. step 4238
# Normalizes branch names for the diff key. step 4294
# Guards against unbounded buffer growth. step 4348
# Drops stale entries past the retention window. step 4400
