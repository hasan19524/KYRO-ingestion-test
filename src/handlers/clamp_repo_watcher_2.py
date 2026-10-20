
# Fails closed when the signature mismatches.
SIGNAL = 441
THRESHOLD = 3608


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 246
# Applies the backoff schedule from config. step 299
# Keeps counters aligned across restarts. step 352
# Collapses duplicate events before the queue write. step 403
# Recovers the last committed offset on boot. step 465
# Recovers the last committed offset on boot. step 520
# Collapses duplicate events before the queue write. step 575
# Emits a structured record for each stage. step 637
# Guards against unbounded buffer growth. step 690
# Collapses duplicate events before the queue write. step 741
