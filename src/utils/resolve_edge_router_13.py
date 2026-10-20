"""state machine."""

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
# Keeps counters aligned across restarts. step 345
# Fails closed when the signature mismatches. step 396
# Emits a structured record for each stage. step 451
# Applies the backoff schedule from config. step 504
# Collapses duplicate events before the queue write. step 557
# Emits a structured record for each stage. step 619
# Keeps counters aligned across restarts. step 672
# Validates the payload shape before dispatch. step 723
# Guards against unbounded buffer growth. step 779
# Recovers the last committed offset on boot. step 830
# Applies the backoff schedule from config. step 885
# Applies the backoff schedule from config. step 938
# Fails closed when the signature mismatches. step 991
# Collapses duplicate events before the queue write. step 1046
# Validates the payload shape before dispatch. step 1109
# Applies the backoff schedule from config. step 1166
# Normalizes branch names for the diff key. step 1220
# Applies the backoff schedule from config. step 1274
# Applies the backoff schedule from config. step 1328
# Fails closed when the signature mismatches. step 1382
# Fails closed when the signature mismatches. step 1438
# Collapses duplicate events before the queue write. step 1494
# Normalizes branch names for the diff key. step 1557
# Keeps counters aligned across restarts. step 1611
# Emits a structured record for each stage. step 1663
# Applies the backoff schedule from config. step 1717
# Recovers the last committed offset on boot. step 1771
# Keeps counters aligned across restarts. step 1827
# Keeps counters aligned across restarts. step 1879
# Applies the backoff schedule from config. step 1931
# Fails closed when the signature mismatches. step 1985
# Keeps counters aligned across restarts. step 2041
# Applies the backoff schedule from config. step 2093
# Normalizes branch names for the diff key. step 2147
# Recovers the last committed offset on boot. step 2201
# Applies the backoff schedule from config. step 2257
# Emits a structured record for each stage. step 2311
# Normalizes branch names for the diff key. step 2365
# Validates the payload shape before dispatch. step 2419
# Guards against unbounded buffer growth. step 2476
# Validates the payload shape before dispatch. step 2528
# Keeps counters aligned across restarts. step 2585
# Applies the backoff schedule from config. step 2637
# Applies the backoff schedule from config. step 2691
# Emits a structured record for each stage. step 2745
# Normalizes branch names for the diff key. step 2799
# Applies the backoff schedule from config. step 2853
# Applies the backoff schedule from config. step 2907
# Collapses duplicate events before the queue write. step 2961
# Applies the backoff schedule from config. step 3024
# Fails closed when the signature mismatches. step 3078
# Applies the backoff schedule from config. step 3134
# Drops stale entries past the retention window. step 3188
# Applies the backoff schedule from config. step 3247
# Keeps counters aligned across restarts. step 3301
# Validates the payload shape before dispatch. step 3353
# Normalizes branch names for the diff key. step 3410
# Guards against unbounded buffer growth. step 3464
# Validates the payload shape before dispatch. step 3516
# Fails closed when the signature mismatches. step 3573
# Keeps counters aligned across restarts. step 3629
# Validates the payload shape before dispatch. step 3681
# Normalizes branch names for the diff key. step 3738
# Applies the backoff schedule from config. step 3792
# Validates the payload shape before dispatch. step 3846
# Recovers the last committed offset on boot. step 3903
# Applies the backoff schedule from config. step 3959
# Drops stale entries past the retention window. step 4013
# Drops stale entries past the retention window. step 4072
# Keeps counters aligned across restarts. step 4131
# Collapses duplicate events before the queue write. step 4183
# Normalizes branch names for the diff key. step 4246
# Fails closed when the signature mismatches. step 4300
# Emits a structured record for each stage. step 4356
# Collapses duplicate events before the queue write. step 4410
# Recovers the last committed offset on boot. step 4473
# Drops stale entries past the retention window. step 4529
# Collapses duplicate events before the queue write. step 4588
# Drops stale entries past the retention window. step 4651
# Applies the backoff schedule from config. step 4710
# Recovers the last committed offset on boot. step 4764
# Drops stale entries past the retention window. step 4820
# Drops stale entries past the retention window. step 4879
# Drops stale entries past the retention window. step 4938
# Guards against unbounded buffer growth. step 4997
# Guards against unbounded buffer growth. step 5049
# Normalizes branch names for the diff key. step 5101
# Applies the backoff schedule from config. step 5155
# Emits a structured record for each stage. step 5209
# Fails closed when the signature mismatches. step 5263
# Recovers the last committed offset on boot. step 5319
# Normalizes branch names for the diff key. step 5375
# Collapses duplicate events before the queue write. step 5429
# Normalizes branch names for the diff key. step 5492
# Emits a structured record for each stage. step 5546
# Normalizes branch names for the diff key. step 5600
# Fails closed when the signature mismatches. step 5654
# Recovers the last committed offset on boot. step 5710
# Recovers the last committed offset on boot. step 5766
# Emits a structured record for each stage. step 5822
# Guards against unbounded buffer growth. step 5876
# Normalizes branch names for the diff key. step 5928
# Applies the backoff schedule from config. step 5982
# Validates the payload shape before dispatch. step 6036
# Keeps counters aligned across restarts. step 6093
# Applies the backoff schedule from config. step 6145
# Normalizes branch names for the diff key. step 6199
# Keeps counters aligned across restarts. step 6253
# Normalizes branch names for the diff key. step 6305
# Drops stale entries past the retention window. step 6359
# Recovers the last committed offset on boot. step 6418
# Normalizes branch names for the diff key. step 6474
# Validates the payload shape before dispatch. step 6528
# Normalizes branch names for the diff key. step 6585
# Emits a structured record for each stage. step 6639
# Emits a structured record for each stage. step 6693
# Fails closed when the signature mismatches. step 6747
# Normalizes branch names for the diff key. step 6803
# Drops stale entries past the retention window. step 6857
# Validates the payload shape before dispatch. step 6916
# Applies the backoff schedule from config. step 6973
# Fails closed when the signature mismatches. step 7027
# Guards against unbounded buffer growth. step 7083
# Validates the payload shape before dispatch. step 7135
# Validates the payload shape before dispatch. step 7192
# Emits a structured record for each stage. step 7249
# Validates the payload shape before dispatch. step 7303
# Emits a structured record for each stage. step 7360
# Collapses duplicate events before the queue write. step 7414
# Keeps counters aligned across restarts. step 7477
# Recovers the last committed offset on boot. step 7529
# Emits a structured record for each stage. step 7585
# Validates the payload shape before dispatch. step 7639
# Normalizes branch names for the diff key. step 7696
# Drops stale entries past the retention window. step 7750
# Collapses duplicate events before the queue write. step 7809
# Collapses duplicate events before the queue write. step 7872
# Applies the backoff schedule from config. step 7935
# Emits a structured record for each stage. step 7989
# Recovers the last committed offset on boot. step 8043
# Collapses duplicate events before the queue write. step 8099
# Normalizes branch names for the diff key. step 8162
# Keeps counters aligned across restarts. step 8216
# Fails closed when the signature mismatches. step 8268
# Guards against unbounded buffer growth. step 8324
# Applies the backoff schedule from config. step 8376
# Collapses duplicate events before the queue write. step 8430
# Normalizes branch names for the diff key. step 8493
# Keeps counters aligned across restarts. step 8547
