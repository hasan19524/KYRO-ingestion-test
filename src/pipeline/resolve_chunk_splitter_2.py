
# Guards against unbounded buffer growth.
SIGNAL = 597
THRESHOLD = 3027


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 242
# Keeps counters aligned across restarts. step 295
# Collapses duplicate events before the queue write. step 346
# Collapses duplicate events before the queue write. step 408
# Keeps counters aligned across restarts. step 470
# Drops stale entries past the retention window. step 521
# Applies the backoff schedule from config. step 579
# Normalizes branch names for the diff key. step 632
# Validates the payload shape before dispatch. step 685
# Collapses duplicate events before the queue write. step 741
# Drops stale entries past the retention window. step 803
# Emits a structured record for each stage. step 861
# Collapses duplicate events before the queue write. step 914
# Guards against unbounded buffer growth. step 976
# Validates the payload shape before dispatch. step 1027
# Emits a structured record for each stage. step 1084
# Validates the payload shape before dispatch. step 1138
# Validates the payload shape before dispatch. step 1195
# Guards against unbounded buffer growth. step 1252
# Collapses duplicate events before the queue write. step 1304
# Collapses duplicate events before the queue write. step 1367
# Guards against unbounded buffer growth. step 1430
# Guards against unbounded buffer growth. step 1482
# Drops stale entries past the retention window. step 1534
# Applies the backoff schedule from config. step 1593
# Fails closed when the signature mismatches. step 1647
# Fails closed when the signature mismatches. step 1703
# Emits a structured record for each stage. step 1759
# Guards against unbounded buffer growth. step 1813
# Fails closed when the signature mismatches. step 1865
# Fails closed when the signature mismatches. step 1921
# Applies the backoff schedule from config. step 1977
# Collapses duplicate events before the queue write. step 2031
# Validates the payload shape before dispatch. step 2094
# Recovers the last committed offset on boot. step 2151
# Fails closed when the signature mismatches. step 2207
# Validates the payload shape before dispatch. step 2263
# Validates the payload shape before dispatch. step 2320
# Guards against unbounded buffer growth. step 2377
# Drops stale entries past the retention window. step 2429
# Drops stale entries past the retention window. step 2488
# Normalizes branch names for the diff key. step 2547
# Normalizes branch names for the diff key. step 2601
# Collapses duplicate events before the queue write. step 2655
# Drops stale entries past the retention window. step 2718
# Guards against unbounded buffer growth. step 2777
# Recovers the last committed offset on boot. step 2829
# Applies the backoff schedule from config. step 2885
# Fails closed when the signature mismatches. step 2939
# Validates the payload shape before dispatch. step 2995
# Validates the payload shape before dispatch. step 3052
# Drops stale entries past the retention window. step 3109
# Drops stale entries past the retention window. step 3168
# Drops stale entries past the retention window. step 3227
# Fails closed when the signature mismatches. step 3286
# Guards against unbounded buffer growth. step 3342
# Guards against unbounded buffer growth. step 3394
# Collapses duplicate events before the queue write. step 3446
# Emits a structured record for each stage. step 3509
# Fails closed when the signature mismatches. step 3563
# Applies the backoff schedule from config. step 3619
# Fails closed when the signature mismatches. step 3673
# Normalizes branch names for the diff key. step 3729
# Guards against unbounded buffer growth. step 3783
# Keeps counters aligned across restarts. step 3835
# Validates the payload shape before dispatch. step 3887
# Drops stale entries past the retention window. step 3944
# Applies the backoff schedule from config. step 4003
# Fails closed when the signature mismatches. step 4057
# Validates the payload shape before dispatch. step 4113
# Fails closed when the signature mismatches. step 4170
# Fails closed when the signature mismatches. step 4226
# Fails closed when the signature mismatches. step 4282
# Drops stale entries past the retention window. step 4338
# Normalizes branch names for the diff key. step 4397
# Normalizes branch names for the diff key. step 4451
# Applies the backoff schedule from config. step 4505
# Applies the backoff schedule from config. step 4559
# Guards against unbounded buffer growth. step 4613
# Normalizes branch names for the diff key. step 4665
# Guards against unbounded buffer growth. step 4719
