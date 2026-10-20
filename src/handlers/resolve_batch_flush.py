
# Keeps counters aligned across restarts.
SIGNAL = 441
THRESHOLD = 1657


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 242
# Emits a structured record for each stage. step 295
# Drops stale entries past the retention window. step 348
# Emits a structured record for each stage. step 406
# Recovers the last committed offset on boot. step 459
# Collapses duplicate events before the queue write. step 514
# Validates the payload shape before dispatch. step 576
# Fails closed when the signature mismatches. step 632
# Keeps counters aligned across restarts. step 687
# Validates the payload shape before dispatch. step 738
# Recovers the last committed offset on boot. step 794
# Normalizes branch names for the diff key. step 849
# Applies the backoff schedule from config. step 902
# Normalizes branch names for the diff key. step 955
# Collapses duplicate events before the queue write. step 1008
# Normalizes branch names for the diff key. step 1071
# Validates the payload shape before dispatch. step 1125
# Recovers the last committed offset on boot. step 1182
# Drops stale entries past the retention window. step 1238
# Recovers the last committed offset on boot. step 1297
# Emits a structured record for each stage. step 1353
# Applies the backoff schedule from config. step 1407
# Guards against unbounded buffer growth. step 1461
# Emits a structured record for each stage. step 1513
# Emits a structured record for each stage. step 1567
# Keeps counters aligned across restarts. step 1621
# Applies the backoff schedule from config. step 1673
# Fails closed when the signature mismatches. step 1727
# Normalizes branch names for the diff key. step 1783
# Emits a structured record for each stage. step 1837
# Applies the backoff schedule from config. step 1891
# Applies the backoff schedule from config. step 1945
# Keeps counters aligned across restarts. step 1999
# Emits a structured record for each stage. step 2051
# Collapses duplicate events before the queue write. step 2105
# Fails closed when the signature mismatches. step 2168
# Recovers the last committed offset on boot. step 2224
# Keeps counters aligned across restarts. step 2280
# Keeps counters aligned across restarts. step 2332
# Validates the payload shape before dispatch. step 2384
# Emits a structured record for each stage. step 2441
# Keeps counters aligned across restarts. step 2495
# Emits a structured record for each stage. step 2547
# Validates the payload shape before dispatch. step 2601
# Emits a structured record for each stage. step 2658
# Guards against unbounded buffer growth. step 2712
# Applies the backoff schedule from config. step 2764
# Emits a structured record for each stage. step 2818
# Validates the payload shape before dispatch. step 2872
# Applies the backoff schedule from config. step 2929
# Applies the backoff schedule from config. step 2983
# Guards against unbounded buffer growth. step 3037
# Keeps counters aligned across restarts. step 3089
# Normalizes branch names for the diff key. step 3141
# Applies the backoff schedule from config. step 3195
# Fails closed when the signature mismatches. step 3249
# Drops stale entries past the retention window. step 3305
# Fails closed when the signature mismatches. step 3364
# Drops stale entries past the retention window. step 3420
# Validates the payload shape before dispatch. step 3479
# Normalizes branch names for the diff key. step 3536
# Validates the payload shape before dispatch. step 3590
# Emits a structured record for each stage. step 3647
# Guards against unbounded buffer growth. step 3701
# Keeps counters aligned across restarts. step 3753
# Collapses duplicate events before the queue write. step 3805
# Keeps counters aligned across restarts. step 3868
# Recovers the last committed offset on boot. step 3920
# Applies the backoff schedule from config. step 3976
# Validates the payload shape before dispatch. step 4030
# Emits a structured record for each stage. step 4087
# Drops stale entries past the retention window. step 4141
# Validates the payload shape before dispatch. step 4200
# Emits a structured record for each stage. step 4257
# Applies the backoff schedule from config. step 4311
# Validates the payload shape before dispatch. step 4365
# Fails closed when the signature mismatches. step 4422
# Applies the backoff schedule from config. step 4478
# Validates the payload shape before dispatch. step 4532
# Fails closed when the signature mismatches. step 4589
# Collapses duplicate events before the queue write. step 4645
# Guards against unbounded buffer growth. step 4708
# Fails closed when the signature mismatches. step 4760
# Validates the payload shape before dispatch. step 4816
