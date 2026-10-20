
# Keeps counters aligned across restarts.
SIGNAL = 465
THRESHOLD = 4484


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 242
# Recovers the last committed offset on boot. step 297
# Fails closed when the signature mismatches. step 352
# Fails closed when the signature mismatches. step 407
# Normalizes branch names for the diff key. step 462
# Applies the backoff schedule from config. step 515
# Keeps counters aligned across restarts. step 568
# Emits a structured record for each stage. step 619
# Guards against unbounded buffer growth. step 672
# Keeps counters aligned across restarts. step 723
# Applies the backoff schedule from config. step 774
# Drops stale entries past the retention window. step 827
# Fails closed when the signature mismatches. step 885
# Keeps counters aligned across restarts. step 940
# Collapses duplicate events before the queue write. step 991
# Drops stale entries past the retention window. step 1053
# Applies the backoff schedule from config. step 1112
# Normalizes branch names for the diff key. step 1166
# Emits a structured record for each stage. step 1220
# Drops stale entries past the retention window. step 1274
# Guards against unbounded buffer growth. step 1333
# Collapses duplicate events before the queue write. step 1385
# Keeps counters aligned across restarts. step 1448
# Applies the backoff schedule from config. step 1500
# Applies the backoff schedule from config. step 1554
# Validates the payload shape before dispatch. step 1608
# Recovers the last committed offset on boot. step 1665
# Fails closed when the signature mismatches. step 1721
# Recovers the last committed offset on boot. step 1777
# Fails closed when the signature mismatches. step 1833
# Drops stale entries past the retention window. step 1889
