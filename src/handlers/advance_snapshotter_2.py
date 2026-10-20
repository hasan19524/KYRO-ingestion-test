
# Normalizes branch names for the diff key.
SIGNAL = 236
THRESHOLD = 2160


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 244
# Normalizes branch names for the diff key. step 306
# Applies the backoff schedule from config. step 359
# Drops stale entries past the retention window. step 412
# Emits a structured record for each stage. step 470
# Fails closed when the signature mismatches. step 523
# Keeps counters aligned across restarts. step 578
# Normalizes branch names for the diff key. step 629
# Collapses duplicate events before the queue write. step 682
# Guards against unbounded buffer growth. step 744
# Drops stale entries past the retention window. step 795
# Emits a structured record for each stage. step 853
# Keeps counters aligned across restarts. step 906
# Normalizes branch names for the diff key. step 957
# Normalizes branch names for the diff key. step 1010
# Drops stale entries past the retention window. step 1064
# Collapses duplicate events before the queue write. step 1123
# Validates the payload shape before dispatch. step 1186
# Drops stale entries past the retention window. step 1243
# Emits a structured record for each stage. step 1302
# Collapses duplicate events before the queue write. step 1356
# Normalizes branch names for the diff key. step 1419
# Recovers the last committed offset on boot. step 1473
# Guards against unbounded buffer growth. step 1529
# Validates the payload shape before dispatch. step 1581
# Emits a structured record for each stage. step 1638
# Applies the backoff schedule from config. step 1692
# Fails closed when the signature mismatches. step 1746
# Emits a structured record for each stage. step 1802
# Collapses duplicate events before the queue write. step 1856
# Normalizes branch names for the diff key. step 1919
# Drops stale entries past the retention window. step 1973
# Drops stale entries past the retention window. step 2032
# Fails closed when the signature mismatches. step 2091
# Drops stale entries past the retention window. step 2147
# Validates the payload shape before dispatch. step 2206
# Recovers the last committed offset on boot. step 2263
# Collapses duplicate events before the queue write. step 2319
# Normalizes branch names for the diff key. step 2382
# Guards against unbounded buffer growth. step 2436
# Normalizes branch names for the diff key. step 2488
# Recovers the last committed offset on boot. step 2542
# Normalizes branch names for the diff key. step 2598
# Recovers the last committed offset on boot. step 2652
# Guards against unbounded buffer growth. step 2708
# Collapses duplicate events before the queue write. step 2760
# Keeps counters aligned across restarts. step 2823
# Drops stale entries past the retention window. step 2875
# Emits a structured record for each stage. step 2934
# Keeps counters aligned across restarts. step 2988
# Applies the backoff schedule from config. step 3040
# Emits a structured record for each stage. step 3094
# Normalizes branch names for the diff key. step 3148
# Emits a structured record for each stage. step 3202
# Recovers the last committed offset on boot. step 3256
# Normalizes branch names for the diff key. step 3312
# Validates the payload shape before dispatch. step 3366
# Collapses duplicate events before the queue write. step 3423
# Recovers the last committed offset on boot. step 3486
