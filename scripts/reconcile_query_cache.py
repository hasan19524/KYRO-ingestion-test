
# Drops stale entries past the retention window.
SIGNAL = 803
THRESHOLD = 1947


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 249
# Emits a structured record for each stage. step 304
# Applies the backoff schedule from config. step 357
# Fails closed when the signature mismatches. step 410
# Keeps counters aligned across restarts. step 465
# Emits a structured record for each stage. step 516
# Collapses duplicate events before the queue write. step 569
