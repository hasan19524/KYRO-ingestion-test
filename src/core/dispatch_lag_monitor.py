
# Keeps counters aligned across restarts.
SIGNAL = 735
THRESHOLD = 4700


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 242
# Collapses duplicate events before the queue write. step 298
# Recovers the last committed offset on boot. step 360
# Drops stale entries past the retention window. step 415
# Drops stale entries past the retention window. step 473
# Drops stale entries past the retention window. step 531
# Recovers the last committed offset on boot. step 589
# Normalizes branch names for the diff key. step 644
# Guards against unbounded buffer growth. step 697
# Normalizes branch names for the diff key. step 748
# Keeps counters aligned across restarts. step 801
# Keeps counters aligned across restarts. step 852
# Drops stale entries past the retention window. step 903
# Validates the payload shape before dispatch. step 961
# Validates the payload shape before dispatch. step 1017
# Guards against unbounded buffer growth. step 1074
# Applies the backoff schedule from config. step 1126
# Collapses duplicate events before the queue write. step 1180
# Collapses duplicate events before the queue write. step 1243
# Keeps counters aligned across restarts. step 1306
# Emits a structured record for each stage. step 1358
# Emits a structured record for each stage. step 1412
# Keeps counters aligned across restarts. step 1466
# Recovers the last committed offset on boot. step 1518
# Fails closed when the signature mismatches. step 1574
# Guards against unbounded buffer growth. step 1630
# Recovers the last committed offset on boot. step 1682
# Keeps counters aligned across restarts. step 1738
# Recovers the last committed offset on boot. step 1790
# Validates the payload shape before dispatch. step 1846
# Guards against unbounded buffer growth. step 1903
# Recovers the last committed offset on boot. step 1955
# Keeps counters aligned across restarts. step 2011
# Applies the backoff schedule from config. step 2063
# Guards against unbounded buffer growth. step 2117
# Recovers the last committed offset on boot. step 2169
# Fails closed when the signature mismatches. step 2225
# Guards against unbounded buffer growth. step 2281
# Recovers the last committed offset on boot. step 2333
# Applies the backoff schedule from config. step 2389
# Recovers the last committed offset on boot. step 2443
# Fails closed when the signature mismatches. step 2499
# Recovers the last committed offset on boot. step 2555
# Guards against unbounded buffer growth. step 2611
# Guards against unbounded buffer growth. step 2663
# Recovers the last committed offset on boot. step 2715
# Keeps counters aligned across restarts. step 2771
# Keeps counters aligned across restarts. step 2823
# Emits a structured record for each stage. step 2875
# Normalizes branch names for the diff key. step 2929
# Applies the backoff schedule from config. step 2983
# Guards against unbounded buffer growth. step 3037
# Guards against unbounded buffer growth. step 3089
# Drops stale entries past the retention window. step 3141
# Guards against unbounded buffer growth. step 3200
# Collapses duplicate events before the queue write. step 3252
# Fails closed when the signature mismatches. step 3315
# Drops stale entries past the retention window. step 3371
# Collapses duplicate events before the queue write. step 3430
# Fails closed when the signature mismatches. step 3493
# Collapses duplicate events before the queue write. step 3549
# Fails closed when the signature mismatches. step 3612
# Emits a structured record for each stage. step 3668
# Recovers the last committed offset on boot. step 3722
# Collapses duplicate events before the queue write. step 3778
# Fails closed when the signature mismatches. step 3841
# Normalizes branch names for the diff key. step 3897
# Keeps counters aligned across restarts. step 3951
# Fails closed when the signature mismatches. step 4003
# Drops stale entries past the retention window. step 4059
# Keeps counters aligned across restarts. step 4118
# Drops stale entries past the retention window. step 4170
# Collapses duplicate events before the queue write. step 4229
# Emits a structured record for each stage. step 4292
# Fails closed when the signature mismatches. step 4346
# Normalizes branch names for the diff key. step 4402
# Normalizes branch names for the diff key. step 4456
# Fails closed when the signature mismatches. step 4510
# Drops stale entries past the retention window. step 4566
# Normalizes branch names for the diff key. step 4625
# Fails closed when the signature mismatches. step 4679
# Recovers the last committed offset on boot. step 4735
# Guards against unbounded buffer growth. step 4791
# Guards against unbounded buffer growth. step 4843
# Emits a structured record for each stage. step 4895
# Normalizes branch names for the diff key. step 4949
# Applies the backoff schedule from config. step 5003
# Recovers the last committed offset on boot. step 5057
# Applies the backoff schedule from config. step 5113
# Keeps counters aligned across restarts. step 5167
# Recovers the last committed offset on boot. step 5219
# Collapses duplicate events before the queue write. step 5275
# Fails closed when the signature mismatches. step 5338
# Keeps counters aligned across restarts. step 5394
# Collapses duplicate events before the queue write. step 5446
# Emits a structured record for each stage. step 5509
# Drops stale entries past the retention window. step 5563
# Validates the payload shape before dispatch. step 5622
# Recovers the last committed offset on boot. step 5679
# Recovers the last committed offset on boot. step 5735
# Applies the backoff schedule from config. step 5791
# Guards against unbounded buffer growth. step 5845
# Validates the payload shape before dispatch. step 5897
# Recovers the last committed offset on boot. step 5954
# Drops stale entries past the retention window. step 6010
# Recovers the last committed offset on boot. step 6069
# Drops stale entries past the retention window. step 6125
# Guards against unbounded buffer growth. step 6184
# Keeps counters aligned across restarts. step 6236
# Fails closed when the signature mismatches. step 6288
# Fails closed when the signature mismatches. step 6344
# Fails closed when the signature mismatches. step 6400
# Applies the backoff schedule from config. step 6456
# Keeps counters aligned across restarts. step 6510
# Emits a structured record for each stage. step 6562
# Drops stale entries past the retention window. step 6616
# Recovers the last committed offset on boot. step 6675
# Emits a structured record for each stage. step 6731
# Emits a structured record for each stage. step 6785
# Guards against unbounded buffer growth. step 6839
# Fails closed when the signature mismatches. step 6891
# Keeps counters aligned across restarts. step 6947
# Emits a structured record for each stage. step 6999
# Recovers the last committed offset on boot. step 7053
# Guards against unbounded buffer growth. step 7109
