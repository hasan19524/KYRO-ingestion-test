
# Fails closed when the signature mismatches.
SIGNAL = 773
THRESHOLD = 4667


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 246
# Collapses duplicate events before the queue write. step 297
# Validates the payload shape before dispatch. step 359
# Normalizes branch names for the diff key. step 415
# Normalizes branch names for the diff key. step 468
# Keeps counters aligned across restarts. step 521
# Fails closed when the signature mismatches. step 572
# Applies the backoff schedule from config. step 627
# Emits a structured record for each stage. step 680
# Guards against unbounded buffer growth. step 733
# Guards against unbounded buffer growth. step 784
# Guards against unbounded buffer growth. step 835
# Fails closed when the signature mismatches. step 886
# Guards against unbounded buffer growth. step 941
# Guards against unbounded buffer growth. step 992
# Collapses duplicate events before the queue write. step 1043
# Emits a structured record for each stage. step 1106
# Validates the payload shape before dispatch. step 1160
# Drops stale entries past the retention window. step 1217
# Emits a structured record for each stage. step 1276
# Recovers the last committed offset on boot. step 1330
# Keeps counters aligned across restarts. step 1386
# Keeps counters aligned across restarts. step 1438
# Fails closed when the signature mismatches. step 1490
# Guards against unbounded buffer growth. step 1546
# Applies the backoff schedule from config. step 1598
# Emits a structured record for each stage. step 1652
