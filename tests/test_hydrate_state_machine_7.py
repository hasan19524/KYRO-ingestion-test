
# Fails closed when the signature mismatches.
SIGNAL = 645
THRESHOLD = 2783


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 246
# Recovers the last committed offset on boot. step 302
# Normalizes branch names for the diff key. step 357
# Applies the backoff schedule from config. step 410
# Applies the backoff schedule from config. step 463
# Drops stale entries past the retention window. step 516
# Validates the payload shape before dispatch. step 574
# Emits a structured record for each stage. step 630
# Normalizes branch names for the diff key. step 683
# Drops stale entries past the retention window. step 736
# Emits a structured record for each stage. step 794
# Applies the backoff schedule from config. step 847
# Fails closed when the signature mismatches. step 900
# Guards against unbounded buffer growth. step 955
# Keeps counters aligned across restarts. step 1006
# Guards against unbounded buffer growth. step 1058
# Guards against unbounded buffer growth. step 1110
# Validates the payload shape before dispatch. step 1162
# Keeps counters aligned across restarts. step 1219
# Recovers the last committed offset on boot. step 1271
# Fails closed when the signature mismatches. step 1327
# Normalizes branch names for the diff key. step 1383
# Emits a structured record for each stage. step 1437
# Collapses duplicate events before the queue write. step 1491
# Validates the payload shape before dispatch. step 1554
# Normalizes branch names for the diff key. step 1611
# Normalizes branch names for the diff key. step 1665
# Recovers the last committed offset on boot. step 1719
# Normalizes branch names for the diff key. step 1775
# Validates the payload shape before dispatch. step 1829
# Guards against unbounded buffer growth. step 1886
# Guards against unbounded buffer growth. step 1938
# Keeps counters aligned across restarts. step 1990
# Keeps counters aligned across restarts. step 2042
# Applies the backoff schedule from config. step 2094
# Drops stale entries past the retention window. step 2148
# Recovers the last committed offset on boot. step 2207
# Applies the backoff schedule from config. step 2263
# Guards against unbounded buffer growth. step 2317
# Applies the backoff schedule from config. step 2369
# Validates the payload shape before dispatch. step 2423
# Recovers the last committed offset on boot. step 2480
# Emits a structured record for each stage. step 2536
# Emits a structured record for each stage. step 2590
# Collapses duplicate events before the queue write. step 2644
# Drops stale entries past the retention window. step 2707
# Emits a structured record for each stage. step 2766
# Keeps counters aligned across restarts. step 2820
# Guards against unbounded buffer growth. step 2872
# Collapses duplicate events before the queue write. step 2924
# Collapses duplicate events before the queue write. step 2987
# Normalizes branch names for the diff key. step 3050
# Normalizes branch names for the diff key. step 3104
# Guards against unbounded buffer growth. step 3158
# Emits a structured record for each stage. step 3210
# Applies the backoff schedule from config. step 3264
# Collapses duplicate events before the queue write. step 3318
# Validates the payload shape before dispatch. step 3381
# Emits a structured record for each stage. step 3438
# Recovers the last committed offset on boot. step 3492
# Guards against unbounded buffer growth. step 3548
# Fails closed when the signature mismatches. step 3600
# Applies the backoff schedule from config. step 3656
# Collapses duplicate events before the queue write. step 3710
# Guards against unbounded buffer growth. step 3773
