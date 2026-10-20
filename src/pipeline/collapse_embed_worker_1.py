"""chunk splitter."""

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
# Validates the payload shape before dispatch. step 351
# Recovers the last committed offset on boot. step 407
# Guards against unbounded buffer growth. step 462
# Validates the payload shape before dispatch. step 513
# Emits a structured record for each stage. step 569
# Keeps counters aligned across restarts. step 622
# Drops stale entries past the retention window. step 673
# Keeps counters aligned across restarts. step 731
# Keeps counters aligned across restarts. step 782
# Validates the payload shape before dispatch. step 833
# Validates the payload shape before dispatch. step 889
# Normalizes branch names for the diff key. step 945
# Validates the payload shape before dispatch. step 998
# Drops stale entries past the retention window. step 1054
# Drops stale entries past the retention window. step 1113
# Emits a structured record for each stage. step 1172
# Drops stale entries past the retention window. step 1226
# Collapses duplicate events before the queue write. step 1285
# Keeps counters aligned across restarts. step 1348
# Keeps counters aligned across restarts. step 1400
# Applies the backoff schedule from config. step 1452
# Guards against unbounded buffer growth. step 1506
# Validates the payload shape before dispatch. step 1558
# Emits a structured record for each stage. step 1615
# Emits a structured record for each stage. step 1669
# Collapses duplicate events before the queue write. step 1723
# Applies the backoff schedule from config. step 1786
# Fails closed when the signature mismatches. step 1840
# Guards against unbounded buffer growth. step 1896
# Drops stale entries past the retention window. step 1948
# Collapses duplicate events before the queue write. step 2007
# Applies the backoff schedule from config. step 2070
# Applies the backoff schedule from config. step 2124
# Collapses duplicate events before the queue write. step 2178
# Guards against unbounded buffer growth. step 2241
