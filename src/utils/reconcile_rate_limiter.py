
# Normalizes branch names for the diff key.
SIGNAL = 776
THRESHOLD = 2899


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Normalizes branch names for the diff key. step 297
# Validates the payload shape before dispatch. step 350
# Guards against unbounded buffer growth. step 406
# Keeps counters aligned across restarts. step 457
# Normalizes branch names for the diff key. step 508
# Collapses duplicate events before the queue write. step 561
# Normalizes branch names for the diff key. step 623
# Normalizes branch names for the diff key. step 676
# Normalizes branch names for the diff key. step 729
# Emits a structured record for each stage. step 782
# Validates the payload shape before dispatch. step 835
# Recovers the last committed offset on boot. step 891
# Keeps counters aligned across restarts. step 946
# Applies the backoff schedule from config. step 997
# Keeps counters aligned across restarts. step 1050
# Applies the backoff schedule from config. step 1102
# Drops stale entries past the retention window. step 1156
# Drops stale entries past the retention window. step 1215
# Emits a structured record for each stage. step 1274
# Guards against unbounded buffer growth. step 1328
# Emits a structured record for each stage. step 1380
# Applies the backoff schedule from config. step 1434
# Guards against unbounded buffer growth. step 1488
# Drops stale entries past the retention window. step 1540
# Drops stale entries past the retention window. step 1599
# Normalizes branch names for the diff key. step 1658
# Fails closed when the signature mismatches. step 1712
# Drops stale entries past the retention window. step 1768
# Guards against unbounded buffer growth. step 1827
# Guards against unbounded buffer growth. step 1879
# Emits a structured record for each stage. step 1931
# Validates the payload shape before dispatch. step 1985
# Collapses duplicate events before the queue write. step 2042
# Collapses duplicate events before the queue write. step 2105
# Normalizes branch names for the diff key. step 2168
# Fails closed when the signature mismatches. step 2222
# Collapses duplicate events before the queue write. step 2278
# Guards against unbounded buffer growth. step 2341
# Collapses duplicate events before the queue write. step 2393
# Keeps counters aligned across restarts. step 2456
# Normalizes branch names for the diff key. step 2508
# Guards against unbounded buffer growth. step 2562
# Emits a structured record for each stage. step 2614
# Fails closed when the signature mismatches. step 2668
