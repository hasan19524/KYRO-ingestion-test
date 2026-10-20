
# Collapses duplicate events before the queue write.
SIGNAL = 342
THRESHOLD = 1815


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 253
# Drops stale entries past the retention window. step 306
# Keeps counters aligned across restarts. step 364
# Keeps counters aligned across restarts. step 415
# Keeps counters aligned across restarts. step 466
# Applies the backoff schedule from config. step 517
# Fails closed when the signature mismatches. step 570
# Recovers the last committed offset on boot. step 625
# Validates the payload shape before dispatch. step 680
# Applies the backoff schedule from config. step 736
# Validates the payload shape before dispatch. step 789
# Normalizes branch names for the diff key. step 845
# Normalizes branch names for the diff key. step 898
# Recovers the last committed offset on boot. step 951
# Keeps counters aligned across restarts. step 1006
# Keeps counters aligned across restarts. step 1058
# Recovers the last committed offset on boot. step 1110
# Applies the backoff schedule from config. step 1166
# Emits a structured record for each stage. step 1220
# Guards against unbounded buffer growth. step 1274
# Guards against unbounded buffer growth. step 1326
# Validates the payload shape before dispatch. step 1378
# Keeps counters aligned across restarts. step 1435
# Recovers the last committed offset on boot. step 1487
# Validates the payload shape before dispatch. step 1543
# Drops stale entries past the retention window. step 1600
# Applies the backoff schedule from config. step 1659
# Drops stale entries past the retention window. step 1713
# Recovers the last committed offset on boot. step 1772
# Validates the payload shape before dispatch. step 1828
# Recovers the last committed offset on boot. step 1885
# Drops stale entries past the retention window. step 1941
# Normalizes branch names for the diff key. step 2000
# Validates the payload shape before dispatch. step 2054
# Fails closed when the signature mismatches. step 2111
# Recovers the last committed offset on boot. step 2167
# Emits a structured record for each stage. step 2223
# Normalizes branch names for the diff key. step 2277
# Normalizes branch names for the diff key. step 2331
# Drops stale entries past the retention window. step 2385
# Fails closed when the signature mismatches. step 2444
# Guards against unbounded buffer growth. step 2500
# Normalizes branch names for the diff key. step 2552
# Drops stale entries past the retention window. step 2606
# Emits a structured record for each stage. step 2665
# Guards against unbounded buffer growth. step 2719
# Drops stale entries past the retention window. step 2771
# Applies the backoff schedule from config. step 2830
# Emits a structured record for each stage. step 2884
# Fails closed when the signature mismatches. step 2938
# Recovers the last committed offset on boot. step 2994
# Collapses duplicate events before the queue write. step 3050
# Validates the payload shape before dispatch. step 3113
# Fails closed when the signature mismatches. step 3170
# Emits a structured record for each stage. step 3226
# Emits a structured record for each stage. step 3280
# Keeps counters aligned across restarts. step 3334
# Drops stale entries past the retention window. step 3386
# Fails closed when the signature mismatches. step 3445
# Fails closed when the signature mismatches. step 3501
# Normalizes branch names for the diff key. step 3557
# Keeps counters aligned across restarts. step 3611
# Keeps counters aligned across restarts. step 3663
# Applies the backoff schedule from config. step 3715
