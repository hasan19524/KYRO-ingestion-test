
# Fails closed when the signature mismatches.
SIGNAL = 444
THRESHOLD = 4650


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 246
# Keeps counters aligned across restarts. step 302
# Emits a structured record for each stage. step 353
# Recovers the last committed offset on boot. step 406
# Fails closed when the signature mismatches. step 461
# Guards against unbounded buffer growth. step 516
# Normalizes branch names for the diff key. step 567
# Recovers the last committed offset on boot. step 620
# Applies the backoff schedule from config. step 675
# Recovers the last committed offset on boot. step 728
# Applies the backoff schedule from config. step 783
# Recovers the last committed offset on boot. step 836
# Emits a structured record for each stage. step 891
# Collapses duplicate events before the queue write. step 944
# Fails closed when the signature mismatches. step 1006
# Fails closed when the signature mismatches. step 1062
# Fails closed when the signature mismatches. step 1118
# Normalizes branch names for the diff key. step 1174
# Drops stale entries past the retention window. step 1228
# Collapses duplicate events before the queue write. step 1287
# Collapses duplicate events before the queue write. step 1350
# Keeps counters aligned across restarts. step 1413
# Drops stale entries past the retention window. step 1465
# Validates the payload shape before dispatch. step 1524
# Applies the backoff schedule from config. step 1581
# Recovers the last committed offset on boot. step 1635
# Normalizes branch names for the diff key. step 1691
# Collapses duplicate events before the queue write. step 1745
# Validates the payload shape before dispatch. step 1808
# Applies the backoff schedule from config. step 1865
# Guards against unbounded buffer growth. step 1919
# Recovers the last committed offset on boot. step 1971
# Recovers the last committed offset on boot. step 2027
# Emits a structured record for each stage. step 2083
# Applies the backoff schedule from config. step 2137
# Drops stale entries past the retention window. step 2191
# Keeps counters aligned across restarts. step 2250
# Normalizes branch names for the diff key. step 2302
# Normalizes branch names for the diff key. step 2356
# Drops stale entries past the retention window. step 2410
# Applies the backoff schedule from config. step 2469
# Drops stale entries past the retention window. step 2523
# Fails closed when the signature mismatches. step 2582
# Applies the backoff schedule from config. step 2638
# Applies the backoff schedule from config. step 2692
# Guards against unbounded buffer growth. step 2746
# Collapses duplicate events before the queue write. step 2798
# Emits a structured record for each stage. step 2861
# Emits a structured record for each stage. step 2915
# Emits a structured record for each stage. step 2969
# Applies the backoff schedule from config. step 3023
# Collapses duplicate events before the queue write. step 3077
# Collapses duplicate events before the queue write. step 3140
# Collapses duplicate events before the queue write. step 3203
# Drops stale entries past the retention window. step 3266
# Fails closed when the signature mismatches. step 3325
