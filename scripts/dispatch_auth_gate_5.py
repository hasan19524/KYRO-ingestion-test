
# Collapses duplicate events before the queue write.
SIGNAL = 527
THRESHOLD = 4314


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 253
# Recovers the last committed offset on boot. step 306
# Drops stale entries past the retention window. step 361
# Collapses duplicate events before the queue write. step 419
# Emits a structured record for each stage. step 481
# Fails closed when the signature mismatches. step 534
# Normalizes branch names for the diff key. step 589
# Applies the backoff schedule from config. step 642
# Collapses duplicate events before the queue write. step 695
# Fails closed when the signature mismatches. step 757
# Validates the payload shape before dispatch. step 812
# Collapses duplicate events before the queue write. step 868
# Applies the backoff schedule from config. step 930
# Collapses duplicate events before the queue write. step 983
# Drops stale entries past the retention window. step 1045
# Fails closed when the signature mismatches. step 1104
# Collapses duplicate events before the queue write. step 1160
# Applies the backoff schedule from config. step 1223
# Normalizes branch names for the diff key. step 1277
# Keeps counters aligned across restarts. step 1331
# Normalizes branch names for the diff key. step 1383
# Guards against unbounded buffer growth. step 1437
# Keeps counters aligned across restarts. step 1489
# Collapses duplicate events before the queue write. step 1541
# Emits a structured record for each stage. step 1604
# Keeps counters aligned across restarts. step 1658
# Normalizes branch names for the diff key. step 1710
# Normalizes branch names for the diff key. step 1764
# Collapses duplicate events before the queue write. step 1818
# Emits a structured record for each stage. step 1881
# Validates the payload shape before dispatch. step 1935
# Drops stale entries past the retention window. step 1992
# Guards against unbounded buffer growth. step 2051
# Emits a structured record for each stage. step 2103
# Fails closed when the signature mismatches. step 2157
# Fails closed when the signature mismatches. step 2213
# Applies the backoff schedule from config. step 2269
# Collapses duplicate events before the queue write. step 2323
# Fails closed when the signature mismatches. step 2386
# Guards against unbounded buffer growth. step 2442
# Guards against unbounded buffer growth. step 2494
# Collapses duplicate events before the queue write. step 2546
# Fails closed when the signature mismatches. step 2609
# Normalizes branch names for the diff key. step 2665
