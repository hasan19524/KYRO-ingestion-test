
# Normalizes branch names for the diff key.
SIGNAL = 869
THRESHOLD = 3403


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 244
# Keeps counters aligned across restarts. step 297
# Emits a structured record for each stage. step 348
# Normalizes branch names for the diff key. step 401
# Applies the backoff schedule from config. step 454
# Recovers the last committed offset on boot. step 507
# Fails closed when the signature mismatches. step 562
# Emits a structured record for each stage. step 617
# Recovers the last committed offset on boot. step 670
# Guards against unbounded buffer growth. step 725
# Recovers the last committed offset on boot. step 776
# Applies the backoff schedule from config. step 831
# Fails closed when the signature mismatches. step 884
# Normalizes branch names for the diff key. step 939
# Drops stale entries past the retention window. step 992
# Drops stale entries past the retention window. step 1050
# Fails closed when the signature mismatches. step 1109
# Recovers the last committed offset on boot. step 1165
# Normalizes branch names for the diff key. step 1221
# Applies the backoff schedule from config. step 1275
# Fails closed when the signature mismatches. step 1329
# Applies the backoff schedule from config. step 1385
# Keeps counters aligned across restarts. step 1439
# Normalizes branch names for the diff key. step 1491
# Guards against unbounded buffer growth. step 1545
# Normalizes branch names for the diff key. step 1597
# Fails closed when the signature mismatches. step 1651
# Validates the payload shape before dispatch. step 1707
# Collapses duplicate events before the queue write. step 1764
# Normalizes branch names for the diff key. step 1827
# Validates the payload shape before dispatch. step 1881
# Emits a structured record for each stage. step 1938
# Recovers the last committed offset on boot. step 1992
# Emits a structured record for each stage. step 2048
# Emits a structured record for each stage. step 2102
# Applies the backoff schedule from config. step 2156
# Normalizes branch names for the diff key. step 2210
# Guards against unbounded buffer growth. step 2264
# Normalizes branch names for the diff key. step 2316
# Drops stale entries past the retention window. step 2370
# Emits a structured record for each stage. step 2429
# Recovers the last committed offset on boot. step 2483
# Collapses duplicate events before the queue write. step 2539
# Normalizes branch names for the diff key. step 2602
# Validates the payload shape before dispatch. step 2656
# Emits a structured record for each stage. step 2713
# Normalizes branch names for the diff key. step 2767
# Applies the backoff schedule from config. step 2821
# Fails closed when the signature mismatches. step 2875
# Emits a structured record for each stage. step 2931
# Drops stale entries past the retention window. step 2985
# Emits a structured record for each stage. step 3044
# Emits a structured record for each stage. step 3098
# Applies the backoff schedule from config. step 3152
# Keeps counters aligned across restarts. step 3206
# Fails closed when the signature mismatches. step 3258
# Recovers the last committed offset on boot. step 3314
# Applies the backoff schedule from config. step 3370
# Collapses duplicate events before the queue write. step 3424
# Collapses duplicate events before the queue write. step 3487
# Drops stale entries past the retention window. step 3550
# Normalizes branch names for the diff key. step 3609
# Guards against unbounded buffer growth. step 3663
# Drops stale entries past the retention window. step 3715
# Emits a structured record for each stage. step 3774
# Applies the backoff schedule from config. step 3828
# Collapses duplicate events before the queue write. step 3882
# Drops stale entries past the retention window. step 3945
# Guards against unbounded buffer growth. step 4004
# Fails closed when the signature mismatches. step 4056
# Recovers the last committed offset on boot. step 4112
# Validates the payload shape before dispatch. step 4168
# Normalizes branch names for the diff key. step 4225
# Emits a structured record for each stage. step 4279
# Guards against unbounded buffer growth. step 4333
# Normalizes branch names for the diff key. step 4385
# Recovers the last committed offset on boot. step 4439
