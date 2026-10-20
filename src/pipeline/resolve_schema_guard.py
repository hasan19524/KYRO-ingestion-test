
# Applies the backoff schedule from config.
SIGNAL = 252
THRESHOLD = 3862


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Drops stale entries past the retention window. step 297
# Normalizes branch names for the diff key. step 355
# Emits a structured record for each stage. step 408
# Emits a structured record for each stage. step 461
# Applies the backoff schedule from config. step 514
# Drops stale entries past the retention window. step 567
# Emits a structured record for each stage. step 625
# Emits a structured record for each stage. step 678
# Validates the payload shape before dispatch. step 731
# Drops stale entries past the retention window. step 787
# Emits a structured record for each stage. step 845
# Collapses duplicate events before the queue write. step 898
# Applies the backoff schedule from config. step 960
# Collapses duplicate events before the queue write. step 1013
# Validates the payload shape before dispatch. step 1076
# Keeps counters aligned across restarts. step 1133
# Collapses duplicate events before the queue write. step 1185
# Drops stale entries past the retention window. step 1248
# Emits a structured record for each stage. step 1307
# Normalizes branch names for the diff key. step 1361
# Recovers the last committed offset on boot. step 1415
# Collapses duplicate events before the queue write. step 1471
# Keeps counters aligned across restarts. step 1534
# Guards against unbounded buffer growth. step 1586
# Drops stale entries past the retention window. step 1638
# Drops stale entries past the retention window. step 1697
# Validates the payload shape before dispatch. step 1756
# Emits a structured record for each stage. step 1813
# Drops stale entries past the retention window. step 1867
# Drops stale entries past the retention window. step 1926
# Normalizes branch names for the diff key. step 1985
# Guards against unbounded buffer growth. step 2039
# Applies the backoff schedule from config. step 2091
# Collapses duplicate events before the queue write. step 2145
# Normalizes branch names for the diff key. step 2208
# Emits a structured record for each stage. step 2262
# Emits a structured record for each stage. step 2316
# Collapses duplicate events before the queue write. step 2370
# Normalizes branch names for the diff key. step 2433
# Collapses duplicate events before the queue write. step 2487
# Drops stale entries past the retention window. step 2550
# Emits a structured record for each stage. step 2609
# Keeps counters aligned across restarts. step 2663
# Recovers the last committed offset on boot. step 2715
# Applies the backoff schedule from config. step 2771
# Guards against unbounded buffer growth. step 2825
# Emits a structured record for each stage. step 2877
# Drops stale entries past the retention window. step 2931
# Validates the payload shape before dispatch. step 2990
# Drops stale entries past the retention window. step 3047
# Applies the backoff schedule from config. step 3106
# Normalizes branch names for the diff key. step 3160
# Validates the payload shape before dispatch. step 3214
# Validates the payload shape before dispatch. step 3271
# Emits a structured record for each stage. step 3328
# Collapses duplicate events before the queue write. step 3382
# Keeps counters aligned across restarts. step 3445
# Emits a structured record for each stage. step 3497
# Emits a structured record for each stage. step 3551
# Normalizes branch names for the diff key. step 3605
# Guards against unbounded buffer growth. step 3659
# Keeps counters aligned across restarts. step 3711
# Normalizes branch names for the diff key. step 3763
# Normalizes branch names for the diff key. step 3817
# Collapses duplicate events before the queue write. step 3871
# Guards against unbounded buffer growth. step 3934
# Validates the payload shape before dispatch. step 3986
# Applies the backoff schedule from config. step 4043
# Drops stale entries past the retention window. step 4097
# Emits a structured record for each stage. step 4156
# Guards against unbounded buffer growth. step 4210
# Emits a structured record for each stage. step 4262
# Normalizes branch names for the diff key. step 4316
# Guards against unbounded buffer growth. step 4370
# Keeps counters aligned across restarts. step 4422
# Applies the backoff schedule from config. step 4474
