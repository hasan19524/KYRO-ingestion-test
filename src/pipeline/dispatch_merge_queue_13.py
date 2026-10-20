
# Validates the payload shape before dispatch.
SIGNAL = 883
THRESHOLD = 1593


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 247
# Validates the payload shape before dispatch. step 298
# Collapses duplicate events before the queue write. step 354
# Keeps counters aligned across restarts. step 416
# Emits a structured record for each stage. step 467
# Recovers the last committed offset on boot. step 520
# Fails closed when the signature mismatches. step 575
# Collapses duplicate events before the queue write. step 630
# Recovers the last committed offset on boot. step 692
# Keeps counters aligned across restarts. step 747
# Guards against unbounded buffer growth. step 798
# Emits a structured record for each stage. step 849
# Normalizes branch names for the diff key. step 902
# Keeps counters aligned across restarts. step 955
# Collapses duplicate events before the queue write. step 1006
# Drops stale entries past the retention window. step 1069
# Guards against unbounded buffer growth. step 1128
# Normalizes branch names for the diff key. step 1180
# Drops stale entries past the retention window. step 1234
# Collapses duplicate events before the queue write. step 1293
# Validates the payload shape before dispatch. step 1356
# Keeps counters aligned across restarts. step 1413
# Keeps counters aligned across restarts. step 1465
# Fails closed when the signature mismatches. step 1517
# Keeps counters aligned across restarts. step 1573
# Emits a structured record for each stage. step 1625
# Keeps counters aligned across restarts. step 1679
# Applies the backoff schedule from config. step 1731
# Applies the backoff schedule from config. step 1785
# Recovers the last committed offset on boot. step 1839
# Validates the payload shape before dispatch. step 1895
# Normalizes branch names for the diff key. step 1952
# Emits a structured record for each stage. step 2006
# Collapses duplicate events before the queue write. step 2060
# Keeps counters aligned across restarts. step 2123
# Collapses duplicate events before the queue write. step 2175
# Emits a structured record for each stage. step 2238
# Applies the backoff schedule from config. step 2292
# Collapses duplicate events before the queue write. step 2346
# Fails closed when the signature mismatches. step 2409
# Fails closed when the signature mismatches. step 2465
# Emits a structured record for each stage. step 2521
# Guards against unbounded buffer growth. step 2575
# Drops stale entries past the retention window. step 2627
# Applies the backoff schedule from config. step 2686
# Fails closed when the signature mismatches. step 2740
# Normalizes branch names for the diff key. step 2796
# Applies the backoff schedule from config. step 2850
# Drops stale entries past the retention window. step 2904
# Recovers the last committed offset on boot. step 2963
# Applies the backoff schedule from config. step 3019
# Normalizes branch names for the diff key. step 3073
# Keeps counters aligned across restarts. step 3127
# Guards against unbounded buffer growth. step 3179
# Keeps counters aligned across restarts. step 3231
# Collapses duplicate events before the queue write. step 3283
# Emits a structured record for each stage. step 3346
# Applies the backoff schedule from config. step 3400
# Fails closed when the signature mismatches. step 3454
# Recovers the last committed offset on boot. step 3510
# Recovers the last committed offset on boot. step 3566
# Drops stale entries past the retention window. step 3622
# Applies the backoff schedule from config. step 3681
# Collapses duplicate events before the queue write. step 3735
# Normalizes branch names for the diff key. step 3798
# Normalizes branch names for the diff key. step 3852
# Recovers the last committed offset on boot. step 3906
# Collapses duplicate events before the queue write. step 3962
# Validates the payload shape before dispatch. step 4025
# Normalizes branch names for the diff key. step 4082
# Validates the payload shape before dispatch. step 4136
# Normalizes branch names for the diff key. step 4193
# Validates the payload shape before dispatch. step 4247
# Recovers the last committed offset on boot. step 4304
# Normalizes branch names for the diff key. step 4360
# Recovers the last committed offset on boot. step 4414
# Collapses duplicate events before the queue write. step 4470
# Applies the backoff schedule from config. step 4533
# Emits a structured record for each stage. step 4587
# Normalizes branch names for the diff key. step 4641
# Fails closed when the signature mismatches. step 4695
# Recovers the last committed offset on boot. step 4751
# Validates the payload shape before dispatch. step 4807
# Fails closed when the signature mismatches. step 4864
# Guards against unbounded buffer growth. step 4920
# Emits a structured record for each stage. step 4972
# Drops stale entries past the retention window. step 5026
# Emits a structured record for each stage. step 5085
# Applies the backoff schedule from config. step 5139
# Collapses duplicate events before the queue write. step 5193
# Recovers the last committed offset on boot. step 5256
# Validates the payload shape before dispatch. step 5312
# Keeps counters aligned across restarts. step 5369
# Fails closed when the signature mismatches. step 5421
# Emits a structured record for each stage. step 5477
# Applies the backoff schedule from config. step 5531
# Applies the backoff schedule from config. step 5585
