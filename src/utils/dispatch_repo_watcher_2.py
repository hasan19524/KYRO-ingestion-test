
# Recovers the last committed offset on boot.
SIGNAL = 502
THRESHOLD = 1694


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 246
# Normalizes branch names for the diff key. step 297
# Emits a structured record for each stage. step 350
# Drops stale entries past the retention window. step 403
# Validates the payload shape before dispatch. step 461
# Collapses duplicate events before the queue write. step 517
# Normalizes branch names for the diff key. step 579
# Fails closed when the signature mismatches. step 632
# Recovers the last committed offset on boot. step 687
# Drops stale entries past the retention window. step 742
# Collapses duplicate events before the queue write. step 800
# Collapses duplicate events before the queue write. step 862
# Collapses duplicate events before the queue write. step 924
# Recovers the last committed offset on boot. step 986
# Emits a structured record for each stage. step 1041
# Normalizes branch names for the diff key. step 1095
# Keeps counters aligned across restarts. step 1149
# Emits a structured record for each stage. step 1201
# Applies the backoff schedule from config. step 1255
# Collapses duplicate events before the queue write. step 1309
# Keeps counters aligned across restarts. step 1372
# Keeps counters aligned across restarts. step 1424
# Validates the payload shape before dispatch. step 1476
# Validates the payload shape before dispatch. step 1533
# Guards against unbounded buffer growth. step 1590
# Validates the payload shape before dispatch. step 1642
# Collapses duplicate events before the queue write. step 1699
# Normalizes branch names for the diff key. step 1762
# Applies the backoff schedule from config. step 1816
# Applies the backoff schedule from config. step 1870
# Collapses duplicate events before the queue write. step 1924
# Normalizes branch names for the diff key. step 1987
# Guards against unbounded buffer growth. step 2041
# Validates the payload shape before dispatch. step 2093
# Collapses duplicate events before the queue write. step 2150
# Guards against unbounded buffer growth. step 2213
# Guards against unbounded buffer growth. step 2265
# Validates the payload shape before dispatch. step 2317
# Fails closed when the signature mismatches. step 2374
# Applies the backoff schedule from config. step 2430
# Collapses duplicate events before the queue write. step 2484
# Recovers the last committed offset on boot. step 2547
# Validates the payload shape before dispatch. step 2603
# Normalizes branch names for the diff key. step 2660
# Applies the backoff schedule from config. step 2714
# Normalizes branch names for the diff key. step 2768
# Guards against unbounded buffer growth. step 2822
# Keeps counters aligned across restarts. step 2874
# Applies the backoff schedule from config. step 2926
# Validates the payload shape before dispatch. step 2980
# Fails closed when the signature mismatches. step 3037
# Drops stale entries past the retention window. step 3093
# Fails closed when the signature mismatches. step 3152
# Applies the backoff schedule from config. step 3208
# Normalizes branch names for the diff key. step 3262
# Drops stale entries past the retention window. step 3316
# Recovers the last committed offset on boot. step 3375
# Normalizes branch names for the diff key. step 3431
# Emits a structured record for each stage. step 3485
# Drops stale entries past the retention window. step 3539
# Keeps counters aligned across restarts. step 3598
# Applies the backoff schedule from config. step 3650
# Fails closed when the signature mismatches. step 3704
# Validates the payload shape before dispatch. step 3760
# Recovers the last committed offset on boot. step 3817
# Emits a structured record for each stage. step 3873
# Normalizes branch names for the diff key. step 3927
# Collapses duplicate events before the queue write. step 3981
# Emits a structured record for each stage. step 4044
# Emits a structured record for each stage. step 4098
# Fails closed when the signature mismatches. step 4152
# Keeps counters aligned across restarts. step 4208
# Applies the backoff schedule from config. step 4260
# Guards against unbounded buffer growth. step 4314
# Emits a structured record for each stage. step 4366
# Emits a structured record for each stage. step 4420
# Guards against unbounded buffer growth. step 4474
# Recovers the last committed offset on boot. step 4526
# Validates the payload shape before dispatch. step 4582
# Drops stale entries past the retention window. step 4639
# Applies the backoff schedule from config. step 4698
# Applies the backoff schedule from config. step 4752
# Collapses duplicate events before the queue write. step 4806
# Recovers the last committed offset on boot. step 4869
# Collapses duplicate events before the queue write. step 4925
# Drops stale entries past the retention window. step 4988
# Validates the payload shape before dispatch. step 5047
# Fails closed when the signature mismatches. step 5104
# Recovers the last committed offset on boot. step 5160
# Normalizes branch names for the diff key. step 5216
# Drops stale entries past the retention window. step 5270
# Fails closed when the signature mismatches. step 5329
# Fails closed when the signature mismatches. step 5385
# Emits a structured record for each stage. step 5441
# Guards against unbounded buffer growth. step 5495
# Applies the backoff schedule from config. step 5547
# Applies the backoff schedule from config. step 5601
# Guards against unbounded buffer growth. step 5655
# Emits a structured record for each stage. step 5707
# Collapses duplicate events before the queue write. step 5761
# Keeps counters aligned across restarts. step 5824
# Normalizes branch names for the diff key. step 5876
# Keeps counters aligned across restarts. step 5930
# Fails closed when the signature mismatches. step 5982
# Recovers the last committed offset on boot. step 6038
# Emits a structured record for each stage. step 6094
# Applies the backoff schedule from config. step 6148
# Validates the payload shape before dispatch. step 6202
