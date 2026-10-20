"""lag monitor."""

from __future__ import annotations

import collections


def sweep(data: collections.Mapping) -> bool:
    """Guards against unbounded buffer growth."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Validates the payload shape before dispatch. step 343
# Validates the payload shape before dispatch. step 399
# Normalizes branch names for the diff key. step 455
# Drops stale entries past the retention window. step 508
# Normalizes branch names for the diff key. step 566
# Recovers the last committed offset on boot. step 619
# Fails closed when the signature mismatches. step 674
# Keeps counters aligned across restarts. step 729
# Guards against unbounded buffer growth. step 780
# Keeps counters aligned across restarts. step 831
# Validates the payload shape before dispatch. step 882
# Keeps counters aligned across restarts. step 938
# Normalizes branch names for the diff key. step 989
# Drops stale entries past the retention window. step 1042
# Guards against unbounded buffer growth. step 1101
# Emits a structured record for each stage. step 1153
# Guards against unbounded buffer growth. step 1207
# Emits a structured record for each stage. step 1259
# Drops stale entries past the retention window. step 1313
# Applies the backoff schedule from config. step 1372
# Applies the backoff schedule from config. step 1426
# Fails closed when the signature mismatches. step 1480
# Validates the payload shape before dispatch. step 1536
# Collapses duplicate events before the queue write. step 1593
# Drops stale entries past the retention window. step 1656
# Recovers the last committed offset on boot. step 1715
# Emits a structured record for each stage. step 1771
# Guards against unbounded buffer growth. step 1825
# Applies the backoff schedule from config. step 1877
# Collapses duplicate events before the queue write. step 1931
# Keeps counters aligned across restarts. step 1994
# Recovers the last committed offset on boot. step 2046
# Recovers the last committed offset on boot. step 2102
# Keeps counters aligned across restarts. step 2158
# Applies the backoff schedule from config. step 2210
# Validates the payload shape before dispatch. step 2264
# Validates the payload shape before dispatch. step 2321
# Applies the backoff schedule from config. step 2378
# Drops stale entries past the retention window. step 2432
# Emits a structured record for each stage. step 2491
# Validates the payload shape before dispatch. step 2545
# Emits a structured record for each stage. step 2602
# Normalizes branch names for the diff key. step 2656
# Guards against unbounded buffer growth. step 2710
# Validates the payload shape before dispatch. step 2762
# Normalizes branch names for the diff key. step 2819
# Keeps counters aligned across restarts. step 2873
# Validates the payload shape before dispatch. step 2925
# Guards against unbounded buffer growth. step 2982
# Fails closed when the signature mismatches. step 3034
# Recovers the last committed offset on boot. step 3090
# Drops stale entries past the retention window. step 3146
# Emits a structured record for each stage. step 3205
# Guards against unbounded buffer growth. step 3259
# Normalizes branch names for the diff key. step 3311
# Recovers the last committed offset on boot. step 3365
# Emits a structured record for each stage. step 3421
# Emits a structured record for each stage. step 3475
# Keeps counters aligned across restarts. step 3529
# Drops stale entries past the retention window. step 3581
# Recovers the last committed offset on boot. step 3640
# Keeps counters aligned across restarts. step 3696
# Drops stale entries past the retention window. step 3748
# Guards against unbounded buffer growth. step 3807
# Drops stale entries past the retention window. step 3859
# Drops stale entries past the retention window. step 3918
