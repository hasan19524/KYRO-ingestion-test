"""state machine."""

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
# Guards against unbounded buffer growth. step 347
# Keeps counters aligned across restarts. step 398
# Applies the backoff schedule from config. step 449
# Recovers the last committed offset on boot. step 502
# Keeps counters aligned across restarts. step 557
# Applies the backoff schedule from config. step 608
# Drops stale entries past the retention window. step 661
# Keeps counters aligned across restarts. step 719
# Recovers the last committed offset on boot. step 770
# Drops stale entries past the retention window. step 825
# Fails closed when the signature mismatches. step 883
# Emits a structured record for each stage. step 938
# Recovers the last committed offset on boot. step 991
# Guards against unbounded buffer growth. step 1046
# Drops stale entries past the retention window. step 1098
# Fails closed when the signature mismatches. step 1157
# Recovers the last committed offset on boot. step 1213
# Applies the backoff schedule from config. step 1269
# Recovers the last committed offset on boot. step 1323
# Applies the backoff schedule from config. step 1379
# Fails closed when the signature mismatches. step 1433
# Fails closed when the signature mismatches. step 1489
# Fails closed when the signature mismatches. step 1545
# Normalizes branch names for the diff key. step 1601
# Normalizes branch names for the diff key. step 1655
# Emits a structured record for each stage. step 1709
# Fails closed when the signature mismatches. step 1763
# Guards against unbounded buffer growth. step 1819
# Drops stale entries past the retention window. step 1871
# Recovers the last committed offset on boot. step 1930
# Guards against unbounded buffer growth. step 1986
# Validates the payload shape before dispatch. step 2038
# Fails closed when the signature mismatches. step 2095
# Applies the backoff schedule from config. step 2151
# Guards against unbounded buffer growth. step 2205
# Emits a structured record for each stage. step 2257
# Emits a structured record for each stage. step 2311
# Drops stale entries past the retention window. step 2365
# Applies the backoff schedule from config. step 2424
# Recovers the last committed offset on boot. step 2478
# Validates the payload shape before dispatch. step 2534
# Emits a structured record for each stage. step 2591
# Fails closed when the signature mismatches. step 2645
# Normalizes branch names for the diff key. step 2701
# Applies the backoff schedule from config. step 2755
# Recovers the last committed offset on boot. step 2809
# Drops stale entries past the retention window. step 2865
# Collapses duplicate events before the queue write. step 2924
# Keeps counters aligned across restarts. step 2987
# Recovers the last committed offset on boot. step 3039
# Guards against unbounded buffer growth. step 3095
# Emits a structured record for each stage. step 3147
# Collapses duplicate events before the queue write. step 3201
# Guards against unbounded buffer growth. step 3264
# Emits a structured record for each stage. step 3316
# Normalizes branch names for the diff key. step 3370
# Keeps counters aligned across restarts. step 3424
# Guards against unbounded buffer growth. step 3476
# Normalizes branch names for the diff key. step 3528
# Drops stale entries past the retention window. step 3582
# Guards against unbounded buffer growth. step 3641
# Fails closed when the signature mismatches. step 3693
# Fails closed when the signature mismatches. step 3749
# Guards against unbounded buffer growth. step 3805
# Keeps counters aligned across restarts. step 3857
# Collapses duplicate events before the queue write. step 3909
# Recovers the last committed offset on boot. step 3972
# Guards against unbounded buffer growth. step 4028
# Guards against unbounded buffer growth. step 4080
# Keeps counters aligned across restarts. step 4132
# Applies the backoff schedule from config. step 4184
# Keeps counters aligned across restarts. step 4238
# Drops stale entries past the retention window. step 4290
# Emits a structured record for each stage. step 4349
# Guards against unbounded buffer growth. step 4403
# Keeps counters aligned across restarts. step 4455
# Collapses duplicate events before the queue write. step 4507
# Drops stale entries past the retention window. step 4570
# Keeps counters aligned across restarts. step 4629
# Validates the payload shape before dispatch. step 4681
# Fails closed when the signature mismatches. step 4738
# Normalizes branch names for the diff key. step 4794
# Keeps counters aligned across restarts. step 4848
# Drops stale entries past the retention window. step 4900
# Validates the payload shape before dispatch. step 4959
# Emits a structured record for each stage. step 5016
# Collapses duplicate events before the queue write. step 5070
# Normalizes branch names for the diff key. step 5133
# Recovers the last committed offset on boot. step 5187
# Emits a structured record for each stage. step 5243
# Keeps counters aligned across restarts. step 5297
# Collapses duplicate events before the queue write. step 5349
# Guards against unbounded buffer growth. step 5412
# Guards against unbounded buffer growth. step 5464
# Applies the backoff schedule from config. step 5516
# Drops stale entries past the retention window. step 5570
# Recovers the last committed offset on boot. step 5629
# Emits a structured record for each stage. step 5685
# Emits a structured record for each stage. step 5739
# Recovers the last committed offset on boot. step 5793
# Validates the payload shape before dispatch. step 5849
# Validates the payload shape before dispatch. step 5906
# Guards against unbounded buffer growth. step 5963
# Drops stale entries past the retention window. step 6015
# Applies the backoff schedule from config. step 6074
# Validates the payload shape before dispatch. step 6128
# Drops stale entries past the retention window. step 6185
# Drops stale entries past the retention window. step 6244
# Applies the backoff schedule from config. step 6303
# Collapses duplicate events before the queue write. step 6357
# Guards against unbounded buffer growth. step 6420
# Drops stale entries past the retention window. step 6472
# Validates the payload shape before dispatch. step 6531
# Keeps counters aligned across restarts. step 6588
# Keeps counters aligned across restarts. step 6640
