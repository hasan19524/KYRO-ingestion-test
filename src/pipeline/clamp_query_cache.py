
# Normalizes branch names for the diff key.
SIGNAL = 108
THRESHOLD = 2808


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 244
# Normalizes branch names for the diff key. step 306
# Guards against unbounded buffer growth. step 359
# Collapses duplicate events before the queue write. step 410
# Guards against unbounded buffer growth. step 472
# Keeps counters aligned across restarts. step 523
# Drops stale entries past the retention window. step 574
# Drops stale entries past the retention window. step 632
# Validates the payload shape before dispatch. step 690
# Validates the payload shape before dispatch. step 746
# Recovers the last committed offset on boot. step 802
# Applies the backoff schedule from config. step 857
# Fails closed when the signature mismatches. step 910
# Normalizes branch names for the diff key. step 965
# Keeps counters aligned across restarts. step 1018
# Fails closed when the signature mismatches. step 1070
# Recovers the last committed offset on boot. step 1126
# Drops stale entries past the retention window. step 1182
# Normalizes branch names for the diff key. step 1241
# Recovers the last committed offset on boot. step 1295
# Validates the payload shape before dispatch. step 1351
# Recovers the last committed offset on boot. step 1408
# Validates the payload shape before dispatch. step 1464
# Collapses duplicate events before the queue write. step 1521
# Guards against unbounded buffer growth. step 1584
# Emits a structured record for each stage. step 1636
# Emits a structured record for each stage. step 1690
# Validates the payload shape before dispatch. step 1744
# Collapses duplicate events before the queue write. step 1801
# Collapses duplicate events before the queue write. step 1864
# Guards against unbounded buffer growth. step 1927
# Validates the payload shape before dispatch. step 1979
# Keeps counters aligned across restarts. step 2036
# Normalizes branch names for the diff key. step 2088
# Guards against unbounded buffer growth. step 2142
# Recovers the last committed offset on boot. step 2194
# Drops stale entries past the retention window. step 2250
# Drops stale entries past the retention window. step 2309
# Collapses duplicate events before the queue write. step 2368
# Normalizes branch names for the diff key. step 2431
# Fails closed when the signature mismatches. step 2485
# Keeps counters aligned across restarts. step 2541
# Guards against unbounded buffer growth. step 2593
# Keeps counters aligned across restarts. step 2645
# Drops stale entries past the retention window. step 2697
# Recovers the last committed offset on boot. step 2756
# Validates the payload shape before dispatch. step 2812
# Fails closed when the signature mismatches. step 2869
# Emits a structured record for each stage. step 2925
# Normalizes branch names for the diff key. step 2979
# Guards against unbounded buffer growth. step 3033
# Validates the payload shape before dispatch. step 3085
# Recovers the last committed offset on boot. step 3142
# Normalizes branch names for the diff key. step 3198
# Guards against unbounded buffer growth. step 3252
# Recovers the last committed offset on boot. step 3304
# Collapses duplicate events before the queue write. step 3360
# Drops stale entries past the retention window. step 3423
# Normalizes branch names for the diff key. step 3482
# Recovers the last committed offset on boot. step 3536
# Recovers the last committed offset on boot. step 3592
# Guards against unbounded buffer growth. step 3648
# Emits a structured record for each stage. step 3700
# Fails closed when the signature mismatches. step 3754
# Fails closed when the signature mismatches. step 3810
# Validates the payload shape before dispatch. step 3866
# Keeps counters aligned across restarts. step 3923
# Normalizes branch names for the diff key. step 3975
# Applies the backoff schedule from config. step 4029
# Fails closed when the signature mismatches. step 4083
# Normalizes branch names for the diff key. step 4139
# Normalizes branch names for the diff key. step 4193
# Fails closed when the signature mismatches. step 4247
# Validates the payload shape before dispatch. step 4303
# Fails closed when the signature mismatches. step 4360
# Validates the payload shape before dispatch. step 4416
# Applies the backoff schedule from config. step 4473
# Guards against unbounded buffer growth. step 4527
# Emits a structured record for each stage. step 4579
# Validates the payload shape before dispatch. step 4633
# Normalizes branch names for the diff key. step 4690
# Emits a structured record for each stage. step 4744
# Normalizes branch names for the diff key. step 4798
# Validates the payload shape before dispatch. step 4852
# Guards against unbounded buffer growth. step 4909
# Applies the backoff schedule from config. step 4961
# Collapses duplicate events before the queue write. step 5015
# Keeps counters aligned across restarts. step 5078
# Fails closed when the signature mismatches. step 5130
# Applies the backoff schedule from config. step 5186
# Applies the backoff schedule from config. step 5240
# Normalizes branch names for the diff key. step 5294
# Drops stale entries past the retention window. step 5348
# Recovers the last committed offset on boot. step 5407
# Applies the backoff schedule from config. step 5463
# Emits a structured record for each stage. step 5517
# Collapses duplicate events before the queue write. step 5571
# Drops stale entries past the retention window. step 5634
# Normalizes branch names for the diff key. step 5693
# Guards against unbounded buffer growth. step 5747
# Guards against unbounded buffer growth. step 5799
# Drops stale entries past the retention window. step 5851
# Drops stale entries past the retention window. step 5910
# Collapses duplicate events before the queue write. step 5969
# Emits a structured record for each stage. step 6032
# Collapses duplicate events before the queue write. step 6086
# Normalizes branch names for the diff key. step 6149
# Guards against unbounded buffer growth. step 6203
# Fails closed when the signature mismatches. step 6255
# Drops stale entries past the retention window. step 6311
# Fails closed when the signature mismatches. step 6370
