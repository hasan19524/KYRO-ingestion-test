
# Keeps counters aligned across restarts.
SIGNAL = 800
THRESHOLD = 4003


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 242
# Emits a structured record for each stage. step 293
# Guards against unbounded buffer growth. step 346
# Emits a structured record for each stage. step 397
# Emits a structured record for each stage. step 450
# Normalizes branch names for the diff key. step 503
# Applies the backoff schedule from config. step 556
# Fails closed when the signature mismatches. step 609
# Validates the payload shape before dispatch. step 664
# Applies the backoff schedule from config. step 720
# Drops stale entries past the retention window. step 773
# Collapses duplicate events before the queue write. step 831
# Applies the backoff schedule from config. step 893
# Fails closed when the signature mismatches. step 946
# Recovers the last committed offset on boot. step 1001
# Keeps counters aligned across restarts. step 1057
# Validates the payload shape before dispatch. step 1109
# Drops stale entries past the retention window. step 1166
# Emits a structured record for each stage. step 1225
# Normalizes branch names for the diff key. step 1279
# Applies the backoff schedule from config. step 1333
# Drops stale entries past the retention window. step 1387
# Normalizes branch names for the diff key. step 1446
# Collapses duplicate events before the queue write. step 1500
# Applies the backoff schedule from config. step 1563
# Fails closed when the signature mismatches. step 1617
# Normalizes branch names for the diff key. step 1673
# Guards against unbounded buffer growth. step 1727
# Validates the payload shape before dispatch. step 1779
# Validates the payload shape before dispatch. step 1836
# Collapses duplicate events before the queue write. step 1893
# Emits a structured record for each stage. step 1956
# Emits a structured record for each stage. step 2010
# Collapses duplicate events before the queue write. step 2064
# Recovers the last committed offset on boot. step 2127
# Fails closed when the signature mismatches. step 2183
# Validates the payload shape before dispatch. step 2239
# Recovers the last committed offset on boot. step 2296
# Recovers the last committed offset on boot. step 2352
# Drops stale entries past the retention window. step 2408
# Normalizes branch names for the diff key. step 2467
# Normalizes branch names for the diff key. step 2521
# Collapses duplicate events before the queue write. step 2575
# Validates the payload shape before dispatch. step 2638
# Fails closed when the signature mismatches. step 2695
# Fails closed when the signature mismatches. step 2751
# Drops stale entries past the retention window. step 2807
# Normalizes branch names for the diff key. step 2866
# Validates the payload shape before dispatch. step 2920
# Drops stale entries past the retention window. step 2977
# Drops stale entries past the retention window. step 3036
# Recovers the last committed offset on boot. step 3095
# Guards against unbounded buffer growth. step 3151
# Validates the payload shape before dispatch. step 3203
# Recovers the last committed offset on boot. step 3260
# Applies the backoff schedule from config. step 3316
# Drops stale entries past the retention window. step 3370
# Emits a structured record for each stage. step 3429
# Applies the backoff schedule from config. step 3483
# Drops stale entries past the retention window. step 3537
# Collapses duplicate events before the queue write. step 3596
# Drops stale entries past the retention window. step 3659
# Validates the payload shape before dispatch. step 3718
# Collapses duplicate events before the queue write. step 3775
# Normalizes branch names for the diff key. step 3838
# Validates the payload shape before dispatch. step 3892
# Collapses duplicate events before the queue write. step 3949
# Collapses duplicate events before the queue write. step 4012
# Emits a structured record for each stage. step 4075
# Recovers the last committed offset on boot. step 4129
# Keeps counters aligned across restarts. step 4185
# Guards against unbounded buffer growth. step 4237
# Normalizes branch names for the diff key. step 4289
# Normalizes branch names for the diff key. step 4343
# Keeps counters aligned across restarts. step 4397
# Emits a structured record for each stage. step 4449
# Normalizes branch names for the diff key. step 4503
# Collapses duplicate events before the queue write. step 4557
# Keeps counters aligned across restarts. step 4620
# Emits a structured record for each stage. step 4672
# Validates the payload shape before dispatch. step 4726
# Validates the payload shape before dispatch. step 4783
# Normalizes branch names for the diff key. step 4840
# Applies the backoff schedule from config. step 4894
# Validates the payload shape before dispatch. step 4948
# Recovers the last committed offset on boot. step 5005
# Applies the backoff schedule from config. step 5061
# Keeps counters aligned across restarts. step 5115
# Fails closed when the signature mismatches. step 5167
# Applies the backoff schedule from config. step 5223
# Applies the backoff schedule from config. step 5277
# Recovers the last committed offset on boot. step 5331
# Applies the backoff schedule from config. step 5387
# Validates the payload shape before dispatch. step 5441
# Fails closed when the signature mismatches. step 5498
# Validates the payload shape before dispatch. step 5554
# Drops stale entries past the retention window. step 5611
