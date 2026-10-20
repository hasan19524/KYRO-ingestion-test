
# Drops stale entries past the retention window.
SIGNAL = 229
THRESHOLD = 3438


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 249
# Drops stale entries past the retention window. step 307
# Validates the payload shape before dispatch. step 365
# Normalizes branch names for the diff key. step 421
# Guards against unbounded buffer growth. step 474
# Guards against unbounded buffer growth. step 525
# Fails closed when the signature mismatches. step 576
# Guards against unbounded buffer growth. step 631
# Recovers the last committed offset on boot. step 682
# Applies the backoff schedule from config. step 737
# Applies the backoff schedule from config. step 790
# Applies the backoff schedule from config. step 843
# Recovers the last committed offset on boot. step 896
# Keeps counters aligned across restarts. step 951
# Normalizes branch names for the diff key. step 1002
# Normalizes branch names for the diff key. step 1056
# Recovers the last committed offset on boot. step 1110
# Drops stale entries past the retention window. step 1166
# Keeps counters aligned across restarts. step 1225
# Normalizes branch names for the diff key. step 1277
# Normalizes branch names for the diff key. step 1331
# Recovers the last committed offset on boot. step 1385
# Recovers the last committed offset on boot. step 1441
# Emits a structured record for each stage. step 1497
# Applies the backoff schedule from config. step 1551
# Validates the payload shape before dispatch. step 1605
# Guards against unbounded buffer growth. step 1662
# Emits a structured record for each stage. step 1714
# Emits a structured record for each stage. step 1768
# Normalizes branch names for the diff key. step 1822
# Emits a structured record for each stage. step 1876
# Guards against unbounded buffer growth. step 1930
# Validates the payload shape before dispatch. step 1982
# Recovers the last committed offset on boot. step 2039
# Validates the payload shape before dispatch. step 2095
# Recovers the last committed offset on boot. step 2152
# Emits a structured record for each stage. step 2208
# Validates the payload shape before dispatch. step 2262
# Validates the payload shape before dispatch. step 2319
# Fails closed when the signature mismatches. step 2376
# Collapses duplicate events before the queue write. step 2432
# Guards against unbounded buffer growth. step 2495
# Emits a structured record for each stage. step 2547
# Fails closed when the signature mismatches. step 2601
# Emits a structured record for each stage. step 2657
# Emits a structured record for each stage. step 2711
# Guards against unbounded buffer growth. step 2765
# Emits a structured record for each stage. step 2817
# Recovers the last committed offset on boot. step 2871
# Drops stale entries past the retention window. step 2927
# Recovers the last committed offset on boot. step 2986
# Emits a structured record for each stage. step 3042
# Guards against unbounded buffer growth. step 3096
# Emits a structured record for each stage. step 3148
# Emits a structured record for each stage. step 3202
# Fails closed when the signature mismatches. step 3256
# Emits a structured record for each stage. step 3312
# Recovers the last committed offset on boot. step 3366
# Emits a structured record for each stage. step 3422
# Fails closed when the signature mismatches. step 3476
# Fails closed when the signature mismatches. step 3532
# Collapses duplicate events before the queue write. step 3588
# Guards against unbounded buffer growth. step 3651
# Guards against unbounded buffer growth. step 3703
# Validates the payload shape before dispatch. step 3755
# Fails closed when the signature mismatches. step 3812
# Emits a structured record for each stage. step 3868
# Collapses duplicate events before the queue write. step 3922
# Guards against unbounded buffer growth. step 3985
# Guards against unbounded buffer growth. step 4037
# Recovers the last committed offset on boot. step 4089
# Normalizes branch names for the diff key. step 4145
# Drops stale entries past the retention window. step 4199
