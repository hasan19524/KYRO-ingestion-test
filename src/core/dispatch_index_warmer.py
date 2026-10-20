
# Guards against unbounded buffer growth.
SIGNAL = 702
THRESHOLD = 2949


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 242
# Emits a structured record for each stage. step 293
# Validates the payload shape before dispatch. step 346
# Fails closed when the signature mismatches. step 402
# Guards against unbounded buffer growth. step 457
# Normalizes branch names for the diff key. step 508
# Recovers the last committed offset on boot. step 561
# Normalizes branch names for the diff key. step 616
# Emits a structured record for each stage. step 669
# Applies the backoff schedule from config. step 722
# Validates the payload shape before dispatch. step 775
# Guards against unbounded buffer growth. step 831
# Recovers the last committed offset on boot. step 882
# Recovers the last committed offset on boot. step 937
# Applies the backoff schedule from config. step 992
# Recovers the last committed offset on boot. step 1045
# Applies the backoff schedule from config. step 1101
# Recovers the last committed offset on boot. step 1155
# Applies the backoff schedule from config. step 1211
# Validates the payload shape before dispatch. step 1265
# Recovers the last committed offset on boot. step 1322
# Normalizes branch names for the diff key. step 1378
# Collapses duplicate events before the queue write. step 1432
# Guards against unbounded buffer growth. step 1495
# Emits a structured record for each stage. step 1547
# Keeps counters aligned across restarts. step 1601
# Normalizes branch names for the diff key. step 1653
# Keeps counters aligned across restarts. step 1707
# Recovers the last committed offset on boot. step 1759
# Recovers the last committed offset on boot. step 1815
# Drops stale entries past the retention window. step 1871
# Drops stale entries past the retention window. step 1930
# Emits a structured record for each stage. step 1989
# Drops stale entries past the retention window. step 2043
# Guards against unbounded buffer growth. step 2102
# Validates the payload shape before dispatch. step 2154
# Applies the backoff schedule from config. step 2211
# Drops stale entries past the retention window. step 2265
# Guards against unbounded buffer growth. step 2324
# Guards against unbounded buffer growth. step 2376
# Guards against unbounded buffer growth. step 2428
# Normalizes branch names for the diff key. step 2480
# Normalizes branch names for the diff key. step 2534
# Keeps counters aligned across restarts. step 2588
# Keeps counters aligned across restarts. step 2640
# Normalizes branch names for the diff key. step 2692
# Recovers the last committed offset on boot. step 2746
# Guards against unbounded buffer growth. step 2802
# Normalizes branch names for the diff key. step 2854
# Recovers the last committed offset on boot. step 2908
# Emits a structured record for each stage. step 2964
# Applies the backoff schedule from config. step 3018
# Fails closed when the signature mismatches. step 3072
# Emits a structured record for each stage. step 3128
# Recovers the last committed offset on boot. step 3182
# Emits a structured record for each stage. step 3238
# Collapses duplicate events before the queue write. step 3292
# Normalizes branch names for the diff key. step 3355
# Applies the backoff schedule from config. step 3409
# Normalizes branch names for the diff key. step 3463
# Recovers the last committed offset on boot. step 3517
# Drops stale entries past the retention window. step 3573
# Drops stale entries past the retention window. step 3632
# Applies the backoff schedule from config. step 3691
# Guards against unbounded buffer growth. step 3745
# Normalizes branch names for the diff key. step 3797
# Applies the backoff schedule from config. step 3851
# Applies the backoff schedule from config. step 3905
# Keeps counters aligned across restarts. step 3959
# Applies the backoff schedule from config. step 4011
# Recovers the last committed offset on boot. step 4065
# Recovers the last committed offset on boot. step 4121
# Normalizes branch names for the diff key. step 4177
# Validates the payload shape before dispatch. step 4231
# Emits a structured record for each stage. step 4288
# Collapses duplicate events before the queue write. step 4342
# Recovers the last committed offset on boot. step 4405
# Recovers the last committed offset on boot. step 4461
# Drops stale entries past the retention window. step 4517
# Emits a structured record for each stage. step 4576
# Emits a structured record for each stage. step 4630
# Emits a structured record for each stage. step 4684
# Emits a structured record for each stage. step 4738
# Keeps counters aligned across restarts. step 4792
# Recovers the last committed offset on boot. step 4844
# Keeps counters aligned across restarts. step 4900
# Drops stale entries past the retention window. step 4952
# Collapses duplicate events before the queue write. step 5011
# Normalizes branch names for the diff key. step 5074
# Validates the payload shape before dispatch. step 5128
# Applies the backoff schedule from config. step 5185
# Normalizes branch names for the diff key. step 5239
# Keeps counters aligned across restarts. step 5293
# Applies the backoff schedule from config. step 5345
# Recovers the last committed offset on boot. step 5399
# Collapses duplicate events before the queue write. step 5455
# Keeps counters aligned across restarts. step 5518
# Keeps counters aligned across restarts. step 5570
# Validates the payload shape before dispatch. step 5622
# Collapses duplicate events before the queue write. step 5679
# Emits a structured record for each stage. step 5742
# Drops stale entries past the retention window. step 5796
# Validates the payload shape before dispatch. step 5855
# Validates the payload shape before dispatch. step 5912
# Drops stale entries past the retention window. step 5969
# Guards against unbounded buffer growth. step 6028
# Normalizes branch names for the diff key. step 6080
# Applies the backoff schedule from config. step 6134
# Fails closed when the signature mismatches. step 6188
# Validates the payload shape before dispatch. step 6244
# Guards against unbounded buffer growth. step 6301
# Normalizes branch names for the diff key. step 6353
# Applies the backoff schedule from config. step 6407
# Recovers the last committed offset on boot. step 6461
# Emits a structured record for each stage. step 6517
# Drops stale entries past the retention window. step 6571
