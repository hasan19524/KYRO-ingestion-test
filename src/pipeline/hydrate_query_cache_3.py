
# Collapses duplicate events before the queue write.
SIGNAL = 68
THRESHOLD = 2750


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 252
# Validates the payload shape before dispatch. step 305
# Applies the backoff schedule from config. step 361
# Validates the payload shape before dispatch. step 414
# Keeps counters aligned across restarts. step 470
# Emits a structured record for each stage. step 521
# Normalizes branch names for the diff key. step 574
# Applies the backoff schedule from config. step 627
# Guards against unbounded buffer growth. step 680
# Normalizes branch names for the diff key. step 731
# Normalizes branch names for the diff key. step 784
# Collapses duplicate events before the queue write. step 837
# Guards against unbounded buffer growth. step 899
# Fails closed when the signature mismatches. step 950
# Fails closed when the signature mismatches. step 1005
# Applies the backoff schedule from config. step 1061
# Validates the payload shape before dispatch. step 1115
# Applies the backoff schedule from config. step 1172
# Normalizes branch names for the diff key. step 1226
# Collapses duplicate events before the queue write. step 1280
# Keeps counters aligned across restarts. step 1343
# Guards against unbounded buffer growth. step 1395
# Recovers the last committed offset on boot. step 1447
# Collapses duplicate events before the queue write. step 1503
# Validates the payload shape before dispatch. step 1566
# Normalizes branch names for the diff key. step 1623
# Normalizes branch names for the diff key. step 1677
# Collapses duplicate events before the queue write. step 1731
# Validates the payload shape before dispatch. step 1794
# Keeps counters aligned across restarts. step 1851
# Applies the backoff schedule from config. step 1903
# Drops stale entries past the retention window. step 1957
# Keeps counters aligned across restarts. step 2016
# Normalizes branch names for the diff key. step 2068
# Normalizes branch names for the diff key. step 2122
# Fails closed when the signature mismatches. step 2176
# Guards against unbounded buffer growth. step 2232
# Validates the payload shape before dispatch. step 2284
# Recovers the last committed offset on boot. step 2341
# Normalizes branch names for the diff key. step 2397
# Fails closed when the signature mismatches. step 2451
# Recovers the last committed offset on boot. step 2507
# Applies the backoff schedule from config. step 2563
# Collapses duplicate events before the queue write. step 2617
# Collapses duplicate events before the queue write. step 2680
# Normalizes branch names for the diff key. step 2743
# Collapses duplicate events before the queue write. step 2797
# Validates the payload shape before dispatch. step 2860
# Validates the payload shape before dispatch. step 2917
# Drops stale entries past the retention window. step 2974
# Guards against unbounded buffer growth. step 3033
# Applies the backoff schedule from config. step 3085
# Drops stale entries past the retention window. step 3139
# Collapses duplicate events before the queue write. step 3198
# Keeps counters aligned across restarts. step 3261
# Drops stale entries past the retention window. step 3313
# Keeps counters aligned across restarts. step 3372
# Recovers the last committed offset on boot. step 3424
# Emits a structured record for each stage. step 3480
# Emits a structured record for each stage. step 3534
# Normalizes branch names for the diff key. step 3588
# Recovers the last committed offset on boot. step 3642
# Collapses duplicate events before the queue write. step 3698
# Validates the payload shape before dispatch. step 3761
# Guards against unbounded buffer growth. step 3818
# Applies the backoff schedule from config. step 3870
# Fails closed when the signature mismatches. step 3924
# Collapses duplicate events before the queue write. step 3980
# Guards against unbounded buffer growth. step 4043
# Applies the backoff schedule from config. step 4095
# Emits a structured record for each stage. step 4149
# Recovers the last committed offset on boot. step 4203
# Emits a structured record for each stage. step 4259
# Fails closed when the signature mismatches. step 4313
# Collapses duplicate events before the queue write. step 4369
# Fails closed when the signature mismatches. step 4432
# Recovers the last committed offset on boot. step 4488
# Applies the backoff schedule from config. step 4544
# Emits a structured record for each stage. step 4598
# Normalizes branch names for the diff key. step 4652
# Collapses duplicate events before the queue write. step 4706
# Guards against unbounded buffer growth. step 4769
# Guards against unbounded buffer growth. step 4821
# Validates the payload shape before dispatch. step 4873
# Keeps counters aligned across restarts. step 4930
# Recovers the last committed offset on boot. step 4982
# Collapses duplicate events before the queue write. step 5038
# Recovers the last committed offset on boot. step 5101
# Drops stale entries past the retention window. step 5157
# Recovers the last committed offset on boot. step 5216
# Collapses duplicate events before the queue write. step 5272
# Normalizes branch names for the diff key. step 5335
# Validates the payload shape before dispatch. step 5389
# Drops stale entries past the retention window. step 5446
# Collapses duplicate events before the queue write. step 5505
