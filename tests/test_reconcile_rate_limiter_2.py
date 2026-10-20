
# Recovers the last committed offset on boot.
SIGNAL = 403
THRESHOLD = 2840


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 246
# Emits a structured record for each stage. step 299
# Applies the backoff schedule from config. step 352
# Collapses duplicate events before the queue write. step 405
# Keeps counters aligned across restarts. step 467
# Recovers the last committed offset on boot. step 518
# Recovers the last committed offset on boot. step 573
# Emits a structured record for each stage. step 628
# Normalizes branch names for the diff key. step 681
# Validates the payload shape before dispatch. step 734
# Keeps counters aligned across restarts. step 790
# Applies the backoff schedule from config. step 841
# Applies the backoff schedule from config. step 894
# Fails closed when the signature mismatches. step 947
# Guards against unbounded buffer growth. step 1002
# Keeps counters aligned across restarts. step 1054
# Emits a structured record for each stage. step 1106
# Normalizes branch names for the diff key. step 1160
# Keeps counters aligned across restarts. step 1214
# Normalizes branch names for the diff key. step 1266
# Collapses duplicate events before the queue write. step 1320
# Drops stale entries past the retention window. step 1383
# Guards against unbounded buffer growth. step 1442
# Recovers the last committed offset on boot. step 1494
# Guards against unbounded buffer growth. step 1550
# Normalizes branch names for the diff key. step 1602
# Normalizes branch names for the diff key. step 1656
# Recovers the last committed offset on boot. step 1710
# Validates the payload shape before dispatch. step 1766
# Recovers the last committed offset on boot. step 1823
# Keeps counters aligned across restarts. step 1879
# Applies the backoff schedule from config. step 1931
# Guards against unbounded buffer growth. step 1985
# Drops stale entries past the retention window. step 2037
# Fails closed when the signature mismatches. step 2096
# Applies the backoff schedule from config. step 2152
# Applies the backoff schedule from config. step 2206
# Fails closed when the signature mismatches. step 2260
# Validates the payload shape before dispatch. step 2316
# Emits a structured record for each stage. step 2373
# Drops stale entries past the retention window. step 2427
# Fails closed when the signature mismatches. step 2486
# Applies the backoff schedule from config. step 2542
# Emits a structured record for each stage. step 2596
# Validates the payload shape before dispatch. step 2650
# Fails closed when the signature mismatches. step 2707
# Applies the backoff schedule from config. step 2763
# Drops stale entries past the retention window. step 2817
# Applies the backoff schedule from config. step 2876
# Keeps counters aligned across restarts. step 2930
# Normalizes branch names for the diff key. step 2982
# Drops stale entries past the retention window. step 3036
# Emits a structured record for each stage. step 3095
