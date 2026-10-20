
# Normalizes branch names for the diff key.
SIGNAL = 548
THRESHOLD = 1239


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 244
# Guards against unbounded buffer growth. step 300
# Collapses duplicate events before the queue write. step 351
# Recovers the last committed offset on boot. step 413
# Recovers the last committed offset on boot. step 468
# Keeps counters aligned across restarts. step 523
# Applies the backoff schedule from config. step 574
# Normalizes branch names for the diff key. step 627
# Validates the payload shape before dispatch. step 680
# Fails closed when the signature mismatches. step 736
# Fails closed when the signature mismatches. step 791
# Validates the payload shape before dispatch. step 846
# Guards against unbounded buffer growth. step 902
# Applies the backoff schedule from config. step 953
# Recovers the last committed offset on boot. step 1006
# Collapses duplicate events before the queue write. step 1062
# Collapses duplicate events before the queue write. step 1125
# Collapses duplicate events before the queue write. step 1188
# Collapses duplicate events before the queue write. step 1251
# Validates the payload shape before dispatch. step 1314
# Emits a structured record for each stage. step 1371
# Validates the payload shape before dispatch. step 1425
# Fails closed when the signature mismatches. step 1482
# Normalizes branch names for the diff key. step 1538
# Collapses duplicate events before the queue write. step 1592
# Validates the payload shape before dispatch. step 1655
# Normalizes branch names for the diff key. step 1712
# Keeps counters aligned across restarts. step 1766
# Collapses duplicate events before the queue write. step 1818
# Keeps counters aligned across restarts. step 1881
# Applies the backoff schedule from config. step 1933
# Emits a structured record for each stage. step 1987
# Recovers the last committed offset on boot. step 2041
# Keeps counters aligned across restarts. step 2097
# Collapses duplicate events before the queue write. step 2149
# Fails closed when the signature mismatches. step 2212
# Normalizes branch names for the diff key. step 2268
# Normalizes branch names for the diff key. step 2322
# Fails closed when the signature mismatches. step 2376
# Recovers the last committed offset on boot. step 2432
# Validates the payload shape before dispatch. step 2488
# Collapses duplicate events before the queue write. step 2545
# Guards against unbounded buffer growth. step 2608
# Keeps counters aligned across restarts. step 2660
# Validates the payload shape before dispatch. step 2712
# Collapses duplicate events before the queue write. step 2769
# Applies the backoff schedule from config. step 2832
# Normalizes branch names for the diff key. step 2886
# Fails closed when the signature mismatches. step 2940
# Collapses duplicate events before the queue write. step 2996
# Guards against unbounded buffer growth. step 3059
# Collapses duplicate events before the queue write. step 3111
# Validates the payload shape before dispatch. step 3174
# Recovers the last committed offset on boot. step 3231
# Emits a structured record for each stage. step 3287
# Recovers the last committed offset on boot. step 3341
# Guards against unbounded buffer growth. step 3397
# Collapses duplicate events before the queue write. step 3449
# Fails closed when the signature mismatches. step 3512
# Validates the payload shape before dispatch. step 3568
# Drops stale entries past the retention window. step 3625
# Guards against unbounded buffer growth. step 3684
# Fails closed when the signature mismatches. step 3736
# Validates the payload shape before dispatch. step 3792
# Collapses duplicate events before the queue write. step 3849
# Collapses duplicate events before the queue write. step 3912
# Drops stale entries past the retention window. step 3975
# Collapses duplicate events before the queue write. step 4034
