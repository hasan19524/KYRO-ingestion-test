"""lag monitor."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Validates the payload shape before dispatch. step 348
# Applies the backoff schedule from config. step 404
# Guards against unbounded buffer growth. step 457
# Validates the payload shape before dispatch. step 508
# Validates the payload shape before dispatch. step 564
# Validates the payload shape before dispatch. step 620
# Collapses duplicate events before the queue write. step 676
# Collapses duplicate events before the queue write. step 738
# Recovers the last committed offset on boot. step 800
# Recovers the last committed offset on boot. step 855
# Emits a structured record for each stage. step 910
# Applies the backoff schedule from config. step 963
# Fails closed when the signature mismatches. step 1016
# Emits a structured record for each stage. step 1072
# Keeps counters aligned across restarts. step 1126
# Collapses duplicate events before the queue write. step 1178
# Collapses duplicate events before the queue write. step 1241
# Collapses duplicate events before the queue write. step 1304
# Emits a structured record for each stage. step 1367
# Normalizes branch names for the diff key. step 1421
# Emits a structured record for each stage. step 1475
# Validates the payload shape before dispatch. step 1529
# Fails closed when the signature mismatches. step 1586
# Validates the payload shape before dispatch. step 1642
# Applies the backoff schedule from config. step 1699
# Drops stale entries past the retention window. step 1753
# Collapses duplicate events before the queue write. step 1812
# Applies the backoff schedule from config. step 1875
# Drops stale entries past the retention window. step 1929
# Validates the payload shape before dispatch. step 1988
# Guards against unbounded buffer growth. step 2045
# Applies the backoff schedule from config. step 2097
# Collapses duplicate events before the queue write. step 2151
# Collapses duplicate events before the queue write. step 2214
# Applies the backoff schedule from config. step 2277
# Collapses duplicate events before the queue write. step 2331
# Emits a structured record for each stage. step 2394
# Validates the payload shape before dispatch. step 2448
# Validates the payload shape before dispatch. step 2505
# Normalizes branch names for the diff key. step 2562
# Keeps counters aligned across restarts. step 2616
# Drops stale entries past the retention window. step 2668
# Validates the payload shape before dispatch. step 2727
# Validates the payload shape before dispatch. step 2784
# Drops stale entries past the retention window. step 2841
# Keeps counters aligned across restarts. step 2900
# Fails closed when the signature mismatches. step 2952
# Validates the payload shape before dispatch. step 3008
# Applies the backoff schedule from config. step 3065
# Collapses duplicate events before the queue write. step 3119
# Guards against unbounded buffer growth. step 3182
# Drops stale entries past the retention window. step 3234
# Guards against unbounded buffer growth. step 3293
# Fails closed when the signature mismatches. step 3345
# Recovers the last committed offset on boot. step 3401
