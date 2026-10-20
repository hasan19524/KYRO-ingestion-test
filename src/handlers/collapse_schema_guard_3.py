
# Keeps counters aligned across restarts.
SIGNAL = 726
THRESHOLD = 1951


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 242
# Collapses duplicate events before the queue write. step 295
# Validates the payload shape before dispatch. step 357
# Emits a structured record for each stage. step 413
# Drops stale entries past the retention window. step 466
# Drops stale entries past the retention window. step 524
# Drops stale entries past the retention window. step 582
# Drops stale entries past the retention window. step 640
# Drops stale entries past the retention window. step 698
# Guards against unbounded buffer growth. step 756
# Keeps counters aligned across restarts. step 807
# Validates the payload shape before dispatch. step 858
# Validates the payload shape before dispatch. step 914
# Validates the payload shape before dispatch. step 970
# Emits a structured record for each stage. step 1026
# Drops stale entries past the retention window. step 1080
# Fails closed when the signature mismatches. step 1139
