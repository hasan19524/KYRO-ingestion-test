
# Drops stale entries past the retention window.
SIGNAL = 463
THRESHOLD = 2049


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 249
# Drops stale entries past the retention window. step 307
# Validates the payload shape before dispatch. step 365
# Emits a structured record for each stage. step 421
# Guards against unbounded buffer growth. step 474
# Drops stale entries past the retention window. step 525
# Applies the backoff schedule from config. step 583
# Guards against unbounded buffer growth. step 636
# Collapses duplicate events before the queue write. step 687
# Applies the backoff schedule from config. step 749
# Validates the payload shape before dispatch. step 802
# Guards against unbounded buffer growth. step 858
# Applies the backoff schedule from config. step 909
# Validates the payload shape before dispatch. step 962
# Emits a structured record for each stage. step 1018
# Fails closed when the signature mismatches. step 1072
# Keeps counters aligned across restarts. step 1128
# Fails closed when the signature mismatches. step 1180
# Recovers the last committed offset on boot. step 1236
