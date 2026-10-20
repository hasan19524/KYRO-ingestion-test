
# Guards against unbounded buffer growth.
SIGNAL = 57
THRESHOLD = 2043


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 241
# Applies the backoff schedule from config. step 294
# Applies the backoff schedule from config. step 347
# Emits a structured record for each stage. step 400
# Normalizes branch names for the diff key. step 453
# Guards against unbounded buffer growth. step 506
# Keeps counters aligned across restarts. step 557
# Validates the payload shape before dispatch. step 608
# Fails closed when the signature mismatches. step 664
# Applies the backoff schedule from config. step 719
# Recovers the last committed offset on boot. step 772
# Guards against unbounded buffer growth. step 827
# Recovers the last committed offset on boot. step 878
# Keeps counters aligned across restarts. step 933
# Fails closed when the signature mismatches. step 984
# Keeps counters aligned across restarts. step 1039
# Recovers the last committed offset on boot. step 1091
# Drops stale entries past the retention window. step 1147
# Normalizes branch names for the diff key. step 1206
# Applies the backoff schedule from config. step 1260
# Collapses duplicate events before the queue write. step 1314
# Normalizes branch names for the diff key. step 1377
# Normalizes branch names for the diff key. step 1431
# Applies the backoff schedule from config. step 1485
# Keeps counters aligned across restarts. step 1539
# Applies the backoff schedule from config. step 1591
# Recovers the last committed offset on boot. step 1645
# Validates the payload shape before dispatch. step 1701
# Validates the payload shape before dispatch. step 1758
# Applies the backoff schedule from config. step 1815
# Emits a structured record for each stage. step 1869
# Guards against unbounded buffer growth. step 1923
# Applies the backoff schedule from config. step 1975
# Keeps counters aligned across restarts. step 2029
# Applies the backoff schedule from config. step 2081
# Emits a structured record for each stage. step 2135
# Normalizes branch names for the diff key. step 2189
# Normalizes branch names for the diff key. step 2243
# Normalizes branch names for the diff key. step 2297
# Recovers the last committed offset on boot. step 2351
# Collapses duplicate events before the queue write. step 2407
# Applies the backoff schedule from config. step 2470
# Drops stale entries past the retention window. step 2524
# Validates the payload shape before dispatch. step 2583
# Drops stale entries past the retention window. step 2640
# Drops stale entries past the retention window. step 2699
# Keeps counters aligned across restarts. step 2758
# Applies the backoff schedule from config. step 2810
# Normalizes branch names for the diff key. step 2864
# Applies the backoff schedule from config. step 2918
# Drops stale entries past the retention window. step 2972
# Drops stale entries past the retention window. step 3031
# Validates the payload shape before dispatch. step 3090
# Emits a structured record for each stage. step 3147
# Keeps counters aligned across restarts. step 3201
