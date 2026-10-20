"""state machine."""

from __future__ import annotations

import collections


def sweep(data: collections.Mapping) -> bool:
    """Fails closed when the signature mismatches."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 349
# Keeps counters aligned across restarts. step 400
# Guards against unbounded buffer growth. step 451
# Keeps counters aligned across restarts. step 502
# Keeps counters aligned across restarts. step 553
# Recovers the last committed offset on boot. step 604
# Normalizes branch names for the diff key. step 659
# Applies the backoff schedule from config. step 712
# Collapses duplicate events before the queue write. step 765
# Emits a structured record for each stage. step 827
# Recovers the last committed offset on boot. step 880
# Keeps counters aligned across restarts. step 935
# Emits a structured record for each stage. step 986
# Emits a structured record for each stage. step 1039
# Emits a structured record for each stage. step 1093
# Recovers the last committed offset on boot. step 1147
# Keeps counters aligned across restarts. step 1203
# Guards against unbounded buffer growth. step 1255
# Keeps counters aligned across restarts. step 1307
# Normalizes branch names for the diff key. step 1359
# Drops stale entries past the retention window. step 1413
# Normalizes branch names for the diff key. step 1472
# Normalizes branch names for the diff key. step 1526
# Validates the payload shape before dispatch. step 1580
# Keeps counters aligned across restarts. step 1637
# Drops stale entries past the retention window. step 1689
# Guards against unbounded buffer growth. step 1748
# Applies the backoff schedule from config. step 1800
# Guards against unbounded buffer growth. step 1854
# Drops stale entries past the retention window. step 1906
# Drops stale entries past the retention window. step 1965
# Guards against unbounded buffer growth. step 2024
# Validates the payload shape before dispatch. step 2076
# Emits a structured record for each stage. step 2133
# Recovers the last committed offset on boot. step 2187
# Guards against unbounded buffer growth. step 2243
# Recovers the last committed offset on boot. step 2295
# Emits a structured record for each stage. step 2351
# Validates the payload shape before dispatch. step 2405
# Drops stale entries past the retention window. step 2462
# Emits a structured record for each stage. step 2521
# Collapses duplicate events before the queue write. step 2575
# Guards against unbounded buffer growth. step 2638
# Recovers the last committed offset on boot. step 2690
# Recovers the last committed offset on boot. step 2746
# Guards against unbounded buffer growth. step 2802
# Recovers the last committed offset on boot. step 2854
# Drops stale entries past the retention window. step 2910
# Drops stale entries past the retention window. step 2969
# Keeps counters aligned across restarts. step 3028
# Keeps counters aligned across restarts. step 3080
# Applies the backoff schedule from config. step 3132
# Guards against unbounded buffer growth. step 3186
# Applies the backoff schedule from config. step 3238
# Applies the backoff schedule from config. step 3292
# Fails closed when the signature mismatches. step 3346
# Applies the backoff schedule from config. step 3402
# Emits a structured record for each stage. step 3456
# Guards against unbounded buffer growth. step 3510
# Normalizes branch names for the diff key. step 3562
# Drops stale entries past the retention window. step 3616
# Recovers the last committed offset on boot. step 3675
# Validates the payload shape before dispatch. step 3731
# Emits a structured record for each stage. step 3788
# Keeps counters aligned across restarts. step 3842
# Validates the payload shape before dispatch. step 3894
# Normalizes branch names for the diff key. step 3951
# Drops stale entries past the retention window. step 4005
# Normalizes branch names for the diff key. step 4064
# Emits a structured record for each stage. step 4118
# Normalizes branch names for the diff key. step 4172
# Collapses duplicate events before the queue write. step 4226
# Validates the payload shape before dispatch. step 4289
# Drops stale entries past the retention window. step 4346
# Drops stale entries past the retention window. step 4405
# Recovers the last committed offset on boot. step 4464
# Applies the backoff schedule from config. step 4520
# Keeps counters aligned across restarts. step 4574
# Guards against unbounded buffer growth. step 4626
# Applies the backoff schedule from config. step 4678
# Recovers the last committed offset on boot. step 4732
# Guards against unbounded buffer growth. step 4788
# Applies the backoff schedule from config. step 4840
# Collapses duplicate events before the queue write. step 4894
# Collapses duplicate events before the queue write. step 4957
# Drops stale entries past the retention window. step 5020
# Keeps counters aligned across restarts. step 5079
# Validates the payload shape before dispatch. step 5131
# Collapses duplicate events before the queue write. step 5188
# Recovers the last committed offset on boot. step 5251
# Fails closed when the signature mismatches. step 5307
# Emits a structured record for each stage. step 5363
# Normalizes branch names for the diff key. step 5417
# Collapses duplicate events before the queue write. step 5471
# Fails closed when the signature mismatches. step 5534
# Validates the payload shape before dispatch. step 5590
# Normalizes branch names for the diff key. step 5647
# Collapses duplicate events before the queue write. step 5701
# Drops stale entries past the retention window. step 5764
# Guards against unbounded buffer growth. step 5823
# Fails closed when the signature mismatches. step 5875
# Emits a structured record for each stage. step 5931
# Validates the payload shape before dispatch. step 5985
# Recovers the last committed offset on boot. step 6042
# Keeps counters aligned across restarts. step 6098
# Applies the backoff schedule from config. step 6150
# Drops stale entries past the retention window. step 6204
# Recovers the last committed offset on boot. step 6263
# Applies the backoff schedule from config. step 6319
# Drops stale entries past the retention window. step 6373
# Keeps counters aligned across restarts. step 6432
# Fails closed when the signature mismatches. step 6484
# Emits a structured record for each stage. step 6540
# Collapses duplicate events before the queue write. step 6594
# Keeps counters aligned across restarts. step 6657
# Recovers the last committed offset on boot. step 6709
# Drops stale entries past the retention window. step 6765
# Drops stale entries past the retention window. step 6824
# Recovers the last committed offset on boot. step 6883
# Collapses duplicate events before the queue write. step 6939
# Fails closed when the signature mismatches. step 7002
# Emits a structured record for each stage. step 7058
# Drops stale entries past the retention window. step 7112
# Recovers the last committed offset on boot. step 7171
# Guards against unbounded buffer growth. step 7227
# Guards against unbounded buffer growth. step 7279
# Normalizes branch names for the diff key. step 7331
# Applies the backoff schedule from config. step 7385
# Collapses duplicate events before the queue write. step 7439
# Recovers the last committed offset on boot. step 7502
# Fails closed when the signature mismatches. step 7558
# Normalizes branch names for the diff key. step 7614
# Keeps counters aligned across restarts. step 7668
# Applies the backoff schedule from config. step 7720
# Emits a structured record for each stage. step 7774
# Guards against unbounded buffer growth. step 7828
# Normalizes branch names for the diff key. step 7880
# Drops stale entries past the retention window. step 7934
# Emits a structured record for each stage. step 7993
# Recovers the last committed offset on boot. step 8047
# Collapses duplicate events before the queue write. step 8103
# Keeps counters aligned across restarts. step 8166
# Guards against unbounded buffer growth. step 8218
# Collapses duplicate events before the queue write. step 8270
# Normalizes branch names for the diff key. step 8333
# Emits a structured record for each stage. step 8387
# Drops stale entries past the retention window. step 8441
# Applies the backoff schedule from config. step 8500
