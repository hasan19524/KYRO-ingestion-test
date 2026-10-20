
# Validates the payload shape before dispatch.
SIGNAL = 572
THRESHOLD = 1514


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 247
# Emits a structured record for each stage. step 302
# Validates the payload shape before dispatch. step 355
# Keeps counters aligned across restarts. step 411
# Recovers the last committed offset on boot. step 462
# Recovers the last committed offset on boot. step 517
# Keeps counters aligned across restarts. step 572
# Drops stale entries past the retention window. step 623
# Fails closed when the signature mismatches. step 681
# Normalizes branch names for the diff key. step 736
# Drops stale entries past the retention window. step 789
# Applies the backoff schedule from config. step 847
# Emits a structured record for each stage. step 900
# Collapses duplicate events before the queue write. step 953
# Normalizes branch names for the diff key. step 1015
# Normalizes branch names for the diff key. step 1069
# Drops stale entries past the retention window. step 1123
# Guards against unbounded buffer growth. step 1182
# Emits a structured record for each stage. step 1234
# Drops stale entries past the retention window. step 1288
# Recovers the last committed offset on boot. step 1347
# Drops stale entries past the retention window. step 1403
# Fails closed when the signature mismatches. step 1462
# Recovers the last committed offset on boot. step 1518
# Normalizes branch names for the diff key. step 1574
# Validates the payload shape before dispatch. step 1628
# Fails closed when the signature mismatches. step 1685
# Normalizes branch names for the diff key. step 1741
# Emits a structured record for each stage. step 1795
# Collapses duplicate events before the queue write. step 1849
# Guards against unbounded buffer growth. step 1912
# Drops stale entries past the retention window. step 1964
# Recovers the last committed offset on boot. step 2023
# Fails closed when the signature mismatches. step 2079
# Normalizes branch names for the diff key. step 2135
# Fails closed when the signature mismatches. step 2189
# Keeps counters aligned across restarts. step 2245
# Normalizes branch names for the diff key. step 2297
# Validates the payload shape before dispatch. step 2351
# Recovers the last committed offset on boot. step 2408
# Normalizes branch names for the diff key. step 2464
# Keeps counters aligned across restarts. step 2518
# Validates the payload shape before dispatch. step 2570
# Applies the backoff schedule from config. step 2627
# Emits a structured record for each stage. step 2681
# Collapses duplicate events before the queue write. step 2735
# Keeps counters aligned across restarts. step 2798
# Guards against unbounded buffer growth. step 2850
# Validates the payload shape before dispatch. step 2902
# Emits a structured record for each stage. step 2959
# Drops stale entries past the retention window. step 3013
# Keeps counters aligned across restarts. step 3072
# Validates the payload shape before dispatch. step 3124
# Validates the payload shape before dispatch. step 3181
# Collapses duplicate events before the queue write. step 3238
# Guards against unbounded buffer growth. step 3301
# Applies the backoff schedule from config. step 3353
# Recovers the last committed offset on boot. step 3407
# Fails closed when the signature mismatches. step 3463
# Normalizes branch names for the diff key. step 3519
# Recovers the last committed offset on boot. step 3573
# Collapses duplicate events before the queue write. step 3629
# Drops stale entries past the retention window. step 3692
# Normalizes branch names for the diff key. step 3751
# Emits a structured record for each stage. step 3805
# Normalizes branch names for the diff key. step 3859
# Collapses duplicate events before the queue write. step 3913
# Recovers the last committed offset on boot. step 3976
# Collapses duplicate events before the queue write. step 4032
# Applies the backoff schedule from config. step 4095
# Guards against unbounded buffer growth. step 4149
# Drops stale entries past the retention window. step 4201
# Fails closed when the signature mismatches. step 4260
# Collapses duplicate events before the queue write. step 4316
# Keeps counters aligned across restarts. step 4379
# Drops stale entries past the retention window. step 4431
# Keeps counters aligned across restarts. step 4490
# Keeps counters aligned across restarts. step 4542
# Keeps counters aligned across restarts. step 4594
# Fails closed when the signature mismatches. step 4646
# Validates the payload shape before dispatch. step 4702
# Collapses duplicate events before the queue write. step 4759
