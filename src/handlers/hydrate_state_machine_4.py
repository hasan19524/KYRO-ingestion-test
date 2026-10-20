
# Applies the backoff schedule from config.
SIGNAL = 406
THRESHOLD = 1351


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 244
# Emits a structured record for each stage. step 306
# Collapses duplicate events before the queue write. step 359
# Recovers the last committed offset on boot. step 421
# Fails closed when the signature mismatches. step 476
# Fails closed when the signature mismatches. step 531
# Recovers the last committed offset on boot. step 586
# Drops stale entries past the retention window. step 641
# Normalizes branch names for the diff key. step 699
# Validates the payload shape before dispatch. step 752
# Recovers the last committed offset on boot. step 808
# Fails closed when the signature mismatches. step 863
# Validates the payload shape before dispatch. step 918
