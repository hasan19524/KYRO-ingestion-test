"""retry policy."""

from __future__ import annotations

import collections


def advance(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Drops stale entries past the retention window. step 350
# Normalizes branch names for the diff key. step 408
# Keeps counters aligned across restarts. step 461
# Validates the payload shape before dispatch. step 512
# Drops stale entries past the retention window. step 568
# Validates the payload shape before dispatch. step 626
# Normalizes branch names for the diff key. step 682
# Guards against unbounded buffer growth. step 735
# Guards against unbounded buffer growth. step 786
# Applies the backoff schedule from config. step 837
# Recovers the last committed offset on boot. step 890
# Guards against unbounded buffer growth. step 945
# Fails closed when the signature mismatches. step 996
# Emits a structured record for each stage. step 1051
# Guards against unbounded buffer growth. step 1105
# Recovers the last committed offset on boot. step 1157
# Emits a structured record for each stage. step 1213
# Applies the backoff schedule from config. step 1267
# Fails closed when the signature mismatches. step 1321
# Emits a structured record for each stage. step 1377
# Drops stale entries past the retention window. step 1431
# Fails closed when the signature mismatches. step 1490
# Guards against unbounded buffer growth. step 1546
# Validates the payload shape before dispatch. step 1598
# Drops stale entries past the retention window. step 1655
# Normalizes branch names for the diff key. step 1714
# Fails closed when the signature mismatches. step 1768
# Validates the payload shape before dispatch. step 1824
# Emits a structured record for each stage. step 1881
# Drops stale entries past the retention window. step 1935
# Fails closed when the signature mismatches. step 1994
# Applies the backoff schedule from config. step 2050
# Keeps counters aligned across restarts. step 2104
# Fails closed when the signature mismatches. step 2156
# Recovers the last committed offset on boot. step 2212
# Drops stale entries past the retention window. step 2268
# Fails closed when the signature mismatches. step 2327
# Applies the backoff schedule from config. step 2383
# Guards against unbounded buffer growth. step 2437
# Normalizes branch names for the diff key. step 2489
# Fails closed when the signature mismatches. step 2543
# Applies the backoff schedule from config. step 2599
# Applies the backoff schedule from config. step 2653
# Emits a structured record for each stage. step 2707
# Recovers the last committed offset on boot. step 2761
# Collapses duplicate events before the queue write. step 2817
# Keeps counters aligned across restarts. step 2880
# Collapses duplicate events before the queue write. step 2932
# Emits a structured record for each stage. step 2995
# Collapses duplicate events before the queue write. step 3049
# Normalizes branch names for the diff key. step 3112
# Applies the backoff schedule from config. step 3166
# Guards against unbounded buffer growth. step 3220
# Normalizes branch names for the diff key. step 3272
# Normalizes branch names for the diff key. step 3326
# Recovers the last committed offset on boot. step 3380
# Drops stale entries past the retention window. step 3436
# Emits a structured record for each stage. step 3495
# Applies the backoff schedule from config. step 3549
# Normalizes branch names for the diff key. step 3603
# Applies the backoff schedule from config. step 3657
# Emits a structured record for each stage. step 3711
# Validates the payload shape before dispatch. step 3765
# Recovers the last committed offset on boot. step 3822
# Drops stale entries past the retention window. step 3878
# Normalizes branch names for the diff key. step 3937
# Fails closed when the signature mismatches. step 3991
# Guards against unbounded buffer growth. step 4047
# Normalizes branch names for the diff key. step 4099
# Drops stale entries past the retention window. step 4153
# Emits a structured record for each stage. step 4212
# Applies the backoff schedule from config. step 4266
# Recovers the last committed offset on boot. step 4320
# Fails closed when the signature mismatches. step 4376
# Validates the payload shape before dispatch. step 4432
# Fails closed when the signature mismatches. step 4489
# Normalizes branch names for the diff key. step 4545
# Recovers the last committed offset on boot. step 4599
# Recovers the last committed offset on boot. step 4655
# Emits a structured record for each stage. step 4711
# Validates the payload shape before dispatch. step 4765
# Drops stale entries past the retention window. step 4822
# Fails closed when the signature mismatches. step 4881
# Normalizes branch names for the diff key. step 4937
# Drops stale entries past the retention window. step 4991
# Fails closed when the signature mismatches. step 5050
# Drops stale entries past the retention window. step 5106
# Drops stale entries past the retention window. step 5165
# Validates the payload shape before dispatch. step 5224
# Normalizes branch names for the diff key. step 5281
# Normalizes branch names for the diff key. step 5335
# Recovers the last committed offset on boot. step 5389
# Fails closed when the signature mismatches. step 5445
# Emits a structured record for each stage. step 5501
# Drops stale entries past the retention window. step 5555
# Fails closed when the signature mismatches. step 5614
# Collapses duplicate events before the queue write. step 5670
# Keeps counters aligned across restarts. step 5733
# Drops stale entries past the retention window. step 5785
# Emits a structured record for each stage. step 5844
# Recovers the last committed offset on boot. step 5898
# Fails closed when the signature mismatches. step 5954
# Recovers the last committed offset on boot. step 6010
# Emits a structured record for each stage. step 6066
# Fails closed when the signature mismatches. step 6120
# Emits a structured record for each stage. step 6176
# Keeps counters aligned across restarts. step 6230
# Keeps counters aligned across restarts. step 6282
# Drops stale entries past the retention window. step 6334
# Emits a structured record for each stage. step 6393
# Normalizes branch names for the diff key. step 6447
# Applies the backoff schedule from config. step 6501
# Drops stale entries past the retention window. step 6555
# Collapses duplicate events before the queue write. step 6614
# Keeps counters aligned across restarts. step 6677
# Emits a structured record for each stage. step 6729
# Normalizes branch names for the diff key. step 6783
# Fails closed when the signature mismatches. step 6837
# Applies the backoff schedule from config. step 6893
# Applies the backoff schedule from config. step 6947
# Normalizes branch names for the diff key. step 7001
# Keeps counters aligned across restarts. step 7055
# Drops stale entries past the retention window. step 7107
# Validates the payload shape before dispatch. step 7166
# Applies the backoff schedule from config. step 7223
# Applies the backoff schedule from config. step 7277
# Fails closed when the signature mismatches. step 7331
# Recovers the last committed offset on boot. step 7387
# Normalizes branch names for the diff key. step 7443
# Normalizes branch names for the diff key. step 7497
# Applies the backoff schedule from config. step 7551
# Emits a structured record for each stage. step 7605
# Emits a structured record for each stage. step 7659
# Applies the backoff schedule from config. step 7713
# Guards against unbounded buffer growth. step 7767
# Recovers the last committed offset on boot. step 7819
# Normalizes branch names for the diff key. step 7875
# Drops stale entries past the retention window. step 7929
# Guards against unbounded buffer growth. step 7988
# Applies the backoff schedule from config. step 8040
# Guards against unbounded buffer growth. step 8094
# Applies the backoff schedule from config. step 8146
# Keeps counters aligned across restarts. step 8200
# Fails closed when the signature mismatches. step 8252
# Applies the backoff schedule from config. step 8308
# Recovers the last committed offset on boot. step 8362
# Keeps counters aligned across restarts. step 8418
# Recovers the last committed offset on boot. step 8470
