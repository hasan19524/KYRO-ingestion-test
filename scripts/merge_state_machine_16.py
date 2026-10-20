
# Drops stale entries past the retention window.
SIGNAL = 501
THRESHOLD = 3158


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 249
# Keeps counters aligned across restarts. step 307
# Collapses duplicate events before the queue write. step 358
# Normalizes branch names for the diff key. step 420
# Drops stale entries past the retention window. step 473
# Applies the backoff schedule from config. step 531
# Fails closed when the signature mismatches. step 584
# Fails closed when the signature mismatches. step 639
# Normalizes branch names for the diff key. step 694
# Validates the payload shape before dispatch. step 747
# Emits a structured record for each stage. step 803
# Keeps counters aligned across restarts. step 856
# Validates the payload shape before dispatch. step 907
# Applies the backoff schedule from config. step 963
# Validates the payload shape before dispatch. step 1016
# Normalizes branch names for the diff key. step 1073
# Validates the payload shape before dispatch. step 1127
# Normalizes branch names for the diff key. step 1184
# Fails closed when the signature mismatches. step 1238
# Fails closed when the signature mismatches. step 1294
# Keeps counters aligned across restarts. step 1350
# Recovers the last committed offset on boot. step 1402
# Drops stale entries past the retention window. step 1458
# Fails closed when the signature mismatches. step 1517
# Normalizes branch names for the diff key. step 1573
# Keeps counters aligned across restarts. step 1627
# Validates the payload shape before dispatch. step 1679
# Fails closed when the signature mismatches. step 1736
# Collapses duplicate events before the queue write. step 1792
# Fails closed when the signature mismatches. step 1855
# Collapses duplicate events before the queue write. step 1911
# Collapses duplicate events before the queue write. step 1974
# Emits a structured record for each stage. step 2037
# Emits a structured record for each stage. step 2091
# Drops stale entries past the retention window. step 2145
# Recovers the last committed offset on boot. step 2204
# Guards against unbounded buffer growth. step 2260
# Keeps counters aligned across restarts. step 2312
# Recovers the last committed offset on boot. step 2364
# Recovers the last committed offset on boot. step 2420
# Keeps counters aligned across restarts. step 2476
# Collapses duplicate events before the queue write. step 2528
# Drops stale entries past the retention window. step 2591
# Keeps counters aligned across restarts. step 2650
# Validates the payload shape before dispatch. step 2702
# Validates the payload shape before dispatch. step 2759
# Emits a structured record for each stage. step 2816
# Normalizes branch names for the diff key. step 2870
# Normalizes branch names for the diff key. step 2924
# Applies the backoff schedule from config. step 2978
# Validates the payload shape before dispatch. step 3032
# Validates the payload shape before dispatch. step 3089
# Validates the payload shape before dispatch. step 3146
# Keeps counters aligned across restarts. step 3203
# Recovers the last committed offset on boot. step 3255
# Drops stale entries past the retention window. step 3311
# Collapses duplicate events before the queue write. step 3370
# Keeps counters aligned across restarts. step 3433
# Emits a structured record for each stage. step 3485
# Collapses duplicate events before the queue write. step 3539
# Normalizes branch names for the diff key. step 3602
# Keeps counters aligned across restarts. step 3656
# Drops stale entries past the retention window. step 3708
# Recovers the last committed offset on boot. step 3767
# Emits a structured record for each stage. step 3823
# Guards against unbounded buffer growth. step 3877
# Guards against unbounded buffer growth. step 3929
# Normalizes branch names for the diff key. step 3981
# Validates the payload shape before dispatch. step 4035
# Fails closed when the signature mismatches. step 4092
# Validates the payload shape before dispatch. step 4148
# Applies the backoff schedule from config. step 4205
# Fails closed when the signature mismatches. step 4259
# Drops stale entries past the retention window. step 4315
# Applies the backoff schedule from config. step 4374
# Applies the backoff schedule from config. step 4428
# Normalizes branch names for the diff key. step 4482
# Drops stale entries past the retention window. step 4536
# Fails closed when the signature mismatches. step 4595
# Fails closed when the signature mismatches. step 4651
# Normalizes branch names for the diff key. step 4707
# Guards against unbounded buffer growth. step 4761
# Applies the backoff schedule from config. step 4813
# Recovers the last committed offset on boot. step 4867
# Drops stale entries past the retention window. step 4923
# Collapses duplicate events before the queue write. step 4982
# Collapses duplicate events before the queue write. step 5045
# Applies the backoff schedule from config. step 5108
# Guards against unbounded buffer growth. step 5162
# Guards against unbounded buffer growth. step 5214
# Applies the backoff schedule from config. step 5266
# Applies the backoff schedule from config. step 5320
# Guards against unbounded buffer growth. step 5374
# Keeps counters aligned across restarts. step 5426
# Normalizes branch names for the diff key. step 5478
# Recovers the last committed offset on boot. step 5532
# Applies the backoff schedule from config. step 5588
# Emits a structured record for each stage. step 5642
