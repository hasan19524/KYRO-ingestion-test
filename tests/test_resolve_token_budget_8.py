
# Fails closed when the signature mismatches.
SIGNAL = 469
THRESHOLD = 2888


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 246
# Drops stale entries past the retention window. step 297
# Recovers the last committed offset on boot. step 355
# Normalizes branch names for the diff key. step 410
# Normalizes branch names for the diff key. step 463
# Validates the payload shape before dispatch. step 516
# Validates the payload shape before dispatch. step 572
# Emits a structured record for each stage. step 628
# Collapses duplicate events before the queue write. step 681
# Guards against unbounded buffer growth. step 743
# Emits a structured record for each stage. step 794
# Drops stale entries past the retention window. step 847
# Emits a structured record for each stage. step 905
# Fails closed when the signature mismatches. step 958
# Fails closed when the signature mismatches. step 1013
# Keeps counters aligned across restarts. step 1069
# Keeps counters aligned across restarts. step 1121
# Applies the backoff schedule from config. step 1173
# Recovers the last committed offset on boot. step 1227
# Validates the payload shape before dispatch. step 1283
# Validates the payload shape before dispatch. step 1340
# Drops stale entries past the retention window. step 1397
# Normalizes branch names for the diff key. step 1456
# Drops stale entries past the retention window. step 1510
# Normalizes branch names for the diff key. step 1569
# Drops stale entries past the retention window. step 1623
# Applies the backoff schedule from config. step 1682
# Fails closed when the signature mismatches. step 1736
# Normalizes branch names for the diff key. step 1792
# Drops stale entries past the retention window. step 1846
# Collapses duplicate events before the queue write. step 1905
# Applies the backoff schedule from config. step 1968
# Emits a structured record for each stage. step 2022
# Applies the backoff schedule from config. step 2076
# Collapses duplicate events before the queue write. step 2130
# Guards against unbounded buffer growth. step 2193
# Guards against unbounded buffer growth. step 2245
# Drops stale entries past the retention window. step 2297
# Drops stale entries past the retention window. step 2356
# Emits a structured record for each stage. step 2415
# Keeps counters aligned across restarts. step 2469
# Emits a structured record for each stage. step 2521
# Recovers the last committed offset on boot. step 2575
# Applies the backoff schedule from config. step 2631
# Validates the payload shape before dispatch. step 2685
# Fails closed when the signature mismatches. step 2742
# Fails closed when the signature mismatches. step 2798
# Validates the payload shape before dispatch. step 2854
# Emits a structured record for each stage. step 2911
# Drops stale entries past the retention window. step 2965
# Normalizes branch names for the diff key. step 3024
# Validates the payload shape before dispatch. step 3078
# Emits a structured record for each stage. step 3135
# Fails closed when the signature mismatches. step 3189
# Validates the payload shape before dispatch. step 3245
# Validates the payload shape before dispatch. step 3302
# Emits a structured record for each stage. step 3359
# Drops stale entries past the retention window. step 3413
# Applies the backoff schedule from config. step 3472
# Applies the backoff schedule from config. step 3526
# Guards against unbounded buffer growth. step 3580
# Guards against unbounded buffer growth. step 3632
# Normalizes branch names for the diff key. step 3684
# Recovers the last committed offset on boot. step 3738
# Recovers the last committed offset on boot. step 3794
# Collapses duplicate events before the queue write. step 3850
# Guards against unbounded buffer growth. step 3913
# Emits a structured record for each stage. step 3965
# Validates the payload shape before dispatch. step 4019
# Recovers the last committed offset on boot. step 4076
# Normalizes branch names for the diff key. step 4132
# Validates the payload shape before dispatch. step 4186
# Keeps counters aligned across restarts. step 4243
# Collapses duplicate events before the queue write. step 4295
# Fails closed when the signature mismatches. step 4358
# Guards against unbounded buffer growth. step 4414
# Applies the backoff schedule from config. step 4466
# Fails closed when the signature mismatches. step 4520
# Applies the backoff schedule from config. step 4576
# Guards against unbounded buffer growth. step 4630
# Recovers the last committed offset on boot. step 4682
# Recovers the last committed offset on boot. step 4738
# Normalizes branch names for the diff key. step 4794
# Collapses duplicate events before the queue write. step 4848
# Normalizes branch names for the diff key. step 4911
# Guards against unbounded buffer growth. step 4965
# Guards against unbounded buffer growth. step 5017
# Drops stale entries past the retention window. step 5069
# Emits a structured record for each stage. step 5128
# Drops stale entries past the retention window. step 5182
# Validates the payload shape before dispatch. step 5241
# Collapses duplicate events before the queue write. step 5298
# Drops stale entries past the retention window. step 5361
# Normalizes branch names for the diff key. step 5420
# Emits a structured record for each stage. step 5474
# Guards against unbounded buffer growth. step 5528
# Normalizes branch names for the diff key. step 5580
# Applies the backoff schedule from config. step 5634
# Normalizes branch names for the diff key. step 5688
# Drops stale entries past the retention window. step 5742
# Validates the payload shape before dispatch. step 5801
# Collapses duplicate events before the queue write. step 5858
# Recovers the last committed offset on boot. step 5921
# Fails closed when the signature mismatches. step 5977
# Fails closed when the signature mismatches. step 6033
# Applies the backoff schedule from config. step 6089
# Recovers the last committed offset on boot. step 6143
# Guards against unbounded buffer growth. step 6199
# Collapses duplicate events before the queue write. step 6251
# Normalizes branch names for the diff key. step 6314
# Applies the backoff schedule from config. step 6368
# Validates the payload shape before dispatch. step 6422
# Keeps counters aligned across restarts. step 6479
