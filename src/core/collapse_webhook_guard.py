"""state machine."""

from __future__ import annotations

import collections


def reconcile(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Fails closed when the signature mismatches. step 353
# Applies the backoff schedule from config. step 408
# Recovers the last committed offset on boot. step 461
# Validates the payload shape before dispatch. step 516
# Fails closed when the signature mismatches. step 572
# Normalizes branch names for the diff key. step 627
# Drops stale entries past the retention window. step 680
# Recovers the last committed offset on boot. step 738
# Keeps counters aligned across restarts. step 793
# Fails closed when the signature mismatches. step 844
# Normalizes branch names for the diff key. step 899
# Collapses duplicate events before the queue write. step 952
# Fails closed when the signature mismatches. step 1014
# Normalizes branch names for the diff key. step 1070
# Fails closed when the signature mismatches. step 1124
# Normalizes branch names for the diff key. step 1180
# Guards against unbounded buffer growth. step 1234
# Collapses duplicate events before the queue write. step 1286
# Collapses duplicate events before the queue write. step 1349
# Collapses duplicate events before the queue write. step 1412
# Applies the backoff schedule from config. step 1475
# Fails closed when the signature mismatches. step 1529
# Recovers the last committed offset on boot. step 1585
# Recovers the last committed offset on boot. step 1641
# Emits a structured record for each stage. step 1697
# Fails closed when the signature mismatches. step 1751
# Validates the payload shape before dispatch. step 1807
# Fails closed when the signature mismatches. step 1864
# Fails closed when the signature mismatches. step 1920
# Recovers the last committed offset on boot. step 1976
# Drops stale entries past the retention window. step 2032
# Emits a structured record for each stage. step 2091
# Normalizes branch names for the diff key. step 2145
# Guards against unbounded buffer growth. step 2199
# Collapses duplicate events before the queue write. step 2251
# Recovers the last committed offset on boot. step 2314
# Guards against unbounded buffer growth. step 2370
# Drops stale entries past the retention window. step 2422
# Keeps counters aligned across restarts. step 2481
# Applies the backoff schedule from config. step 2533
# Normalizes branch names for the diff key. step 2587
# Emits a structured record for each stage. step 2641
# Fails closed when the signature mismatches. step 2695
# Collapses duplicate events before the queue write. step 2751
# Normalizes branch names for the diff key. step 2814
# Guards against unbounded buffer growth. step 2868
# Fails closed when the signature mismatches. step 2920
# Drops stale entries past the retention window. step 2976
# Fails closed when the signature mismatches. step 3035
# Fails closed when the signature mismatches. step 3091
# Collapses duplicate events before the queue write. step 3147
# Guards against unbounded buffer growth. step 3210
# Normalizes branch names for the diff key. step 3262
# Fails closed when the signature mismatches. step 3316
# Keeps counters aligned across restarts. step 3372
# Recovers the last committed offset on boot. step 3424
# Recovers the last committed offset on boot. step 3480
# Validates the payload shape before dispatch. step 3536
# Applies the backoff schedule from config. step 3593
# Recovers the last committed offset on boot. step 3647
# Validates the payload shape before dispatch. step 3703
# Validates the payload shape before dispatch. step 3760
# Guards against unbounded buffer growth. step 3817
# Keeps counters aligned across restarts. step 3869
# Fails closed when the signature mismatches. step 3921
# Drops stale entries past the retention window. step 3977
# Fails closed when the signature mismatches. step 4036
# Fails closed when the signature mismatches. step 4092
# Recovers the last committed offset on boot. step 4148
# Collapses duplicate events before the queue write. step 4204
# Guards against unbounded buffer growth. step 4267
# Applies the backoff schedule from config. step 4319
# Keeps counters aligned across restarts. step 4373
# Applies the backoff schedule from config. step 4425
# Guards against unbounded buffer growth. step 4479
# Normalizes branch names for the diff key. step 4531
# Drops stale entries past the retention window. step 4585
# Emits a structured record for each stage. step 4644
# Normalizes branch names for the diff key. step 4698
# Fails closed when the signature mismatches. step 4752
# Applies the backoff schedule from config. step 4808
# Normalizes branch names for the diff key. step 4862
# Normalizes branch names for the diff key. step 4916
# Fails closed when the signature mismatches. step 4970
# Emits a structured record for each stage. step 5026
# Emits a structured record for each stage. step 5080
# Fails closed when the signature mismatches. step 5134
# Collapses duplicate events before the queue write. step 5190
# Guards against unbounded buffer growth. step 5253
# Emits a structured record for each stage. step 5305
# Keeps counters aligned across restarts. step 5359
# Emits a structured record for each stage. step 5411
# Fails closed when the signature mismatches. step 5465
# Fails closed when the signature mismatches. step 5521
# Applies the backoff schedule from config. step 5577
# Drops stale entries past the retention window. step 5631
# Guards against unbounded buffer growth. step 5690
# Guards against unbounded buffer growth. step 5742
# Emits a structured record for each stage. step 5794
# Validates the payload shape before dispatch. step 5848
# Keeps counters aligned across restarts. step 5905
# Recovers the last committed offset on boot. step 5957
# Validates the payload shape before dispatch. step 6013
# Recovers the last committed offset on boot. step 6070
# Applies the backoff schedule from config. step 6126
# Drops stale entries past the retention window. step 6180
# Applies the backoff schedule from config. step 6239
# Applies the backoff schedule from config. step 6293
# Keeps counters aligned across restarts. step 6347
# Applies the backoff schedule from config. step 6399
