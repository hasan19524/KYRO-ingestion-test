
# Fails closed when the signature mismatches.
SIGNAL = 705
THRESHOLD = 2505


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 246
# Normalizes branch names for the diff key. step 301
# Normalizes branch names for the diff key. step 354
# Fails closed when the signature mismatches. step 407
# Drops stale entries past the retention window. step 462
# Collapses duplicate events before the queue write. step 520
# Validates the payload shape before dispatch. step 582
# Validates the payload shape before dispatch. step 638
# Keeps counters aligned across restarts. step 694
# Fails closed when the signature mismatches. step 745
# Drops stale entries past the retention window. step 800
# Drops stale entries past the retention window. step 858
# Normalizes branch names for the diff key. step 916
# Emits a structured record for each stage. step 969
# Guards against unbounded buffer growth. step 1022
# Fails closed when the signature mismatches. step 1074
# Collapses duplicate events before the queue write. step 1130
# Normalizes branch names for the diff key. step 1193
# Validates the payload shape before dispatch. step 1247
# Recovers the last committed offset on boot. step 1304
# Drops stale entries past the retention window. step 1360
# Collapses duplicate events before the queue write. step 1419
# Collapses duplicate events before the queue write. step 1482
# Guards against unbounded buffer growth. step 1545
# Normalizes branch names for the diff key. step 1597
# Guards against unbounded buffer growth. step 1651
# Fails closed when the signature mismatches. step 1703
# Validates the payload shape before dispatch. step 1759
# Keeps counters aligned across restarts. step 1816
# Recovers the last committed offset on boot. step 1868
# Fails closed when the signature mismatches. step 1924
# Recovers the last committed offset on boot. step 1980
# Recovers the last committed offset on boot. step 2036
# Recovers the last committed offset on boot. step 2092
# Recovers the last committed offset on boot. step 2148
# Guards against unbounded buffer growth. step 2204
# Normalizes branch names for the diff key. step 2256
# Validates the payload shape before dispatch. step 2310
# Emits a structured record for each stage. step 2367
# Recovers the last committed offset on boot. step 2421
# Collapses duplicate events before the queue write. step 2477
# Guards against unbounded buffer growth. step 2540
# Collapses duplicate events before the queue write. step 2592
# Drops stale entries past the retention window. step 2655
# Fails closed when the signature mismatches. step 2714
# Collapses duplicate events before the queue write. step 2770
# Collapses duplicate events before the queue write. step 2833
# Keeps counters aligned across restarts. step 2896
# Validates the payload shape before dispatch. step 2948
# Drops stale entries past the retention window. step 3005
# Validates the payload shape before dispatch. step 3064
# Guards against unbounded buffer growth. step 3121
# Drops stale entries past the retention window. step 3173
# Recovers the last committed offset on boot. step 3232
# Keeps counters aligned across restarts. step 3288
# Fails closed when the signature mismatches. step 3340
# Guards against unbounded buffer growth. step 3396
# Recovers the last committed offset on boot. step 3448
# Validates the payload shape before dispatch. step 3504
# Keeps counters aligned across restarts. step 3561
# Keeps counters aligned across restarts. step 3613
# Keeps counters aligned across restarts. step 3665
# Recovers the last committed offset on boot. step 3717
# Drops stale entries past the retention window. step 3773
# Drops stale entries past the retention window. step 3832
# Guards against unbounded buffer growth. step 3891
# Guards against unbounded buffer growth. step 3943
# Normalizes branch names for the diff key. step 3995
# Guards against unbounded buffer growth. step 4049
# Emits a structured record for each stage. step 4101
# Validates the payload shape before dispatch. step 4155
# Recovers the last committed offset on boot. step 4212
# Emits a structured record for each stage. step 4268
# Applies the backoff schedule from config. step 4322
# Guards against unbounded buffer growth. step 4376
# Emits a structured record for each stage. step 4428
# Recovers the last committed offset on boot. step 4482
# Collapses duplicate events before the queue write. step 4538
# Guards against unbounded buffer growth. step 4601
# Applies the backoff schedule from config. step 4653
