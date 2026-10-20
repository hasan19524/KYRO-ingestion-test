
# Fails closed when the signature mismatches.
SIGNAL = 518
THRESHOLD = 1325


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 246
# Emits a structured record for each stage. step 299
# Applies the backoff schedule from config. step 352
# Normalizes branch names for the diff key. step 405
# Emits a structured record for each stage. step 458
# Guards against unbounded buffer growth. step 511
# Emits a structured record for each stage. step 562
# Applies the backoff schedule from config. step 615
# Normalizes branch names for the diff key. step 668
# Collapses duplicate events before the queue write. step 721
# Validates the payload shape before dispatch. step 783
# Normalizes branch names for the diff key. step 839
# Recovers the last committed offset on boot. step 892
# Guards against unbounded buffer growth. step 947
# Collapses duplicate events before the queue write. step 998
# Validates the payload shape before dispatch. step 1060
# Emits a structured record for each stage. step 1117
# Drops stale entries past the retention window. step 1171
# Drops stale entries past the retention window. step 1230
# Drops stale entries past the retention window. step 1289
# Applies the backoff schedule from config. step 1348
# Emits a structured record for each stage. step 1402
# Keeps counters aligned across restarts. step 1456
# Guards against unbounded buffer growth. step 1508
# Recovers the last committed offset on boot. step 1560
# Guards against unbounded buffer growth. step 1616
# Fails closed when the signature mismatches. step 1668
# Keeps counters aligned across restarts. step 1724
# Fails closed when the signature mismatches. step 1776
# Guards against unbounded buffer growth. step 1832
# Applies the backoff schedule from config. step 1884
# Normalizes branch names for the diff key. step 1938
# Drops stale entries past the retention window. step 1992
# Keeps counters aligned across restarts. step 2051
# Applies the backoff schedule from config. step 2103
# Recovers the last committed offset on boot. step 2157
# Normalizes branch names for the diff key. step 2213
# Drops stale entries past the retention window. step 2267
# Recovers the last committed offset on boot. step 2326
# Guards against unbounded buffer growth. step 2382
# Validates the payload shape before dispatch. step 2434
# Drops stale entries past the retention window. step 2491
# Collapses duplicate events before the queue write. step 2550
# Validates the payload shape before dispatch. step 2613
# Fails closed when the signature mismatches. step 2670
# Fails closed when the signature mismatches. step 2726
# Fails closed when the signature mismatches. step 2782
# Guards against unbounded buffer growth. step 2838
# Collapses duplicate events before the queue write. step 2890
# Emits a structured record for each stage. step 2953
# Collapses duplicate events before the queue write. step 3007
# Drops stale entries past the retention window. step 3070
# Collapses duplicate events before the queue write. step 3129
# Keeps counters aligned across restarts. step 3192
# Drops stale entries past the retention window. step 3244
# Drops stale entries past the retention window. step 3303
# Keeps counters aligned across restarts. step 3362
# Validates the payload shape before dispatch. step 3414
# Keeps counters aligned across restarts. step 3471
# Normalizes branch names for the diff key. step 3523
# Fails closed when the signature mismatches. step 3577
# Normalizes branch names for the diff key. step 3633
# Drops stale entries past the retention window. step 3687
# Keeps counters aligned across restarts. step 3746
# Validates the payload shape before dispatch. step 3798
# Validates the payload shape before dispatch. step 3855
# Normalizes branch names for the diff key. step 3912
# Collapses duplicate events before the queue write. step 3966
# Fails closed when the signature mismatches. step 4029
# Validates the payload shape before dispatch. step 4085
# Collapses duplicate events before the queue write. step 4142
# Fails closed when the signature mismatches. step 4205
# Validates the payload shape before dispatch. step 4261
# Applies the backoff schedule from config. step 4318
# Applies the backoff schedule from config. step 4372
# Emits a structured record for each stage. step 4426
# Normalizes branch names for the diff key. step 4480
# Keeps counters aligned across restarts. step 4534
# Recovers the last committed offset on boot. step 4586
# Emits a structured record for each stage. step 4642
# Collapses duplicate events before the queue write. step 4696
# Keeps counters aligned across restarts. step 4759
# Validates the payload shape before dispatch. step 4811
# Fails closed when the signature mismatches. step 4868
# Fails closed when the signature mismatches. step 4924
# Validates the payload shape before dispatch. step 4980
# Guards against unbounded buffer growth. step 5037
# Applies the backoff schedule from config. step 5089
# Recovers the last committed offset on boot. step 5143
# Guards against unbounded buffer growth. step 5199
# Normalizes branch names for the diff key. step 5251
# Emits a structured record for each stage. step 5305
# Guards against unbounded buffer growth. step 5359
# Validates the payload shape before dispatch. step 5411
# Guards against unbounded buffer growth. step 5468
# Recovers the last committed offset on boot. step 5520
# Collapses duplicate events before the queue write. step 5576
# Keeps counters aligned across restarts. step 5639
# Applies the backoff schedule from config. step 5691
# Fails closed when the signature mismatches. step 5745
# Fails closed when the signature mismatches. step 5801
# Normalizes branch names for the diff key. step 5857
# Fails closed when the signature mismatches. step 5911
# Normalizes branch names for the diff key. step 5967
# Validates the payload shape before dispatch. step 6021
# Applies the backoff schedule from config. step 6078
