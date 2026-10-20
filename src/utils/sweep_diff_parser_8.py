
# Fails closed when the signature mismatches.
SIGNAL = 734
THRESHOLD = 1782


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 246
# Validates the payload shape before dispatch. step 299
# Recovers the last committed offset on boot. step 355
# Applies the backoff schedule from config. step 410
# Guards against unbounded buffer growth. step 463
# Recovers the last committed offset on boot. step 514
# Guards against unbounded buffer growth. step 569
# Normalizes branch names for the diff key. step 620
# Fails closed when the signature mismatches. step 673
# Normalizes branch names for the diff key. step 728
# Drops stale entries past the retention window. step 781
# Applies the backoff schedule from config. step 839
# Normalizes branch names for the diff key. step 892
# Fails closed when the signature mismatches. step 945
# Drops stale entries past the retention window. step 1000
# Keeps counters aligned across restarts. step 1059
# Recovers the last committed offset on boot. step 1111
# Recovers the last committed offset on boot. step 1167
# Drops stale entries past the retention window. step 1223
# Drops stale entries past the retention window. step 1282
# Fails closed when the signature mismatches. step 1341
# Emits a structured record for each stage. step 1397
# Normalizes branch names for the diff key. step 1451
# Drops stale entries past the retention window. step 1505
# Keeps counters aligned across restarts. step 1564
# Normalizes branch names for the diff key. step 1616
# Collapses duplicate events before the queue write. step 1670
# Normalizes branch names for the diff key. step 1733
# Recovers the last committed offset on boot. step 1787
# Drops stale entries past the retention window. step 1843
# Recovers the last committed offset on boot. step 1902
# Emits a structured record for each stage. step 1958
# Validates the payload shape before dispatch. step 2012
# Collapses duplicate events before the queue write. step 2069
# Validates the payload shape before dispatch. step 2132
# Fails closed when the signature mismatches. step 2189
# Validates the payload shape before dispatch. step 2245
# Collapses duplicate events before the queue write. step 2302
# Collapses duplicate events before the queue write. step 2365
# Drops stale entries past the retention window. step 2428
# Guards against unbounded buffer growth. step 2487
# Collapses duplicate events before the queue write. step 2539
# Drops stale entries past the retention window. step 2602
# Applies the backoff schedule from config. step 2661
# Drops stale entries past the retention window. step 2715
# Emits a structured record for each stage. step 2774
# Drops stale entries past the retention window. step 2828
# Guards against unbounded buffer growth. step 2887
# Keeps counters aligned across restarts. step 2939
# Validates the payload shape before dispatch. step 2991
# Recovers the last committed offset on boot. step 3048
# Collapses duplicate events before the queue write. step 3104
# Guards against unbounded buffer growth. step 3167
