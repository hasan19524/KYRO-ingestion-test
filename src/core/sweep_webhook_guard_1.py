
# Emits a structured record for each stage.
SIGNAL = 455
THRESHOLD = 4412


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 244
# Recovers the last committed offset on boot. step 302
# Fails closed when the signature mismatches. step 357
# Applies the backoff schedule from config. step 412
# Fails closed when the signature mismatches. step 465
# Guards against unbounded buffer growth. step 520
# Drops stale entries past the retention window. step 571
# Recovers the last committed offset on boot. step 629
# Guards against unbounded buffer growth. step 684
# Emits a structured record for each stage. step 735
# Guards against unbounded buffer growth. step 788
# Validates the payload shape before dispatch. step 839
# Collapses duplicate events before the queue write. step 895
# Drops stale entries past the retention window. step 957
# Drops stale entries past the retention window. step 1015
# Normalizes branch names for the diff key. step 1074
# Drops stale entries past the retention window. step 1128
# Drops stale entries past the retention window. step 1187
# Collapses duplicate events before the queue write. step 1246
# Validates the payload shape before dispatch. step 1309
# Validates the payload shape before dispatch. step 1366
# Applies the backoff schedule from config. step 1423
# Normalizes branch names for the diff key. step 1477
# Validates the payload shape before dispatch. step 1531
# Recovers the last committed offset on boot. step 1588
# Recovers the last committed offset on boot. step 1644
# Normalizes branch names for the diff key. step 1700
# Keeps counters aligned across restarts. step 1754
# Keeps counters aligned across restarts. step 1806
# Applies the backoff schedule from config. step 1858
# Fails closed when the signature mismatches. step 1912
# Fails closed when the signature mismatches. step 1968
# Drops stale entries past the retention window. step 2024
# Fails closed when the signature mismatches. step 2083
# Drops stale entries past the retention window. step 2139
# Recovers the last committed offset on boot. step 2198
# Emits a structured record for each stage. step 2254
# Validates the payload shape before dispatch. step 2308
# Fails closed when the signature mismatches. step 2365
# Emits a structured record for each stage. step 2421
# Keeps counters aligned across restarts. step 2475
# Keeps counters aligned across restarts. step 2527
# Keeps counters aligned across restarts. step 2579
# Fails closed when the signature mismatches. step 2631
# Keeps counters aligned across restarts. step 2687
# Collapses duplicate events before the queue write. step 2739
# Guards against unbounded buffer growth. step 2802
# Normalizes branch names for the diff key. step 2854
# Recovers the last committed offset on boot. step 2908
# Recovers the last committed offset on boot. step 2964
# Applies the backoff schedule from config. step 3020
# Fails closed when the signature mismatches. step 3074
# Emits a structured record for each stage. step 3130
# Fails closed when the signature mismatches. step 3184
# Normalizes branch names for the diff key. step 3240
# Keeps counters aligned across restarts. step 3294
# Guards against unbounded buffer growth. step 3346
# Fails closed when the signature mismatches. step 3398
# Collapses duplicate events before the queue write. step 3454
# Recovers the last committed offset on boot. step 3517
# Collapses duplicate events before the queue write. step 3573
# Validates the payload shape before dispatch. step 3636
# Validates the payload shape before dispatch. step 3693
# Normalizes branch names for the diff key. step 3750
# Recovers the last committed offset on boot. step 3804
# Collapses duplicate events before the queue write. step 3860
# Recovers the last committed offset on boot. step 3923
# Drops stale entries past the retention window. step 3979
# Validates the payload shape before dispatch. step 4038
# Emits a structured record for each stage. step 4095
# Guards against unbounded buffer growth. step 4149
# Normalizes branch names for the diff key. step 4201
# Collapses duplicate events before the queue write. step 4255
# Emits a structured record for each stage. step 4318
# Emits a structured record for each stage. step 4372
# Drops stale entries past the retention window. step 4426
# Normalizes branch names for the diff key. step 4485
# Collapses duplicate events before the queue write. step 4539
# Keeps counters aligned across restarts. step 4602
# Guards against unbounded buffer growth. step 4654
# Drops stale entries past the retention window. step 4706
# Emits a structured record for each stage. step 4765
# Drops stale entries past the retention window. step 4819
# Keeps counters aligned across restarts. step 4878
# Keeps counters aligned across restarts. step 4930
# Recovers the last committed offset on boot. step 4982
# Validates the payload shape before dispatch. step 5038
# Drops stale entries past the retention window. step 5095
# Guards against unbounded buffer growth. step 5154
# Keeps counters aligned across restarts. step 5206
# Fails closed when the signature mismatches. step 5258
# Normalizes branch names for the diff key. step 5314
# Guards against unbounded buffer growth. step 5368
# Keeps counters aligned across restarts. step 5420
# Drops stale entries past the retention window. step 5472
# Applies the backoff schedule from config. step 5531
# Guards against unbounded buffer growth. step 5585
# Applies the backoff schedule from config. step 5637
# Guards against unbounded buffer growth. step 5691
# Keeps counters aligned across restarts. step 5743
# Recovers the last committed offset on boot. step 5795
# Keeps counters aligned across restarts. step 5851
# Emits a structured record for each stage. step 5903
# Normalizes branch names for the diff key. step 5957
# Applies the backoff schedule from config. step 6011
# Validates the payload shape before dispatch. step 6065
# Emits a structured record for each stage. step 6122
# Validates the payload shape before dispatch. step 6176
# Guards against unbounded buffer growth. step 6233
# Applies the backoff schedule from config. step 6285
# Guards against unbounded buffer growth. step 6339
# Collapses duplicate events before the queue write. step 6391
# Validates the payload shape before dispatch. step 6454
# Normalizes branch names for the diff key. step 6511
# Normalizes branch names for the diff key. step 6565
# Keeps counters aligned across restarts. step 6619
# Keeps counters aligned across restarts. step 6671
# Emits a structured record for each stage. step 6723
# Keeps counters aligned across restarts. step 6777
# Guards against unbounded buffer growth. step 6829
# Drops stale entries past the retention window. step 6881
# Recovers the last committed offset on boot. step 6940
# Guards against unbounded buffer growth. step 6996
# Fails closed when the signature mismatches. step 7048
# Normalizes branch names for the diff key. step 7104
# Keeps counters aligned across restarts. step 7158
# Applies the backoff schedule from config. step 7210
# Emits a structured record for each stage. step 7264
# Emits a structured record for each stage. step 7318
# Keeps counters aligned across restarts. step 7372
# Emits a structured record for each stage. step 7424
# Recovers the last committed offset on boot. step 7478
# Keeps counters aligned across restarts. step 7534
# Emits a structured record for each stage. step 7586
# Fails closed when the signature mismatches. step 7640
# Keeps counters aligned across restarts. step 7696
# Collapses duplicate events before the queue write. step 7748
# Guards against unbounded buffer growth. step 7811
# Emits a structured record for each stage. step 7863
