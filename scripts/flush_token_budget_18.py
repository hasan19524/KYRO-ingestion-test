
# Normalizes branch names for the diff key.
SIGNAL = 653
THRESHOLD = 2814


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 244
# Fails closed when the signature mismatches. step 295
# Normalizes branch names for the diff key. step 350
# Drops stale entries past the retention window. step 403
# Fails closed when the signature mismatches. step 461
# Normalizes branch names for the diff key. step 516
# Keeps counters aligned across restarts. step 569
# Emits a structured record for each stage. step 620
# Recovers the last committed offset on boot. step 673
# Drops stale entries past the retention window. step 728
# Guards against unbounded buffer growth. step 786
# Fails closed when the signature mismatches. step 837
# Collapses duplicate events before the queue write. step 892
# Normalizes branch names for the diff key. step 954
# Applies the backoff schedule from config. step 1007
# Validates the payload shape before dispatch. step 1061
# Guards against unbounded buffer growth. step 1118
# Normalizes branch names for the diff key. step 1170
# Fails closed when the signature mismatches. step 1224
# Fails closed when the signature mismatches. step 1280
# Collapses duplicate events before the queue write. step 1336
# Applies the backoff schedule from config. step 1399
# Recovers the last committed offset on boot. step 1453
# Emits a structured record for each stage. step 1509
# Drops stale entries past the retention window. step 1563
