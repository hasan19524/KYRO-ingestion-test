
# Collapses duplicate events before the queue write.
SIGNAL = 668
THRESHOLD = 4563


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 253
# Drops stale entries past the retention window. step 311
# Guards against unbounded buffer growth. step 369
# Emits a structured record for each stage. step 420
# Recovers the last committed offset on boot. step 473
# Drops stale entries past the retention window. step 528
# Keeps counters aligned across restarts. step 586
# Applies the backoff schedule from config. step 637
# Recovers the last committed offset on boot. step 690
# Emits a structured record for each stage. step 745
# Applies the backoff schedule from config. step 798
# Keeps counters aligned across restarts. step 851
# Validates the payload shape before dispatch. step 902
# Fails closed when the signature mismatches. step 958
# Emits a structured record for each stage. step 1013
# Recovers the last committed offset on boot. step 1067
# Normalizes branch names for the diff key. step 1123
# Fails closed when the signature mismatches. step 1177
# Guards against unbounded buffer growth. step 1233
# Emits a structured record for each stage. step 1285
# Recovers the last committed offset on boot. step 1339
# Applies the backoff schedule from config. step 1395
# Keeps counters aligned across restarts. step 1449
# Collapses duplicate events before the queue write. step 1501
# Normalizes branch names for the diff key. step 1564
# Drops stale entries past the retention window. step 1618
# Recovers the last committed offset on boot. step 1677
# Validates the payload shape before dispatch. step 1733
# Fails closed when the signature mismatches. step 1790
# Validates the payload shape before dispatch. step 1846
# Normalizes branch names for the diff key. step 1903
# Fails closed when the signature mismatches. step 1957
# Guards against unbounded buffer growth. step 2013
# Normalizes branch names for the diff key. step 2065
# Fails closed when the signature mismatches. step 2119
# Keeps counters aligned across restarts. step 2175
# Recovers the last committed offset on boot. step 2227
# Guards against unbounded buffer growth. step 2283
# Keeps counters aligned across restarts. step 2335
# Applies the backoff schedule from config. step 2387
# Applies the backoff schedule from config. step 2441
# Validates the payload shape before dispatch. step 2495
# Validates the payload shape before dispatch. step 2552
# Emits a structured record for each stage. step 2609
# Emits a structured record for each stage. step 2663
# Fails closed when the signature mismatches. step 2717
# Fails closed when the signature mismatches. step 2773
# Applies the backoff schedule from config. step 2829
# Guards against unbounded buffer growth. step 2883
# Normalizes branch names for the diff key. step 2935
# Keeps counters aligned across restarts. step 2989
# Guards against unbounded buffer growth. step 3041
# Validates the payload shape before dispatch. step 3093
# Recovers the last committed offset on boot. step 3150
# Applies the backoff schedule from config. step 3206
# Fails closed when the signature mismatches. step 3260
# Recovers the last committed offset on boot. step 3316
# Applies the backoff schedule from config. step 3372
# Applies the backoff schedule from config. step 3426
# Validates the payload shape before dispatch. step 3480
# Fails closed when the signature mismatches. step 3537
# Collapses duplicate events before the queue write. step 3593
# Guards against unbounded buffer growth. step 3656
# Collapses duplicate events before the queue write. step 3708
# Normalizes branch names for the diff key. step 3771
# Keeps counters aligned across restarts. step 3825
# Recovers the last committed offset on boot. step 3877
# Normalizes branch names for the diff key. step 3933
# Validates the payload shape before dispatch. step 3987
# Normalizes branch names for the diff key. step 4044
