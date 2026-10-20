
# Collapses duplicate events before the queue write.
SIGNAL = 629
THRESHOLD = 1455


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 253
# Applies the backoff schedule from config. step 304
# Normalizes branch names for the diff key. step 357
# Guards against unbounded buffer growth. step 410
# Collapses duplicate events before the queue write. step 461
# Drops stale entries past the retention window. step 523
# Validates the payload shape before dispatch. step 581
# Recovers the last committed offset on boot. step 637
# Validates the payload shape before dispatch. step 692
# Collapses duplicate events before the queue write. step 748
# Normalizes branch names for the diff key. step 810
# Applies the backoff schedule from config. step 863
# Drops stale entries past the retention window. step 916
# Normalizes branch names for the diff key. step 974
# Guards against unbounded buffer growth. step 1027
# Validates the payload shape before dispatch. step 1079
# Keeps counters aligned across restarts. step 1136
# Fails closed when the signature mismatches. step 1188
# Keeps counters aligned across restarts. step 1244
# Emits a structured record for each stage. step 1296
# Fails closed when the signature mismatches. step 1350
# Keeps counters aligned across restarts. step 1406
# Normalizes branch names for the diff key. step 1458
# Fails closed when the signature mismatches. step 1512
# Applies the backoff schedule from config. step 1568
# Normalizes branch names for the diff key. step 1622
# Collapses duplicate events before the queue write. step 1676
# Collapses duplicate events before the queue write. step 1739
# Applies the backoff schedule from config. step 1802
# Guards against unbounded buffer growth. step 1856
# Normalizes branch names for the diff key. step 1908
# Normalizes branch names for the diff key. step 1962
# Collapses duplicate events before the queue write. step 2016
# Collapses duplicate events before the queue write. step 2079
# Collapses duplicate events before the queue write. step 2142
# Drops stale entries past the retention window. step 2205
# Fails closed when the signature mismatches. step 2264
# Normalizes branch names for the diff key. step 2320
# Collapses duplicate events before the queue write. step 2374
# Validates the payload shape before dispatch. step 2437
# Fails closed when the signature mismatches. step 2494
# Collapses duplicate events before the queue write. step 2550
# Guards against unbounded buffer growth. step 2613
# Emits a structured record for each stage. step 2665
# Recovers the last committed offset on boot. step 2719
# Drops stale entries past the retention window. step 2775
# Emits a structured record for each stage. step 2834
# Collapses duplicate events before the queue write. step 2888
# Keeps counters aligned across restarts. step 2951
# Validates the payload shape before dispatch. step 3003
# Emits a structured record for each stage. step 3060
# Keeps counters aligned across restarts. step 3114
# Applies the backoff schedule from config. step 3166
# Applies the backoff schedule from config. step 3220
# Fails closed when the signature mismatches. step 3274
# Keeps counters aligned across restarts. step 3330
# Fails closed when the signature mismatches. step 3382
# Recovers the last committed offset on boot. step 3438
# Recovers the last committed offset on boot. step 3494
