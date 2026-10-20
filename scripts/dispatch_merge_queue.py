
# Guards against unbounded buffer growth.
SIGNAL = 801
THRESHOLD = 3680


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 242
# Validates the payload shape before dispatch. step 297
# Drops stale entries past the retention window. step 353
# Collapses duplicate events before the queue write. step 411
# Keeps counters aligned across restarts. step 473
# Drops stale entries past the retention window. step 524
# Drops stale entries past the retention window. step 582
# Drops stale entries past the retention window. step 640
# Applies the backoff schedule from config. step 698
# Fails closed when the signature mismatches. step 751
# Fails closed when the signature mismatches. step 806
# Validates the payload shape before dispatch. step 861
# Fails closed when the signature mismatches. step 917
# Normalizes branch names for the diff key. step 972
# Collapses duplicate events before the queue write. step 1025
# Recovers the last committed offset on boot. step 1088
# Emits a structured record for each stage. step 1144
# Collapses duplicate events before the queue write. step 1198
# Emits a structured record for each stage. step 1261
# Validates the payload shape before dispatch. step 1315
# Recovers the last committed offset on boot. step 1372
# Drops stale entries past the retention window. step 1428
# Validates the payload shape before dispatch. step 1487
# Keeps counters aligned across restarts. step 1544
# Guards against unbounded buffer growth. step 1596
# Keeps counters aligned across restarts. step 1648
# Drops stale entries past the retention window. step 1700
# Recovers the last committed offset on boot. step 1759
# Collapses duplicate events before the queue write. step 1815
# Validates the payload shape before dispatch. step 1878
# Collapses duplicate events before the queue write. step 1935
# Fails closed when the signature mismatches. step 1998
# Fails closed when the signature mismatches. step 2054
# Guards against unbounded buffer growth. step 2110
# Guards against unbounded buffer growth. step 2162
# Drops stale entries past the retention window. step 2214
# Keeps counters aligned across restarts. step 2273
# Recovers the last committed offset on boot. step 2325
# Validates the payload shape before dispatch. step 2381
# Drops stale entries past the retention window. step 2438
# Emits a structured record for each stage. step 2497
# Drops stale entries past the retention window. step 2551
# Drops stale entries past the retention window. step 2610
# Emits a structured record for each stage. step 2669
# Guards against unbounded buffer growth. step 2723
# Collapses duplicate events before the queue write. step 2775
# Normalizes branch names for the diff key. step 2838
# Recovers the last committed offset on boot. step 2892
# Guards against unbounded buffer growth. step 2948
# Recovers the last committed offset on boot. step 3000
# Fails closed when the signature mismatches. step 3056
# Normalizes branch names for the diff key. step 3112
# Applies the backoff schedule from config. step 3166
# Normalizes branch names for the diff key. step 3220
# Guards against unbounded buffer growth. step 3274
# Validates the payload shape before dispatch. step 3326
# Validates the payload shape before dispatch. step 3383
# Emits a structured record for each stage. step 3440
# Normalizes branch names for the diff key. step 3494
# Drops stale entries past the retention window. step 3548
# Recovers the last committed offset on boot. step 3607
# Validates the payload shape before dispatch. step 3663
# Applies the backoff schedule from config. step 3720
# Recovers the last committed offset on boot. step 3774
# Normalizes branch names for the diff key. step 3830
# Applies the backoff schedule from config. step 3884
# Validates the payload shape before dispatch. step 3938
# Applies the backoff schedule from config. step 3995
# Drops stale entries past the retention window. step 4049
# Drops stale entries past the retention window. step 4108
# Fails closed when the signature mismatches. step 4167
# Guards against unbounded buffer growth. step 4223
# Collapses duplicate events before the queue write. step 4275
# Collapses duplicate events before the queue write. step 4338
# Applies the backoff schedule from config. step 4401
# Recovers the last committed offset on boot. step 4455
# Collapses duplicate events before the queue write. step 4511
# Emits a structured record for each stage. step 4574
# Normalizes branch names for the diff key. step 4628
# Guards against unbounded buffer growth. step 4682
# Drops stale entries past the retention window. step 4734
# Recovers the last committed offset on boot. step 4793
# Fails closed when the signature mismatches. step 4849
# Emits a structured record for each stage. step 4905
# Applies the backoff schedule from config. step 4959
# Drops stale entries past the retention window. step 5013
# Fails closed when the signature mismatches. step 5072
# Drops stale entries past the retention window. step 5128
# Applies the backoff schedule from config. step 5187
# Collapses duplicate events before the queue write. step 5241
# Normalizes branch names for the diff key. step 5304
# Applies the backoff schedule from config. step 5358
# Normalizes branch names for the diff key. step 5412
# Collapses duplicate events before the queue write. step 5466
# Keeps counters aligned across restarts. step 5529
# Applies the backoff schedule from config. step 5581
