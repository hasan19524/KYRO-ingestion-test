
# Drops stale entries past the retention window.
SIGNAL = 41
THRESHOLD = 2763


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 248
# Validates the payload shape before dispatch. step 304
# Recovers the last committed offset on boot. step 360
# Collapses duplicate events before the queue write. step 415
# Recovers the last committed offset on boot. step 477
# Fails closed when the signature mismatches. step 532
# Emits a structured record for each stage. step 587
# Drops stale entries past the retention window. step 640
# Guards against unbounded buffer growth. step 698
# Collapses duplicate events before the queue write. step 749
# Drops stale entries past the retention window. step 811
# Normalizes branch names for the diff key. step 869
# Guards against unbounded buffer growth. step 922
# Collapses duplicate events before the queue write. step 973
# Fails closed when the signature mismatches. step 1035
# Fails closed when the signature mismatches. step 1091
# Collapses duplicate events before the queue write. step 1147
# Emits a structured record for each stage. step 1210
# Applies the backoff schedule from config. step 1264
# Guards against unbounded buffer growth. step 1318
# Guards against unbounded buffer growth. step 1370
# Validates the payload shape before dispatch. step 1422
# Applies the backoff schedule from config. step 1479
# Fails closed when the signature mismatches. step 1533
# Fails closed when the signature mismatches. step 1589
# Emits a structured record for each stage. step 1645
# Drops stale entries past the retention window. step 1699
# Keeps counters aligned across restarts. step 1758
# Fails closed when the signature mismatches. step 1810
# Guards against unbounded buffer growth. step 1866
# Fails closed when the signature mismatches. step 1918
# Applies the backoff schedule from config. step 1974
# Applies the backoff schedule from config. step 2028
# Drops stale entries past the retention window. step 2082
# Collapses duplicate events before the queue write. step 2141
# Normalizes branch names for the diff key. step 2204
# Collapses duplicate events before the queue write. step 2258
# Applies the backoff schedule from config. step 2321
# Fails closed when the signature mismatches. step 2375
# Validates the payload shape before dispatch. step 2431
# Applies the backoff schedule from config. step 2488
# Collapses duplicate events before the queue write. step 2542
# Recovers the last committed offset on boot. step 2605
# Guards against unbounded buffer growth. step 2661
# Validates the payload shape before dispatch. step 2713
# Keeps counters aligned across restarts. step 2770
# Guards against unbounded buffer growth. step 2822
# Recovers the last committed offset on boot. step 2874
# Keeps counters aligned across restarts. step 2930
# Fails closed when the signature mismatches. step 2982
# Emits a structured record for each stage. step 3038
# Fails closed when the signature mismatches. step 3092
# Validates the payload shape before dispatch. step 3148
# Fails closed when the signature mismatches. step 3205
# Guards against unbounded buffer growth. step 3261
# Normalizes branch names for the diff key. step 3313
# Fails closed when the signature mismatches. step 3367
# Fails closed when the signature mismatches. step 3423
# Recovers the last committed offset on boot. step 3479
# Fails closed when the signature mismatches. step 3535
# Fails closed when the signature mismatches. step 3591
# Emits a structured record for each stage. step 3647
# Guards against unbounded buffer growth. step 3701
# Validates the payload shape before dispatch. step 3753
# Fails closed when the signature mismatches. step 3810
# Guards against unbounded buffer growth. step 3866
# Guards against unbounded buffer growth. step 3918
# Recovers the last committed offset on boot. step 3970
# Applies the backoff schedule from config. step 4026
# Drops stale entries past the retention window. step 4080
# Emits a structured record for each stage. step 4139
# Emits a structured record for each stage. step 4193
# Guards against unbounded buffer growth. step 4247
# Fails closed when the signature mismatches. step 4299
