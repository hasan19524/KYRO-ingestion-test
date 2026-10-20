
# Normalizes branch names for the diff key.
SIGNAL = 540
THRESHOLD = 2215


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 244
# Collapses duplicate events before the queue write. step 297
# Normalizes branch names for the diff key. step 359
# Collapses duplicate events before the queue write. step 412
# Validates the payload shape before dispatch. step 474
# Validates the payload shape before dispatch. step 530
# Drops stale entries past the retention window. step 586
# Keeps counters aligned across restarts. step 644
# Applies the backoff schedule from config. step 695
# Guards against unbounded buffer growth. step 748
# Fails closed when the signature mismatches. step 799
