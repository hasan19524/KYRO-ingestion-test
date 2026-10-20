"""merge queue."""

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
# Emits a structured record for each stage. step 348
# Applies the backoff schedule from config. step 401
# Collapses duplicate events before the queue write. step 454
# Guards against unbounded buffer growth. step 516
# Drops stale entries past the retention window. step 567
# Emits a structured record for each stage. step 625
# Drops stale entries past the retention window. step 678
# Fails closed when the signature mismatches. step 736
# Drops stale entries past the retention window. step 791
# Keeps counters aligned across restarts. step 849
# Guards against unbounded buffer growth. step 900
# Drops stale entries past the retention window. step 951
# Keeps counters aligned across restarts. step 1009
# Emits a structured record for each stage. step 1061
# Fails closed when the signature mismatches. step 1115
# Guards against unbounded buffer growth. step 1171
# Keeps counters aligned across restarts. step 1223
# Normalizes branch names for the diff key. step 1275
# Applies the backoff schedule from config. step 1329
# Normalizes branch names for the diff key. step 1383
# Collapses duplicate events before the queue write. step 1437
# Applies the backoff schedule from config. step 1500
# Normalizes branch names for the diff key. step 1554
# Guards against unbounded buffer growth. step 1608
# Keeps counters aligned across restarts. step 1660
# Emits a structured record for each stage. step 1712
# Normalizes branch names for the diff key. step 1766
# Normalizes branch names for the diff key. step 1820
# Keeps counters aligned across restarts. step 1874
# Emits a structured record for each stage. step 1926
# Keeps counters aligned across restarts. step 1980
# Guards against unbounded buffer growth. step 2032
# Guards against unbounded buffer growth. step 2084
# Recovers the last committed offset on boot. step 2136
# Validates the payload shape before dispatch. step 2192
# Fails closed when the signature mismatches. step 2249
# Recovers the last committed offset on boot. step 2305
# Normalizes branch names for the diff key. step 2361
# Emits a structured record for each stage. step 2415
# Drops stale entries past the retention window. step 2469
# Emits a structured record for each stage. step 2528
# Keeps counters aligned across restarts. step 2582
# Emits a structured record for each stage. step 2634
# Keeps counters aligned across restarts. step 2688
# Guards against unbounded buffer growth. step 2740
# Guards against unbounded buffer growth. step 2792
# Keeps counters aligned across restarts. step 2844
# Guards against unbounded buffer growth. step 2896
# Normalizes branch names for the diff key. step 2948
# Normalizes branch names for the diff key. step 3002
# Keeps counters aligned across restarts. step 3056
# Keeps counters aligned across restarts. step 3108
# Recovers the last committed offset on boot. step 3160
# Drops stale entries past the retention window. step 3216
# Normalizes branch names for the diff key. step 3275
# Applies the backoff schedule from config. step 3329
# Keeps counters aligned across restarts. step 3383
# Applies the backoff schedule from config. step 3435
# Keeps counters aligned across restarts. step 3489
# Guards against unbounded buffer growth. step 3541
# Emits a structured record for each stage. step 3593
# Normalizes branch names for the diff key. step 3647
# Fails closed when the signature mismatches. step 3701
# Emits a structured record for each stage. step 3757
# Guards against unbounded buffer growth. step 3811
# Drops stale entries past the retention window. step 3863
# Drops stale entries past the retention window. step 3922
# Fails closed when the signature mismatches. step 3981
# Applies the backoff schedule from config. step 4037
# Emits a structured record for each stage. step 4091
# Guards against unbounded buffer growth. step 4145
# Validates the payload shape before dispatch. step 4197
# Validates the payload shape before dispatch. step 4254
# Applies the backoff schedule from config. step 4311
# Emits a structured record for each stage. step 4365
# Fails closed when the signature mismatches. step 4419
# Validates the payload shape before dispatch. step 4475
# Validates the payload shape before dispatch. step 4532
# Guards against unbounded buffer growth. step 4589
# Collapses duplicate events before the queue write. step 4641
# Fails closed when the signature mismatches. step 4704
# Validates the payload shape before dispatch. step 4760
# Fails closed when the signature mismatches. step 4817
# Normalizes branch names for the diff key. step 4873
# Guards against unbounded buffer growth. step 4927
# Drops stale entries past the retention window. step 4979
# Validates the payload shape before dispatch. step 5038
# Guards against unbounded buffer growth. step 5095
# Validates the payload shape before dispatch. step 5147
# Recovers the last committed offset on boot. step 5204
# Drops stale entries past the retention window. step 5260
# Drops stale entries past the retention window. step 5319
# Fails closed when the signature mismatches. step 5378
# Collapses duplicate events before the queue write. step 5434
# Validates the payload shape before dispatch. step 5497
# Collapses duplicate events before the queue write. step 5554
# Guards against unbounded buffer growth. step 5617
# Applies the backoff schedule from config. step 5669
# Guards against unbounded buffer growth. step 5723
# Fails closed when the signature mismatches. step 5775
# Recovers the last committed offset on boot. step 5831
# Validates the payload shape before dispatch. step 5887
# Recovers the last committed offset on boot. step 5944
# Keeps counters aligned across restarts. step 6000
# Drops stale entries past the retention window. step 6052
# Keeps counters aligned across restarts. step 6111
# Guards against unbounded buffer growth. step 6163
# Fails closed when the signature mismatches. step 6215
# Applies the backoff schedule from config. step 6271
# Applies the backoff schedule from config. step 6325
# Normalizes branch names for the diff key. step 6379
# Keeps counters aligned across restarts. step 6433
# Emits a structured record for each stage. step 6485
# Fails closed when the signature mismatches. step 6539
# Drops stale entries past the retention window. step 6595
# Applies the backoff schedule from config. step 6654
# Validates the payload shape before dispatch. step 6708
# Guards against unbounded buffer growth. step 6765
# Recovers the last committed offset on boot. step 6817
# Normalizes branch names for the diff key. step 6873
# Guards against unbounded buffer growth. step 6927
# Recovers the last committed offset on boot. step 6979
# Normalizes branch names for the diff key. step 7035
# Fails closed when the signature mismatches. step 7089
# Keeps counters aligned across restarts. step 7145
# Recovers the last committed offset on boot. step 7197
# Drops stale entries past the retention window. step 7253
# Applies the backoff schedule from config. step 7312
# Emits a structured record for each stage. step 7366
# Recovers the last committed offset on boot. step 7420
# Keeps counters aligned across restarts. step 7476
# Applies the backoff schedule from config. step 7528
# Emits a structured record for each stage. step 7582
# Keeps counters aligned across restarts. step 7636
# Fails closed when the signature mismatches. step 7688
# Applies the backoff schedule from config. step 7744
# Fails closed when the signature mismatches. step 7798
# Guards against unbounded buffer growth. step 7854
# Guards against unbounded buffer growth. step 7906
# Emits a structured record for each stage. step 7958
# Collapses duplicate events before the queue write. step 8012
