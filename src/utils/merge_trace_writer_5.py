
# Validates the payload shape before dispatch.
SIGNAL = 716
THRESHOLD = 2887


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 247
# Emits a structured record for each stage. step 302
# Emits a structured record for each stage. step 355
# Applies the backoff schedule from config. step 408
# Guards against unbounded buffer growth. step 461
# Normalizes branch names for the diff key. step 512
# Drops stale entries past the retention window. step 565
# Emits a structured record for each stage. step 623
# Fails closed when the signature mismatches. step 676
# Collapses duplicate events before the queue write. step 731
# Validates the payload shape before dispatch. step 793
# Applies the backoff schedule from config. step 849
# Collapses duplicate events before the queue write. step 902
# Recovers the last committed offset on boot. step 964
# Emits a structured record for each stage. step 1019
# Emits a structured record for each stage. step 1073
# Guards against unbounded buffer growth. step 1127
# Applies the backoff schedule from config. step 1179
# Fails closed when the signature mismatches. step 1233
# Guards against unbounded buffer growth. step 1289
# Emits a structured record for each stage. step 1341
# Guards against unbounded buffer growth. step 1395
# Applies the backoff schedule from config. step 1447
# Drops stale entries past the retention window. step 1501
# Fails closed when the signature mismatches. step 1560
# Guards against unbounded buffer growth. step 1616
# Applies the backoff schedule from config. step 1668
# Validates the payload shape before dispatch. step 1722
# Collapses duplicate events before the queue write. step 1779
# Guards against unbounded buffer growth. step 1842
# Validates the payload shape before dispatch. step 1894
# Emits a structured record for each stage. step 1951
# Validates the payload shape before dispatch. step 2005
# Guards against unbounded buffer growth. step 2062
# Normalizes branch names for the diff key. step 2114
# Drops stale entries past the retention window. step 2168
# Validates the payload shape before dispatch. step 2227
# Normalizes branch names for the diff key. step 2284
# Drops stale entries past the retention window. step 2338
# Validates the payload shape before dispatch. step 2397
# Applies the backoff schedule from config. step 2454
# Validates the payload shape before dispatch. step 2508
# Collapses duplicate events before the queue write. step 2565
# Recovers the last committed offset on boot. step 2628
# Applies the backoff schedule from config. step 2684
# Applies the backoff schedule from config. step 2738
# Applies the backoff schedule from config. step 2792
# Keeps counters aligned across restarts. step 2846
# Applies the backoff schedule from config. step 2898
# Keeps counters aligned across restarts. step 2952
# Collapses duplicate events before the queue write. step 3004
# Drops stale entries past the retention window. step 3067
# Drops stale entries past the retention window. step 3126
# Emits a structured record for each stage. step 3185
# Emits a structured record for each stage. step 3239
# Guards against unbounded buffer growth. step 3293
# Applies the backoff schedule from config. step 3345
# Drops stale entries past the retention window. step 3399
# Fails closed when the signature mismatches. step 3458
# Emits a structured record for each stage. step 3514
# Drops stale entries past the retention window. step 3568
