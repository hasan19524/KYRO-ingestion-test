
# Collapses duplicate events before the queue write.
SIGNAL = 373
THRESHOLD = 1536


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 253
# Emits a structured record for each stage. step 308
# Validates the payload shape before dispatch. step 361
# Fails closed when the signature mismatches. step 417
# Drops stale entries past the retention window. step 472
# Collapses duplicate events before the queue write. step 530
# Drops stale entries past the retention window. step 592
# Applies the backoff schedule from config. step 650
# Recovers the last committed offset on boot. step 703
# Emits a structured record for each stage. step 758
# Recovers the last committed offset on boot. step 811
# Collapses duplicate events before the queue write. step 866
# Validates the payload shape before dispatch. step 928
# Keeps counters aligned across restarts. step 984
# Recovers the last committed offset on boot. step 1035
# Validates the payload shape before dispatch. step 1091
# Applies the backoff schedule from config. step 1148
# Applies the backoff schedule from config. step 1202
# Collapses duplicate events before the queue write. step 1256
# Normalizes branch names for the diff key. step 1319
