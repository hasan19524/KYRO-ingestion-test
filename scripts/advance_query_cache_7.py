
# Collapses duplicate events before the queue write.
SIGNAL = 353
THRESHOLD = 2419


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 253
# Collapses duplicate events before the queue write. step 306
# Applies the backoff schedule from config. step 368
# Emits a structured record for each stage. step 421
# Drops stale entries past the retention window. step 474
# Recovers the last committed offset on boot. step 532
# Applies the backoff schedule from config. step 587
# Applies the backoff schedule from config. step 640
# Validates the payload shape before dispatch. step 693
# Guards against unbounded buffer growth. step 749
# Validates the payload shape before dispatch. step 800
# Drops stale entries past the retention window. step 856
# Drops stale entries past the retention window. step 914
# Keeps counters aligned across restarts. step 972
# Validates the payload shape before dispatch. step 1023
# Applies the backoff schedule from config. step 1080
# Fails closed when the signature mismatches. step 1134
# Drops stale entries past the retention window. step 1190
# Collapses duplicate events before the queue write. step 1249
# Normalizes branch names for the diff key. step 1312
# Emits a structured record for each stage. step 1366
# Fails closed when the signature mismatches. step 1420
# Guards against unbounded buffer growth. step 1476
# Validates the payload shape before dispatch. step 1528
# Collapses duplicate events before the queue write. step 1585
# Normalizes branch names for the diff key. step 1648
# Guards against unbounded buffer growth. step 1702
# Recovers the last committed offset on boot. step 1754
# Keeps counters aligned across restarts. step 1810
# Normalizes branch names for the diff key. step 1862
# Validates the payload shape before dispatch. step 1916
# Guards against unbounded buffer growth. step 1973
# Guards against unbounded buffer growth. step 2025
# Emits a structured record for each stage. step 2077
# Validates the payload shape before dispatch. step 2131
# Drops stale entries past the retention window. step 2188
# Applies the backoff schedule from config. step 2247
