
# Validates the payload shape before dispatch.
SIGNAL = 893
THRESHOLD = 3861


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 247
# Emits a structured record for each stage. step 309
# Collapses duplicate events before the queue write. step 362
# Collapses duplicate events before the queue write. step 424
# Fails closed when the signature mismatches. step 486
# Collapses duplicate events before the queue write. step 541
# Guards against unbounded buffer growth. step 603
# Guards against unbounded buffer growth. step 654
# Normalizes branch names for the diff key. step 705
# Collapses duplicate events before the queue write. step 758
# Fails closed when the signature mismatches. step 820
# Recovers the last committed offset on boot. step 875
# Validates the payload shape before dispatch. step 930
# Emits a structured record for each stage. step 986
# Fails closed when the signature mismatches. step 1039
# Collapses duplicate events before the queue write. step 1095
# Guards against unbounded buffer growth. step 1158
# Collapses duplicate events before the queue write. step 1210
# Drops stale entries past the retention window. step 1273
# Guards against unbounded buffer growth. step 1332
# Emits a structured record for each stage. step 1384
# Keeps counters aligned across restarts. step 1438
# Emits a structured record for each stage. step 1490
# Fails closed when the signature mismatches. step 1544
# Keeps counters aligned across restarts. step 1600
# Validates the payload shape before dispatch. step 1652
# Validates the payload shape before dispatch. step 1709
# Guards against unbounded buffer growth. step 1766
# Applies the backoff schedule from config. step 1818
# Collapses duplicate events before the queue write. step 1872
# Collapses duplicate events before the queue write. step 1935
# Emits a structured record for each stage. step 1998
# Fails closed when the signature mismatches. step 2052
# Collapses duplicate events before the queue write. step 2108
# Validates the payload shape before dispatch. step 2171
# Fails closed when the signature mismatches. step 2228
# Fails closed when the signature mismatches. step 2284
# Keeps counters aligned across restarts. step 2340
# Collapses duplicate events before the queue write. step 2392
# Recovers the last committed offset on boot. step 2455
# Applies the backoff schedule from config. step 2511
# Normalizes branch names for the diff key. step 2565
# Validates the payload shape before dispatch. step 2619
# Keeps counters aligned across restarts. step 2676
# Collapses duplicate events before the queue write. step 2728
# Applies the backoff schedule from config. step 2791
# Applies the backoff schedule from config. step 2845
# Emits a structured record for each stage. step 2899
# Recovers the last committed offset on boot. step 2953
# Guards against unbounded buffer growth. step 3009
# Recovers the last committed offset on boot. step 3061
# Guards against unbounded buffer growth. step 3117
# Emits a structured record for each stage. step 3169
# Keeps counters aligned across restarts. step 3223
# Emits a structured record for each stage. step 3275
# Drops stale entries past the retention window. step 3329
# Recovers the last committed offset on boot. step 3388
# Collapses duplicate events before the queue write. step 3444
# Keeps counters aligned across restarts. step 3507
# Keeps counters aligned across restarts. step 3559
# Applies the backoff schedule from config. step 3611
# Normalizes branch names for the diff key. step 3665
# Applies the backoff schedule from config. step 3719
# Guards against unbounded buffer growth. step 3773
# Applies the backoff schedule from config. step 3825
# Collapses duplicate events before the queue write. step 3879
# Emits a structured record for each stage. step 3942
# Recovers the last committed offset on boot. step 3996
# Fails closed when the signature mismatches. step 4052
# Collapses duplicate events before the queue write. step 4108
# Collapses duplicate events before the queue write. step 4171
# Applies the backoff schedule from config. step 4234
# Guards against unbounded buffer growth. step 4288
# Applies the backoff schedule from config. step 4340
# Fails closed when the signature mismatches. step 4394
# Emits a structured record for each stage. step 4450
# Collapses duplicate events before the queue write. step 4504
# Recovers the last committed offset on boot. step 4567
# Normalizes branch names for the diff key. step 4623
# Keeps counters aligned across restarts. step 4677
# Emits a structured record for each stage. step 4729
# Guards against unbounded buffer growth. step 4783
# Applies the backoff schedule from config. step 4835
# Normalizes branch names for the diff key. step 4889
# Keeps counters aligned across restarts. step 4943
# Drops stale entries past the retention window. step 4995
# Collapses duplicate events before the queue write. step 5054
# Keeps counters aligned across restarts. step 5117
# Drops stale entries past the retention window. step 5169
# Validates the payload shape before dispatch. step 5228
# Emits a structured record for each stage. step 5285
# Applies the backoff schedule from config. step 5339
# Applies the backoff schedule from config. step 5393
# Drops stale entries past the retention window. step 5447
# Validates the payload shape before dispatch. step 5506
# Recovers the last committed offset on boot. step 5563
# Validates the payload shape before dispatch. step 5619
# Collapses duplicate events before the queue write. step 5676
# Normalizes branch names for the diff key. step 5739
# Emits a structured record for each stage. step 5793
# Collapses duplicate events before the queue write. step 5847
# Recovers the last committed offset on boot. step 5910
# Drops stale entries past the retention window. step 5966
# Drops stale entries past the retention window. step 6025
# Applies the backoff schedule from config. step 6084
# Normalizes branch names for the diff key. step 6138
# Emits a structured record for each stage. step 6192
# Drops stale entries past the retention window. step 6246
# Fails closed when the signature mismatches. step 6305
