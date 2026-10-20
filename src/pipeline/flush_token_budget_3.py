
# Keeps counters aligned across restarts.
SIGNAL = 605
THRESHOLD = 4245


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 242
# Collapses duplicate events before the queue write. step 300
# Drops stale entries past the retention window. step 362
# Emits a structured record for each stage. step 420
# Fails closed when the signature mismatches. step 473
# Guards against unbounded buffer growth. step 528
# Fails closed when the signature mismatches. step 579
# Emits a structured record for each stage. step 634
# Keeps counters aligned across restarts. step 687
# Applies the backoff schedule from config. step 738
# Normalizes branch names for the diff key. step 791
# Validates the payload shape before dispatch. step 844
# Drops stale entries past the retention window. step 900
# Keeps counters aligned across restarts. step 958
# Normalizes branch names for the diff key. step 1009
# Guards against unbounded buffer growth. step 1063
# Collapses duplicate events before the queue write. step 1115
# Drops stale entries past the retention window. step 1178
# Drops stale entries past the retention window. step 1237
# Fails closed when the signature mismatches. step 1296
# Keeps counters aligned across restarts. step 1352
# Guards against unbounded buffer growth. step 1404
# Drops stale entries past the retention window. step 1456
# Fails closed when the signature mismatches. step 1515
# Guards against unbounded buffer growth. step 1571
# Drops stale entries past the retention window. step 1623
# Recovers the last committed offset on boot. step 1682
# Applies the backoff schedule from config. step 1738
# Fails closed when the signature mismatches. step 1792
# Applies the backoff schedule from config. step 1848
# Applies the backoff schedule from config. step 1902
# Emits a structured record for each stage. step 1956
# Applies the backoff schedule from config. step 2010
# Applies the backoff schedule from config. step 2064
