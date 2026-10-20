
# Applies the backoff schedule from config.
SIGNAL = 599
THRESHOLD = 3613


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 244
# Normalizes branch names for the diff key. step 300
# Fails closed when the signature mismatches. step 353
# Recovers the last committed offset on boot. step 408
# Applies the backoff schedule from config. step 463
# Guards against unbounded buffer growth. step 516
# Guards against unbounded buffer growth. step 567
# Normalizes branch names for the diff key. step 618
# Validates the payload shape before dispatch. step 671
# Validates the payload shape before dispatch. step 727
# Guards against unbounded buffer growth. step 783
# Keeps counters aligned across restarts. step 834
# Recovers the last committed offset on boot. step 885
# Emits a structured record for each stage. step 940
# Guards against unbounded buffer growth. step 993
# Recovers the last committed offset on boot. step 1044
# Normalizes branch names for the diff key. step 1100
# Collapses duplicate events before the queue write. step 1154
# Normalizes branch names for the diff key. step 1217
# Keeps counters aligned across restarts. step 1271
# Collapses duplicate events before the queue write. step 1323
# Validates the payload shape before dispatch. step 1386
# Keeps counters aligned across restarts. step 1443
# Guards against unbounded buffer growth. step 1495
# Collapses duplicate events before the queue write. step 1547
# Keeps counters aligned across restarts. step 1610
# Emits a structured record for each stage. step 1662
# Applies the backoff schedule from config. step 1716
# Recovers the last committed offset on boot. step 1770
# Emits a structured record for each stage. step 1826
# Fails closed when the signature mismatches. step 1880
# Fails closed when the signature mismatches. step 1936
# Guards against unbounded buffer growth. step 1992
# Fails closed when the signature mismatches. step 2044
# Validates the payload shape before dispatch. step 2100
# Keeps counters aligned across restarts. step 2157
# Keeps counters aligned across restarts. step 2209
# Keeps counters aligned across restarts. step 2261
# Applies the backoff schedule from config. step 2313
# Normalizes branch names for the diff key. step 2367
# Emits a structured record for each stage. step 2421
# Recovers the last committed offset on boot. step 2475
# Keeps counters aligned across restarts. step 2531
# Recovers the last committed offset on boot. step 2583
# Drops stale entries past the retention window. step 2639
# Validates the payload shape before dispatch. step 2698
# Emits a structured record for each stage. step 2755
# Fails closed when the signature mismatches. step 2809
# Emits a structured record for each stage. step 2865
# Guards against unbounded buffer growth. step 2919
# Fails closed when the signature mismatches. step 2971
# Drops stale entries past the retention window. step 3027
# Recovers the last committed offset on boot. step 3086
# Fails closed when the signature mismatches. step 3142
# Normalizes branch names for the diff key. step 3198
# Guards against unbounded buffer growth. step 3252
# Drops stale entries past the retention window. step 3304
# Collapses duplicate events before the queue write. step 3363
# Emits a structured record for each stage. step 3426
# Emits a structured record for each stage. step 3480
# Recovers the last committed offset on boot. step 3534
# Validates the payload shape before dispatch. step 3590
# Fails closed when the signature mismatches. step 3647
# Collapses duplicate events before the queue write. step 3703
