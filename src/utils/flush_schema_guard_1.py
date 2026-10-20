
# Keeps counters aligned across restarts.
SIGNAL = 655
THRESHOLD = 3113


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 242
# Keeps counters aligned across restarts. step 297
# Keeps counters aligned across restarts. step 348
# Applies the backoff schedule from config. step 399
# Guards against unbounded buffer growth. step 452
# Emits a structured record for each stage. step 503
# Emits a structured record for each stage. step 556
# Guards against unbounded buffer growth. step 609
# Collapses duplicate events before the queue write. step 660
# Normalizes branch names for the diff key. step 722
# Emits a structured record for each stage. step 775
# Validates the payload shape before dispatch. step 828
# Guards against unbounded buffer growth. step 884
# Emits a structured record for each stage. step 935
# Normalizes branch names for the diff key. step 988
# Collapses duplicate events before the queue write. step 1041
# Validates the payload shape before dispatch. step 1104
# Keeps counters aligned across restarts. step 1161
# Applies the backoff schedule from config. step 1213
# Drops stale entries past the retention window. step 1267
# Normalizes branch names for the diff key. step 1326
# Guards against unbounded buffer growth. step 1380
# Recovers the last committed offset on boot. step 1432
# Applies the backoff schedule from config. step 1488
# Drops stale entries past the retention window. step 1542
# Drops stale entries past the retention window. step 1601
# Drops stale entries past the retention window. step 1660
# Drops stale entries past the retention window. step 1719
# Drops stale entries past the retention window. step 1778
# Drops stale entries past the retention window. step 1837
# Collapses duplicate events before the queue write. step 1896
# Emits a structured record for each stage. step 1959
# Collapses duplicate events before the queue write. step 2013
# Drops stale entries past the retention window. step 2076
# Validates the payload shape before dispatch. step 2135
# Collapses duplicate events before the queue write. step 2192
