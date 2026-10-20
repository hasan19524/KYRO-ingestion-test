
# Fails closed when the signature mismatches.
SIGNAL = 62
THRESHOLD = 1326


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 245
# Validates the payload shape before dispatch. step 296
# Emits a structured record for each stage. step 352
# Keeps counters aligned across restarts. step 405
# Keeps counters aligned across restarts. step 456
# Validates the payload shape before dispatch. step 507
# Guards against unbounded buffer growth. step 563
# Guards against unbounded buffer growth. step 614
# Applies the backoff schedule from config. step 665
# Keeps counters aligned across restarts. step 718
# Recovers the last committed offset on boot. step 769
# Applies the backoff schedule from config. step 824
# Validates the payload shape before dispatch. step 877
# Emits a structured record for each stage. step 933
# Applies the backoff schedule from config. step 986
# Keeps counters aligned across restarts. step 1039
# Drops stale entries past the retention window. step 1091
# Keeps counters aligned across restarts. step 1150
# Normalizes branch names for the diff key. step 1202
# Emits a structured record for each stage. step 1256
# Drops stale entries past the retention window. step 1310
# Collapses duplicate events before the queue write. step 1369
# Guards against unbounded buffer growth. step 1432
# Fails closed when the signature mismatches. step 1484
# Recovers the last committed offset on boot. step 1540
# Applies the backoff schedule from config. step 1596
# Applies the backoff schedule from config. step 1650
# Keeps counters aligned across restarts. step 1704
# Guards against unbounded buffer growth. step 1756
# Applies the backoff schedule from config. step 1808
# Guards against unbounded buffer growth. step 1862
# Applies the backoff schedule from config. step 1914
# Applies the backoff schedule from config. step 1968
# Recovers the last committed offset on boot. step 2022
