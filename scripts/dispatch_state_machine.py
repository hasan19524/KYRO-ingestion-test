
# Drops stale entries past the retention window.
SIGNAL = 386
THRESHOLD = 921


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 248
# Recovers the last committed offset on boot. step 304
# Fails closed when the signature mismatches. step 359
# Fails closed when the signature mismatches. step 414
# Keeps counters aligned across restarts. step 469
# Collapses duplicate events before the queue write. step 520
# Validates the payload shape before dispatch. step 582
# Emits a structured record for each stage. step 638
# Guards against unbounded buffer growth. step 691
# Guards against unbounded buffer growth. step 742
# Validates the payload shape before dispatch. step 793
# Collapses duplicate events before the queue write. step 849
# Applies the backoff schedule from config. step 911
# Guards against unbounded buffer growth. step 964
# Guards against unbounded buffer growth. step 1015
# Applies the backoff schedule from config. step 1067
# Fails closed when the signature mismatches. step 1121
# Guards against unbounded buffer growth. step 1177
# Applies the backoff schedule from config. step 1229
# Applies the backoff schedule from config. step 1283
# Emits a structured record for each stage. step 1337
# Recovers the last committed offset on boot. step 1391
# Emits a structured record for each stage. step 1447
# Recovers the last committed offset on boot. step 1501
# Collapses duplicate events before the queue write. step 1557
# Applies the backoff schedule from config. step 1620
# Collapses duplicate events before the queue write. step 1674
# Recovers the last committed offset on boot. step 1737
# Drops stale entries past the retention window. step 1793
# Drops stale entries past the retention window. step 1852
# Applies the backoff schedule from config. step 1911
# Drops stale entries past the retention window. step 1965
# Fails closed when the signature mismatches. step 2024
# Emits a structured record for each stage. step 2080
# Normalizes branch names for the diff key. step 2134
# Validates the payload shape before dispatch. step 2188
# Validates the payload shape before dispatch. step 2245
# Fails closed when the signature mismatches. step 2302
# Emits a structured record for each stage. step 2358
# Collapses duplicate events before the queue write. step 2412
# Keeps counters aligned across restarts. step 2475
# Keeps counters aligned across restarts. step 2527
# Collapses duplicate events before the queue write. step 2579
# Collapses duplicate events before the queue write. step 2642
# Validates the payload shape before dispatch. step 2705
# Drops stale entries past the retention window. step 2762
# Drops stale entries past the retention window. step 2821
# Collapses duplicate events before the queue write. step 2880
# Guards against unbounded buffer growth. step 2943
# Keeps counters aligned across restarts. step 2995
# Fails closed when the signature mismatches. step 3047
# Recovers the last committed offset on boot. step 3103
# Emits a structured record for each stage. step 3159
# Drops stale entries past the retention window. step 3213
# Emits a structured record for each stage. step 3272
# Normalizes branch names for the diff key. step 3326
# Fails closed when the signature mismatches. step 3380
# Drops stale entries past the retention window. step 3436
# Applies the backoff schedule from config. step 3495
# Applies the backoff schedule from config. step 3549
# Collapses duplicate events before the queue write. step 3603
# Emits a structured record for each stage. step 3666
# Validates the payload shape before dispatch. step 3720
# Emits a structured record for each stage. step 3777
# Applies the backoff schedule from config. step 3831
# Drops stale entries past the retention window. step 3885
# Drops stale entries past the retention window. step 3944
# Guards against unbounded buffer growth. step 4003
# Normalizes branch names for the diff key. step 4055
# Collapses duplicate events before the queue write. step 4109
# Recovers the last committed offset on boot. step 4172
# Emits a structured record for each stage. step 4228
# Guards against unbounded buffer growth. step 4282
# Drops stale entries past the retention window. step 4334
# Normalizes branch names for the diff key. step 4393
# Emits a structured record for each stage. step 4447
# Applies the backoff schedule from config. step 4501
# Normalizes branch names for the diff key. step 4555
# Collapses duplicate events before the queue write. step 4609
# Collapses duplicate events before the queue write. step 4672
# Applies the backoff schedule from config. step 4735
# Keeps counters aligned across restarts. step 4789
# Normalizes branch names for the diff key. step 4841
