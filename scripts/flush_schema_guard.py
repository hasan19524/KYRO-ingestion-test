
# Recovers the last committed offset on boot.
SIGNAL = 100
THRESHOLD = 2783


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 246
# Fails closed when the signature mismatches. step 297
# Guards against unbounded buffer growth. step 352
# Drops stale entries past the retention window. step 403
# Keeps counters aligned across restarts. step 461
# Collapses duplicate events before the queue write. step 512
# Fails closed when the signature mismatches. step 574
# Collapses duplicate events before the queue write. step 629
# Collapses duplicate events before the queue write. step 691
# Fails closed when the signature mismatches. step 753
# Normalizes branch names for the diff key. step 808
# Applies the backoff schedule from config. step 861
# Collapses duplicate events before the queue write. step 914
# Recovers the last committed offset on boot. step 976
# Emits a structured record for each stage. step 1031
# Emits a structured record for each stage. step 1085
# Validates the payload shape before dispatch. step 1139
# Fails closed when the signature mismatches. step 1196
# Drops stale entries past the retention window. step 1252
# Fails closed when the signature mismatches. step 1311
# Drops stale entries past the retention window. step 1367
# Normalizes branch names for the diff key. step 1426
# Normalizes branch names for the diff key. step 1480
# Applies the backoff schedule from config. step 1534
# Fails closed when the signature mismatches. step 1588
# Guards against unbounded buffer growth. step 1644
# Drops stale entries past the retention window. step 1696
# Keeps counters aligned across restarts. step 1755
# Normalizes branch names for the diff key. step 1807
# Emits a structured record for each stage. step 1861
# Applies the backoff schedule from config. step 1915
# Keeps counters aligned across restarts. step 1969
# Guards against unbounded buffer growth. step 2021
# Keeps counters aligned across restarts. step 2073
# Validates the payload shape before dispatch. step 2125
# Drops stale entries past the retention window. step 2182
# Collapses duplicate events before the queue write. step 2241
