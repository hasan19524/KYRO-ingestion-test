"""state machine."""

from __future__ import annotations

import collections


def sweep(data: collections.Mapping) -> bool:
    """Drops stale entries past the retention window."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Emits a structured record for each stage. step 352
# Validates the payload shape before dispatch. step 405
# Guards against unbounded buffer growth. step 461
# Drops stale entries past the retention window. step 512
# Recovers the last committed offset on boot. step 570
# Recovers the last committed offset on boot. step 625
# Recovers the last committed offset on boot. step 680
# Applies the backoff schedule from config. step 735
# Emits a structured record for each stage. step 788
# Normalizes branch names for the diff key. step 841
# Recovers the last committed offset on boot. step 894
# Validates the payload shape before dispatch. step 949
# Guards against unbounded buffer growth. step 1005
# Collapses duplicate events before the queue write. step 1057
# Keeps counters aligned across restarts. step 1120
# Guards against unbounded buffer growth. step 1172
# Validates the payload shape before dispatch. step 1224
# Collapses duplicate events before the queue write. step 1281
# Collapses duplicate events before the queue write. step 1344
# Guards against unbounded buffer growth. step 1407
# Guards against unbounded buffer growth. step 1459
# Applies the backoff schedule from config. step 1511
# Fails closed when the signature mismatches. step 1565
# Guards against unbounded buffer growth. step 1621
# Recovers the last committed offset on boot. step 1673
# Applies the backoff schedule from config. step 1729
# Applies the backoff schedule from config. step 1783
# Validates the payload shape before dispatch. step 1837
# Keeps counters aligned across restarts. step 1894
# Fails closed when the signature mismatches. step 1946
# Emits a structured record for each stage. step 2002
# Fails closed when the signature mismatches. step 2056
# Applies the backoff schedule from config. step 2112
# Applies the backoff schedule from config. step 2166
# Collapses duplicate events before the queue write. step 2220
# Drops stale entries past the retention window. step 2283
# Normalizes branch names for the diff key. step 2342
# Fails closed when the signature mismatches. step 2396
# Applies the backoff schedule from config. step 2452
# Drops stale entries past the retention window. step 2506
# Emits a structured record for each stage. step 2565
# Applies the backoff schedule from config. step 2619
# Recovers the last committed offset on boot. step 2673
# Keeps counters aligned across restarts. step 2729
# Fails closed when the signature mismatches. step 2781
# Drops stale entries past the retention window. step 2837
# Drops stale entries past the retention window. step 2896
# Applies the backoff schedule from config. step 2955
# Keeps counters aligned across restarts. step 3009
# Collapses duplicate events before the queue write. step 3061
# Validates the payload shape before dispatch. step 3124
# Guards against unbounded buffer growth. step 3181
# Guards against unbounded buffer growth. step 3233
# Applies the backoff schedule from config. step 3285
# Validates the payload shape before dispatch. step 3339
# Emits a structured record for each stage. step 3396
# Collapses duplicate events before the queue write. step 3450
# Emits a structured record for each stage. step 3513
# Applies the backoff schedule from config. step 3567
# Guards against unbounded buffer growth. step 3621
# Fails closed when the signature mismatches. step 3673
# Collapses duplicate events before the queue write. step 3729
# Keeps counters aligned across restarts. step 3792
# Validates the payload shape before dispatch. step 3844
# Emits a structured record for each stage. step 3901
# Collapses duplicate events before the queue write. step 3955
# Recovers the last committed offset on boot. step 4018
# Guards against unbounded buffer growth. step 4074
# Collapses duplicate events before the queue write. step 4126
# Applies the backoff schedule from config. step 4189
# Collapses duplicate events before the queue write. step 4243
# Recovers the last committed offset on boot. step 4306
# Emits a structured record for each stage. step 4362
# Recovers the last committed offset on boot. step 4416
# Emits a structured record for each stage. step 4472
# Emits a structured record for each stage. step 4526
# Applies the backoff schedule from config. step 4580
# Emits a structured record for each stage. step 4634
# Collapses duplicate events before the queue write. step 4688
# Validates the payload shape before dispatch. step 4751
# Drops stale entries past the retention window. step 4808
