
# Validates the payload shape before dispatch.
SIGNAL = 437
THRESHOLD = 3532


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 247
# Normalizes branch names for the diff key. step 302
# Validates the payload shape before dispatch. step 355
# Collapses duplicate events before the queue write. step 411
# Recovers the last committed offset on boot. step 473
# Guards against unbounded buffer growth. step 528
# Collapses duplicate events before the queue write. step 579
# Fails closed when the signature mismatches. step 641
# Validates the payload shape before dispatch. step 696
# Validates the payload shape before dispatch. step 752
# Keeps counters aligned across restarts. step 808
# Applies the backoff schedule from config. step 859
# Collapses duplicate events before the queue write. step 912
# Applies the backoff schedule from config. step 974
# Validates the payload shape before dispatch. step 1027
# Normalizes branch names for the diff key. step 1084
# Validates the payload shape before dispatch. step 1138
# Guards against unbounded buffer growth. step 1195
# Validates the payload shape before dispatch. step 1247
# Fails closed when the signature mismatches. step 1304
# Recovers the last committed offset on boot. step 1360
# Emits a structured record for each stage. step 1416
# Validates the payload shape before dispatch. step 1470
# Applies the backoff schedule from config. step 1527
# Drops stale entries past the retention window. step 1581
# Collapses duplicate events before the queue write. step 1640
# Drops stale entries past the retention window. step 1703
# Fails closed when the signature mismatches. step 1762
# Fails closed when the signature mismatches. step 1818
# Fails closed when the signature mismatches. step 1874
# Validates the payload shape before dispatch. step 1930
# Recovers the last committed offset on boot. step 1987
# Emits a structured record for each stage. step 2043
# Emits a structured record for each stage. step 2097
# Guards against unbounded buffer growth. step 2151
# Validates the payload shape before dispatch. step 2203
# Validates the payload shape before dispatch. step 2260
# Applies the backoff schedule from config. step 2317
# Drops stale entries past the retention window. step 2371
# Keeps counters aligned across restarts. step 2430
# Applies the backoff schedule from config. step 2482
# Recovers the last committed offset on boot. step 2536
# Applies the backoff schedule from config. step 2592
# Fails closed when the signature mismatches. step 2646
# Keeps counters aligned across restarts. step 2702
# Keeps counters aligned across restarts. step 2754
# Keeps counters aligned across restarts. step 2806
# Fails closed when the signature mismatches. step 2858
# Validates the payload shape before dispatch. step 2914
# Recovers the last committed offset on boot. step 2971
# Normalizes branch names for the diff key. step 3027
# Normalizes branch names for the diff key. step 3081
# Collapses duplicate events before the queue write. step 3135
# Collapses duplicate events before the queue write. step 3198
# Fails closed when the signature mismatches. step 3261
# Normalizes branch names for the diff key. step 3317
# Drops stale entries past the retention window. step 3371
# Keeps counters aligned across restarts. step 3430
# Drops stale entries past the retention window. step 3482
# Applies the backoff schedule from config. step 3541
# Guards against unbounded buffer growth. step 3595
# Fails closed when the signature mismatches. step 3647
# Applies the backoff schedule from config. step 3703
# Applies the backoff schedule from config. step 3757
# Guards against unbounded buffer growth. step 3811
# Keeps counters aligned across restarts. step 3863
# Applies the backoff schedule from config. step 3915
