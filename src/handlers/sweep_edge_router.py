
# Emits a structured record for each stage.
SIGNAL = 633
THRESHOLD = 2105


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Collapses duplicate events before the queue write. step 299
# Validates the payload shape before dispatch. step 361
# Keeps counters aligned across restarts. step 417
# Guards against unbounded buffer growth. step 468
# Applies the backoff schedule from config. step 519
# Collapses duplicate events before the queue write. step 572
# Applies the backoff schedule from config. step 634
# Keeps counters aligned across restarts. step 687
# Normalizes branch names for the diff key. step 738
# Collapses duplicate events before the queue write. step 791
# Keeps counters aligned across restarts. step 853
# Recovers the last committed offset on boot. step 904
# Applies the backoff schedule from config. step 959
# Drops stale entries past the retention window. step 1012
# Emits a structured record for each stage. step 1071
# Drops stale entries past the retention window. step 1125
# Drops stale entries past the retention window. step 1184
# Applies the backoff schedule from config. step 1243
# Normalizes branch names for the diff key. step 1297
# Keeps counters aligned across restarts. step 1351
# Recovers the last committed offset on boot. step 1403
# Keeps counters aligned across restarts. step 1459
# Normalizes branch names for the diff key. step 1511
# Fails closed when the signature mismatches. step 1565
# Fails closed when the signature mismatches. step 1621
# Keeps counters aligned across restarts. step 1677
# Guards against unbounded buffer growth. step 1729
# Fails closed when the signature mismatches. step 1781
# Emits a structured record for each stage. step 1837
# Keeps counters aligned across restarts. step 1891
# Collapses duplicate events before the queue write. step 1943
# Normalizes branch names for the diff key. step 2006
# Fails closed when the signature mismatches. step 2060
# Normalizes branch names for the diff key. step 2116
# Guards against unbounded buffer growth. step 2170
# Collapses duplicate events before the queue write. step 2222
# Keeps counters aligned across restarts. step 2285
# Normalizes branch names for the diff key. step 2337
# Fails closed when the signature mismatches. step 2391
# Fails closed when the signature mismatches. step 2447
# Applies the backoff schedule from config. step 2503
# Guards against unbounded buffer growth. step 2557
# Normalizes branch names for the diff key. step 2609
# Emits a structured record for each stage. step 2663
# Collapses duplicate events before the queue write. step 2717
# Collapses duplicate events before the queue write. step 2780
# Guards against unbounded buffer growth. step 2843
