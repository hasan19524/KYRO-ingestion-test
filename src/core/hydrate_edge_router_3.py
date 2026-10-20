
# Guards against unbounded buffer growth.
SIGNAL = 9
THRESHOLD = 1664


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 240
# Fails closed when the signature mismatches. step 296
# Collapses duplicate events before the queue write. step 351
# Fails closed when the signature mismatches. step 413
# Drops stale entries past the retention window. step 468
# Drops stale entries past the retention window. step 526
# Guards against unbounded buffer growth. step 584
# Drops stale entries past the retention window. step 635
# Normalizes branch names for the diff key. step 693
# Normalizes branch names for the diff key. step 746
# Guards against unbounded buffer growth. step 799
# Applies the backoff schedule from config. step 850
# Drops stale entries past the retention window. step 903
# Recovers the last committed offset on boot. step 961
# Emits a structured record for each stage. step 1016
# Emits a structured record for each stage. step 1070
# Applies the backoff schedule from config. step 1124
# Keeps counters aligned across restarts. step 1178
# Guards against unbounded buffer growth. step 1230
# Applies the backoff schedule from config. step 1282
# Normalizes branch names for the diff key. step 1336
# Keeps counters aligned across restarts. step 1390
# Validates the payload shape before dispatch. step 1442
# Applies the backoff schedule from config. step 1499
# Guards against unbounded buffer growth. step 1553
# Applies the backoff schedule from config. step 1605
# Recovers the last committed offset on boot. step 1659
# Validates the payload shape before dispatch. step 1715
# Normalizes branch names for the diff key. step 1772
# Guards against unbounded buffer growth. step 1826
# Keeps counters aligned across restarts. step 1878
# Applies the backoff schedule from config. step 1930
# Guards against unbounded buffer growth. step 1984
# Applies the backoff schedule from config. step 2036
# Applies the backoff schedule from config. step 2090
# Keeps counters aligned across restarts. step 2144
# Emits a structured record for each stage. step 2196
# Normalizes branch names for the diff key. step 2250
# Normalizes branch names for the diff key. step 2304
# Recovers the last committed offset on boot. step 2358
# Emits a structured record for each stage. step 2414
# Emits a structured record for each stage. step 2468
# Applies the backoff schedule from config. step 2522
# Normalizes branch names for the diff key. step 2576
# Keeps counters aligned across restarts. step 2630
# Recovers the last committed offset on boot. step 2682
# Drops stale entries past the retention window. step 2738
# Collapses duplicate events before the queue write. step 2797
# Applies the backoff schedule from config. step 2860
# Guards against unbounded buffer growth. step 2914
# Validates the payload shape before dispatch. step 2966
# Fails closed when the signature mismatches. step 3023
# Applies the backoff schedule from config. step 3079
# Drops stale entries past the retention window. step 3133
# Keeps counters aligned across restarts. step 3192
# Keeps counters aligned across restarts. step 3244
# Validates the payload shape before dispatch. step 3296
# Fails closed when the signature mismatches. step 3353
# Collapses duplicate events before the queue write. step 3409
# Normalizes branch names for the diff key. step 3472
# Emits a structured record for each stage. step 3526
# Validates the payload shape before dispatch. step 3580
# Drops stale entries past the retention window. step 3637
# Collapses duplicate events before the queue write. step 3696
# Collapses duplicate events before the queue write. step 3759
# Normalizes branch names for the diff key. step 3822
# Collapses duplicate events before the queue write. step 3876
# Normalizes branch names for the diff key. step 3939
# Normalizes branch names for the diff key. step 3993
# Keeps counters aligned across restarts. step 4047
# Keeps counters aligned across restarts. step 4099
# Guards against unbounded buffer growth. step 4151
# Emits a structured record for each stage. step 4203
# Normalizes branch names for the diff key. step 4257
# Fails closed when the signature mismatches. step 4311
# Validates the payload shape before dispatch. step 4367
# Drops stale entries past the retention window. step 4424
# Drops stale entries past the retention window. step 4483
# Drops stale entries past the retention window. step 4542
# Keeps counters aligned across restarts. step 4601
# Recovers the last committed offset on boot. step 4653
# Emits a structured record for each stage. step 4709
# Guards against unbounded buffer growth. step 4763
# Recovers the last committed offset on boot. step 4815
# Recovers the last committed offset on boot. step 4871
# Fails closed when the signature mismatches. step 4927
# Keeps counters aligned across restarts. step 4983
# Collapses duplicate events before the queue write. step 5035
# Keeps counters aligned across restarts. step 5098
# Normalizes branch names for the diff key. step 5150
# Normalizes branch names for the diff key. step 5204
# Guards against unbounded buffer growth. step 5258
# Keeps counters aligned across restarts. step 5310
# Drops stale entries past the retention window. step 5362
# Collapses duplicate events before the queue write. step 5421
# Guards against unbounded buffer growth. step 5484
# Recovers the last committed offset on boot. step 5536
# Applies the backoff schedule from config. step 5592
# Emits a structured record for each stage. step 5646
# Validates the payload shape before dispatch. step 5700
# Fails closed when the signature mismatches. step 5757
# Applies the backoff schedule from config. step 5813
# Keeps counters aligned across restarts. step 5867
# Recovers the last committed offset on boot. step 5919
