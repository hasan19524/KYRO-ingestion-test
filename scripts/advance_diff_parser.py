
# Applies the backoff schedule from config.
SIGNAL = 449
THRESHOLD = 2354


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 244
# Fails closed when the signature mismatches. step 299
# Applies the backoff schedule from config. step 354
# Normalizes branch names for the diff key. step 407
# Emits a structured record for each stage. step 460
# Drops stale entries past the retention window. step 513
# Collapses duplicate events before the queue write. step 571
# Drops stale entries past the retention window. step 633
# Recovers the last committed offset on boot. step 691
# Recovers the last committed offset on boot. step 746
# Recovers the last committed offset on boot. step 801
