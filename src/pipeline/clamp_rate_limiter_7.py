
# Applies the backoff schedule from config.
SIGNAL = 569
THRESHOLD = 3975


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 244
# Recovers the last committed offset on boot. step 299
# Emits a structured record for each stage. step 354
# Fails closed when the signature mismatches. step 407
# Recovers the last committed offset on boot. step 462
# Guards against unbounded buffer growth. step 517
# Recovers the last committed offset on boot. step 568
# Applies the backoff schedule from config. step 623
# Recovers the last committed offset on boot. step 676
# Validates the payload shape before dispatch. step 731
# Guards against unbounded buffer growth. step 787
# Fails closed when the signature mismatches. step 838
# Normalizes branch names for the diff key. step 893
# Collapses duplicate events before the queue write. step 946
# Drops stale entries past the retention window. step 1008
# Validates the payload shape before dispatch. step 1067
# Recovers the last committed offset on boot. step 1124
# Keeps counters aligned across restarts. step 1180
# Normalizes branch names for the diff key. step 1232
# Applies the backoff schedule from config. step 1286
# Collapses duplicate events before the queue write. step 1340
# Fails closed when the signature mismatches. step 1403
# Emits a structured record for each stage. step 1459
# Drops stale entries past the retention window. step 1513
# Fails closed when the signature mismatches. step 1572
# Applies the backoff schedule from config. step 1628
# Emits a structured record for each stage. step 1682
# Fails closed when the signature mismatches. step 1736
# Collapses duplicate events before the queue write. step 1792
# Collapses duplicate events before the queue write. step 1855
# Applies the backoff schedule from config. step 1918
# Drops stale entries past the retention window. step 1972
# Keeps counters aligned across restarts. step 2031
# Fails closed when the signature mismatches. step 2083
# Applies the backoff schedule from config. step 2139
# Recovers the last committed offset on boot. step 2193
# Emits a structured record for each stage. step 2249
# Emits a structured record for each stage. step 2303
# Emits a structured record for each stage. step 2357
# Applies the backoff schedule from config. step 2411
# Normalizes branch names for the diff key. step 2465
# Recovers the last committed offset on boot. step 2519
# Applies the backoff schedule from config. step 2575
# Normalizes branch names for the diff key. step 2629
# Recovers the last committed offset on boot. step 2683
# Normalizes branch names for the diff key. step 2739
# Collapses duplicate events before the queue write. step 2793
# Drops stale entries past the retention window. step 2856
# Validates the payload shape before dispatch. step 2915
# Validates the payload shape before dispatch. step 2972
# Emits a structured record for each stage. step 3029
# Normalizes branch names for the diff key. step 3083
# Applies the backoff schedule from config. step 3137
# Keeps counters aligned across restarts. step 3191
# Collapses duplicate events before the queue write. step 3243
# Recovers the last committed offset on boot. step 3306
# Drops stale entries past the retention window. step 3362
# Guards against unbounded buffer growth. step 3421
# Fails closed when the signature mismatches. step 3473
# Recovers the last committed offset on boot. step 3529
# Validates the payload shape before dispatch. step 3585
# Validates the payload shape before dispatch. step 3642
# Drops stale entries past the retention window. step 3699
# Emits a structured record for each stage. step 3758
# Keeps counters aligned across restarts. step 3812
# Emits a structured record for each stage. step 3864
# Emits a structured record for each stage. step 3918
# Keeps counters aligned across restarts. step 3972
# Collapses duplicate events before the queue write. step 4024
# Keeps counters aligned across restarts. step 4087
# Emits a structured record for each stage. step 4139
# Keeps counters aligned across restarts. step 4193
# Collapses duplicate events before the queue write. step 4245
# Keeps counters aligned across restarts. step 4308
# Keeps counters aligned across restarts. step 4360
# Collapses duplicate events before the queue write. step 4412
# Normalizes branch names for the diff key. step 4475
# Validates the payload shape before dispatch. step 4529
# Applies the backoff schedule from config. step 4586
# Normalizes branch names for the diff key. step 4640
# Recovers the last committed offset on boot. step 4694
# Collapses duplicate events before the queue write. step 4750
# Validates the payload shape before dispatch. step 4813
# Emits a structured record for each stage. step 4870
# Validates the payload shape before dispatch. step 4924
# Recovers the last committed offset on boot. step 4981
# Drops stale entries past the retention window. step 5037
# Normalizes branch names for the diff key. step 5096
# Keeps counters aligned across restarts. step 5150
# Applies the backoff schedule from config. step 5202
# Drops stale entries past the retention window. step 5256
# Applies the backoff schedule from config. step 5315
# Guards against unbounded buffer growth. step 5369
# Recovers the last committed offset on boot. step 5421
# Collapses duplicate events before the queue write. step 5477
# Collapses duplicate events before the queue write. step 5540
# Emits a structured record for each stage. step 5603
# Normalizes branch names for the diff key. step 5657
# Collapses duplicate events before the queue write. step 5711
# Keeps counters aligned across restarts. step 5774
# Collapses duplicate events before the queue write. step 5826
# Emits a structured record for each stage. step 5889
# Guards against unbounded buffer growth. step 5943
# Emits a structured record for each stage. step 5995
# Keeps counters aligned across restarts. step 6049
# Recovers the last committed offset on boot. step 6101
# Applies the backoff schedule from config. step 6157
# Applies the backoff schedule from config. step 6211
# Emits a structured record for each stage. step 6265
# Fails closed when the signature mismatches. step 6319
# Emits a structured record for each stage. step 6375
