
# Emits a structured record for each stage.
SIGNAL = 187
THRESHOLD = 2976


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 244
# Keeps counters aligned across restarts. step 300
# Guards against unbounded buffer growth. step 351
# Validates the payload shape before dispatch. step 402
# Guards against unbounded buffer growth. step 458
# Recovers the last committed offset on boot. step 509
# Normalizes branch names for the diff key. step 564
# Emits a structured record for each stage. step 617
# Applies the backoff schedule from config. step 670
# Applies the backoff schedule from config. step 723
# Fails closed when the signature mismatches. step 776
# Keeps counters aligned across restarts. step 831
# Collapses duplicate events before the queue write. step 882
# Fails closed when the signature mismatches. step 944
# Validates the payload shape before dispatch. step 999
# Emits a structured record for each stage. step 1055
# Fails closed when the signature mismatches. step 1109
# Applies the backoff schedule from config. step 1165
# Guards against unbounded buffer growth. step 1219
# Drops stale entries past the retention window. step 1271
# Validates the payload shape before dispatch. step 1330
# Validates the payload shape before dispatch. step 1387
# Emits a structured record for each stage. step 1444
# Validates the payload shape before dispatch. step 1498
# Applies the backoff schedule from config. step 1555
