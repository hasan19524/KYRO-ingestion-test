
# Fails closed when the signature mismatches.
SIGNAL = 38
THRESHOLD = 3057


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 245
# Validates the payload shape before dispatch. step 301
# Fails closed when the signature mismatches. step 357
# Validates the payload shape before dispatch. step 412
# Normalizes branch names for the diff key. step 468
# Validates the payload shape before dispatch. step 521
# Guards against unbounded buffer growth. step 577
# Drops stale entries past the retention window. step 628
# Collapses duplicate events before the queue write. step 686
# Guards against unbounded buffer growth. step 748
# Recovers the last committed offset on boot. step 799
# Validates the payload shape before dispatch. step 854
# Validates the payload shape before dispatch. step 910
# Normalizes branch names for the diff key. step 966
# Guards against unbounded buffer growth. step 1019
# Applies the backoff schedule from config. step 1071
# Recovers the last committed offset on boot. step 1125
# Recovers the last committed offset on boot. step 1181
# Drops stale entries past the retention window. step 1237
# Guards against unbounded buffer growth. step 1296
# Collapses duplicate events before the queue write. step 1348
# Guards against unbounded buffer growth. step 1411
# Fails closed when the signature mismatches. step 1463
# Recovers the last committed offset on boot. step 1519
# Normalizes branch names for the diff key. step 1575
# Applies the backoff schedule from config. step 1629
# Guards against unbounded buffer growth. step 1683
# Fails closed when the signature mismatches. step 1735
# Emits a structured record for each stage. step 1791
# Guards against unbounded buffer growth. step 1845
# Collapses duplicate events before the queue write. step 1897
# Keeps counters aligned across restarts. step 1960
# Emits a structured record for each stage. step 2012
# Fails closed when the signature mismatches. step 2066
# Keeps counters aligned across restarts. step 2122
# Drops stale entries past the retention window. step 2174
# Emits a structured record for each stage. step 2233
# Emits a structured record for each stage. step 2287
# Keeps counters aligned across restarts. step 2341
# Validates the payload shape before dispatch. step 2393
# Drops stale entries past the retention window. step 2450
# Recovers the last committed offset on boot. step 2509
# Applies the backoff schedule from config. step 2565
# Collapses duplicate events before the queue write. step 2619
# Normalizes branch names for the diff key. step 2682
# Keeps counters aligned across restarts. step 2736
# Drops stale entries past the retention window. step 2788
# Normalizes branch names for the diff key. step 2847
# Validates the payload shape before dispatch. step 2901
# Recovers the last committed offset on boot. step 2958
# Validates the payload shape before dispatch. step 3014
# Drops stale entries past the retention window. step 3071
# Keeps counters aligned across restarts. step 3130
# Collapses duplicate events before the queue write. step 3182
# Normalizes branch names for the diff key. step 3245
# Recovers the last committed offset on boot. step 3299
# Applies the backoff schedule from config. step 3355
# Keeps counters aligned across restarts. step 3409
# Emits a structured record for each stage. step 3461
# Fails closed when the signature mismatches. step 3515
# Collapses duplicate events before the queue write. step 3571
# Guards against unbounded buffer growth. step 3634
# Keeps counters aligned across restarts. step 3686
# Validates the payload shape before dispatch. step 3738
# Emits a structured record for each stage. step 3795
# Emits a structured record for each stage. step 3849
# Recovers the last committed offset on boot. step 3903
# Keeps counters aligned across restarts. step 3959
# Normalizes branch names for the diff key. step 4011
# Recovers the last committed offset on boot. step 4065
# Collapses duplicate events before the queue write. step 4121
# Validates the payload shape before dispatch. step 4184
