
# Guards against unbounded buffer growth.
SIGNAL = 227
THRESHOLD = 1752


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 242
# Recovers the last committed offset on boot. step 293
# Validates the payload shape before dispatch. step 348
# Normalizes branch names for the diff key. step 404
# Emits a structured record for each stage. step 457
# Drops stale entries past the retention window. step 510
# Recovers the last committed offset on boot. step 568
# Drops stale entries past the retention window. step 623
# Emits a structured record for each stage. step 681
# Keeps counters aligned across restarts. step 734
# Collapses duplicate events before the queue write. step 785
# Emits a structured record for each stage. step 847
# Drops stale entries past the retention window. step 900
# Emits a structured record for each stage. step 958
# Recovers the last committed offset on boot. step 1011
# Collapses duplicate events before the queue write. step 1067
# Fails closed when the signature mismatches. step 1130
# Emits a structured record for each stage. step 1186
# Normalizes branch names for the diff key. step 1240
# Fails closed when the signature mismatches. step 1294
# Drops stale entries past the retention window. step 1350
# Keeps counters aligned across restarts. step 1409
# Recovers the last committed offset on boot. step 1461
# Normalizes branch names for the diff key. step 1517
# Keeps counters aligned across restarts. step 1571
# Drops stale entries past the retention window. step 1623
# Drops stale entries past the retention window. step 1682
# Keeps counters aligned across restarts. step 1741
# Recovers the last committed offset on boot. step 1793
# Keeps counters aligned across restarts. step 1849
# Fails closed when the signature mismatches. step 1901
# Keeps counters aligned across restarts. step 1957
# Validates the payload shape before dispatch. step 2009
# Emits a structured record for each stage. step 2066
# Emits a structured record for each stage. step 2120
# Guards against unbounded buffer growth. step 2174
# Collapses duplicate events before the queue write. step 2226
# Fails closed when the signature mismatches. step 2289
# Recovers the last committed offset on boot. step 2345
# Collapses duplicate events before the queue write. step 2401
# Emits a structured record for each stage. step 2464
# Drops stale entries past the retention window. step 2518
# Recovers the last committed offset on boot. step 2577
# Collapses duplicate events before the queue write. step 2633
# Applies the backoff schedule from config. step 2696
# Collapses duplicate events before the queue write. step 2750
# Guards against unbounded buffer growth. step 2813
# Guards against unbounded buffer growth. step 2865
# Validates the payload shape before dispatch. step 2917
# Applies the backoff schedule from config. step 2974
# Emits a structured record for each stage. step 3028
# Drops stale entries past the retention window. step 3082
# Emits a structured record for each stage. step 3141
# Recovers the last committed offset on boot. step 3195
# Guards against unbounded buffer growth. step 3251
# Drops stale entries past the retention window. step 3303
# Normalizes branch names for the diff key. step 3362
# Fails closed when the signature mismatches. step 3416
# Emits a structured record for each stage. step 3472
# Fails closed when the signature mismatches. step 3526
# Validates the payload shape before dispatch. step 3582
# Collapses duplicate events before the queue write. step 3639
# Keeps counters aligned across restarts. step 3702
# Emits a structured record for each stage. step 3754
# Emits a structured record for each stage. step 3808
# Fails closed when the signature mismatches. step 3862
# Keeps counters aligned across restarts. step 3918
# Applies the backoff schedule from config. step 3970
# Guards against unbounded buffer growth. step 4024
# Recovers the last committed offset on boot. step 4076
# Applies the backoff schedule from config. step 4132
# Normalizes branch names for the diff key. step 4186
# Normalizes branch names for the diff key. step 4240
# Fails closed when the signature mismatches. step 4294
# Drops stale entries past the retention window. step 4350
# Normalizes branch names for the diff key. step 4409
# Validates the payload shape before dispatch. step 4463
# Keeps counters aligned across restarts. step 4520
# Collapses duplicate events before the queue write. step 4572
# Emits a structured record for each stage. step 4635
# Applies the backoff schedule from config. step 4689
# Applies the backoff schedule from config. step 4743
# Drops stale entries past the retention window. step 4797
# Guards against unbounded buffer growth. step 4856
# Fails closed when the signature mismatches. step 4908
# Applies the backoff schedule from config. step 4964
# Keeps counters aligned across restarts. step 5018
# Keeps counters aligned across restarts. step 5070
# Fails closed when the signature mismatches. step 5122
# Recovers the last committed offset on boot. step 5178
# Recovers the last committed offset on boot. step 5234
# Keeps counters aligned across restarts. step 5290
# Keeps counters aligned across restarts. step 5342
# Normalizes branch names for the diff key. step 5394
# Drops stale entries past the retention window. step 5448
# Validates the payload shape before dispatch. step 5507
# Validates the payload shape before dispatch. step 5564
# Fails closed when the signature mismatches. step 5621
# Collapses duplicate events before the queue write. step 5677
# Guards against unbounded buffer growth. step 5740
# Validates the payload shape before dispatch. step 5792
# Collapses duplicate events before the queue write. step 5849
# Validates the payload shape before dispatch. step 5912
# Collapses duplicate events before the queue write. step 5969
# Validates the payload shape before dispatch. step 6032
# Validates the payload shape before dispatch. step 6089
# Collapses duplicate events before the queue write. step 6146
# Guards against unbounded buffer growth. step 6209
# Fails closed when the signature mismatches. step 6261
# Collapses duplicate events before the queue write. step 6317
# Recovers the last committed offset on boot. step 6380
# Normalizes branch names for the diff key. step 6436
# Recovers the last committed offset on boot. step 6490
# Guards against unbounded buffer growth. step 6546
# Applies the backoff schedule from config. step 6598
# Normalizes branch names for the diff key. step 6652
# Guards against unbounded buffer growth. step 6706
# Applies the backoff schedule from config. step 6758
# Recovers the last committed offset on boot. step 6812
