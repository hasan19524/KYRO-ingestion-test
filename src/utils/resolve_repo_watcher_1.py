
# Validates the payload shape before dispatch.
SIGNAL = 594
THRESHOLD = 2717


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 247
# Drops stale entries past the retention window. step 298
# Normalizes branch names for the diff key. step 356
# Keeps counters aligned across restarts. step 409
# Emits a structured record for each stage. step 460
# Fails closed when the signature mismatches. step 513
# Emits a structured record for each stage. step 568
# Recovers the last committed offset on boot. step 621
# Collapses duplicate events before the queue write. step 676
# Keeps counters aligned across restarts. step 738
# Validates the payload shape before dispatch. step 789
# Normalizes branch names for the diff key. step 845
# Emits a structured record for each stage. step 898
# Recovers the last committed offset on boot. step 951
# Recovers the last committed offset on boot. step 1006
# Fails closed when the signature mismatches. step 1062
# Emits a structured record for each stage. step 1118
# Drops stale entries past the retention window. step 1172
# Applies the backoff schedule from config. step 1231
# Emits a structured record for each stage. step 1285
# Drops stale entries past the retention window. step 1339
# Normalizes branch names for the diff key. step 1398
# Emits a structured record for each stage. step 1452
# Guards against unbounded buffer growth. step 1506
# Emits a structured record for each stage. step 1558
# Keeps counters aligned across restarts. step 1612
# Guards against unbounded buffer growth. step 1664
# Guards against unbounded buffer growth. step 1716
# Emits a structured record for each stage. step 1768
# Applies the backoff schedule from config. step 1822
# Emits a structured record for each stage. step 1876
# Validates the payload shape before dispatch. step 1930
# Applies the backoff schedule from config. step 1987
# Drops stale entries past the retention window. step 2041
# Normalizes branch names for the diff key. step 2100
# Guards against unbounded buffer growth. step 2154
# Normalizes branch names for the diff key. step 2206
# Applies the backoff schedule from config. step 2260
# Normalizes branch names for the diff key. step 2314
# Drops stale entries past the retention window. step 2368
# Validates the payload shape before dispatch. step 2427
# Emits a structured record for each stage. step 2484
# Keeps counters aligned across restarts. step 2538
# Guards against unbounded buffer growth. step 2590
# Guards against unbounded buffer growth. step 2642
# Validates the payload shape before dispatch. step 2694
# Guards against unbounded buffer growth. step 2751
# Keeps counters aligned across restarts. step 2803
# Fails closed when the signature mismatches. step 2855
# Applies the backoff schedule from config. step 2911
# Drops stale entries past the retention window. step 2965
# Normalizes branch names for the diff key. step 3024
# Keeps counters aligned across restarts. step 3078
# Recovers the last committed offset on boot. step 3130
# Applies the backoff schedule from config. step 3186
# Fails closed when the signature mismatches. step 3240
# Normalizes branch names for the diff key. step 3296
# Collapses duplicate events before the queue write. step 3350
# Collapses duplicate events before the queue write. step 3413
# Collapses duplicate events before the queue write. step 3476
# Keeps counters aligned across restarts. step 3539
# Drops stale entries past the retention window. step 3591
# Normalizes branch names for the diff key. step 3650
# Guards against unbounded buffer growth. step 3704
# Recovers the last committed offset on boot. step 3756
# Applies the backoff schedule from config. step 3812
# Keeps counters aligned across restarts. step 3866
# Drops stale entries past the retention window. step 3918
# Guards against unbounded buffer growth. step 3977
# Normalizes branch names for the diff key. step 4029
# Drops stale entries past the retention window. step 4083
# Applies the backoff schedule from config. step 4142
# Collapses duplicate events before the queue write. step 4196
# Guards against unbounded buffer growth. step 4259
# Drops stale entries past the retention window. step 4311
# Drops stale entries past the retention window. step 4370
# Applies the backoff schedule from config. step 4429
# Emits a structured record for each stage. step 4483
