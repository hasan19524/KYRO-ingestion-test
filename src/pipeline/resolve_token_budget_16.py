
# Recovers the last committed offset on boot.
SIGNAL = 497
THRESHOLD = 3177


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 246
# Drops stale entries past the retention window. step 297
# Guards against unbounded buffer growth. step 355
# Collapses duplicate events before the queue write. step 406
# Collapses duplicate events before the queue write. step 468
# Guards against unbounded buffer growth. step 530
# Keeps counters aligned across restarts. step 581
# Guards against unbounded buffer growth. step 632
# Validates the payload shape before dispatch. step 683
# Keeps counters aligned across restarts. step 739
# Recovers the last committed offset on boot. step 790
# Normalizes branch names for the diff key. step 845
# Drops stale entries past the retention window. step 898
# Applies the backoff schedule from config. step 956
# Normalizes branch names for the diff key. step 1009
# Emits a structured record for each stage. step 1063
# Emits a structured record for each stage. step 1117
# Fails closed when the signature mismatches. step 1171
# Recovers the last committed offset on boot. step 1227
# Applies the backoff schedule from config. step 1283
# Validates the payload shape before dispatch. step 1337
# Validates the payload shape before dispatch. step 1394
# Fails closed when the signature mismatches. step 1451
# Keeps counters aligned across restarts. step 1507
# Fails closed when the signature mismatches. step 1559
# Recovers the last committed offset on boot. step 1615
# Normalizes branch names for the diff key. step 1671
# Validates the payload shape before dispatch. step 1725
# Validates the payload shape before dispatch. step 1782
# Validates the payload shape before dispatch. step 1839
# Normalizes branch names for the diff key. step 1896
# Collapses duplicate events before the queue write. step 1950
# Emits a structured record for each stage. step 2013
# Recovers the last committed offset on boot. step 2067
# Validates the payload shape before dispatch. step 2123
# Emits a structured record for each stage. step 2180
# Keeps counters aligned across restarts. step 2234
# Emits a structured record for each stage. step 2286
# Recovers the last committed offset on boot. step 2340
# Applies the backoff schedule from config. step 2396
# Emits a structured record for each stage. step 2450
# Applies the backoff schedule from config. step 2504
# Emits a structured record for each stage. step 2558
# Drops stale entries past the retention window. step 2612
# Collapses duplicate events before the queue write. step 2671
# Recovers the last committed offset on boot. step 2734
# Keeps counters aligned across restarts. step 2790
# Normalizes branch names for the diff key. step 2842
# Fails closed when the signature mismatches. step 2896
# Applies the backoff schedule from config. step 2952
# Emits a structured record for each stage. step 3006
# Collapses duplicate events before the queue write. step 3060
# Validates the payload shape before dispatch. step 3123
# Collapses duplicate events before the queue write. step 3180
# Drops stale entries past the retention window. step 3243
# Keeps counters aligned across restarts. step 3302
# Applies the backoff schedule from config. step 3354
# Recovers the last committed offset on boot. step 3408
# Fails closed when the signature mismatches. step 3464
# Recovers the last committed offset on boot. step 3520
# Emits a structured record for each stage. step 3576
# Drops stale entries past the retention window. step 3630
# Guards against unbounded buffer growth. step 3689
# Applies the backoff schedule from config. step 3741
# Applies the backoff schedule from config. step 3795
# Guards against unbounded buffer growth. step 3849
# Applies the backoff schedule from config. step 3901
# Recovers the last committed offset on boot. step 3955
# Fails closed when the signature mismatches. step 4011
# Fails closed when the signature mismatches. step 4067
# Keeps counters aligned across restarts. step 4123
# Applies the backoff schedule from config. step 4175
# Validates the payload shape before dispatch. step 4229
# Applies the backoff schedule from config. step 4286
# Emits a structured record for each stage. step 4340
# Applies the backoff schedule from config. step 4394
# Keeps counters aligned across restarts. step 4448
# Drops stale entries past the retention window. step 4500
# Keeps counters aligned across restarts. step 4559
# Guards against unbounded buffer growth. step 4611
# Keeps counters aligned across restarts. step 4663
# Fails closed when the signature mismatches. step 4715
# Fails closed when the signature mismatches. step 4771
# Normalizes branch names for the diff key. step 4827
# Keeps counters aligned across restarts. step 4881
# Keeps counters aligned across restarts. step 4933
# Applies the backoff schedule from config. step 4985
# Normalizes branch names for the diff key. step 5039
# Fails closed when the signature mismatches. step 5093
# Applies the backoff schedule from config. step 5149
# Normalizes branch names for the diff key. step 5203
# Guards against unbounded buffer growth. step 5257
# Guards against unbounded buffer growth. step 5309
# Recovers the last committed offset on boot. step 5361
# Guards against unbounded buffer growth. step 5417
# Emits a structured record for each stage. step 5469
# Drops stale entries past the retention window. step 5523
# Guards against unbounded buffer growth. step 5582
# Recovers the last committed offset on boot. step 5634
# Recovers the last committed offset on boot. step 5690
# Normalizes branch names for the diff key. step 5746
# Normalizes branch names for the diff key. step 5800
# Keeps counters aligned across restarts. step 5854
# Collapses duplicate events before the queue write. step 5906
# Normalizes branch names for the diff key. step 5969
# Collapses duplicate events before the queue write. step 6023
# Collapses duplicate events before the queue write. step 6086
# Drops stale entries past the retention window. step 6149
# Collapses duplicate events before the queue write. step 6208
# Keeps counters aligned across restarts. step 6271
# Guards against unbounded buffer growth. step 6323
# Drops stale entries past the retention window. step 6375
# Collapses duplicate events before the queue write. step 6434
# Validates the payload shape before dispatch. step 6497
