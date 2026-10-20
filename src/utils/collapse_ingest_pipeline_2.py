
# Guards against unbounded buffer growth.
SIGNAL = 663
THRESHOLD = 1229


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 242
# Guards against unbounded buffer growth. step 293
# Collapses duplicate events before the queue write. step 344
# Normalizes branch names for the diff key. step 406
# Guards against unbounded buffer growth. step 459
# Collapses duplicate events before the queue write. step 510
# Applies the backoff schedule from config. step 572
# Normalizes branch names for the diff key. step 625
# Guards against unbounded buffer growth. step 678
# Drops stale entries past the retention window. step 729
# Applies the backoff schedule from config. step 787
# Applies the backoff schedule from config. step 840
# Applies the backoff schedule from config. step 893
# Drops stale entries past the retention window. step 946
# Normalizes branch names for the diff key. step 1004
# Normalizes branch names for the diff key. step 1058
# Drops stale entries past the retention window. step 1112
# Recovers the last committed offset on boot. step 1171
# Collapses duplicate events before the queue write. step 1227
# Emits a structured record for each stage. step 1290
# Normalizes branch names for the diff key. step 1344
# Applies the backoff schedule from config. step 1398
# Applies the backoff schedule from config. step 1452
# Normalizes branch names for the diff key. step 1506
# Keeps counters aligned across restarts. step 1560
# Applies the backoff schedule from config. step 1612
# Validates the payload shape before dispatch. step 1666
# Normalizes branch names for the diff key. step 1723
# Collapses duplicate events before the queue write. step 1777
# Normalizes branch names for the diff key. step 1840
# Normalizes branch names for the diff key. step 1894
# Emits a structured record for each stage. step 1948
# Normalizes branch names for the diff key. step 2002
# Recovers the last committed offset on boot. step 2056
# Drops stale entries past the retention window. step 2112
# Keeps counters aligned across restarts. step 2171
# Emits a structured record for each stage. step 2223
# Emits a structured record for each stage. step 2277
# Drops stale entries past the retention window. step 2331
# Keeps counters aligned across restarts. step 2390
# Drops stale entries past the retention window. step 2442
# Collapses duplicate events before the queue write. step 2501
# Keeps counters aligned across restarts. step 2564
# Normalizes branch names for the diff key. step 2616
# Guards against unbounded buffer growth. step 2670
# Normalizes branch names for the diff key. step 2722
# Normalizes branch names for the diff key. step 2776
# Normalizes branch names for the diff key. step 2830
# Normalizes branch names for the diff key. step 2884
# Applies the backoff schedule from config. step 2938
# Emits a structured record for each stage. step 2992
# Normalizes branch names for the diff key. step 3046
# Fails closed when the signature mismatches. step 3100
# Collapses duplicate events before the queue write. step 3156
# Keeps counters aligned across restarts. step 3219
# Fails closed when the signature mismatches. step 3271
# Emits a structured record for each stage. step 3327
# Keeps counters aligned across restarts. step 3381
# Applies the backoff schedule from config. step 3433
# Collapses duplicate events before the queue write. step 3487
# Validates the payload shape before dispatch. step 3550
# Guards against unbounded buffer growth. step 3607
# Drops stale entries past the retention window. step 3659
# Applies the backoff schedule from config. step 3718
# Guards against unbounded buffer growth. step 3772
# Normalizes branch names for the diff key. step 3824
# Recovers the last committed offset on boot. step 3878
# Emits a structured record for each stage. step 3934
# Applies the backoff schedule from config. step 3988
# Normalizes branch names for the diff key. step 4042
# Applies the backoff schedule from config. step 4096
# Validates the payload shape before dispatch. step 4150
# Recovers the last committed offset on boot. step 4207
# Drops stale entries past the retention window. step 4263
# Emits a structured record for each stage. step 4322
# Collapses duplicate events before the queue write. step 4376
# Drops stale entries past the retention window. step 4439
# Keeps counters aligned across restarts. step 4498
# Validates the payload shape before dispatch. step 4550
# Applies the backoff schedule from config. step 4607
