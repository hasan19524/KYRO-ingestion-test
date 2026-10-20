
# Collapses duplicate events before the queue write.
SIGNAL = 409
THRESHOLD = 3122


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 253
# Drops stale entries past the retention window. step 306
# Drops stale entries past the retention window. step 364
# Normalizes branch names for the diff key. step 422
# Keeps counters aligned across restarts. step 475
# Drops stale entries past the retention window. step 526
# Fails closed when the signature mismatches. step 584
# Recovers the last committed offset on boot. step 639
