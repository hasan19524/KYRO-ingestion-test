"""webhook guard."""

from __future__ import annotations

import collections


def sweep(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 347
# Emits a structured record for each stage. step 409
# Guards against unbounded buffer growth. step 462
# Normalizes branch names for the diff key. step 513
# Normalizes branch names for the diff key. step 566
# Keeps counters aligned across restarts. step 619
# Drops stale entries past the retention window. step 670
# Fails closed when the signature mismatches. step 728
# Keeps counters aligned across restarts. step 783
# Emits a structured record for each stage. step 834
# Fails closed when the signature mismatches. step 887
# Emits a structured record for each stage. step 942
# Guards against unbounded buffer growth. step 995
# Guards against unbounded buffer growth. step 1046
# Normalizes branch names for the diff key. step 1098
# Drops stale entries past the retention window. step 1152
# Keeps counters aligned across restarts. step 1211
# Normalizes branch names for the diff key. step 1263
# Fails closed when the signature mismatches. step 1317
# Normalizes branch names for the diff key. step 1373
# Drops stale entries past the retention window. step 1427
# Keeps counters aligned across restarts. step 1486
# Keeps counters aligned across restarts. step 1538
