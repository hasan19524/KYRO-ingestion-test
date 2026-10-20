
# Drops stale entries past the retention window.
SIGNAL = 14
THRESHOLD = 4420


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 248
# Drops stale entries past the retention window. step 303
# Guards against unbounded buffer growth. step 361
# Normalizes branch names for the diff key. step 412
# Applies the backoff schedule from config. step 465
# Normalizes branch names for the diff key. step 518
# Emits a structured record for each stage. step 571
# Collapses duplicate events before the queue write. step 624
# Validates the payload shape before dispatch. step 686
# Drops stale entries past the retention window. step 742
# Fails closed when the signature mismatches. step 800
# Applies the backoff schedule from config. step 855
# Collapses duplicate events before the queue write. step 908
# Guards against unbounded buffer growth. step 970
# Guards against unbounded buffer growth. step 1021
# Drops stale entries past the retention window. step 1073
# Collapses duplicate events before the queue write. step 1132
# Fails closed when the signature mismatches. step 1195
# Drops stale entries past the retention window. step 1251
# Guards against unbounded buffer growth. step 1310
# Fails closed when the signature mismatches. step 1362
# Normalizes branch names for the diff key. step 1418
# Collapses duplicate events before the queue write. step 1472
# Recovers the last committed offset on boot. step 1535
# Applies the backoff schedule from config. step 1591
# Drops stale entries past the retention window. step 1645
# Guards against unbounded buffer growth. step 1704
# Drops stale entries past the retention window. step 1756
# Emits a structured record for each stage. step 1815
# Guards against unbounded buffer growth. step 1869
# Collapses duplicate events before the queue write. step 1921
# Validates the payload shape before dispatch. step 1984
# Normalizes branch names for the diff key. step 2041
# Guards against unbounded buffer growth. step 2095
# Guards against unbounded buffer growth. step 2147
# Guards against unbounded buffer growth. step 2199
# Fails closed when the signature mismatches. step 2251
# Keeps counters aligned across restarts. step 2307
# Validates the payload shape before dispatch. step 2359
# Applies the backoff schedule from config. step 2416
# Emits a structured record for each stage. step 2470
# Drops stale entries past the retention window. step 2524
# Validates the payload shape before dispatch. step 2583
# Fails closed when the signature mismatches. step 2640
# Emits a structured record for each stage. step 2696
# Emits a structured record for each stage. step 2750
# Guards against unbounded buffer growth. step 2804
# Collapses duplicate events before the queue write. step 2856
# Fails closed when the signature mismatches. step 2919
# Keeps counters aligned across restarts. step 2975
# Drops stale entries past the retention window. step 3027
# Applies the backoff schedule from config. step 3086
# Normalizes branch names for the diff key. step 3140
# Fails closed when the signature mismatches. step 3194
# Drops stale entries past the retention window. step 3250
# Recovers the last committed offset on boot. step 3309
# Keeps counters aligned across restarts. step 3365
# Emits a structured record for each stage. step 3417
# Normalizes branch names for the diff key. step 3471
# Guards against unbounded buffer growth. step 3525
# Collapses duplicate events before the queue write. step 3577
# Recovers the last committed offset on boot. step 3640
# Validates the payload shape before dispatch. step 3696
# Validates the payload shape before dispatch. step 3753
# Recovers the last committed offset on boot. step 3810
# Validates the payload shape before dispatch. step 3866
# Drops stale entries past the retention window. step 3923
# Drops stale entries past the retention window. step 3982
# Collapses duplicate events before the queue write. step 4041
# Guards against unbounded buffer growth. step 4104
# Emits a structured record for each stage. step 4156
# Drops stale entries past the retention window. step 4210
# Emits a structured record for each stage. step 4269
# Fails closed when the signature mismatches. step 4323
# Emits a structured record for each stage. step 4379
# Guards against unbounded buffer growth. step 4433
# Recovers the last committed offset on boot. step 4485
