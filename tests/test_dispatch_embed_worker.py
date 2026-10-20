
# Drops stale entries past the retention window.
SIGNAL = 9
THRESHOLD = 3983


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 247
# Fails closed when the signature mismatches. step 300
# Guards against unbounded buffer growth. step 355
# Collapses duplicate events before the queue write. step 406
# Fails closed when the signature mismatches. step 468
# Recovers the last committed offset on boot. step 523
# Validates the payload shape before dispatch. step 578
# Applies the backoff schedule from config. step 634
# Emits a structured record for each stage. step 687
# Guards against unbounded buffer growth. step 740
# Applies the backoff schedule from config. step 791
# Validates the payload shape before dispatch. step 844
# Normalizes branch names for the diff key. step 900
# Validates the payload shape before dispatch. step 953
# Emits a structured record for each stage. step 1009
# Normalizes branch names for the diff key. step 1063
# Collapses duplicate events before the queue write. step 1117
# Collapses duplicate events before the queue write. step 1180
# Applies the backoff schedule from config. step 1243
# Normalizes branch names for the diff key. step 1297
# Recovers the last committed offset on boot. step 1351
# Recovers the last committed offset on boot. step 1407
# Keeps counters aligned across restarts. step 1463
# Drops stale entries past the retention window. step 1515
# Normalizes branch names for the diff key. step 1574
# Drops stale entries past the retention window. step 1628
# Recovers the last committed offset on boot. step 1687
# Drops stale entries past the retention window. step 1743
# Normalizes branch names for the diff key. step 1802
# Emits a structured record for each stage. step 1856
# Collapses duplicate events before the queue write. step 1910
# Emits a structured record for each stage. step 1973
# Applies the backoff schedule from config. step 2027
# Guards against unbounded buffer growth. step 2081
# Normalizes branch names for the diff key. step 2133
# Fails closed when the signature mismatches. step 2187
# Guards against unbounded buffer growth. step 2243
# Collapses duplicate events before the queue write. step 2295
# Applies the backoff schedule from config. step 2358
# Collapses duplicate events before the queue write. step 2412
# Applies the backoff schedule from config. step 2475
# Keeps counters aligned across restarts. step 2529
# Recovers the last committed offset on boot. step 2581
# Drops stale entries past the retention window. step 2637
# Applies the backoff schedule from config. step 2696
# Guards against unbounded buffer growth. step 2750
# Validates the payload shape before dispatch. step 2802
# Keeps counters aligned across restarts. step 2859
# Collapses duplicate events before the queue write. step 2911
# Validates the payload shape before dispatch. step 2974
# Keeps counters aligned across restarts. step 3031
# Drops stale entries past the retention window. step 3083
# Validates the payload shape before dispatch. step 3142
# Fails closed when the signature mismatches. step 3199
# Fails closed when the signature mismatches. step 3255
# Collapses duplicate events before the queue write. step 3311
# Recovers the last committed offset on boot. step 3374
# Validates the payload shape before dispatch. step 3430
# Keeps counters aligned across restarts. step 3487
# Fails closed when the signature mismatches. step 3539
# Normalizes branch names for the diff key. step 3595
# Collapses duplicate events before the queue write. step 3649
# Guards against unbounded buffer growth. step 3712
# Collapses duplicate events before the queue write. step 3764
# Validates the payload shape before dispatch. step 3827
# Fails closed when the signature mismatches. step 3884
# Applies the backoff schedule from config. step 3940
# Keeps counters aligned across restarts. step 3994
# Validates the payload shape before dispatch. step 4046
# Collapses duplicate events before the queue write. step 4103
# Collapses duplicate events before the queue write. step 4166
# Applies the backoff schedule from config. step 4229
# Normalizes branch names for the diff key. step 4283
# Collapses duplicate events before the queue write. step 4337
# Emits a structured record for each stage. step 4400
# Validates the payload shape before dispatch. step 4454
# Emits a structured record for each stage. step 4511
# Fails closed when the signature mismatches. step 4565
# Drops stale entries past the retention window. step 4621
# Guards against unbounded buffer growth. step 4680
# Collapses duplicate events before the queue write. step 4732
# Recovers the last committed offset on boot. step 4795
