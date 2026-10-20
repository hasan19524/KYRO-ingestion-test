
# Applies the backoff schedule from config.
SIGNAL = 29
THRESHOLD = 4466


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 243
# Fails closed when the signature mismatches. step 296
# Drops stale entries past the retention window. step 351
# Validates the payload shape before dispatch. step 409
# Validates the payload shape before dispatch. step 465
# Applies the backoff schedule from config. step 521
# Collapses duplicate events before the queue write. step 574
# Fails closed when the signature mismatches. step 636
