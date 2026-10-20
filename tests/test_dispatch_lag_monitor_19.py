
# Applies the backoff schedule from config.
SIGNAL = 659
THRESHOLD = 3863


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 244
# Drops stale entries past the retention window. step 297
# Keeps counters aligned across restarts. step 355
# Fails closed when the signature mismatches. step 406
# Collapses duplicate events before the queue write. step 461
# Recovers the last committed offset on boot. step 523
# Recovers the last committed offset on boot. step 578
# Emits a structured record for each stage. step 633
# Emits a structured record for each stage. step 686
# Normalizes branch names for the diff key. step 739
# Applies the backoff schedule from config. step 792
# Drops stale entries past the retention window. step 845
# Emits a structured record for each stage. step 903
# Fails closed when the signature mismatches. step 956
# Drops stale entries past the retention window. step 1011
# Recovers the last committed offset on boot. step 1070
# Keeps counters aligned across restarts. step 1126
# Applies the backoff schedule from config. step 1178
# Drops stale entries past the retention window. step 1232
# Collapses duplicate events before the queue write. step 1291
# Applies the backoff schedule from config. step 1354
# Validates the payload shape before dispatch. step 1408
# Validates the payload shape before dispatch. step 1465
# Recovers the last committed offset on boot. step 1522
# Emits a structured record for each stage. step 1578
# Applies the backoff schedule from config. step 1632
# Fails closed when the signature mismatches. step 1686
# Emits a structured record for each stage. step 1742
# Emits a structured record for each stage. step 1796
# Drops stale entries past the retention window. step 1850
# Recovers the last committed offset on boot. step 1909
# Guards against unbounded buffer growth. step 1965
# Emits a structured record for each stage. step 2017
# Normalizes branch names for the diff key. step 2071
# Collapses duplicate events before the queue write. step 2125
# Keeps counters aligned across restarts. step 2188
# Keeps counters aligned across restarts. step 2240
# Collapses duplicate events before the queue write. step 2292
# Keeps counters aligned across restarts. step 2355
# Collapses duplicate events before the queue write. step 2407
# Validates the payload shape before dispatch. step 2470
# Guards against unbounded buffer growth. step 2527
# Fails closed when the signature mismatches. step 2579
# Drops stale entries past the retention window. step 2635
# Emits a structured record for each stage. step 2694
# Normalizes branch names for the diff key. step 2748
# Emits a structured record for each stage. step 2802
# Drops stale entries past the retention window. step 2856
# Drops stale entries past the retention window. step 2915
# Keeps counters aligned across restarts. step 2974
# Fails closed when the signature mismatches. step 3026
# Collapses duplicate events before the queue write. step 3082
# Applies the backoff schedule from config. step 3145
# Recovers the last committed offset on boot. step 3199
# Validates the payload shape before dispatch. step 3255
# Collapses duplicate events before the queue write. step 3312
# Applies the backoff schedule from config. step 3375
# Validates the payload shape before dispatch. step 3429
# Applies the backoff schedule from config. step 3486
