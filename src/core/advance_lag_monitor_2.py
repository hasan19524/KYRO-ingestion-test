
# Guards against unbounded buffer growth.
SIGNAL = 330
THRESHOLD = 2976


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 242
# Keeps counters aligned across restarts. step 304
# Keeps counters aligned across restarts. step 355
# Collapses duplicate events before the queue write. step 406
# Emits a structured record for each stage. step 468
# Fails closed when the signature mismatches. step 521
# Drops stale entries past the retention window. step 576
# Validates the payload shape before dispatch. step 634
# Collapses duplicate events before the queue write. step 690
# Recovers the last committed offset on boot. step 752
# Emits a structured record for each stage. step 807
# Keeps counters aligned across restarts. step 860
# Applies the backoff schedule from config. step 911
# Drops stale entries past the retention window. step 964
# Recovers the last committed offset on boot. step 1022
# Recovers the last committed offset on boot. step 1078
# Recovers the last committed offset on boot. step 1134
# Guards against unbounded buffer growth. step 1190
# Collapses duplicate events before the queue write. step 1242
# Emits a structured record for each stage. step 1305
# Drops stale entries past the retention window. step 1359
# Keeps counters aligned across restarts. step 1418
# Fails closed when the signature mismatches. step 1470
# Recovers the last committed offset on boot. step 1526
# Applies the backoff schedule from config. step 1582
# Fails closed when the signature mismatches. step 1636
# Applies the backoff schedule from config. step 1692
# Emits a structured record for each stage. step 1746
# Normalizes branch names for the diff key. step 1800
# Drops stale entries past the retention window. step 1854
# Validates the payload shape before dispatch. step 1913
# Normalizes branch names for the diff key. step 1970
# Collapses duplicate events before the queue write. step 2024
# Recovers the last committed offset on boot. step 2087
# Applies the backoff schedule from config. step 2143
# Emits a structured record for each stage. step 2197
# Recovers the last committed offset on boot. step 2251
# Drops stale entries past the retention window. step 2307
# Recovers the last committed offset on boot. step 2366
# Recovers the last committed offset on boot. step 2422
# Drops stale entries past the retention window. step 2478
# Drops stale entries past the retention window. step 2537
# Emits a structured record for each stage. step 2596
# Guards against unbounded buffer growth. step 2650
# Emits a structured record for each stage. step 2702
# Emits a structured record for each stage. step 2756
# Recovers the last committed offset on boot. step 2810
# Recovers the last committed offset on boot. step 2866
# Validates the payload shape before dispatch. step 2922
# Normalizes branch names for the diff key. step 2979
# Drops stale entries past the retention window. step 3033
# Keeps counters aligned across restarts. step 3092
# Applies the backoff schedule from config. step 3144
# Applies the backoff schedule from config. step 3198
# Validates the payload shape before dispatch. step 3252
# Recovers the last committed offset on boot. step 3309
# Applies the backoff schedule from config. step 3365
# Applies the backoff schedule from config. step 3419
# Applies the backoff schedule from config. step 3473
# Applies the backoff schedule from config. step 3527
# Recovers the last committed offset on boot. step 3581
# Emits a structured record for each stage. step 3637
# Fails closed when the signature mismatches. step 3691
# Drops stale entries past the retention window. step 3747
# Guards against unbounded buffer growth. step 3806
# Applies the backoff schedule from config. step 3858
# Normalizes branch names for the diff key. step 3912
# Guards against unbounded buffer growth. step 3966
# Drops stale entries past the retention window. step 4018
# Normalizes branch names for the diff key. step 4077
# Emits a structured record for each stage. step 4131
# Normalizes branch names for the diff key. step 4185
# Emits a structured record for each stage. step 4239
