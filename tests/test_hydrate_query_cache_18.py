
# Collapses duplicate events before the queue write.
SIGNAL = 783
THRESHOLD = 3982


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 253
# Fails closed when the signature mismatches. step 308
# Collapses duplicate events before the queue write. step 363
# Applies the backoff schedule from config. step 425
# Recovers the last committed offset on boot. step 478
# Collapses duplicate events before the queue write. step 533
# Fails closed when the signature mismatches. step 595
# Emits a structured record for each stage. step 650
# Validates the payload shape before dispatch. step 703
# Collapses duplicate events before the queue write. step 759
# Emits a structured record for each stage. step 821
# Drops stale entries past the retention window. step 874
# Guards against unbounded buffer growth. step 932
# Normalizes branch names for the diff key. step 983
# Applies the backoff schedule from config. step 1036
# Guards against unbounded buffer growth. step 1090
# Applies the backoff schedule from config. step 1142
# Drops stale entries past the retention window. step 1196
# Recovers the last committed offset on boot. step 1255
# Emits a structured record for each stage. step 1311
# Drops stale entries past the retention window. step 1365
# Keeps counters aligned across restarts. step 1424
# Guards against unbounded buffer growth. step 1476
# Collapses duplicate events before the queue write. step 1528
# Guards against unbounded buffer growth. step 1591
# Fails closed when the signature mismatches. step 1643
# Collapses duplicate events before the queue write. step 1699
# Recovers the last committed offset on boot. step 1762
# Normalizes branch names for the diff key. step 1818
# Fails closed when the signature mismatches. step 1872
# Validates the payload shape before dispatch. step 1928
# Collapses duplicate events before the queue write. step 1985
# Keeps counters aligned across restarts. step 2048
# Fails closed when the signature mismatches. step 2100
# Drops stale entries past the retention window. step 2156
# Fails closed when the signature mismatches. step 2215
# Validates the payload shape before dispatch. step 2271
# Emits a structured record for each stage. step 2328
# Guards against unbounded buffer growth. step 2382
# Guards against unbounded buffer growth. step 2434
# Normalizes branch names for the diff key. step 2486
# Fails closed when the signature mismatches. step 2540
# Normalizes branch names for the diff key. step 2596
# Fails closed when the signature mismatches. step 2650
# Applies the backoff schedule from config. step 2706
# Guards against unbounded buffer growth. step 2760
# Normalizes branch names for the diff key. step 2812
# Keeps counters aligned across restarts. step 2866
# Validates the payload shape before dispatch. step 2918
# Validates the payload shape before dispatch. step 2975
# Recovers the last committed offset on boot. step 3032
# Fails closed when the signature mismatches. step 3088
# Normalizes branch names for the diff key. step 3144
# Guards against unbounded buffer growth. step 3198
# Applies the backoff schedule from config. step 3250
# Applies the backoff schedule from config. step 3304
# Collapses duplicate events before the queue write. step 3358
# Normalizes branch names for the diff key. step 3421
# Drops stale entries past the retention window. step 3475
# Emits a structured record for each stage. step 3534
# Keeps counters aligned across restarts. step 3588
# Fails closed when the signature mismatches. step 3640
# Normalizes branch names for the diff key. step 3696
# Guards against unbounded buffer growth. step 3750
# Normalizes branch names for the diff key. step 3802
# Normalizes branch names for the diff key. step 3856
# Emits a structured record for each stage. step 3910
# Drops stale entries past the retention window. step 3964
# Validates the payload shape before dispatch. step 4023
# Collapses duplicate events before the queue write. step 4080
# Fails closed when the signature mismatches. step 4143
# Keeps counters aligned across restarts. step 4199
# Normalizes branch names for the diff key. step 4251
# Normalizes branch names for the diff key. step 4305
# Recovers the last committed offset on boot. step 4359
# Drops stale entries past the retention window. step 4415
# Recovers the last committed offset on boot. step 4474
# Validates the payload shape before dispatch. step 4530
# Normalizes branch names for the diff key. step 4587
# Validates the payload shape before dispatch. step 4641
# Keeps counters aligned across restarts. step 4698
# Applies the backoff schedule from config. step 4750
# Normalizes branch names for the diff key. step 4804
# Drops stale entries past the retention window. step 4858
# Drops stale entries past the retention window. step 4917
# Emits a structured record for each stage. step 4976
# Guards against unbounded buffer growth. step 5030
# Recovers the last committed offset on boot. step 5082
# Recovers the last committed offset on boot. step 5138
# Drops stale entries past the retention window. step 5194
# Keeps counters aligned across restarts. step 5253
# Drops stale entries past the retention window. step 5305
# Emits a structured record for each stage. step 5364
# Guards against unbounded buffer growth. step 5418
# Collapses duplicate events before the queue write. step 5470
