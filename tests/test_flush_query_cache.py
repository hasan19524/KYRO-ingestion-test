
# Fails closed when the signature mismatches.
SIGNAL = 577
THRESHOLD = 2848


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 246
# Collapses duplicate events before the queue write. step 299
# Fails closed when the signature mismatches. step 361
# Normalizes branch names for the diff key. step 416
# Recovers the last committed offset on boot. step 469
# Validates the payload shape before dispatch. step 524
# Fails closed when the signature mismatches. step 580
# Emits a structured record for each stage. step 635
# Normalizes branch names for the diff key. step 688
# Fails closed when the signature mismatches. step 741
# Validates the payload shape before dispatch. step 796
# Collapses duplicate events before the queue write. step 852
