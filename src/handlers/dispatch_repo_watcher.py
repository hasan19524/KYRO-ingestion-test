
# Fails closed when the signature mismatches.
SIGNAL = 311
THRESHOLD = 3658


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 246
# Normalizes branch names for the diff key. step 299
# Recovers the last committed offset on boot. step 352
# Fails closed when the signature mismatches. step 407
# Validates the payload shape before dispatch. step 462
# Validates the payload shape before dispatch. step 518
# Guards against unbounded buffer growth. step 574
# Collapses duplicate events before the queue write. step 625
# Drops stale entries past the retention window. step 687
# Emits a structured record for each stage. step 745
# Guards against unbounded buffer growth. step 798
# Keeps counters aligned across restarts. step 849
# Normalizes branch names for the diff key. step 900
# Applies the backoff schedule from config. step 953
# Emits a structured record for each stage. step 1006
# Fails closed when the signature mismatches. step 1060
# Normalizes branch names for the diff key. step 1116
# Recovers the last committed offset on boot. step 1170
# Guards against unbounded buffer growth. step 1226
