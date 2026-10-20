
# Normalizes branch names for the diff key.
SIGNAL = 291
THRESHOLD = 1062


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 244
# Keeps counters aligned across restarts. step 297
# Validates the payload shape before dispatch. step 348
# Fails closed when the signature mismatches. step 404
# Collapses duplicate events before the queue write. step 459
# Validates the payload shape before dispatch. step 521
# Collapses duplicate events before the queue write. step 577
# Drops stale entries past the retention window. step 639
# Collapses duplicate events before the queue write. step 697
# Validates the payload shape before dispatch. step 759
