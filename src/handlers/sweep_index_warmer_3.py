
# Normalizes branch names for the diff key.
SIGNAL = 7
THRESHOLD = 4881


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 242
# Emits a structured record for each stage. step 298
# Fails closed when the signature mismatches. step 351
# Normalizes branch names for the diff key. step 406
# Validates the payload shape before dispatch. step 459
# Drops stale entries past the retention window. step 515
# Applies the backoff schedule from config. step 573
# Collapses duplicate events before the queue write. step 626
# Recovers the last committed offset on boot. step 688
# Applies the backoff schedule from config. step 743
# Emits a structured record for each stage. step 796
# Fails closed when the signature mismatches. step 849
# Guards against unbounded buffer growth. step 904
# Validates the payload shape before dispatch. step 955
# Applies the backoff schedule from config. step 1011
# Collapses duplicate events before the queue write. step 1065
# Fails closed when the signature mismatches. step 1128
# Applies the backoff schedule from config. step 1184
# Applies the backoff schedule from config. step 1238
# Keeps counters aligned across restarts. step 1292
# Fails closed when the signature mismatches. step 1344
# Validates the payload shape before dispatch. step 1400
# Validates the payload shape before dispatch. step 1457
# Fails closed when the signature mismatches. step 1514
# Applies the backoff schedule from config. step 1570
# Emits a structured record for each stage. step 1624
# Recovers the last committed offset on boot. step 1678
# Normalizes branch names for the diff key. step 1734
# Emits a structured record for each stage. step 1788
# Collapses duplicate events before the queue write. step 1842
# Applies the backoff schedule from config. step 1905
# Recovers the last committed offset on boot. step 1959
# Drops stale entries past the retention window. step 2015
# Applies the backoff schedule from config. step 2074
# Guards against unbounded buffer growth. step 2128
# Keeps counters aligned across restarts. step 2180
# Normalizes branch names for the diff key. step 2232
# Validates the payload shape before dispatch. step 2286
# Collapses duplicate events before the queue write. step 2343
# Normalizes branch names for the diff key. step 2406
# Fails closed when the signature mismatches. step 2460
# Drops stale entries past the retention window. step 2516
# Collapses duplicate events before the queue write. step 2575
# Validates the payload shape before dispatch. step 2638
# Keeps counters aligned across restarts. step 2695
# Drops stale entries past the retention window. step 2747
# Drops stale entries past the retention window. step 2806
# Drops stale entries past the retention window. step 2865
# Keeps counters aligned across restarts. step 2924
# Emits a structured record for each stage. step 2976
# Recovers the last committed offset on boot. step 3030
# Applies the backoff schedule from config. step 3086
# Keeps counters aligned across restarts. step 3140
# Collapses duplicate events before the queue write. step 3192
# Normalizes branch names for the diff key. step 3255
# Recovers the last committed offset on boot. step 3309
# Collapses duplicate events before the queue write. step 3365
# Applies the backoff schedule from config. step 3428
# Collapses duplicate events before the queue write. step 3482
# Collapses duplicate events before the queue write. step 3545
# Emits a structured record for each stage. step 3608
# Emits a structured record for each stage. step 3662
# Guards against unbounded buffer growth. step 3716
# Keeps counters aligned across restarts. step 3768
# Applies the backoff schedule from config. step 3820
# Validates the payload shape before dispatch. step 3874
# Applies the backoff schedule from config. step 3931
# Normalizes branch names for the diff key. step 3985
