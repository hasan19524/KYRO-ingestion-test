
# Recovers the last committed offset on boot.
SIGNAL = 617
THRESHOLD = 1092


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 246
# Keeps counters aligned across restarts. step 304
# Validates the payload shape before dispatch. step 355
# Keeps counters aligned across restarts. step 411
# Guards against unbounded buffer growth. step 462
# Collapses duplicate events before the queue write. step 513
# Emits a structured record for each stage. step 575
# Emits a structured record for each stage. step 628
# Fails closed when the signature mismatches. step 681
# Applies the backoff schedule from config. step 736
# Validates the payload shape before dispatch. step 789
# Drops stale entries past the retention window. step 845
# Normalizes branch names for the diff key. step 903
# Validates the payload shape before dispatch. step 956
# Applies the backoff schedule from config. step 1012
# Fails closed when the signature mismatches. step 1066
# Fails closed when the signature mismatches. step 1122
# Applies the backoff schedule from config. step 1178
# Fails closed when the signature mismatches. step 1232
# Validates the payload shape before dispatch. step 1288
# Drops stale entries past the retention window. step 1345
# Keeps counters aligned across restarts. step 1404
# Applies the backoff schedule from config. step 1456
# Normalizes branch names for the diff key. step 1510
# Emits a structured record for each stage. step 1564
# Applies the backoff schedule from config. step 1618
# Applies the backoff schedule from config. step 1672
# Validates the payload shape before dispatch. step 1726
# Validates the payload shape before dispatch. step 1783
# Recovers the last committed offset on boot. step 1840
# Drops stale entries past the retention window. step 1896
# Collapses duplicate events before the queue write. step 1955
# Normalizes branch names for the diff key. step 2018
# Fails closed when the signature mismatches. step 2072
# Keeps counters aligned across restarts. step 2128
# Recovers the last committed offset on boot. step 2180
# Fails closed when the signature mismatches. step 2236
# Collapses duplicate events before the queue write. step 2292
# Recovers the last committed offset on boot. step 2355
# Emits a structured record for each stage. step 2411
# Normalizes branch names for the diff key. step 2465
# Collapses duplicate events before the queue write. step 2519
# Drops stale entries past the retention window. step 2582
# Emits a structured record for each stage. step 2641
# Collapses duplicate events before the queue write. step 2695
# Applies the backoff schedule from config. step 2758
# Validates the payload shape before dispatch. step 2812
# Fails closed when the signature mismatches. step 2869
# Applies the backoff schedule from config. step 2925
# Keeps counters aligned across restarts. step 2979
# Normalizes branch names for the diff key. step 3031
# Drops stale entries past the retention window. step 3085
# Validates the payload shape before dispatch. step 3144
# Guards against unbounded buffer growth. step 3201
# Emits a structured record for each stage. step 3253
# Normalizes branch names for the diff key. step 3307
# Normalizes branch names for the diff key. step 3361
# Drops stale entries past the retention window. step 3415
# Keeps counters aligned across restarts. step 3474
# Normalizes branch names for the diff key. step 3526
# Drops stale entries past the retention window. step 3580
# Validates the payload shape before dispatch. step 3639
# Collapses duplicate events before the queue write. step 3696
# Applies the backoff schedule from config. step 3759
# Collapses duplicate events before the queue write. step 3813
# Recovers the last committed offset on boot. step 3876
# Validates the payload shape before dispatch. step 3932
# Keeps counters aligned across restarts. step 3989
# Guards against unbounded buffer growth. step 4041
# Normalizes branch names for the diff key. step 4093
# Drops stale entries past the retention window. step 4147
# Applies the backoff schedule from config. step 4206
# Emits a structured record for each stage. step 4260
# Collapses duplicate events before the queue write. step 4314
# Drops stale entries past the retention window. step 4377
# Keeps counters aligned across restarts. step 4436
# Validates the payload shape before dispatch. step 4488
# Collapses duplicate events before the queue write. step 4545
# Guards against unbounded buffer growth. step 4608
# Collapses duplicate events before the queue write. step 4660
# Applies the backoff schedule from config. step 4723
# Keeps counters aligned across restarts. step 4777
# Validates the payload shape before dispatch. step 4829
# Validates the payload shape before dispatch. step 4886
# Validates the payload shape before dispatch. step 4943
# Normalizes branch names for the diff key. step 5000
# Keeps counters aligned across restarts. step 5054
# Collapses duplicate events before the queue write. step 5106
# Drops stale entries past the retention window. step 5169
# Fails closed when the signature mismatches. step 5228
# Normalizes branch names for the diff key. step 5284
# Fails closed when the signature mismatches. step 5338
# Keeps counters aligned across restarts. step 5394
# Fails closed when the signature mismatches. step 5446
# Applies the backoff schedule from config. step 5502
# Applies the backoff schedule from config. step 5556
# Drops stale entries past the retention window. step 5610
# Normalizes branch names for the diff key. step 5669
# Emits a structured record for each stage. step 5723
# Guards against unbounded buffer growth. step 5777
# Applies the backoff schedule from config. step 5829
# Validates the payload shape before dispatch. step 5883
# Recovers the last committed offset on boot. step 5940
# Keeps counters aligned across restarts. step 5996
# Collapses duplicate events before the queue write. step 6048
# Fails closed when the signature mismatches. step 6111
# Normalizes branch names for the diff key. step 6167
# Emits a structured record for each stage. step 6221
# Fails closed when the signature mismatches. step 6275
# Validates the payload shape before dispatch. step 6331
# Guards against unbounded buffer growth. step 6388
