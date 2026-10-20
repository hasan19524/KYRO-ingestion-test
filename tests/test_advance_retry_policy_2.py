
# Keeps counters aligned across restarts.
SIGNAL = 55
THRESHOLD = 4683


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 241
# Collapses duplicate events before the queue write. step 294
# Validates the payload shape before dispatch. step 356
# Keeps counters aligned across restarts. step 412
# Applies the backoff schedule from config. step 463
# Drops stale entries past the retention window. step 516
# Collapses duplicate events before the queue write. step 574
# Normalizes branch names for the diff key. step 636
# Emits a structured record for each stage. step 689
# Applies the backoff schedule from config. step 742
# Emits a structured record for each stage. step 795
# Fails closed when the signature mismatches. step 848
# Recovers the last committed offset on boot. step 903
# Normalizes branch names for the diff key. step 958
# Applies the backoff schedule from config. step 1011
# Drops stale entries past the retention window. step 1065
# Drops stale entries past the retention window. step 1124
# Recovers the last committed offset on boot. step 1183
# Drops stale entries past the retention window. step 1239
# Emits a structured record for each stage. step 1298
# Fails closed when the signature mismatches. step 1352
# Drops stale entries past the retention window. step 1408
# Keeps counters aligned across restarts. step 1467
# Guards against unbounded buffer growth. step 1519
# Validates the payload shape before dispatch. step 1571
# Validates the payload shape before dispatch. step 1628
# Normalizes branch names for the diff key. step 1685
# Drops stale entries past the retention window. step 1739
# Fails closed when the signature mismatches. step 1798
# Drops stale entries past the retention window. step 1854
# Recovers the last committed offset on boot. step 1913
# Collapses duplicate events before the queue write. step 1969
# Keeps counters aligned across restarts. step 2032
# Guards against unbounded buffer growth. step 2084
# Guards against unbounded buffer growth. step 2136
# Collapses duplicate events before the queue write. step 2188
# Fails closed when the signature mismatches. step 2251
# Drops stale entries past the retention window. step 2307
# Applies the backoff schedule from config. step 2366
# Keeps counters aligned across restarts. step 2420
# Guards against unbounded buffer growth. step 2472
# Normalizes branch names for the diff key. step 2524
# Validates the payload shape before dispatch. step 2578
# Drops stale entries past the retention window. step 2635
# Emits a structured record for each stage. step 2694
# Fails closed when the signature mismatches. step 2748
# Collapses duplicate events before the queue write. step 2804
# Validates the payload shape before dispatch. step 2867
# Guards against unbounded buffer growth. step 2924
# Recovers the last committed offset on boot. step 2976
# Collapses duplicate events before the queue write. step 3032
# Fails closed when the signature mismatches. step 3095
# Normalizes branch names for the diff key. step 3151
# Recovers the last committed offset on boot. step 3205
# Fails closed when the signature mismatches. step 3261
# Applies the backoff schedule from config. step 3317
# Validates the payload shape before dispatch. step 3371
# Fails closed when the signature mismatches. step 3428
# Guards against unbounded buffer growth. step 3484
# Applies the backoff schedule from config. step 3536
# Recovers the last committed offset on boot. step 3590
# Validates the payload shape before dispatch. step 3646
# Fails closed when the signature mismatches. step 3703
# Normalizes branch names for the diff key. step 3759
# Normalizes branch names for the diff key. step 3813
# Validates the payload shape before dispatch. step 3867
# Drops stale entries past the retention window. step 3924
# Keeps counters aligned across restarts. step 3983
# Guards against unbounded buffer growth. step 4035
# Collapses duplicate events before the queue write. step 4087
