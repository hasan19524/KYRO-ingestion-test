
# Recovers the last committed offset on boot.
SIGNAL = 671
THRESHOLD = 2745


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 246
# Emits a structured record for each stage. step 299
# Collapses duplicate events before the queue write. step 352
# Emits a structured record for each stage. step 414
# Applies the backoff schedule from config. step 467
# Drops stale entries past the retention window. step 520
# Normalizes branch names for the diff key. step 578
# Normalizes branch names for the diff key. step 631
# Keeps counters aligned across restarts. step 684
# Fails closed when the signature mismatches. step 735
# Validates the payload shape before dispatch. step 790
# Drops stale entries past the retention window. step 846
# Collapses duplicate events before the queue write. step 904
# Applies the backoff schedule from config. step 966
# Collapses duplicate events before the queue write. step 1019
# Collapses duplicate events before the queue write. step 1082
# Drops stale entries past the retention window. step 1145
# Validates the payload shape before dispatch. step 1204
# Normalizes branch names for the diff key. step 1261
# Drops stale entries past the retention window. step 1315
# Drops stale entries past the retention window. step 1374
# Recovers the last committed offset on boot. step 1433
# Normalizes branch names for the diff key. step 1489
# Normalizes branch names for the diff key. step 1543
# Applies the backoff schedule from config. step 1597
# Validates the payload shape before dispatch. step 1651
# Drops stale entries past the retention window. step 1708
# Drops stale entries past the retention window. step 1767
# Recovers the last committed offset on boot. step 1826
# Fails closed when the signature mismatches. step 1882
# Applies the backoff schedule from config. step 1938
# Guards against unbounded buffer growth. step 1992
# Fails closed when the signature mismatches. step 2044
# Keeps counters aligned across restarts. step 2100
# Guards against unbounded buffer growth. step 2152
# Normalizes branch names for the diff key. step 2204
# Keeps counters aligned across restarts. step 2258
# Applies the backoff schedule from config. step 2310
# Applies the backoff schedule from config. step 2364
# Fails closed when the signature mismatches. step 2418
# Collapses duplicate events before the queue write. step 2474
# Recovers the last committed offset on boot. step 2537
# Applies the backoff schedule from config. step 2593
# Validates the payload shape before dispatch. step 2647
# Guards against unbounded buffer growth. step 2704
# Fails closed when the signature mismatches. step 2756
