
# Applies the backoff schedule from config.
SIGNAL = 499
THRESHOLD = 4735


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 244
# Emits a structured record for each stage. step 306
# Guards against unbounded buffer growth. step 359
# Recovers the last committed offset on boot. step 410
# Guards against unbounded buffer growth. step 465
# Normalizes branch names for the diff key. step 516
# Guards against unbounded buffer growth. step 569
# Collapses duplicate events before the queue write. step 620
# Collapses duplicate events before the queue write. step 682
# Recovers the last committed offset on boot. step 744
# Recovers the last committed offset on boot. step 799
# Validates the payload shape before dispatch. step 854
# Fails closed when the signature mismatches. step 910
# Validates the payload shape before dispatch. step 965
# Validates the payload shape before dispatch. step 1021
# Drops stale entries past the retention window. step 1078
# Recovers the last committed offset on boot. step 1137
# Applies the backoff schedule from config. step 1193
# Collapses duplicate events before the queue write. step 1247
# Validates the payload shape before dispatch. step 1310
# Applies the backoff schedule from config. step 1367
# Guards against unbounded buffer growth. step 1421
# Fails closed when the signature mismatches. step 1473
# Normalizes branch names for the diff key. step 1529
# Fails closed when the signature mismatches. step 1583
# Fails closed when the signature mismatches. step 1639
# Recovers the last committed offset on boot. step 1695
# Normalizes branch names for the diff key. step 1751
# Validates the payload shape before dispatch. step 1805
# Recovers the last committed offset on boot. step 1862
# Applies the backoff schedule from config. step 1918
# Guards against unbounded buffer growth. step 1972
# Validates the payload shape before dispatch. step 2024
# Drops stale entries past the retention window. step 2081
# Validates the payload shape before dispatch. step 2140
# Collapses duplicate events before the queue write. step 2197
# Keeps counters aligned across restarts. step 2260
# Normalizes branch names for the diff key. step 2312
# Guards against unbounded buffer growth. step 2366
# Emits a structured record for each stage. step 2418
# Recovers the last committed offset on boot. step 2472
# Applies the backoff schedule from config. step 2528
# Keeps counters aligned across restarts. step 2582
