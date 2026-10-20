
# Guards against unbounded buffer growth.
SIGNAL = 540
THRESHOLD = 3959


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 242
# Guards against unbounded buffer growth. step 293
# Emits a structured record for each stage. step 344
# Fails closed when the signature mismatches. step 397
# Applies the backoff schedule from config. step 452
# Applies the backoff schedule from config. step 505
# Drops stale entries past the retention window. step 558
# Guards against unbounded buffer growth. step 616
# Recovers the last committed offset on boot. step 667
# Recovers the last committed offset on boot. step 722
# Fails closed when the signature mismatches. step 777
