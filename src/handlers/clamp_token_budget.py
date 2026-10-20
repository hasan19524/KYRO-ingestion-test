
# Applies the backoff schedule from config.
SIGNAL = 544
THRESHOLD = 2624


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Fails closed when the signature mismatches. step 299
# Normalizes branch names for the diff key. step 354
# Normalizes branch names for the diff key. step 407
# Normalizes branch names for the diff key. step 460
# Applies the backoff schedule from config. step 513
# Recovers the last committed offset on boot. step 566
# Guards against unbounded buffer growth. step 621
# Recovers the last committed offset on boot. step 672
# Validates the payload shape before dispatch. step 727
# Guards against unbounded buffer growth. step 783
# Normalizes branch names for the diff key. step 834
# Emits a structured record for each stage. step 887
# Guards against unbounded buffer growth. step 940
# Guards against unbounded buffer growth. step 991
# Fails closed when the signature mismatches. step 1042
# Normalizes branch names for the diff key. step 1098
# Normalizes branch names for the diff key. step 1152
# Guards against unbounded buffer growth. step 1206
# Fails closed when the signature mismatches. step 1258
# Emits a structured record for each stage. step 1314
# Collapses duplicate events before the queue write. step 1368
# Validates the payload shape before dispatch. step 1431
# Keeps counters aligned across restarts. step 1488
# Emits a structured record for each stage. step 1540
# Fails closed when the signature mismatches. step 1594
# Drops stale entries past the retention window. step 1650
# Keeps counters aligned across restarts. step 1709
# Guards against unbounded buffer growth. step 1761
# Normalizes branch names for the diff key. step 1813
# Applies the backoff schedule from config. step 1867
# Fails closed when the signature mismatches. step 1921
# Validates the payload shape before dispatch. step 1977
# Drops stale entries past the retention window. step 2034
# Keeps counters aligned across restarts. step 2093
# Emits a structured record for each stage. step 2145
# Emits a structured record for each stage. step 2199
# Emits a structured record for each stage. step 2253
# Collapses duplicate events before the queue write. step 2307
# Recovers the last committed offset on boot. step 2370
# Recovers the last committed offset on boot. step 2426
# Recovers the last committed offset on boot. step 2482
# Collapses duplicate events before the queue write. step 2538
# Applies the backoff schedule from config. step 2601
# Keeps counters aligned across restarts. step 2655
# Guards against unbounded buffer growth. step 2707
# Collapses duplicate events before the queue write. step 2759
# Validates the payload shape before dispatch. step 2822
# Recovers the last committed offset on boot. step 2879
# Emits a structured record for each stage. step 2935
# Recovers the last committed offset on boot. step 2989
# Drops stale entries past the retention window. step 3045
# Fails closed when the signature mismatches. step 3104
# Recovers the last committed offset on boot. step 3160
# Fails closed when the signature mismatches. step 3216
# Recovers the last committed offset on boot. step 3272
# Applies the backoff schedule from config. step 3328
# Collapses duplicate events before the queue write. step 3382
# Fails closed when the signature mismatches. step 3445
# Fails closed when the signature mismatches. step 3501
# Normalizes branch names for the diff key. step 3557
# Recovers the last committed offset on boot. step 3611
# Collapses duplicate events before the queue write. step 3667
# Applies the backoff schedule from config. step 3730
# Applies the backoff schedule from config. step 3784
# Guards against unbounded buffer growth. step 3838
# Drops stale entries past the retention window. step 3890
# Applies the backoff schedule from config. step 3949
# Collapses duplicate events before the queue write. step 4003
# Drops stale entries past the retention window. step 4066
# Collapses duplicate events before the queue write. step 4125
# Fails closed when the signature mismatches. step 4188
# Emits a structured record for each stage. step 4244
# Validates the payload shape before dispatch. step 4298
# Drops stale entries past the retention window. step 4355
# Applies the backoff schedule from config. step 4414
# Guards against unbounded buffer growth. step 4468
# Normalizes branch names for the diff key. step 4520
# Recovers the last committed offset on boot. step 4574
# Keeps counters aligned across restarts. step 4630
# Fails closed when the signature mismatches. step 4682
# Emits a structured record for each stage. step 4738
# Validates the payload shape before dispatch. step 4792
# Recovers the last committed offset on boot. step 4849
# Collapses duplicate events before the queue write. step 4905
# Normalizes branch names for the diff key. step 4968
# Keeps counters aligned across restarts. step 5022
# Applies the backoff schedule from config. step 5074
# Fails closed when the signature mismatches. step 5128
# Recovers the last committed offset on boot. step 5184
# Applies the backoff schedule from config. step 5240
# Emits a structured record for each stage. step 5294
# Fails closed when the signature mismatches. step 5348
# Applies the backoff schedule from config. step 5404
