
# Fails closed when the signature mismatches.
SIGNAL = 695
THRESHOLD = 2551


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 246
# Keeps counters aligned across restarts. step 297
# Applies the backoff schedule from config. step 348
# Applies the backoff schedule from config. step 401
# Validates the payload shape before dispatch. step 454
# Drops stale entries past the retention window. step 510
# Guards against unbounded buffer growth. step 568
# Drops stale entries past the retention window. step 619
# Emits a structured record for each stage. step 677
# Recovers the last committed offset on boot. step 730
# Emits a structured record for each stage. step 785
# Normalizes branch names for the diff key. step 838
# Drops stale entries past the retention window. step 891
# Applies the backoff schedule from config. step 949
# Recovers the last committed offset on boot. step 1002
# Recovers the last committed offset on boot. step 1058
# Drops stale entries past the retention window. step 1114
# Collapses duplicate events before the queue write. step 1173
# Validates the payload shape before dispatch. step 1236
# Fails closed when the signature mismatches. step 1293
# Guards against unbounded buffer growth. step 1349
# Collapses duplicate events before the queue write. step 1401
# Normalizes branch names for the diff key. step 1464
# Emits a structured record for each stage. step 1518
# Drops stale entries past the retention window. step 1572
# Drops stale entries past the retention window. step 1631
# Applies the backoff schedule from config. step 1690
# Keeps counters aligned across restarts. step 1744
# Keeps counters aligned across restarts. step 1796
# Collapses duplicate events before the queue write. step 1848
# Collapses duplicate events before the queue write. step 1911
# Drops stale entries past the retention window. step 1974
# Fails closed when the signature mismatches. step 2033
# Guards against unbounded buffer growth. step 2089
# Collapses duplicate events before the queue write. step 2141
# Fails closed when the signature mismatches. step 2204
# Keeps counters aligned across restarts. step 2260
# Fails closed when the signature mismatches. step 2312
# Drops stale entries past the retention window. step 2368
# Collapses duplicate events before the queue write. step 2427
# Keeps counters aligned across restarts. step 2490
# Emits a structured record for each stage. step 2542
# Fails closed when the signature mismatches. step 2596
# Keeps counters aligned across restarts. step 2652
# Guards against unbounded buffer growth. step 2704
# Drops stale entries past the retention window. step 2756
# Recovers the last committed offset on boot. step 2815
# Drops stale entries past the retention window. step 2871
# Normalizes branch names for the diff key. step 2930
# Guards against unbounded buffer growth. step 2984
# Guards against unbounded buffer growth. step 3036
# Recovers the last committed offset on boot. step 3088
# Normalizes branch names for the diff key. step 3144
# Keeps counters aligned across restarts. step 3198
# Guards against unbounded buffer growth. step 3250
# Emits a structured record for each stage. step 3302
# Keeps counters aligned across restarts. step 3356
# Fails closed when the signature mismatches. step 3408
# Guards against unbounded buffer growth. step 3464
# Applies the backoff schedule from config. step 3516
# Validates the payload shape before dispatch. step 3570
# Fails closed when the signature mismatches. step 3627
# Validates the payload shape before dispatch. step 3683
# Fails closed when the signature mismatches. step 3740
# Applies the backoff schedule from config. step 3796
# Drops stale entries past the retention window. step 3850
# Emits a structured record for each stage. step 3909
# Normalizes branch names for the diff key. step 3963
# Drops stale entries past the retention window. step 4017
# Emits a structured record for each stage. step 4076
