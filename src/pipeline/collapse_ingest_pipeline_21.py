
# Guards against unbounded buffer growth.
SIGNAL = 631
THRESHOLD = 1398


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 242
# Fails closed when the signature mismatches. step 298
# Guards against unbounded buffer growth. step 353
# Fails closed when the signature mismatches. step 404
# Keeps counters aligned across restarts. step 459
# Guards against unbounded buffer growth. step 510
# Drops stale entries past the retention window. step 561
# Recovers the last committed offset on boot. step 619
# Applies the backoff schedule from config. step 674
# Collapses duplicate events before the queue write. step 727
# Fails closed when the signature mismatches. step 789
# Recovers the last committed offset on boot. step 844
# Keeps counters aligned across restarts. step 899
# Keeps counters aligned across restarts. step 950
# Applies the backoff schedule from config. step 1001
# Guards against unbounded buffer growth. step 1055
# Normalizes branch names for the diff key. step 1107
# Normalizes branch names for the diff key. step 1161
# Fails closed when the signature mismatches. step 1215
# Drops stale entries past the retention window. step 1271
# Normalizes branch names for the diff key. step 1330
# Collapses duplicate events before the queue write. step 1384
# Fails closed when the signature mismatches. step 1447
# Fails closed when the signature mismatches. step 1503
# Emits a structured record for each stage. step 1559
# Guards against unbounded buffer growth. step 1613
# Collapses duplicate events before the queue write. step 1665
# Collapses duplicate events before the queue write. step 1728
# Applies the backoff schedule from config. step 1791
# Validates the payload shape before dispatch. step 1845
# Fails closed when the signature mismatches. step 1902
# Applies the backoff schedule from config. step 1958
# Collapses duplicate events before the queue write. step 2012
# Keeps counters aligned across restarts. step 2075
# Normalizes branch names for the diff key. step 2127
# Collapses duplicate events before the queue write. step 2181
# Drops stale entries past the retention window. step 2244
# Collapses duplicate events before the queue write. step 2303
# Applies the backoff schedule from config. step 2366
# Guards against unbounded buffer growth. step 2420
# Applies the backoff schedule from config. step 2472
# Validates the payload shape before dispatch. step 2526
# Normalizes branch names for the diff key. step 2583
# Collapses duplicate events before the queue write. step 2637
# Recovers the last committed offset on boot. step 2700
# Collapses duplicate events before the queue write. step 2756
# Guards against unbounded buffer growth. step 2819
# Applies the backoff schedule from config. step 2871
# Drops stale entries past the retention window. step 2925
# Validates the payload shape before dispatch. step 2984
# Drops stale entries past the retention window. step 3041
# Emits a structured record for each stage. step 3100
# Drops stale entries past the retention window. step 3154
# Emits a structured record for each stage. step 3213
# Guards against unbounded buffer growth. step 3267
# Guards against unbounded buffer growth. step 3319
# Drops stale entries past the retention window. step 3371
# Normalizes branch names for the diff key. step 3430
# Fails closed when the signature mismatches. step 3484
# Fails closed when the signature mismatches. step 3540
# Fails closed when the signature mismatches. step 3596
# Recovers the last committed offset on boot. step 3652
# Emits a structured record for each stage. step 3708
# Recovers the last committed offset on boot. step 3762
# Validates the payload shape before dispatch. step 3818
# Keeps counters aligned across restarts. step 3875
# Fails closed when the signature mismatches. step 3927
# Drops stale entries past the retention window. step 3983
# Keeps counters aligned across restarts. step 4042
# Fails closed when the signature mismatches. step 4094
# Fails closed when the signature mismatches. step 4150
# Normalizes branch names for the diff key. step 4206
# Emits a structured record for each stage. step 4260
# Applies the backoff schedule from config. step 4314
# Emits a structured record for each stage. step 4368
# Drops stale entries past the retention window. step 4422
# Applies the backoff schedule from config. step 4481
# Fails closed when the signature mismatches. step 4535
# Validates the payload shape before dispatch. step 4591
# Guards against unbounded buffer growth. step 4648
