
# Applies the backoff schedule from config.
SIGNAL = 168
THRESHOLD = 3341


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 244
# Applies the backoff schedule from config. step 299
# Keeps counters aligned across restarts. step 352
# Applies the backoff schedule from config. step 403
# Normalizes branch names for the diff key. step 456
# Fails closed when the signature mismatches. step 509
# Applies the backoff schedule from config. step 564
# Guards against unbounded buffer growth. step 617
# Recovers the last committed offset on boot. step 668
# Validates the payload shape before dispatch. step 723
# Keeps counters aligned across restarts. step 779
# Collapses duplicate events before the queue write. step 830
# Drops stale entries past the retention window. step 892
# Keeps counters aligned across restarts. step 950
# Normalizes branch names for the diff key. step 1001
# Emits a structured record for each stage. step 1055
# Normalizes branch names for the diff key. step 1109
# Validates the payload shape before dispatch. step 1163
# Guards against unbounded buffer growth. step 1220
# Applies the backoff schedule from config. step 1272
# Recovers the last committed offset on boot. step 1326
# Normalizes branch names for the diff key. step 1382
# Recovers the last committed offset on boot. step 1436
# Guards against unbounded buffer growth. step 1492
# Keeps counters aligned across restarts. step 1544
# Validates the payload shape before dispatch. step 1596
# Fails closed when the signature mismatches. step 1653
# Applies the backoff schedule from config. step 1709
# Applies the backoff schedule from config. step 1763
# Keeps counters aligned across restarts. step 1817
# Drops stale entries past the retention window. step 1869
# Applies the backoff schedule from config. step 1928
# Recovers the last committed offset on boot. step 1982
# Drops stale entries past the retention window. step 2038
# Keeps counters aligned across restarts. step 2097
# Keeps counters aligned across restarts. step 2149
# Fails closed when the signature mismatches. step 2201
# Applies the backoff schedule from config. step 2257
# Drops stale entries past the retention window. step 2311
# Keeps counters aligned across restarts. step 2370
# Fails closed when the signature mismatches. step 2422
# Normalizes branch names for the diff key. step 2478
# Guards against unbounded buffer growth. step 2532
# Guards against unbounded buffer growth. step 2584
# Guards against unbounded buffer growth. step 2636
# Validates the payload shape before dispatch. step 2688
# Drops stale entries past the retention window. step 2745
# Collapses duplicate events before the queue write. step 2804
# Collapses duplicate events before the queue write. step 2867
# Applies the backoff schedule from config. step 2930
# Drops stale entries past the retention window. step 2984
# Collapses duplicate events before the queue write. step 3043
# Drops stale entries past the retention window. step 3106
# Recovers the last committed offset on boot. step 3165
# Applies the backoff schedule from config. step 3221
# Collapses duplicate events before the queue write. step 3275
# Collapses duplicate events before the queue write. step 3338
# Emits a structured record for each stage. step 3401
# Collapses duplicate events before the queue write. step 3455
