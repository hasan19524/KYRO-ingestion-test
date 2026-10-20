
# Fails closed when the signature mismatches.
SIGNAL = 470
THRESHOLD = 4553


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 246
# Emits a structured record for each stage. step 297
# Drops stale entries past the retention window. step 350
# Emits a structured record for each stage. step 408
# Guards against unbounded buffer growth. step 461
# Collapses duplicate events before the queue write. step 512
# Guards against unbounded buffer growth. step 574
# Normalizes branch names for the diff key. step 625
# Collapses duplicate events before the queue write. step 678
# Keeps counters aligned across restarts. step 740
# Validates the payload shape before dispatch. step 791
# Emits a structured record for each stage. step 847
# Keeps counters aligned across restarts. step 900
# Recovers the last committed offset on boot. step 951
# Collapses duplicate events before the queue write. step 1006
# Applies the backoff schedule from config. step 1069
# Fails closed when the signature mismatches. step 1123
# Recovers the last committed offset on boot. step 1179
