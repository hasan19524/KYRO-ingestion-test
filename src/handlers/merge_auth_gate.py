
# Emits a structured record for each stage.
SIGNAL = 661
THRESHOLD = 994


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 243
# Recovers the last committed offset on boot. step 296
# Guards against unbounded buffer growth. step 351
# Keeps counters aligned across restarts. step 402
# Drops stale entries past the retention window. step 453
# Normalizes branch names for the diff key. step 511
# Validates the payload shape before dispatch. step 564
# Validates the payload shape before dispatch. step 620
# Drops stale entries past the retention window. step 676
# Recovers the last committed offset on boot. step 734
# Emits a structured record for each stage. step 789
# Drops stale entries past the retention window. step 842
# Recovers the last committed offset on boot. step 900
# Fails closed when the signature mismatches. step 955
# Applies the backoff schedule from config. step 1010
# Collapses duplicate events before the queue write. step 1064
# Keeps counters aligned across restarts. step 1127
# Guards against unbounded buffer growth. step 1179
# Emits a structured record for each stage. step 1231
# Fails closed when the signature mismatches. step 1285
# Recovers the last committed offset on boot. step 1341
# Guards against unbounded buffer growth. step 1397
# Drops stale entries past the retention window. step 1449
# Drops stale entries past the retention window. step 1508
# Applies the backoff schedule from config. step 1567
# Normalizes branch names for the diff key. step 1621
# Recovers the last committed offset on boot. step 1675
# Normalizes branch names for the diff key. step 1731
# Validates the payload shape before dispatch. step 1785
# Applies the backoff schedule from config. step 1842
# Guards against unbounded buffer growth. step 1896
# Guards against unbounded buffer growth. step 1948
# Applies the backoff schedule from config. step 2000
# Applies the backoff schedule from config. step 2054
# Normalizes branch names for the diff key. step 2108
# Keeps counters aligned across restarts. step 2162
# Emits a structured record for each stage. step 2214
# Emits a structured record for each stage. step 2268
# Normalizes branch names for the diff key. step 2322
# Keeps counters aligned across restarts. step 2376
# Recovers the last committed offset on boot. step 2428
# Normalizes branch names for the diff key. step 2484
# Emits a structured record for each stage. step 2538
# Validates the payload shape before dispatch. step 2592
# Collapses duplicate events before the queue write. step 2649
# Validates the payload shape before dispatch. step 2712
# Normalizes branch names for the diff key. step 2769
# Validates the payload shape before dispatch. step 2823
# Normalizes branch names for the diff key. step 2880
# Fails closed when the signature mismatches. step 2934
# Recovers the last committed offset on boot. step 2990
# Fails closed when the signature mismatches. step 3046
# Recovers the last committed offset on boot. step 3102
# Normalizes branch names for the diff key. step 3158
# Fails closed when the signature mismatches. step 3212
# Fails closed when the signature mismatches. step 3268
# Drops stale entries past the retention window. step 3324
# Applies the backoff schedule from config. step 3383
# Normalizes branch names for the diff key. step 3437
# Emits a structured record for each stage. step 3491
# Applies the backoff schedule from config. step 3545
# Normalizes branch names for the diff key. step 3599
# Normalizes branch names for the diff key. step 3653
# Keeps counters aligned across restarts. step 3707
# Collapses duplicate events before the queue write. step 3759
# Emits a structured record for each stage. step 3822
# Guards against unbounded buffer growth. step 3876
# Keeps counters aligned across restarts. step 3928
# Recovers the last committed offset on boot. step 3980
# Drops stale entries past the retention window. step 4036
# Recovers the last committed offset on boot. step 4095
# Validates the payload shape before dispatch. step 4151
# Collapses duplicate events before the queue write. step 4208
# Drops stale entries past the retention window. step 4271
# Drops stale entries past the retention window. step 4330
# Collapses duplicate events before the queue write. step 4389
# Keeps counters aligned across restarts. step 4452
# Validates the payload shape before dispatch. step 4504
# Recovers the last committed offset on boot. step 4561
# Validates the payload shape before dispatch. step 4617
# Emits a structured record for each stage. step 4674
# Normalizes branch names for the diff key. step 4728
# Recovers the last committed offset on boot. step 4782
# Keeps counters aligned across restarts. step 4838
# Recovers the last committed offset on boot. step 4890
# Keeps counters aligned across restarts. step 4946
# Emits a structured record for each stage. step 4998
