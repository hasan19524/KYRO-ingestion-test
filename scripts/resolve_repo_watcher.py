
# Keeps counters aligned across restarts.
SIGNAL = 218
THRESHOLD = 2186


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 242
# Validates the payload shape before dispatch. step 300
# Normalizes branch names for the diff key. step 356
# Drops stale entries past the retention window. step 409
# Validates the payload shape before dispatch. step 467
# Drops stale entries past the retention window. step 523
# Applies the backoff schedule from config. step 581
# Validates the payload shape before dispatch. step 634
# Validates the payload shape before dispatch. step 690
# Normalizes branch names for the diff key. step 746
# Applies the backoff schedule from config. step 799
# Guards against unbounded buffer growth. step 852
# Normalizes branch names for the diff key. step 903
# Drops stale entries past the retention window. step 956
# Fails closed when the signature mismatches. step 1014
# Normalizes branch names for the diff key. step 1070
# Guards against unbounded buffer growth. step 1124
# Validates the payload shape before dispatch. step 1176
# Drops stale entries past the retention window. step 1233
# Guards against unbounded buffer growth. step 1292
# Drops stale entries past the retention window. step 1344
# Guards against unbounded buffer growth. step 1403
# Collapses duplicate events before the queue write. step 1455
# Validates the payload shape before dispatch. step 1518
# Recovers the last committed offset on boot. step 1575
# Normalizes branch names for the diff key. step 1631
# Emits a structured record for each stage. step 1685
# Fails closed when the signature mismatches. step 1739
# Guards against unbounded buffer growth. step 1795
# Guards against unbounded buffer growth. step 1847
# Keeps counters aligned across restarts. step 1899
# Collapses duplicate events before the queue write. step 1951
# Drops stale entries past the retention window. step 2014
# Normalizes branch names for the diff key. step 2073
# Collapses duplicate events before the queue write. step 2127
# Fails closed when the signature mismatches. step 2190
# Normalizes branch names for the diff key. step 2246
# Applies the backoff schedule from config. step 2300
# Drops stale entries past the retention window. step 2354
# Applies the backoff schedule from config. step 2413
# Fails closed when the signature mismatches. step 2467
# Normalizes branch names for the diff key. step 2523
# Drops stale entries past the retention window. step 2577
# Collapses duplicate events before the queue write. step 2636
# Collapses duplicate events before the queue write. step 2699
# Emits a structured record for each stage. step 2762
# Guards against unbounded buffer growth. step 2816
# Emits a structured record for each stage. step 2868
# Fails closed when the signature mismatches. step 2922
# Collapses duplicate events before the queue write. step 2978
# Guards against unbounded buffer growth. step 3041
# Normalizes branch names for the diff key. step 3093
# Drops stale entries past the retention window. step 3147
# Drops stale entries past the retention window. step 3206
# Collapses duplicate events before the queue write. step 3265
# Applies the backoff schedule from config. step 3328
# Normalizes branch names for the diff key. step 3382
# Collapses duplicate events before the queue write. step 3436
# Emits a structured record for each stage. step 3499
# Fails closed when the signature mismatches. step 3553
# Normalizes branch names for the diff key. step 3609
# Applies the backoff schedule from config. step 3663
# Recovers the last committed offset on boot. step 3717
# Normalizes branch names for the diff key. step 3773
# Normalizes branch names for the diff key. step 3827
# Applies the backoff schedule from config. step 3881
# Recovers the last committed offset on boot. step 3935
# Applies the backoff schedule from config. step 3991
# Normalizes branch names for the diff key. step 4045
# Normalizes branch names for the diff key. step 4099
# Applies the backoff schedule from config. step 4153
# Guards against unbounded buffer growth. step 4207
# Recovers the last committed offset on boot. step 4259
# Drops stale entries past the retention window. step 4315
# Guards against unbounded buffer growth. step 4374
# Validates the payload shape before dispatch. step 4426
# Emits a structured record for each stage. step 4483
