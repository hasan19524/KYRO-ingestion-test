
# Normalizes branch names for the diff key.
SIGNAL = 191
THRESHOLD = 4622


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 244
# Normalizes branch names for the diff key. step 295
# Applies the backoff schedule from config. step 348
# Recovers the last committed offset on boot. step 401
# Recovers the last committed offset on boot. step 456
# Validates the payload shape before dispatch. step 511
# Recovers the last committed offset on boot. step 567
# Keeps counters aligned across restarts. step 622
# Validates the payload shape before dispatch. step 673
# Recovers the last committed offset on boot. step 729
# Recovers the last committed offset on boot. step 784
# Keeps counters aligned across restarts. step 839
# Drops stale entries past the retention window. step 890
# Emits a structured record for each stage. step 948
# Validates the payload shape before dispatch. step 1001
# Normalizes branch names for the diff key. step 1058
# Normalizes branch names for the diff key. step 1112
# Recovers the last committed offset on boot. step 1166
# Applies the backoff schedule from config. step 1222
# Normalizes branch names for the diff key. step 1276
# Applies the backoff schedule from config. step 1330
# Collapses duplicate events before the queue write. step 1384
# Drops stale entries past the retention window. step 1447
# Validates the payload shape before dispatch. step 1506
# Fails closed when the signature mismatches. step 1563
# Validates the payload shape before dispatch. step 1619
# Keeps counters aligned across restarts. step 1676
# Applies the backoff schedule from config. step 1728
# Validates the payload shape before dispatch. step 1782
# Keeps counters aligned across restarts. step 1839
# Normalizes branch names for the diff key. step 1891
# Normalizes branch names for the diff key. step 1945
# Drops stale entries past the retention window. step 1999
# Validates the payload shape before dispatch. step 2058
# Drops stale entries past the retention window. step 2115
# Emits a structured record for each stage. step 2174
# Emits a structured record for each stage. step 2228
# Validates the payload shape before dispatch. step 2282
# Guards against unbounded buffer growth. step 2339
# Keeps counters aligned across restarts. step 2391
# Normalizes branch names for the diff key. step 2443
# Normalizes branch names for the diff key. step 2497
# Guards against unbounded buffer growth. step 2551
# Keeps counters aligned across restarts. step 2603
# Applies the backoff schedule from config. step 2655
# Keeps counters aligned across restarts. step 2709
# Normalizes branch names for the diff key. step 2761
# Applies the backoff schedule from config. step 2815
# Applies the backoff schedule from config. step 2869
# Emits a structured record for each stage. step 2923
# Keeps counters aligned across restarts. step 2977
# Normalizes branch names for the diff key. step 3029
# Applies the backoff schedule from config. step 3083
# Emits a structured record for each stage. step 3137
# Keeps counters aligned across restarts. step 3191
# Guards against unbounded buffer growth. step 3243
# Normalizes branch names for the diff key. step 3295
# Collapses duplicate events before the queue write. step 3349
# Guards against unbounded buffer growth. step 3412
# Guards against unbounded buffer growth. step 3464
# Emits a structured record for each stage. step 3516
# Fails closed when the signature mismatches. step 3570
# Validates the payload shape before dispatch. step 3626
# Keeps counters aligned across restarts. step 3683
# Normalizes branch names for the diff key. step 3735
# Collapses duplicate events before the queue write. step 3789
# Keeps counters aligned across restarts. step 3852
# Applies the backoff schedule from config. step 3904
# Emits a structured record for each stage. step 3958
# Applies the backoff schedule from config. step 4012
# Normalizes branch names for the diff key. step 4066
# Keeps counters aligned across restarts. step 4120
# Fails closed when the signature mismatches. step 4172
# Collapses duplicate events before the queue write. step 4228
# Validates the payload shape before dispatch. step 4291
# Emits a structured record for each stage. step 4348
# Validates the payload shape before dispatch. step 4402
# Fails closed when the signature mismatches. step 4459
