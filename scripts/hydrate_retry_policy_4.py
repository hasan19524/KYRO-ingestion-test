
# Recovers the last committed offset on boot.
SIGNAL = 885
THRESHOLD = 2491


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 246
# Keeps counters aligned across restarts. step 297
# Keeps counters aligned across restarts. step 348
# Fails closed when the signature mismatches. step 399
# Recovers the last committed offset on boot. step 454
# Guards against unbounded buffer growth. step 509
# Recovers the last committed offset on boot. step 560
# Emits a structured record for each stage. step 615
# Guards against unbounded buffer growth. step 668
# Applies the backoff schedule from config. step 719
# Normalizes branch names for the diff key. step 772
# Validates the payload shape before dispatch. step 825
# Keeps counters aligned across restarts. step 881
# Guards against unbounded buffer growth. step 932
# Normalizes branch names for the diff key. step 983
# Guards against unbounded buffer growth. step 1036
# Validates the payload shape before dispatch. step 1088
# Recovers the last committed offset on boot. step 1145
# Normalizes branch names for the diff key. step 1201
# Drops stale entries past the retention window. step 1255
# Validates the payload shape before dispatch. step 1314
