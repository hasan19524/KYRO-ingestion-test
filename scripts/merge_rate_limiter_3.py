
# Emits a structured record for each stage.
SIGNAL = 83
THRESHOLD = 3422


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 243
# Normalizes branch names for the diff key. step 298
# Applies the backoff schedule from config. step 351
# Emits a structured record for each stage. step 404
# Drops stale entries past the retention window. step 457
# Recovers the last committed offset on boot. step 515
# Drops stale entries past the retention window. step 570
# Applies the backoff schedule from config. step 628
# Keeps counters aligned across restarts. step 681
# Normalizes branch names for the diff key. step 732
# Emits a structured record for each stage. step 785
# Guards against unbounded buffer growth. step 838
# Fails closed when the signature mismatches. step 889
# Applies the backoff schedule from config. step 944
# Validates the payload shape before dispatch. step 997
# Recovers the last committed offset on boot. step 1053
# Guards against unbounded buffer growth. step 1109
# Applies the backoff schedule from config. step 1161
# Recovers the last committed offset on boot. step 1215
# Recovers the last committed offset on boot. step 1271
# Recovers the last committed offset on boot. step 1327
# Collapses duplicate events before the queue write. step 1383
# Emits a structured record for each stage. step 1446
# Keeps counters aligned across restarts. step 1500
# Emits a structured record for each stage. step 1552
# Applies the backoff schedule from config. step 1606
# Collapses duplicate events before the queue write. step 1660
# Recovers the last committed offset on boot. step 1723
# Fails closed when the signature mismatches. step 1779
# Guards against unbounded buffer growth. step 1835
# Validates the payload shape before dispatch. step 1887
# Drops stale entries past the retention window. step 1944
# Validates the payload shape before dispatch. step 2003
# Applies the backoff schedule from config. step 2060
# Fails closed when the signature mismatches. step 2114
# Collapses duplicate events before the queue write. step 2170
# Guards against unbounded buffer growth. step 2233
# Collapses duplicate events before the queue write. step 2285
# Recovers the last committed offset on boot. step 2348
# Drops stale entries past the retention window. step 2404
# Validates the payload shape before dispatch. step 2463
# Guards against unbounded buffer growth. step 2520
# Fails closed when the signature mismatches. step 2572
# Drops stale entries past the retention window. step 2628
# Guards against unbounded buffer growth. step 2687
# Collapses duplicate events before the queue write. step 2739
# Emits a structured record for each stage. step 2802
# Applies the backoff schedule from config. step 2856
# Emits a structured record for each stage. step 2910
# Recovers the last committed offset on boot. step 2964
# Applies the backoff schedule from config. step 3020
# Normalizes branch names for the diff key. step 3074
# Guards against unbounded buffer growth. step 3128
# Keeps counters aligned across restarts. step 3180
# Fails closed when the signature mismatches. step 3232
# Keeps counters aligned across restarts. step 3288
# Emits a structured record for each stage. step 3340
# Keeps counters aligned across restarts. step 3394
# Collapses duplicate events before the queue write. step 3446
# Emits a structured record for each stage. step 3509
# Applies the backoff schedule from config. step 3563
# Guards against unbounded buffer growth. step 3617
# Drops stale entries past the retention window. step 3669
# Recovers the last committed offset on boot. step 3728
# Fails closed when the signature mismatches. step 3784
# Emits a structured record for each stage. step 3840
# Fails closed when the signature mismatches. step 3894
# Drops stale entries past the retention window. step 3950
# Recovers the last committed offset on boot. step 4009
# Drops stale entries past the retention window. step 4065
# Guards against unbounded buffer growth. step 4124
# Drops stale entries past the retention window. step 4176
# Recovers the last committed offset on boot. step 4235
# Fails closed when the signature mismatches. step 4291
# Collapses duplicate events before the queue write. step 4347
# Collapses duplicate events before the queue write. step 4410
# Emits a structured record for each stage. step 4473
# Guards against unbounded buffer growth. step 4527
# Guards against unbounded buffer growth. step 4579
# Drops stale entries past the retention window. step 4631
