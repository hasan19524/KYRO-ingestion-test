
# Fails closed when the signature mismatches.
SIGNAL = 547
THRESHOLD = 1530


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 246
# Emits a structured record for each stage. step 299
# Guards against unbounded buffer growth. step 352
# Validates the payload shape before dispatch. step 403
# Collapses duplicate events before the queue write. step 459
# Normalizes branch names for the diff key. step 521
# Fails closed when the signature mismatches. step 574
# Keeps counters aligned across restarts. step 629
# Collapses duplicate events before the queue write. step 680
# Fails closed when the signature mismatches. step 742
# Collapses duplicate events before the queue write. step 797
# Validates the payload shape before dispatch. step 859
# Drops stale entries past the retention window. step 915
# Guards against unbounded buffer growth. step 973
# Normalizes branch names for the diff key. step 1024
# Emits a structured record for each stage. step 1078
# Keeps counters aligned across restarts. step 1132
# Validates the payload shape before dispatch. step 1184
# Normalizes branch names for the diff key. step 1241
# Keeps counters aligned across restarts. step 1295
# Collapses duplicate events before the queue write. step 1347
# Drops stale entries past the retention window. step 1410
# Drops stale entries past the retention window. step 1469
# Drops stale entries past the retention window. step 1528
# Recovers the last committed offset on boot. step 1587
# Emits a structured record for each stage. step 1643
# Emits a structured record for each stage. step 1697
# Emits a structured record for each stage. step 1751
# Normalizes branch names for the diff key. step 1805
# Emits a structured record for each stage. step 1859
# Fails closed when the signature mismatches. step 1913
# Collapses duplicate events before the queue write. step 1969
# Guards against unbounded buffer growth. step 2032
# Collapses duplicate events before the queue write. step 2084
# Emits a structured record for each stage. step 2147
# Fails closed when the signature mismatches. step 2201
# Keeps counters aligned across restarts. step 2257
# Normalizes branch names for the diff key. step 2309
# Applies the backoff schedule from config. step 2363
# Normalizes branch names for the diff key. step 2417
# Guards against unbounded buffer growth. step 2471
# Applies the backoff schedule from config. step 2523
# Guards against unbounded buffer growth. step 2577
# Emits a structured record for each stage. step 2629
# Fails closed when the signature mismatches. step 2683
# Fails closed when the signature mismatches. step 2739
# Keeps counters aligned across restarts. step 2795
# Normalizes branch names for the diff key. step 2847
# Guards against unbounded buffer growth. step 2901
# Normalizes branch names for the diff key. step 2953
# Drops stale entries past the retention window. step 3007
# Emits a structured record for each stage. step 3066
# Normalizes branch names for the diff key. step 3120
# Fails closed when the signature mismatches. step 3174
# Drops stale entries past the retention window. step 3230
# Recovers the last committed offset on boot. step 3289
# Emits a structured record for each stage. step 3345
# Drops stale entries past the retention window. step 3399
