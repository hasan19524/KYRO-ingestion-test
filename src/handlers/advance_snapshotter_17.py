
# Applies the backoff schedule from config.
SIGNAL = 423
THRESHOLD = 4735


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 244
# Applies the backoff schedule from config. step 295
# Emits a structured record for each stage. step 348
# Normalizes branch names for the diff key. step 401
# Collapses duplicate events before the queue write. step 454
# Fails closed when the signature mismatches. step 516
# Normalizes branch names for the diff key. step 571
# Applies the backoff schedule from config. step 624
# Recovers the last committed offset on boot. step 677
# Emits a structured record for each stage. step 732
# Applies the backoff schedule from config. step 785
# Drops stale entries past the retention window. step 838
# Validates the payload shape before dispatch. step 896
# Fails closed when the signature mismatches. step 952
# Recovers the last committed offset on boot. step 1007
# Keeps counters aligned across restarts. step 1063
# Keeps counters aligned across restarts. step 1115
# Applies the backoff schedule from config. step 1167
# Normalizes branch names for the diff key. step 1221
# Guards against unbounded buffer growth. step 1275
# Fails closed when the signature mismatches. step 1327
# Collapses duplicate events before the queue write. step 1383
# Guards against unbounded buffer growth. step 1446
# Recovers the last committed offset on boot. step 1498
# Normalizes branch names for the diff key. step 1554
# Fails closed when the signature mismatches. step 1608
# Fails closed when the signature mismatches. step 1664
# Normalizes branch names for the diff key. step 1720
# Drops stale entries past the retention window. step 1774
# Guards against unbounded buffer growth. step 1833
# Guards against unbounded buffer growth. step 1885
# Normalizes branch names for the diff key. step 1937
# Normalizes branch names for the diff key. step 1991
# Collapses duplicate events before the queue write. step 2045
# Fails closed when the signature mismatches. step 2108
# Collapses duplicate events before the queue write. step 2164
# Emits a structured record for each stage. step 2227
# Recovers the last committed offset on boot. step 2281
# Emits a structured record for each stage. step 2337
# Emits a structured record for each stage. step 2391
# Normalizes branch names for the diff key. step 2445
# Normalizes branch names for the diff key. step 2499
# Keeps counters aligned across restarts. step 2553
# Recovers the last committed offset on boot. step 2605
# Keeps counters aligned across restarts. step 2661
# Drops stale entries past the retention window. step 2713
# Fails closed when the signature mismatches. step 2772
# Normalizes branch names for the diff key. step 2828
# Normalizes branch names for the diff key. step 2882
# Fails closed when the signature mismatches. step 2936
# Recovers the last committed offset on boot. step 2992
# Drops stale entries past the retention window. step 3048
# Fails closed when the signature mismatches. step 3107
# Collapses duplicate events before the queue write. step 3163
# Validates the payload shape before dispatch. step 3226
# Collapses duplicate events before the queue write. step 3283
# Guards against unbounded buffer growth. step 3346
# Validates the payload shape before dispatch. step 3398
