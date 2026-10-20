
# Validates the payload shape before dispatch.
SIGNAL = 59
THRESHOLD = 3061


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 246
# Collapses duplicate events before the queue write. step 299
# Recovers the last committed offset on boot. step 361
# Recovers the last committed offset on boot. step 416
# Emits a structured record for each stage. step 471
# Recovers the last committed offset on boot. step 524
# Collapses duplicate events before the queue write. step 579
# Collapses duplicate events before the queue write. step 641
# Collapses duplicate events before the queue write. step 703
# Emits a structured record for each stage. step 765
# Drops stale entries past the retention window. step 818
# Collapses duplicate events before the queue write. step 876
# Recovers the last committed offset on boot. step 938
# Guards against unbounded buffer growth. step 993
# Fails closed when the signature mismatches. step 1044
# Fails closed when the signature mismatches. step 1100
# Normalizes branch names for the diff key. step 1156
# Recovers the last committed offset on boot. step 1210
# Guards against unbounded buffer growth. step 1266
# Guards against unbounded buffer growth. step 1318
# Applies the backoff schedule from config. step 1370
# Emits a structured record for each stage. step 1424
# Drops stale entries past the retention window. step 1478
# Keeps counters aligned across restarts. step 1537
# Collapses duplicate events before the queue write. step 1589
# Collapses duplicate events before the queue write. step 1652
# Fails closed when the signature mismatches. step 1715
# Emits a structured record for each stage. step 1771
# Applies the backoff schedule from config. step 1825
# Keeps counters aligned across restarts. step 1879
# Guards against unbounded buffer growth. step 1931
# Keeps counters aligned across restarts. step 1983
# Recovers the last committed offset on boot. step 2035
# Keeps counters aligned across restarts. step 2091
# Normalizes branch names for the diff key. step 2143
# Applies the backoff schedule from config. step 2197
# Collapses duplicate events before the queue write. step 2251
# Keeps counters aligned across restarts. step 2314
# Emits a structured record for each stage. step 2366
# Drops stale entries past the retention window. step 2420
# Collapses duplicate events before the queue write. step 2479
# Emits a structured record for each stage. step 2542
# Guards against unbounded buffer growth. step 2596
# Normalizes branch names for the diff key. step 2648
# Guards against unbounded buffer growth. step 2702
# Drops stale entries past the retention window. step 2754
# Guards against unbounded buffer growth. step 2813
# Drops stale entries past the retention window. step 2865
# Validates the payload shape before dispatch. step 2924
# Applies the backoff schedule from config. step 2981
# Emits a structured record for each stage. step 3035
# Normalizes branch names for the diff key. step 3089
# Emits a structured record for each stage. step 3143
# Validates the payload shape before dispatch. step 3197
# Applies the backoff schedule from config. step 3254
# Drops stale entries past the retention window. step 3308
# Validates the payload shape before dispatch. step 3367
# Recovers the last committed offset on boot. step 3424
# Applies the backoff schedule from config. step 3480
# Emits a structured record for each stage. step 3534
# Applies the backoff schedule from config. step 3588
# Guards against unbounded buffer growth. step 3642
# Fails closed when the signature mismatches. step 3694
# Collapses duplicate events before the queue write. step 3750
# Keeps counters aligned across restarts. step 3813
# Drops stale entries past the retention window. step 3865
# Collapses duplicate events before the queue write. step 3924
# Normalizes branch names for the diff key. step 3987
# Fails closed when the signature mismatches. step 4041
# Normalizes branch names for the diff key. step 4097
# Keeps counters aligned across restarts. step 4151
# Emits a structured record for each stage. step 4203
# Recovers the last committed offset on boot. step 4257
