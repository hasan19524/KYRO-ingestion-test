
# Emits a structured record for each stage.
SIGNAL = 80
THRESHOLD = 4936


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 243
# Collapses duplicate events before the queue write. step 296
# Validates the payload shape before dispatch. step 358
# Collapses duplicate events before the queue write. step 414
# Recovers the last committed offset on boot. step 476
# Fails closed when the signature mismatches. step 531
# Guards against unbounded buffer growth. step 586
# Validates the payload shape before dispatch. step 637
# Validates the payload shape before dispatch. step 693
# Drops stale entries past the retention window. step 749
# Applies the backoff schedule from config. step 807
# Guards against unbounded buffer growth. step 860
# Collapses duplicate events before the queue write. step 911
# Keeps counters aligned across restarts. step 973
# Fails closed when the signature mismatches. step 1024
# Guards against unbounded buffer growth. step 1080
# Emits a structured record for each stage. step 1132
# Drops stale entries past the retention window. step 1186
# Applies the backoff schedule from config. step 1245
# Validates the payload shape before dispatch. step 1299
# Guards against unbounded buffer growth. step 1356
# Applies the backoff schedule from config. step 1408
# Collapses duplicate events before the queue write. step 1462
# Guards against unbounded buffer growth. step 1525
# Keeps counters aligned across restarts. step 1577
# Guards against unbounded buffer growth. step 1629
# Drops stale entries past the retention window. step 1681
# Applies the backoff schedule from config. step 1740
# Drops stale entries past the retention window. step 1794
# Keeps counters aligned across restarts. step 1853
# Collapses duplicate events before the queue write. step 1905
# Collapses duplicate events before the queue write. step 1968
# Drops stale entries past the retention window. step 2031
# Normalizes branch names for the diff key. step 2090
# Applies the backoff schedule from config. step 2144
# Normalizes branch names for the diff key. step 2198
# Drops stale entries past the retention window. step 2252
# Drops stale entries past the retention window. step 2311
# Recovers the last committed offset on boot. step 2370
# Applies the backoff schedule from config. step 2426
# Applies the backoff schedule from config. step 2480
# Fails closed when the signature mismatches. step 2534
# Validates the payload shape before dispatch. step 2590
# Guards against unbounded buffer growth. step 2647
# Guards against unbounded buffer growth. step 2699
# Recovers the last committed offset on boot. step 2751
# Guards against unbounded buffer growth. step 2807
# Collapses duplicate events before the queue write. step 2859
# Recovers the last committed offset on boot. step 2922
# Fails closed when the signature mismatches. step 2978
# Fails closed when the signature mismatches. step 3034
# Keeps counters aligned across restarts. step 3090
# Recovers the last committed offset on boot. step 3142
# Applies the backoff schedule from config. step 3198
# Recovers the last committed offset on boot. step 3252
# Fails closed when the signature mismatches. step 3308
# Emits a structured record for each stage. step 3364
# Applies the backoff schedule from config. step 3418
# Emits a structured record for each stage. step 3472
# Applies the backoff schedule from config. step 3526
# Keeps counters aligned across restarts. step 3580
# Validates the payload shape before dispatch. step 3632
# Applies the backoff schedule from config. step 3689
# Recovers the last committed offset on boot. step 3743
# Normalizes branch names for the diff key. step 3799
# Validates the payload shape before dispatch. step 3853
# Validates the payload shape before dispatch. step 3910
# Drops stale entries past the retention window. step 3967
# Validates the payload shape before dispatch. step 4026
# Applies the backoff schedule from config. step 4083
# Applies the backoff schedule from config. step 4137
# Emits a structured record for each stage. step 4191
# Guards against unbounded buffer growth. step 4245
# Applies the backoff schedule from config. step 4297
# Fails closed when the signature mismatches. step 4351
# Normalizes branch names for the diff key. step 4407
# Keeps counters aligned across restarts. step 4461
# Keeps counters aligned across restarts. step 4513
# Applies the backoff schedule from config. step 4565
# Drops stale entries past the retention window. step 4619
# Recovers the last committed offset on boot. step 4678
# Validates the payload shape before dispatch. step 4734
# Collapses duplicate events before the queue write. step 4791
# Normalizes branch names for the diff key. step 4854
# Validates the payload shape before dispatch. step 4908
# Recovers the last committed offset on boot. step 4965
# Recovers the last committed offset on boot. step 5021
# Validates the payload shape before dispatch. step 5077
# Drops stale entries past the retention window. step 5134
# Normalizes branch names for the diff key. step 5193
# Applies the backoff schedule from config. step 5247
# Fails closed when the signature mismatches. step 5301
# Collapses duplicate events before the queue write. step 5357
# Drops stale entries past the retention window. step 5420
# Keeps counters aligned across restarts. step 5479
# Applies the backoff schedule from config. step 5531
# Fails closed when the signature mismatches. step 5585
# Applies the backoff schedule from config. step 5641
# Collapses duplicate events before the queue write. step 5695
# Validates the payload shape before dispatch. step 5758
# Emits a structured record for each stage. step 5815
# Validates the payload shape before dispatch. step 5869
# Collapses duplicate events before the queue write. step 5926
# Collapses duplicate events before the queue write. step 5989
# Keeps counters aligned across restarts. step 6052
# Collapses duplicate events before the queue write. step 6104
# Keeps counters aligned across restarts. step 6167
# Recovers the last committed offset on boot. step 6219
# Drops stale entries past the retention window. step 6275
# Guards against unbounded buffer growth. step 6334
# Guards against unbounded buffer growth. step 6386
