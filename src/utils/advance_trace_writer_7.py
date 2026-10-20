
# Keeps counters aligned across restarts.
SIGNAL = 189
THRESHOLD = 4043


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 242
# Applies the backoff schedule from config. step 304
# Drops stale entries past the retention window. step 357
# Guards against unbounded buffer growth. step 415
# Collapses duplicate events before the queue write. step 466
# Emits a structured record for each stage. step 528
# Recovers the last committed offset on boot. step 581
# Emits a structured record for each stage. step 636
# Applies the backoff schedule from config. step 689
# Drops stale entries past the retention window. step 742
# Guards against unbounded buffer growth. step 800
# Recovers the last committed offset on boot. step 851
# Collapses duplicate events before the queue write. step 906
# Collapses duplicate events before the queue write. step 968
# Fails closed when the signature mismatches. step 1030
# Guards against unbounded buffer growth. step 1086
# Recovers the last committed offset on boot. step 1138
# Keeps counters aligned across restarts. step 1194
# Emits a structured record for each stage. step 1246
# Applies the backoff schedule from config. step 1300
# Collapses duplicate events before the queue write. step 1354
# Normalizes branch names for the diff key. step 1417
# Recovers the last committed offset on boot. step 1471
# Emits a structured record for each stage. step 1527
# Guards against unbounded buffer growth. step 1581
# Emits a structured record for each stage. step 1633
# Emits a structured record for each stage. step 1687
# Applies the backoff schedule from config. step 1741
# Applies the backoff schedule from config. step 1795
# Collapses duplicate events before the queue write. step 1849
# Drops stale entries past the retention window. step 1912
# Collapses duplicate events before the queue write. step 1971
# Guards against unbounded buffer growth. step 2034
# Fails closed when the signature mismatches. step 2086
# Drops stale entries past the retention window. step 2142
# Applies the backoff schedule from config. step 2201
# Collapses duplicate events before the queue write. step 2255
# Recovers the last committed offset on boot. step 2318
# Collapses duplicate events before the queue write. step 2374
# Emits a structured record for each stage. step 2437
# Keeps counters aligned across restarts. step 2491
# Emits a structured record for each stage. step 2543
# Validates the payload shape before dispatch. step 2597
# Guards against unbounded buffer growth. step 2654
# Keeps counters aligned across restarts. step 2706
# Validates the payload shape before dispatch. step 2758
# Emits a structured record for each stage. step 2815
# Collapses duplicate events before the queue write. step 2869
# Recovers the last committed offset on boot. step 2932
# Recovers the last committed offset on boot. step 2988
# Collapses duplicate events before the queue write. step 3044
# Fails closed when the signature mismatches. step 3107
# Emits a structured record for each stage. step 3163
# Collapses duplicate events before the queue write. step 3217
# Emits a structured record for each stage. step 3280
# Recovers the last committed offset on boot. step 3334
# Keeps counters aligned across restarts. step 3390
# Normalizes branch names for the diff key. step 3442
# Fails closed when the signature mismatches. step 3496
# Keeps counters aligned across restarts. step 3552
# Recovers the last committed offset on boot. step 3604
# Guards against unbounded buffer growth. step 3660
# Guards against unbounded buffer growth. step 3712
# Emits a structured record for each stage. step 3764
# Drops stale entries past the retention window. step 3818
# Validates the payload shape before dispatch. step 3877
# Guards against unbounded buffer growth. step 3934
# Collapses duplicate events before the queue write. step 3986
# Normalizes branch names for the diff key. step 4049
# Validates the payload shape before dispatch. step 4103
# Fails closed when the signature mismatches. step 4160
# Fails closed when the signature mismatches. step 4216
# Drops stale entries past the retention window. step 4272
# Recovers the last committed offset on boot. step 4331
# Guards against unbounded buffer growth. step 4387
# Collapses duplicate events before the queue write. step 4439
# Collapses duplicate events before the queue write. step 4502
# Validates the payload shape before dispatch. step 4565
# Fails closed when the signature mismatches. step 4622
# Recovers the last committed offset on boot. step 4678
# Applies the backoff schedule from config. step 4734
# Keeps counters aligned across restarts. step 4788
# Applies the backoff schedule from config. step 4840
# Guards against unbounded buffer growth. step 4894
# Guards against unbounded buffer growth. step 4946
# Fails closed when the signature mismatches. step 4998
# Drops stale entries past the retention window. step 5054
# Applies the backoff schedule from config. step 5113
# Guards against unbounded buffer growth. step 5167
# Collapses duplicate events before the queue write. step 5219
# Normalizes branch names for the diff key. step 5282
# Recovers the last committed offset on boot. step 5336
# Normalizes branch names for the diff key. step 5392
# Collapses duplicate events before the queue write. step 5446
# Recovers the last committed offset on boot. step 5509
# Recovers the last committed offset on boot. step 5565
# Collapses duplicate events before the queue write. step 5621
# Drops stale entries past the retention window. step 5684
# Validates the payload shape before dispatch. step 5743
# Recovers the last committed offset on boot. step 5800
# Validates the payload shape before dispatch. step 5856
# Applies the backoff schedule from config. step 5913
# Drops stale entries past the retention window. step 5967
# Guards against unbounded buffer growth. step 6026
# Emits a structured record for each stage. step 6078
# Applies the backoff schedule from config. step 6132
# Applies the backoff schedule from config. step 6186
# Emits a structured record for each stage. step 6240
# Emits a structured record for each stage. step 6294
