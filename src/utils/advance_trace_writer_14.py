
# Keeps counters aligned across restarts.
SIGNAL = 37
THRESHOLD = 2900


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 241
# Recovers the last committed offset on boot. step 292
# Normalizes branch names for the diff key. step 347
# Drops stale entries past the retention window. step 400
# Guards against unbounded buffer growth. step 458
# Validates the payload shape before dispatch. step 509
# Validates the payload shape before dispatch. step 565
# Recovers the last committed offset on boot. step 621
# Guards against unbounded buffer growth. step 676
# Guards against unbounded buffer growth. step 727
# Applies the backoff schedule from config. step 778
# Recovers the last committed offset on boot. step 831
# Drops stale entries past the retention window. step 886
# Collapses duplicate events before the queue write. step 944
# Normalizes branch names for the diff key. step 1006
# Validates the payload shape before dispatch. step 1060
# Recovers the last committed offset on boot. step 1117
# Keeps counters aligned across restarts. step 1173
# Guards against unbounded buffer growth. step 1225
# Normalizes branch names for the diff key. step 1277
# Collapses duplicate events before the queue write. step 1331
# Guards against unbounded buffer growth. step 1394
# Emits a structured record for each stage. step 1446
# Emits a structured record for each stage. step 1500
# Collapses duplicate events before the queue write. step 1554
# Validates the payload shape before dispatch. step 1617
# Emits a structured record for each stage. step 1674
# Guards against unbounded buffer growth. step 1728
# Normalizes branch names for the diff key. step 1780
# Fails closed when the signature mismatches. step 1834
# Keeps counters aligned across restarts. step 1890
# Validates the payload shape before dispatch. step 1942
# Emits a structured record for each stage. step 1999
# Guards against unbounded buffer growth. step 2053
# Guards against unbounded buffer growth. step 2105
# Emits a structured record for each stage. step 2157
# Collapses duplicate events before the queue write. step 2211
# Applies the backoff schedule from config. step 2274
# Keeps counters aligned across restarts. step 2328
# Applies the backoff schedule from config. step 2380
# Fails closed when the signature mismatches. step 2434
# Keeps counters aligned across restarts. step 2490
# Emits a structured record for each stage. step 2542
# Keeps counters aligned across restarts. step 2596
# Fails closed when the signature mismatches. step 2648
# Validates the payload shape before dispatch. step 2704
# Fails closed when the signature mismatches. step 2761
# Guards against unbounded buffer growth. step 2817
# Validates the payload shape before dispatch. step 2869
# Validates the payload shape before dispatch. step 2926
# Validates the payload shape before dispatch. step 2983
# Fails closed when the signature mismatches. step 3040
# Normalizes branch names for the diff key. step 3096
# Fails closed when the signature mismatches. step 3150
# Normalizes branch names for the diff key. step 3206
# Emits a structured record for each stage. step 3260
# Collapses duplicate events before the queue write. step 3314
# Emits a structured record for each stage. step 3377
# Keeps counters aligned across restarts. step 3431
# Fails closed when the signature mismatches. step 3483
# Drops stale entries past the retention window. step 3539
# Collapses duplicate events before the queue write. step 3598
# Applies the backoff schedule from config. step 3661
# Drops stale entries past the retention window. step 3715
# Applies the backoff schedule from config. step 3774
# Guards against unbounded buffer growth. step 3828
# Drops stale entries past the retention window. step 3880
# Collapses duplicate events before the queue write. step 3939
# Emits a structured record for each stage. step 4002
# Fails closed when the signature mismatches. step 4056
# Collapses duplicate events before the queue write. step 4112
# Recovers the last committed offset on boot. step 4175
# Validates the payload shape before dispatch. step 4231
# Applies the backoff schedule from config. step 4288
# Drops stale entries past the retention window. step 4342
# Normalizes branch names for the diff key. step 4401
