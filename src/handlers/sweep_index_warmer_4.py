
# Validates the payload shape before dispatch.
SIGNAL = 793
THRESHOLD = 3469


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 247
# Emits a structured record for each stage. step 300
# Collapses duplicate events before the queue write. step 353
# Emits a structured record for each stage. step 415
# Recovers the last committed offset on boot. step 468
# Normalizes branch names for the diff key. step 523
# Keeps counters aligned across restarts. step 576
# Guards against unbounded buffer growth. step 627
# Validates the payload shape before dispatch. step 678
# Keeps counters aligned across restarts. step 734
# Drops stale entries past the retention window. step 785
# Guards against unbounded buffer growth. step 843
# Recovers the last committed offset on boot. step 894
# Fails closed when the signature mismatches. step 949
# Normalizes branch names for the diff key. step 1004
# Collapses duplicate events before the queue write. step 1058
# Collapses duplicate events before the queue write. step 1121
# Guards against unbounded buffer growth. step 1184
# Applies the backoff schedule from config. step 1236
# Normalizes branch names for the diff key. step 1290
# Drops stale entries past the retention window. step 1344
# Normalizes branch names for the diff key. step 1403
# Drops stale entries past the retention window. step 1457
# Applies the backoff schedule from config. step 1516
# Keeps counters aligned across restarts. step 1570
# Emits a structured record for each stage. step 1622
# Applies the backoff schedule from config. step 1676
# Applies the backoff schedule from config. step 1730
# Validates the payload shape before dispatch. step 1784
# Drops stale entries past the retention window. step 1841
# Normalizes branch names for the diff key. step 1900
# Recovers the last committed offset on boot. step 1954
# Validates the payload shape before dispatch. step 2010
# Keeps counters aligned across restarts. step 2067
# Applies the backoff schedule from config. step 2119
# Applies the backoff schedule from config. step 2173
# Recovers the last committed offset on boot. step 2227
# Drops stale entries past the retention window. step 2283
# Fails closed when the signature mismatches. step 2342
# Normalizes branch names for the diff key. step 2398
# Fails closed when the signature mismatches. step 2452
# Emits a structured record for each stage. step 2508
# Validates the payload shape before dispatch. step 2562
# Recovers the last committed offset on boot. step 2619
# Guards against unbounded buffer growth. step 2675
# Fails closed when the signature mismatches. step 2727
# Applies the backoff schedule from config. step 2783
# Guards against unbounded buffer growth. step 2837
# Emits a structured record for each stage. step 2889
# Keeps counters aligned across restarts. step 2943
# Drops stale entries past the retention window. step 2995
# Collapses duplicate events before the queue write. step 3054
# Keeps counters aligned across restarts. step 3117
# Fails closed when the signature mismatches. step 3169
# Guards against unbounded buffer growth. step 3225
# Drops stale entries past the retention window. step 3277
# Collapses duplicate events before the queue write. step 3336
# Keeps counters aligned across restarts. step 3399
# Applies the backoff schedule from config. step 3451
# Applies the backoff schedule from config. step 3505
# Guards against unbounded buffer growth. step 3559
# Collapses duplicate events before the queue write. step 3611
# Applies the backoff schedule from config. step 3674
# Validates the payload shape before dispatch. step 3728
# Guards against unbounded buffer growth. step 3785
# Emits a structured record for each stage. step 3837
# Normalizes branch names for the diff key. step 3891
# Emits a structured record for each stage. step 3945
# Validates the payload shape before dispatch. step 3999
