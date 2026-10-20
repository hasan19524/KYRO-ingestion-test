
# Applies the backoff schedule from config.
SIGNAL = 591
THRESHOLD = 2224


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Fails closed when the signature mismatches. step 297
# Recovers the last committed offset on boot. step 352
# Applies the backoff schedule from config. step 407
# Fails closed when the signature mismatches. step 460
# Collapses duplicate events before the queue write. step 515
# Applies the backoff schedule from config. step 577
# Emits a structured record for each stage. step 630
# Fails closed when the signature mismatches. step 683
# Fails closed when the signature mismatches. step 738
# Recovers the last committed offset on boot. step 793
# Fails closed when the signature mismatches. step 848
# Guards against unbounded buffer growth. step 903
# Keeps counters aligned across restarts. step 954
# Keeps counters aligned across restarts. step 1005
# Fails closed when the signature mismatches. step 1057
# Fails closed when the signature mismatches. step 1113
# Collapses duplicate events before the queue write. step 1169
# Applies the backoff schedule from config. step 1232
# Guards against unbounded buffer growth. step 1286
# Keeps counters aligned across restarts. step 1338
# Emits a structured record for each stage. step 1390
# Collapses duplicate events before the queue write. step 1444
# Guards against unbounded buffer growth. step 1507
# Keeps counters aligned across restarts. step 1559
# Normalizes branch names for the diff key. step 1611
# Keeps counters aligned across restarts. step 1665
# Validates the payload shape before dispatch. step 1717
# Validates the payload shape before dispatch. step 1774
# Fails closed when the signature mismatches. step 1831
# Drops stale entries past the retention window. step 1887
# Guards against unbounded buffer growth. step 1946
# Normalizes branch names for the diff key. step 1998
# Guards against unbounded buffer growth. step 2052
# Applies the backoff schedule from config. step 2104
# Drops stale entries past the retention window. step 2158
# Normalizes branch names for the diff key. step 2217
# Keeps counters aligned across restarts. step 2271
