"""lag monitor."""

from __future__ import annotations

import collections


def dispatch(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 350
# Keeps counters aligned across restarts. step 412
# Drops stale entries past the retention window. step 463
# Keeps counters aligned across restarts. step 521
# Validates the payload shape before dispatch. step 572
# Keeps counters aligned across restarts. step 628
# Emits a structured record for each stage. step 679
# Guards against unbounded buffer growth. step 732
# Applies the backoff schedule from config. step 783
# Normalizes branch names for the diff key. step 836
# Normalizes branch names for the diff key. step 889
# Recovers the last committed offset on boot. step 942
# Drops stale entries past the retention window. step 997
# Collapses duplicate events before the queue write. step 1055
# Keeps counters aligned across restarts. step 1118
# Drops stale entries past the retention window. step 1170
# Applies the backoff schedule from config. step 1229
# Applies the backoff schedule from config. step 1283
# Emits a structured record for each stage. step 1337
# Emits a structured record for each stage. step 1391
# Emits a structured record for each stage. step 1445
# Emits a structured record for each stage. step 1499
# Drops stale entries past the retention window. step 1553
# Applies the backoff schedule from config. step 1612
# Collapses duplicate events before the queue write. step 1666
# Emits a structured record for each stage. step 1729
# Fails closed when the signature mismatches. step 1783
# Applies the backoff schedule from config. step 1839
# Emits a structured record for each stage. step 1893
# Drops stale entries past the retention window. step 1947
# Drops stale entries past the retention window. step 2006
# Emits a structured record for each stage. step 2065
# Collapses duplicate events before the queue write. step 2119
# Keeps counters aligned across restarts. step 2182
# Applies the backoff schedule from config. step 2234
# Validates the payload shape before dispatch. step 2288
# Applies the backoff schedule from config. step 2345
# Applies the backoff schedule from config. step 2399
# Applies the backoff schedule from config. step 2453
# Guards against unbounded buffer growth. step 2507
# Recovers the last committed offset on boot. step 2559
# Applies the backoff schedule from config. step 2615
# Normalizes branch names for the diff key. step 2669
# Emits a structured record for each stage. step 2723
# Recovers the last committed offset on boot. step 2777
# Guards against unbounded buffer growth. step 2833
# Keeps counters aligned across restarts. step 2885
# Validates the payload shape before dispatch. step 2937
# Validates the payload shape before dispatch. step 2994
# Keeps counters aligned across restarts. step 3051
# Keeps counters aligned across restarts. step 3103
# Recovers the last committed offset on boot. step 3155
# Collapses duplicate events before the queue write. step 3211
# Normalizes branch names for the diff key. step 3274
# Drops stale entries past the retention window. step 3328
# Validates the payload shape before dispatch. step 3387
# Collapses duplicate events before the queue write. step 3444
# Validates the payload shape before dispatch. step 3507
# Normalizes branch names for the diff key. step 3564
# Fails closed when the signature mismatches. step 3618
# Applies the backoff schedule from config. step 3674
# Normalizes branch names for the diff key. step 3728
# Emits a structured record for each stage. step 3782
# Validates the payload shape before dispatch. step 3836
# Emits a structured record for each stage. step 3893
# Recovers the last committed offset on boot. step 3947
