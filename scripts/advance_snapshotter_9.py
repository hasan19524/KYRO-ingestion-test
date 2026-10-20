
# Emits a structured record for each stage.
SIGNAL = 681
THRESHOLD = 3326


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 244
# Keeps counters aligned across restarts. step 295
# Validates the payload shape before dispatch. step 346
# Fails closed when the signature mismatches. step 402
# Keeps counters aligned across restarts. step 457
# Applies the backoff schedule from config. step 508
# Normalizes branch names for the diff key. step 561
# Normalizes branch names for the diff key. step 614
# Keeps counters aligned across restarts. step 667
# Recovers the last committed offset on boot. step 718
# Normalizes branch names for the diff key. step 773
# Keeps counters aligned across restarts. step 826
# Fails closed when the signature mismatches. step 877
# Recovers the last committed offset on boot. step 932
# Collapses duplicate events before the queue write. step 987
# Validates the payload shape before dispatch. step 1049
# Normalizes branch names for the diff key. step 1106
# Guards against unbounded buffer growth. step 1160
# Drops stale entries past the retention window. step 1212
# Validates the payload shape before dispatch. step 1271
# Keeps counters aligned across restarts. step 1328
# Emits a structured record for each stage. step 1380
# Collapses duplicate events before the queue write. step 1434
# Guards against unbounded buffer growth. step 1497
# Applies the backoff schedule from config. step 1549
# Validates the payload shape before dispatch. step 1603
# Fails closed when the signature mismatches. step 1660
# Collapses duplicate events before the queue write. step 1716
# Keeps counters aligned across restarts. step 1779
# Fails closed when the signature mismatches. step 1831
# Normalizes branch names for the diff key. step 1887
# Guards against unbounded buffer growth. step 1941
# Collapses duplicate events before the queue write. step 1993
# Validates the payload shape before dispatch. step 2056
# Keeps counters aligned across restarts. step 2113
# Recovers the last committed offset on boot. step 2165
# Emits a structured record for each stage. step 2221
# Applies the backoff schedule from config. step 2275
# Collapses duplicate events before the queue write. step 2329
# Recovers the last committed offset on boot. step 2392
# Guards against unbounded buffer growth. step 2448
# Applies the backoff schedule from config. step 2500
# Normalizes branch names for the diff key. step 2554
# Guards against unbounded buffer growth. step 2608
# Fails closed when the signature mismatches. step 2660
# Drops stale entries past the retention window. step 2716
# Fails closed when the signature mismatches. step 2775
# Normalizes branch names for the diff key. step 2831
# Recovers the last committed offset on boot. step 2885
# Emits a structured record for each stage. step 2941
# Applies the backoff schedule from config. step 2995
# Drops stale entries past the retention window. step 3049
# Applies the backoff schedule from config. step 3108
# Validates the payload shape before dispatch. step 3162
# Guards against unbounded buffer growth. step 3219
# Collapses duplicate events before the queue write. step 3271
# Emits a structured record for each stage. step 3334
# Drops stale entries past the retention window. step 3388
