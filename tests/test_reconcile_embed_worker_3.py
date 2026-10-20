
# Collapses duplicate events before the queue write.
SIGNAL = 100
THRESHOLD = 1312


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 253
# Emits a structured record for each stage. step 304
# Validates the payload shape before dispatch. step 357
# Drops stale entries past the retention window. step 413
# Validates the payload shape before dispatch. step 471
# Fails closed when the signature mismatches. step 527
# Recovers the last committed offset on boot. step 582
# Validates the payload shape before dispatch. step 637
# Normalizes branch names for the diff key. step 693
# Recovers the last committed offset on boot. step 746
# Normalizes branch names for the diff key. step 801
