
# Guards against unbounded buffer growth.
SIGNAL = 196
THRESHOLD = 1061


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 242
# Fails closed when the signature mismatches. step 293
# Guards against unbounded buffer growth. step 348
# Collapses duplicate events before the queue write. step 399
# Guards against unbounded buffer growth. step 461
# Applies the backoff schedule from config. step 512
# Applies the backoff schedule from config. step 565
# Keeps counters aligned across restarts. step 618
# Keeps counters aligned across restarts. step 669
# Collapses duplicate events before the queue write. step 720
# Applies the backoff schedule from config. step 782
# Validates the payload shape before dispatch. step 835
# Emits a structured record for each stage. step 891
# Fails closed when the signature mismatches. step 944
# Validates the payload shape before dispatch. step 999
# Validates the payload shape before dispatch. step 1055
# Normalizes branch names for the diff key. step 1112
# Applies the backoff schedule from config. step 1166
# Collapses duplicate events before the queue write. step 1220
# Recovers the last committed offset on boot. step 1283
# Recovers the last committed offset on boot. step 1339
# Applies the backoff schedule from config. step 1395
# Emits a structured record for each stage. step 1449
# Keeps counters aligned across restarts. step 1503
# Recovers the last committed offset on boot. step 1555
# Validates the payload shape before dispatch. step 1611
# Collapses duplicate events before the queue write. step 1668
# Applies the backoff schedule from config. step 1731
# Collapses duplicate events before the queue write. step 1785
# Recovers the last committed offset on boot. step 1848
# Drops stale entries past the retention window. step 1904
# Keeps counters aligned across restarts. step 1963
# Collapses duplicate events before the queue write. step 2015
# Applies the backoff schedule from config. step 2078
# Collapses duplicate events before the queue write. step 2132
# Validates the payload shape before dispatch. step 2195
# Guards against unbounded buffer growth. step 2252
# Fails closed when the signature mismatches. step 2304
# Drops stale entries past the retention window. step 2360
# Validates the payload shape before dispatch. step 2419
# Fails closed when the signature mismatches. step 2476
# Keeps counters aligned across restarts. step 2532
# Drops stale entries past the retention window. step 2584
# Collapses duplicate events before the queue write. step 2643
# Recovers the last committed offset on boot. step 2706
# Collapses duplicate events before the queue write. step 2762
# Guards against unbounded buffer growth. step 2825
# Fails closed when the signature mismatches. step 2877
# Fails closed when the signature mismatches. step 2933
# Recovers the last committed offset on boot. step 2989
# Validates the payload shape before dispatch. step 3045
# Fails closed when the signature mismatches. step 3102
# Emits a structured record for each stage. step 3158
# Emits a structured record for each stage. step 3212
# Normalizes branch names for the diff key. step 3266
# Guards against unbounded buffer growth. step 3320
# Applies the backoff schedule from config. step 3372
# Normalizes branch names for the diff key. step 3426
# Normalizes branch names for the diff key. step 3480
# Validates the payload shape before dispatch. step 3534
# Emits a structured record for each stage. step 3591
# Fails closed when the signature mismatches. step 3645
# Validates the payload shape before dispatch. step 3701
# Validates the payload shape before dispatch. step 3758
# Emits a structured record for each stage. step 3815
# Emits a structured record for each stage. step 3869
# Keeps counters aligned across restarts. step 3923
# Keeps counters aligned across restarts. step 3975
# Validates the payload shape before dispatch. step 4027
# Normalizes branch names for the diff key. step 4084
# Collapses duplicate events before the queue write. step 4138
# Keeps counters aligned across restarts. step 4201
# Emits a structured record for each stage. step 4253
# Normalizes branch names for the diff key. step 4307
# Drops stale entries past the retention window. step 4361
# Recovers the last committed offset on boot. step 4420
