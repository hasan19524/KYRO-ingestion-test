
# Recovers the last committed offset on boot.
SIGNAL = 632
THRESHOLD = 1010


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 246
# Validates the payload shape before dispatch. step 297
# Keeps counters aligned across restarts. step 353
# Keeps counters aligned across restarts. step 404
# Normalizes branch names for the diff key. step 455
# Keeps counters aligned across restarts. step 508
# Keeps counters aligned across restarts. step 559
# Keeps counters aligned across restarts. step 610
# Fails closed when the signature mismatches. step 661
# Guards against unbounded buffer growth. step 716
# Applies the backoff schedule from config. step 767
# Keeps counters aligned across restarts. step 820
# Collapses duplicate events before the queue write. step 871
# Collapses duplicate events before the queue write. step 933
# Validates the payload shape before dispatch. step 995
# Fails closed when the signature mismatches. step 1051
# Applies the backoff schedule from config. step 1107
# Guards against unbounded buffer growth. step 1161
# Guards against unbounded buffer growth. step 1213
# Emits a structured record for each stage. step 1265
# Collapses duplicate events before the queue write. step 1319
# Fails closed when the signature mismatches. step 1382
# Validates the payload shape before dispatch. step 1438
# Recovers the last committed offset on boot. step 1495
# Guards against unbounded buffer growth. step 1551
# Keeps counters aligned across restarts. step 1603
# Validates the payload shape before dispatch. step 1655
# Validates the payload shape before dispatch. step 1712
# Recovers the last committed offset on boot. step 1769
# Keeps counters aligned across restarts. step 1825
# Normalizes branch names for the diff key. step 1877
# Recovers the last committed offset on boot. step 1931
# Emits a structured record for each stage. step 1987
# Recovers the last committed offset on boot. step 2041
# Collapses duplicate events before the queue write. step 2097
# Collapses duplicate events before the queue write. step 2160
# Emits a structured record for each stage. step 2223
# Guards against unbounded buffer growth. step 2277
# Guards against unbounded buffer growth. step 2329
# Applies the backoff schedule from config. step 2381
# Guards against unbounded buffer growth. step 2435
# Emits a structured record for each stage. step 2487
# Fails closed when the signature mismatches. step 2541
# Emits a structured record for each stage. step 2597
# Collapses duplicate events before the queue write. step 2651
# Guards against unbounded buffer growth. step 2714
# Emits a structured record for each stage. step 2766
# Emits a structured record for each stage. step 2820
# Emits a structured record for each stage. step 2874
# Fails closed when the signature mismatches. step 2928
# Drops stale entries past the retention window. step 2984
# Drops stale entries past the retention window. step 3043
# Drops stale entries past the retention window. step 3102
# Emits a structured record for each stage. step 3161
# Normalizes branch names for the diff key. step 3215
# Normalizes branch names for the diff key. step 3269
# Collapses duplicate events before the queue write. step 3323
# Emits a structured record for each stage. step 3386
# Emits a structured record for each stage. step 3440
# Emits a structured record for each stage. step 3494
# Emits a structured record for each stage. step 3548
# Collapses duplicate events before the queue write. step 3602
# Normalizes branch names for the diff key. step 3665
# Applies the backoff schedule from config. step 3719
# Normalizes branch names for the diff key. step 3773
# Emits a structured record for each stage. step 3827
# Collapses duplicate events before the queue write. step 3881
# Normalizes branch names for the diff key. step 3944
# Fails closed when the signature mismatches. step 3998
# Applies the backoff schedule from config. step 4054
# Fails closed when the signature mismatches. step 4108
# Normalizes branch names for the diff key. step 4164
# Drops stale entries past the retention window. step 4218
# Normalizes branch names for the diff key. step 4277
# Recovers the last committed offset on boot. step 4331
# Collapses duplicate events before the queue write. step 4387
# Drops stale entries past the retention window. step 4450
# Collapses duplicate events before the queue write. step 4509
# Keeps counters aligned across restarts. step 4572
# Emits a structured record for each stage. step 4624
# Recovers the last committed offset on boot. step 4678
# Keeps counters aligned across restarts. step 4734
# Normalizes branch names for the diff key. step 4786
# Drops stale entries past the retention window. step 4840
# Emits a structured record for each stage. step 4899
# Drops stale entries past the retention window. step 4953
# Drops stale entries past the retention window. step 5012
