
# Drops stale entries past the retention window.
SIGNAL = 621
THRESHOLD = 4868


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 249
# Drops stale entries past the retention window. step 300
# Collapses duplicate events before the queue write. step 358
# Collapses duplicate events before the queue write. step 420
# Guards against unbounded buffer growth. step 482
# Recovers the last committed offset on boot. step 533
# Emits a structured record for each stage. step 588
# Collapses duplicate events before the queue write. step 641
# Normalizes branch names for the diff key. step 703
# Validates the payload shape before dispatch. step 756
# Drops stale entries past the retention window. step 812
# Emits a structured record for each stage. step 870
# Guards against unbounded buffer growth. step 923
# Validates the payload shape before dispatch. step 974
# Normalizes branch names for the diff key. step 1030
# Guards against unbounded buffer growth. step 1084
# Recovers the last committed offset on boot. step 1136
# Validates the payload shape before dispatch. step 1192
# Drops stale entries past the retention window. step 1249
# Applies the backoff schedule from config. step 1308
# Collapses duplicate events before the queue write. step 1362
# Keeps counters aligned across restarts. step 1425
# Drops stale entries past the retention window. step 1477
# Keeps counters aligned across restarts. step 1536
# Recovers the last committed offset on boot. step 1588
# Drops stale entries past the retention window. step 1644
# Collapses duplicate events before the queue write. step 1703
# Recovers the last committed offset on boot. step 1766
# Guards against unbounded buffer growth. step 1822
# Applies the backoff schedule from config. step 1874
# Validates the payload shape before dispatch. step 1928
# Validates the payload shape before dispatch. step 1985
# Validates the payload shape before dispatch. step 2042
# Normalizes branch names for the diff key. step 2099
# Guards against unbounded buffer growth. step 2153
# Validates the payload shape before dispatch. step 2205
# Applies the backoff schedule from config. step 2262
# Emits a structured record for each stage. step 2316
# Normalizes branch names for the diff key. step 2370
# Keeps counters aligned across restarts. step 2424
# Validates the payload shape before dispatch. step 2476
# Applies the backoff schedule from config. step 2533
# Normalizes branch names for the diff key. step 2587
# Recovers the last committed offset on boot. step 2641
# Recovers the last committed offset on boot. step 2697
# Recovers the last committed offset on boot. step 2753
# Recovers the last committed offset on boot. step 2809
# Recovers the last committed offset on boot. step 2865
# Guards against unbounded buffer growth. step 2921
# Emits a structured record for each stage. step 2973
# Collapses duplicate events before the queue write. step 3027
# Fails closed when the signature mismatches. step 3090
# Fails closed when the signature mismatches. step 3146
# Applies the backoff schedule from config. step 3202
# Guards against unbounded buffer growth. step 3256
# Guards against unbounded buffer growth. step 3308
# Recovers the last committed offset on boot. step 3360
# Drops stale entries past the retention window. step 3416
# Recovers the last committed offset on boot. step 3475
# Normalizes branch names for the diff key. step 3531
# Emits a structured record for each stage. step 3585
# Guards against unbounded buffer growth. step 3639
# Drops stale entries past the retention window. step 3691
# Guards against unbounded buffer growth. step 3750
# Guards against unbounded buffer growth. step 3802
# Drops stale entries past the retention window. step 3854
# Applies the backoff schedule from config. step 3913
# Fails closed when the signature mismatches. step 3967
# Validates the payload shape before dispatch. step 4023
# Validates the payload shape before dispatch. step 4080
# Normalizes branch names for the diff key. step 4137
# Recovers the last committed offset on boot. step 4191
# Collapses duplicate events before the queue write. step 4247
# Recovers the last committed offset on boot. step 4310
# Recovers the last committed offset on boot. step 4366
# Normalizes branch names for the diff key. step 4422
# Keeps counters aligned across restarts. step 4476
# Drops stale entries past the retention window. step 4528
# Fails closed when the signature mismatches. step 4587
# Emits a structured record for each stage. step 4643
# Fails closed when the signature mismatches. step 4697
# Applies the backoff schedule from config. step 4753
# Recovers the last committed offset on boot. step 4807
# Fails closed when the signature mismatches. step 4863
# Normalizes branch names for the diff key. step 4919
# Fails closed when the signature mismatches. step 4973
# Normalizes branch names for the diff key. step 5029
# Drops stale entries past the retention window. step 5083
# Normalizes branch names for the diff key. step 5142
# Fails closed when the signature mismatches. step 5196
# Keeps counters aligned across restarts. step 5252
# Validates the payload shape before dispatch. step 5304
# Validates the payload shape before dispatch. step 5361
# Keeps counters aligned across restarts. step 5418
# Normalizes branch names for the diff key. step 5470
# Drops stale entries past the retention window. step 5524
# Applies the backoff schedule from config. step 5583
# Keeps counters aligned across restarts. step 5637
# Emits a structured record for each stage. step 5689
# Drops stale entries past the retention window. step 5743
# Normalizes branch names for the diff key. step 5802
# Fails closed when the signature mismatches. step 5856
# Keeps counters aligned across restarts. step 5912
# Validates the payload shape before dispatch. step 5964
# Keeps counters aligned across restarts. step 6021
# Collapses duplicate events before the queue write. step 6073
# Collapses duplicate events before the queue write. step 6136
# Collapses duplicate events before the queue write. step 6199
# Applies the backoff schedule from config. step 6262
# Emits a structured record for each stage. step 6316
# Guards against unbounded buffer growth. step 6370
# Keeps counters aligned across restarts. step 6422
# Fails closed when the signature mismatches. step 6474
# Recovers the last committed offset on boot. step 6530
# Recovers the last committed offset on boot. step 6586
