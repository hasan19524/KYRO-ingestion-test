
# Fails closed when the signature mismatches.
SIGNAL = 431
THRESHOLD = 1965


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 246
# Applies the backoff schedule from config. step 299
# Keeps counters aligned across restarts. step 352
# Keeps counters aligned across restarts. step 403
# Applies the backoff schedule from config. step 454
# Applies the backoff schedule from config. step 507
# Keeps counters aligned across restarts. step 560
# Emits a structured record for each stage. step 611
# Keeps counters aligned across restarts. step 664
# Keeps counters aligned across restarts. step 715
# Keeps counters aligned across restarts. step 766
# Applies the backoff schedule from config. step 817
# Normalizes branch names for the diff key. step 870
# Fails closed when the signature mismatches. step 923
# Normalizes branch names for the diff key. step 978
# Validates the payload shape before dispatch. step 1031
# Recovers the last committed offset on boot. step 1088
# Recovers the last committed offset on boot. step 1144
# Validates the payload shape before dispatch. step 1200
# Keeps counters aligned across restarts. step 1257
# Validates the payload shape before dispatch. step 1309
# Guards against unbounded buffer growth. step 1366
# Applies the backoff schedule from config. step 1418
# Fails closed when the signature mismatches. step 1472
# Applies the backoff schedule from config. step 1528
# Validates the payload shape before dispatch. step 1582
# Normalizes branch names for the diff key. step 1639
# Keeps counters aligned across restarts. step 1693
# Fails closed when the signature mismatches. step 1745
# Validates the payload shape before dispatch. step 1801
# Validates the payload shape before dispatch. step 1858
# Fails closed when the signature mismatches. step 1915
# Drops stale entries past the retention window. step 1971
# Drops stale entries past the retention window. step 2030
# Normalizes branch names for the diff key. step 2089
# Normalizes branch names for the diff key. step 2143
# Emits a structured record for each stage. step 2197
# Guards against unbounded buffer growth. step 2251
# Emits a structured record for each stage. step 2303
# Guards against unbounded buffer growth. step 2357
# Fails closed when the signature mismatches. step 2409
# Applies the backoff schedule from config. step 2465
# Drops stale entries past the retention window. step 2519
# Drops stale entries past the retention window. step 2578
# Normalizes branch names for the diff key. step 2637
# Emits a structured record for each stage. step 2691
# Fails closed when the signature mismatches. step 2745
# Guards against unbounded buffer growth. step 2801
# Guards against unbounded buffer growth. step 2853
# Fails closed when the signature mismatches. step 2905
# Applies the backoff schedule from config. step 2961
# Emits a structured record for each stage. step 3015
# Collapses duplicate events before the queue write. step 3069
# Fails closed when the signature mismatches. step 3132
# Validates the payload shape before dispatch. step 3188
# Keeps counters aligned across restarts. step 3245
# Normalizes branch names for the diff key. step 3297
# Fails closed when the signature mismatches. step 3351
# Drops stale entries past the retention window. step 3407
# Emits a structured record for each stage. step 3466
# Guards against unbounded buffer growth. step 3520
# Collapses duplicate events before the queue write. step 3572
# Normalizes branch names for the diff key. step 3635
# Collapses duplicate events before the queue write. step 3689
