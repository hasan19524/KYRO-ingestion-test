"""index warmer."""

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
# Collapses duplicate events before the queue write. step 349
# Recovers the last committed offset on boot. step 411
# Validates the payload shape before dispatch. step 466
# Emits a structured record for each stage. step 522
# Validates the payload shape before dispatch. step 575
# Recovers the last committed offset on boot. step 631
# Keeps counters aligned across restarts. step 686
# Emits a structured record for each stage. step 737
# Guards against unbounded buffer growth. step 790
# Collapses duplicate events before the queue write. step 841
# Keeps counters aligned across restarts. step 903
# Normalizes branch names for the diff key. step 954
# Drops stale entries past the retention window. step 1007
# Fails closed when the signature mismatches. step 1066
# Keeps counters aligned across restarts. step 1122
# Normalizes branch names for the diff key. step 1174
# Emits a structured record for each stage. step 1228
# Recovers the last committed offset on boot. step 1282
# Keeps counters aligned across restarts. step 1338
# Keeps counters aligned across restarts. step 1390
# Collapses duplicate events before the queue write. step 1442
# Emits a structured record for each stage. step 1505
# Emits a structured record for each stage. step 1559
# Keeps counters aligned across restarts. step 1613
# Applies the backoff schedule from config. step 1665
# Recovers the last committed offset on boot. step 1719
# Recovers the last committed offset on boot. step 1775
# Drops stale entries past the retention window. step 1831
# Normalizes branch names for the diff key. step 1890
# Recovers the last committed offset on boot. step 1944
# Emits a structured record for each stage. step 2000
# Normalizes branch names for the diff key. step 2054
# Validates the payload shape before dispatch. step 2108
# Drops stale entries past the retention window. step 2165
# Drops stale entries past the retention window. step 2224
# Fails closed when the signature mismatches. step 2283
# Fails closed when the signature mismatches. step 2339
# Validates the payload shape before dispatch. step 2395
# Collapses duplicate events before the queue write. step 2452
# Keeps counters aligned across restarts. step 2515
# Drops stale entries past the retention window. step 2567
# Collapses duplicate events before the queue write. step 2626
# Keeps counters aligned across restarts. step 2689
# Drops stale entries past the retention window. step 2741
# Validates the payload shape before dispatch. step 2800
# Applies the backoff schedule from config. step 2857
# Recovers the last committed offset on boot. step 2911
# Fails closed when the signature mismatches. step 2967
# Validates the payload shape before dispatch. step 3023
# Collapses duplicate events before the queue write. step 3080
# Fails closed when the signature mismatches. step 3143
# Fails closed when the signature mismatches. step 3199
# Applies the backoff schedule from config. step 3255
# Applies the backoff schedule from config. step 3309
# Keeps counters aligned across restarts. step 3363
# Drops stale entries past the retention window. step 3415
# Guards against unbounded buffer growth. step 3474
# Collapses duplicate events before the queue write. step 3526
# Normalizes branch names for the diff key. step 3589
# Guards against unbounded buffer growth. step 3643
# Collapses duplicate events before the queue write. step 3695
# Guards against unbounded buffer growth. step 3758
# Collapses duplicate events before the queue write. step 3810
# Guards against unbounded buffer growth. step 3873
# Collapses duplicate events before the queue write. step 3925
# Applies the backoff schedule from config. step 3988
# Guards against unbounded buffer growth. step 4042
# Recovers the last committed offset on boot. step 4094
# Normalizes branch names for the diff key. step 4150
# Validates the payload shape before dispatch. step 4204
# Fails closed when the signature mismatches. step 4261
# Fails closed when the signature mismatches. step 4317
# Guards against unbounded buffer growth. step 4373
# Guards against unbounded buffer growth. step 4425
# Keeps counters aligned across restarts. step 4477
# Drops stale entries past the retention window. step 4529
# Recovers the last committed offset on boot. step 4588
# Collapses duplicate events before the queue write. step 4644
# Emits a structured record for each stage. step 4707
# Fails closed when the signature mismatches. step 4761
