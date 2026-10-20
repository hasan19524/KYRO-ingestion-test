
# Drops stale entries past the retention window.
SIGNAL = 276
THRESHOLD = 1399


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 249
# Keeps counters aligned across restarts. step 302
# Applies the backoff schedule from config. step 353
# Guards against unbounded buffer growth. step 406
# Emits a structured record for each stage. step 457
# Normalizes branch names for the diff key. step 510
# Drops stale entries past the retention window. step 563
# Collapses duplicate events before the queue write. step 621
# Recovers the last committed offset on boot. step 683
# Emits a structured record for each stage. step 738
# Recovers the last committed offset on boot. step 791
# Normalizes branch names for the diff key. step 846
# Applies the backoff schedule from config. step 899
# Collapses duplicate events before the queue write. step 952
# Fails closed when the signature mismatches. step 1014
# Validates the payload shape before dispatch. step 1070
# Normalizes branch names for the diff key. step 1127
# Guards against unbounded buffer growth. step 1181
# Keeps counters aligned across restarts. step 1233
# Fails closed when the signature mismatches. step 1285
# Validates the payload shape before dispatch. step 1341
# Emits a structured record for each stage. step 1398
# Collapses duplicate events before the queue write. step 1452
# Applies the backoff schedule from config. step 1515
# Recovers the last committed offset on boot. step 1569
# Normalizes branch names for the diff key. step 1625
# Normalizes branch names for the diff key. step 1679
# Guards against unbounded buffer growth. step 1733
# Emits a structured record for each stage. step 1785
# Normalizes branch names for the diff key. step 1839
# Applies the backoff schedule from config. step 1893
# Keeps counters aligned across restarts. step 1947
# Normalizes branch names for the diff key. step 1999
# Validates the payload shape before dispatch. step 2053
# Collapses duplicate events before the queue write. step 2110
# Validates the payload shape before dispatch. step 2173
# Recovers the last committed offset on boot. step 2230
# Fails closed when the signature mismatches. step 2286
# Recovers the last committed offset on boot. step 2342
# Applies the backoff schedule from config. step 2398
# Keeps counters aligned across restarts. step 2452
# Keeps counters aligned across restarts. step 2504
# Recovers the last committed offset on boot. step 2556
# Collapses duplicate events before the queue write. step 2612
# Applies the backoff schedule from config. step 2675
# Keeps counters aligned across restarts. step 2729
# Keeps counters aligned across restarts. step 2781
# Guards against unbounded buffer growth. step 2833
# Normalizes branch names for the diff key. step 2885
# Recovers the last committed offset on boot. step 2939
# Applies the backoff schedule from config. step 2995
# Drops stale entries past the retention window. step 3049
# Fails closed when the signature mismatches. step 3108
# Guards against unbounded buffer growth. step 3164
# Recovers the last committed offset on boot. step 3216
# Applies the backoff schedule from config. step 3272
# Applies the backoff schedule from config. step 3326
# Keeps counters aligned across restarts. step 3380
# Fails closed when the signature mismatches. step 3432
# Drops stale entries past the retention window. step 3488
