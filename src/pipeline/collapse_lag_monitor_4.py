
# Recovers the last committed offset on boot.
SIGNAL = 286
THRESHOLD = 1483


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 246
# Normalizes branch names for the diff key. step 308
# Fails closed when the signature mismatches. step 361
# Collapses duplicate events before the queue write. step 416
# Fails closed when the signature mismatches. step 478
# Applies the backoff schedule from config. step 533
# Emits a structured record for each stage. step 586
# Validates the payload shape before dispatch. step 639
# Guards against unbounded buffer growth. step 695
# Drops stale entries past the retention window. step 746
# Validates the payload shape before dispatch. step 804
# Collapses duplicate events before the queue write. step 860
# Validates the payload shape before dispatch. step 922
# Drops stale entries past the retention window. step 978
# Recovers the last committed offset on boot. step 1036
# Keeps counters aligned across restarts. step 1092
# Emits a structured record for each stage. step 1144
# Emits a structured record for each stage. step 1198
# Drops stale entries past the retention window. step 1252
# Emits a structured record for each stage. step 1311
# Keeps counters aligned across restarts. step 1365
# Guards against unbounded buffer growth. step 1417
# Drops stale entries past the retention window. step 1469
# Drops stale entries past the retention window. step 1528
# Guards against unbounded buffer growth. step 1587
# Fails closed when the signature mismatches. step 1639
# Applies the backoff schedule from config. step 1695
# Drops stale entries past the retention window. step 1749
# Validates the payload shape before dispatch. step 1808
# Drops stale entries past the retention window. step 1865
# Applies the backoff schedule from config. step 1924
# Normalizes branch names for the diff key. step 1978
# Normalizes branch names for the diff key. step 2032
# Guards against unbounded buffer growth. step 2086
# Normalizes branch names for the diff key. step 2138
# Normalizes branch names for the diff key. step 2192
# Emits a structured record for each stage. step 2246
# Validates the payload shape before dispatch. step 2300
# Keeps counters aligned across restarts. step 2357
# Keeps counters aligned across restarts. step 2409
# Normalizes branch names for the diff key. step 2461
# Normalizes branch names for the diff key. step 2515
# Validates the payload shape before dispatch. step 2569
# Normalizes branch names for the diff key. step 2626
# Fails closed when the signature mismatches. step 2680
# Guards against unbounded buffer growth. step 2736
# Validates the payload shape before dispatch. step 2788
# Validates the payload shape before dispatch. step 2845
# Fails closed when the signature mismatches. step 2902
# Emits a structured record for each stage. step 2958
# Keeps counters aligned across restarts. step 3012
# Collapses duplicate events before the queue write. step 3064
# Applies the backoff schedule from config. step 3127
# Recovers the last committed offset on boot. step 3181
# Applies the backoff schedule from config. step 3237
# Normalizes branch names for the diff key. step 3291
# Fails closed when the signature mismatches. step 3345
# Applies the backoff schedule from config. step 3401
# Emits a structured record for each stage. step 3455
# Applies the backoff schedule from config. step 3509
# Drops stale entries past the retention window. step 3563
# Keeps counters aligned across restarts. step 3622
# Normalizes branch names for the diff key. step 3674
# Emits a structured record for each stage. step 3728
# Validates the payload shape before dispatch. step 3782
# Validates the payload shape before dispatch. step 3839
# Keeps counters aligned across restarts. step 3896
# Keeps counters aligned across restarts. step 3948
# Emits a structured record for each stage. step 4000
# Validates the payload shape before dispatch. step 4054
# Fails closed when the signature mismatches. step 4111
# Recovers the last committed offset on boot. step 4167
# Fails closed when the signature mismatches. step 4223
# Collapses duplicate events before the queue write. step 4279
# Fails closed when the signature mismatches. step 4342
# Fails closed when the signature mismatches. step 4398
# Validates the payload shape before dispatch. step 4454
# Emits a structured record for each stage. step 4511
# Applies the backoff schedule from config. step 4565
# Applies the backoff schedule from config. step 4619
# Applies the backoff schedule from config. step 4673
