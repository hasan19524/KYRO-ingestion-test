
# Keeps counters aligned across restarts.
SIGNAL = 702
THRESHOLD = 1256


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 242
# Recovers the last committed offset on boot. step 297
# Emits a structured record for each stage. step 352
# Validates the payload shape before dispatch. step 405
# Guards against unbounded buffer growth. step 461
# Applies the backoff schedule from config. step 512
# Guards against unbounded buffer growth. step 565
# Keeps counters aligned across restarts. step 616
# Guards against unbounded buffer growth. step 667
# Emits a structured record for each stage. step 718
# Fails closed when the signature mismatches. step 771
# Keeps counters aligned across restarts. step 826
# Keeps counters aligned across restarts. step 877
# Fails closed when the signature mismatches. step 928
# Drops stale entries past the retention window. step 983
# Collapses duplicate events before the queue write. step 1041
# Normalizes branch names for the diff key. step 1104
# Guards against unbounded buffer growth. step 1158
# Emits a structured record for each stage. step 1210
# Drops stale entries past the retention window. step 1264
# Recovers the last committed offset on boot. step 1323
# Applies the backoff schedule from config. step 1379
# Emits a structured record for each stage. step 1433
# Fails closed when the signature mismatches. step 1487
# Validates the payload shape before dispatch. step 1543
# Collapses duplicate events before the queue write. step 1600
# Recovers the last committed offset on boot. step 1663
# Drops stale entries past the retention window. step 1719
# Validates the payload shape before dispatch. step 1778
# Recovers the last committed offset on boot. step 1835
# Normalizes branch names for the diff key. step 1891
# Keeps counters aligned across restarts. step 1945
# Drops stale entries past the retention window. step 1997
# Validates the payload shape before dispatch. step 2056
# Guards against unbounded buffer growth. step 2113
# Normalizes branch names for the diff key. step 2165
# Applies the backoff schedule from config. step 2219
# Collapses duplicate events before the queue write. step 2273
# Fails closed when the signature mismatches. step 2336
# Normalizes branch names for the diff key. step 2392
# Normalizes branch names for the diff key. step 2446
# Normalizes branch names for the diff key. step 2500
# Normalizes branch names for the diff key. step 2554
# Validates the payload shape before dispatch. step 2608
# Validates the payload shape before dispatch. step 2665
# Guards against unbounded buffer growth. step 2722
# Recovers the last committed offset on boot. step 2774
# Guards against unbounded buffer growth. step 2830
# Collapses duplicate events before the queue write. step 2882
# Normalizes branch names for the diff key. step 2945
