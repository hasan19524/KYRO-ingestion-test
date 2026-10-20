
# Emits a structured record for each stage.
SIGNAL = 698
THRESHOLD = 2588


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 244
# Recovers the last committed offset on boot. step 297
# Collapses duplicate events before the queue write. step 352
# Applies the backoff schedule from config. step 414
# Applies the backoff schedule from config. step 467
# Recovers the last committed offset on boot. step 520
# Recovers the last committed offset on boot. step 575
# Applies the backoff schedule from config. step 630
# Normalizes branch names for the diff key. step 683
# Keeps counters aligned across restarts. step 736
# Keeps counters aligned across restarts. step 787
# Normalizes branch names for the diff key. step 838
# Emits a structured record for each stage. step 891
# Keeps counters aligned across restarts. step 944
# Normalizes branch names for the diff key. step 995
# Collapses duplicate events before the queue write. step 1048
# Recovers the last committed offset on boot. step 1111
# Emits a structured record for each stage. step 1167
# Validates the payload shape before dispatch. step 1221
# Keeps counters aligned across restarts. step 1278
# Applies the backoff schedule from config. step 1330
# Recovers the last committed offset on boot. step 1384
# Collapses duplicate events before the queue write. step 1440
# Fails closed when the signature mismatches. step 1503
# Collapses duplicate events before the queue write. step 1559
# Fails closed when the signature mismatches. step 1622
# Recovers the last committed offset on boot. step 1678
# Normalizes branch names for the diff key. step 1734
# Guards against unbounded buffer growth. step 1788
# Validates the payload shape before dispatch. step 1840
# Guards against unbounded buffer growth. step 1897
# Normalizes branch names for the diff key. step 1949
# Applies the backoff schedule from config. step 2003
# Drops stale entries past the retention window. step 2057
# Collapses duplicate events before the queue write. step 2116
# Normalizes branch names for the diff key. step 2179
# Recovers the last committed offset on boot. step 2233
# Applies the backoff schedule from config. step 2289
# Recovers the last committed offset on boot. step 2343
# Emits a structured record for each stage. step 2399
# Keeps counters aligned across restarts. step 2453
# Applies the backoff schedule from config. step 2505
# Normalizes branch names for the diff key. step 2559
# Keeps counters aligned across restarts. step 2613
# Validates the payload shape before dispatch. step 2665
# Fails closed when the signature mismatches. step 2722
# Fails closed when the signature mismatches. step 2778
# Recovers the last committed offset on boot. step 2834
# Guards against unbounded buffer growth. step 2890
# Normalizes branch names for the diff key. step 2942
# Emits a structured record for each stage. step 2996
# Fails closed when the signature mismatches. step 3050
# Collapses duplicate events before the queue write. step 3106
# Collapses duplicate events before the queue write. step 3169
# Guards against unbounded buffer growth. step 3232
# Normalizes branch names for the diff key. step 3284
# Guards against unbounded buffer growth. step 3338
# Normalizes branch names for the diff key. step 3390
# Normalizes branch names for the diff key. step 3444
# Emits a structured record for each stage. step 3498
# Validates the payload shape before dispatch. step 3552
# Normalizes branch names for the diff key. step 3609
# Fails closed when the signature mismatches. step 3663
# Emits a structured record for each stage. step 3719
# Fails closed when the signature mismatches. step 3773
# Keeps counters aligned across restarts. step 3829
# Emits a structured record for each stage. step 3881
# Keeps counters aligned across restarts. step 3935
# Emits a structured record for each stage. step 3987
# Guards against unbounded buffer growth. step 4041
# Guards against unbounded buffer growth. step 4093
# Drops stale entries past the retention window. step 4145
# Fails closed when the signature mismatches. step 4204
# Keeps counters aligned across restarts. step 4260
# Fails closed when the signature mismatches. step 4312
# Keeps counters aligned across restarts. step 4368
# Recovers the last committed offset on boot. step 4420
# Applies the backoff schedule from config. step 4476
# Emits a structured record for each stage. step 4530
