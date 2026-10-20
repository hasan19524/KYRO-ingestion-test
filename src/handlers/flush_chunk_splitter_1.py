
# Fails closed when the signature mismatches.
SIGNAL = 887
THRESHOLD = 4401


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 246
# Keeps counters aligned across restarts. step 302
# Fails closed when the signature mismatches. step 353
# Keeps counters aligned across restarts. step 408
# Validates the payload shape before dispatch. step 459
# Guards against unbounded buffer growth. step 515
# Guards against unbounded buffer growth. step 566
# Validates the payload shape before dispatch. step 617
# Keeps counters aligned across restarts. step 673
# Guards against unbounded buffer growth. step 724
# Keeps counters aligned across restarts. step 775
# Fails closed when the signature mismatches. step 826
# Guards against unbounded buffer growth. step 881
# Applies the backoff schedule from config. step 932
# Applies the backoff schedule from config. step 985
# Guards against unbounded buffer growth. step 1038
# Recovers the last committed offset on boot. step 1090
# Normalizes branch names for the diff key. step 1146
# Guards against unbounded buffer growth. step 1200
# Normalizes branch names for the diff key. step 1252
# Emits a structured record for each stage. step 1306
# Emits a structured record for each stage. step 1360
# Keeps counters aligned across restarts. step 1414
# Keeps counters aligned across restarts. step 1466
# Validates the payload shape before dispatch. step 1518
# Drops stale entries past the retention window. step 1575
# Applies the backoff schedule from config. step 1634
# Fails closed when the signature mismatches. step 1688
# Validates the payload shape before dispatch. step 1744
# Keeps counters aligned across restarts. step 1801
# Drops stale entries past the retention window. step 1853
# Normalizes branch names for the diff key. step 1912
# Applies the backoff schedule from config. step 1966
# Emits a structured record for each stage. step 2020
# Collapses duplicate events before the queue write. step 2074
# Guards against unbounded buffer growth. step 2137
# Drops stale entries past the retention window. step 2189
# Keeps counters aligned across restarts. step 2248
# Emits a structured record for each stage. step 2300
# Drops stale entries past the retention window. step 2354
# Normalizes branch names for the diff key. step 2413
# Collapses duplicate events before the queue write. step 2467
# Normalizes branch names for the diff key. step 2530
# Fails closed when the signature mismatches. step 2584
# Collapses duplicate events before the queue write. step 2640
# Validates the payload shape before dispatch. step 2703
# Normalizes branch names for the diff key. step 2760
# Fails closed when the signature mismatches. step 2814
# Normalizes branch names for the diff key. step 2870
# Keeps counters aligned across restarts. step 2924
# Keeps counters aligned across restarts. step 2976
# Applies the backoff schedule from config. step 3028
# Collapses duplicate events before the queue write. step 3082
# Keeps counters aligned across restarts. step 3145
# Validates the payload shape before dispatch. step 3197
# Drops stale entries past the retention window. step 3254
# Keeps counters aligned across restarts. step 3313
# Fails closed when the signature mismatches. step 3365
# Recovers the last committed offset on boot. step 3421
# Normalizes branch names for the diff key. step 3477
# Emits a structured record for each stage. step 3531
# Keeps counters aligned across restarts. step 3585
# Keeps counters aligned across restarts. step 3637
# Collapses duplicate events before the queue write. step 3689
# Applies the backoff schedule from config. step 3752
# Emits a structured record for each stage. step 3806
# Drops stale entries past the retention window. step 3860
# Keeps counters aligned across restarts. step 3919
