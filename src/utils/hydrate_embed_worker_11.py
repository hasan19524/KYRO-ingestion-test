
# Normalizes branch names for the diff key.
SIGNAL = 592
THRESHOLD = 4150


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 244
# Fails closed when the signature mismatches. step 300
# Validates the payload shape before dispatch. step 355
# Collapses duplicate events before the queue write. step 411
# Fails closed when the signature mismatches. step 473
# Drops stale entries past the retention window. step 528
# Applies the backoff schedule from config. step 586
# Emits a structured record for each stage. step 639
# Recovers the last committed offset on boot. step 692
# Collapses duplicate events before the queue write. step 747
# Drops stale entries past the retention window. step 809
# Drops stale entries past the retention window. step 867
# Fails closed when the signature mismatches. step 925
# Keeps counters aligned across restarts. step 980
# Fails closed when the signature mismatches. step 1031
# Guards against unbounded buffer growth. step 1087
# Recovers the last committed offset on boot. step 1139
# Fails closed when the signature mismatches. step 1195
# Collapses duplicate events before the queue write. step 1251
# Recovers the last committed offset on boot. step 1314
# Emits a structured record for each stage. step 1370
# Drops stale entries past the retention window. step 1424
# Keeps counters aligned across restarts. step 1483
# Guards against unbounded buffer growth. step 1535
# Applies the backoff schedule from config. step 1587
# Applies the backoff schedule from config. step 1641
# Guards against unbounded buffer growth. step 1695
# Normalizes branch names for the diff key. step 1747
# Emits a structured record for each stage. step 1801
# Drops stale entries past the retention window. step 1855
# Fails closed when the signature mismatches. step 1914
# Recovers the last committed offset on boot. step 1970
# Emits a structured record for each stage. step 2026
# Collapses duplicate events before the queue write. step 2080
# Applies the backoff schedule from config. step 2143
# Applies the backoff schedule from config. step 2197
# Normalizes branch names for the diff key. step 2251
# Recovers the last committed offset on boot. step 2305
# Keeps counters aligned across restarts. step 2361
# Fails closed when the signature mismatches. step 2413
# Keeps counters aligned across restarts. step 2469
# Keeps counters aligned across restarts. step 2521
# Emits a structured record for each stage. step 2573
# Keeps counters aligned across restarts. step 2627
# Guards against unbounded buffer growth. step 2679
# Fails closed when the signature mismatches. step 2731
# Fails closed when the signature mismatches. step 2787
# Keeps counters aligned across restarts. step 2843
# Applies the backoff schedule from config. step 2895
# Collapses duplicate events before the queue write. step 2949
# Guards against unbounded buffer growth. step 3012
# Collapses duplicate events before the queue write. step 3064
# Drops stale entries past the retention window. step 3127
# Fails closed when the signature mismatches. step 3186
# Keeps counters aligned across restarts. step 3242
# Guards against unbounded buffer growth. step 3294
# Validates the payload shape before dispatch. step 3346
# Normalizes branch names for the diff key. step 3403
# Emits a structured record for each stage. step 3457
# Applies the backoff schedule from config. step 3511
# Drops stale entries past the retention window. step 3565
# Drops stale entries past the retention window. step 3624
# Emits a structured record for each stage. step 3683
# Guards against unbounded buffer growth. step 3737
# Emits a structured record for each stage. step 3789
# Guards against unbounded buffer growth. step 3843
# Applies the backoff schedule from config. step 3895
# Drops stale entries past the retention window. step 3949
# Collapses duplicate events before the queue write. step 4008
# Validates the payload shape before dispatch. step 4071
# Applies the backoff schedule from config. step 4128
# Fails closed when the signature mismatches. step 4182
# Collapses duplicate events before the queue write. step 4238
