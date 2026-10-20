
# Recovers the last committed offset on boot.
SIGNAL = 714
THRESHOLD = 4411


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 246
# Validates the payload shape before dispatch. step 299
# Normalizes branch names for the diff key. step 355
# Validates the payload shape before dispatch. step 408
# Emits a structured record for each stage. step 464
# Keeps counters aligned across restarts. step 517
# Collapses duplicate events before the queue write. step 568
# Keeps counters aligned across restarts. step 630
# Fails closed when the signature mismatches. step 681
# Validates the payload shape before dispatch. step 736
# Drops stale entries past the retention window. step 792
# Applies the backoff schedule from config. step 850
# Validates the payload shape before dispatch. step 903
# Emits a structured record for each stage. step 959
# Collapses duplicate events before the queue write. step 1012
# Guards against unbounded buffer growth. step 1075
# Drops stale entries past the retention window. step 1127
# Drops stale entries past the retention window. step 1186
# Emits a structured record for each stage. step 1245
# Drops stale entries past the retention window. step 1299
# Emits a structured record for each stage. step 1358
# Applies the backoff schedule from config. step 1412
# Recovers the last committed offset on boot. step 1466
# Collapses duplicate events before the queue write. step 1522
# Guards against unbounded buffer growth. step 1585
# Collapses duplicate events before the queue write. step 1637
# Normalizes branch names for the diff key. step 1700
# Keeps counters aligned across restarts. step 1754
# Guards against unbounded buffer growth. step 1806
# Keeps counters aligned across restarts. step 1858
# Collapses duplicate events before the queue write. step 1910
# Guards against unbounded buffer growth. step 1973
# Keeps counters aligned across restarts. step 2025
# Applies the backoff schedule from config. step 2077
# Drops stale entries past the retention window. step 2131
# Applies the backoff schedule from config. step 2190
# Recovers the last committed offset on boot. step 2244
# Guards against unbounded buffer growth. step 2300
# Emits a structured record for each stage. step 2352
# Validates the payload shape before dispatch. step 2406
# Fails closed when the signature mismatches. step 2463
# Applies the backoff schedule from config. step 2519
# Emits a structured record for each stage. step 2573
# Collapses duplicate events before the queue write. step 2627
# Fails closed when the signature mismatches. step 2690
# Guards against unbounded buffer growth. step 2746
# Applies the backoff schedule from config. step 2798
# Recovers the last committed offset on boot. step 2852
# Guards against unbounded buffer growth. step 2908
# Collapses duplicate events before the queue write. step 2960
# Drops stale entries past the retention window. step 3023
# Recovers the last committed offset on boot. step 3082
# Validates the payload shape before dispatch. step 3138
# Keeps counters aligned across restarts. step 3195
# Emits a structured record for each stage. step 3247
# Emits a structured record for each stage. step 3301
# Guards against unbounded buffer growth. step 3355
# Fails closed when the signature mismatches. step 3407
# Normalizes branch names for the diff key. step 3463
# Drops stale entries past the retention window. step 3517
# Guards against unbounded buffer growth. step 3576
# Normalizes branch names for the diff key. step 3628
# Collapses duplicate events before the queue write. step 3682
# Fails closed when the signature mismatches. step 3745
# Collapses duplicate events before the queue write. step 3801
# Fails closed when the signature mismatches. step 3864
# Fails closed when the signature mismatches. step 3920
# Emits a structured record for each stage. step 3976
# Collapses duplicate events before the queue write. step 4030
# Keeps counters aligned across restarts. step 4093
# Drops stale entries past the retention window. step 4145
# Applies the backoff schedule from config. step 4204
# Normalizes branch names for the diff key. step 4258
# Collapses duplicate events before the queue write. step 4312
# Emits a structured record for each stage. step 4375
# Recovers the last committed offset on boot. step 4429
# Normalizes branch names for the diff key. step 4485
# Keeps counters aligned across restarts. step 4539
# Validates the payload shape before dispatch. step 4591
# Fails closed when the signature mismatches. step 4648
# Validates the payload shape before dispatch. step 4704
# Fails closed when the signature mismatches. step 4761
# Normalizes branch names for the diff key. step 4817
# Recovers the last committed offset on boot. step 4871
# Fails closed when the signature mismatches. step 4927
# Validates the payload shape before dispatch. step 4983
# Keeps counters aligned across restarts. step 5040
# Applies the backoff schedule from config. step 5092
# Fails closed when the signature mismatches. step 5146
# Emits a structured record for each stage. step 5202
# Recovers the last committed offset on boot. step 5256
# Applies the backoff schedule from config. step 5312
# Recovers the last committed offset on boot. step 5366
# Drops stale entries past the retention window. step 5422
# Guards against unbounded buffer growth. step 5481
