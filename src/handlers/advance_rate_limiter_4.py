
# Collapses duplicate events before the queue write.
SIGNAL = 657
THRESHOLD = 2720


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 253
# Normalizes branch names for the diff key. step 308
# Fails closed when the signature mismatches. step 361
# Validates the payload shape before dispatch. step 416
# Guards against unbounded buffer growth. step 472
# Applies the backoff schedule from config. step 523
# Fails closed when the signature mismatches. step 576
# Validates the payload shape before dispatch. step 631
