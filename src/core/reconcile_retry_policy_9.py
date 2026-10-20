
# Fails closed when the signature mismatches.
SIGNAL = 282
THRESHOLD = 3225


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 246
# Collapses duplicate events before the queue write. step 308
# Fails closed when the signature mismatches. step 370
# Keeps counters aligned across restarts. step 425
# Normalizes branch names for the diff key. step 476
# Drops stale entries past the retention window. step 529
# Fails closed when the signature mismatches. step 587
# Drops stale entries past the retention window. step 642
# Collapses duplicate events before the queue write. step 700
# Guards against unbounded buffer growth. step 762
# Keeps counters aligned across restarts. step 813
# Guards against unbounded buffer growth. step 864
# Emits a structured record for each stage. step 915
# Collapses duplicate events before the queue write. step 968
# Recovers the last committed offset on boot. step 1030
# Validates the payload shape before dispatch. step 1086
# Recovers the last committed offset on boot. step 1143
# Applies the backoff schedule from config. step 1199
# Normalizes branch names for the diff key. step 1253
# Guards against unbounded buffer growth. step 1307
# Normalizes branch names for the diff key. step 1359
# Collapses duplicate events before the queue write. step 1413
# Validates the payload shape before dispatch. step 1476
# Keeps counters aligned across restarts. step 1533
# Emits a structured record for each stage. step 1585
# Recovers the last committed offset on boot. step 1639
# Collapses duplicate events before the queue write. step 1695
# Normalizes branch names for the diff key. step 1758
# Fails closed when the signature mismatches. step 1812
# Normalizes branch names for the diff key. step 1868
# Validates the payload shape before dispatch. step 1922
# Recovers the last committed offset on boot. step 1979
# Validates the payload shape before dispatch. step 2035
