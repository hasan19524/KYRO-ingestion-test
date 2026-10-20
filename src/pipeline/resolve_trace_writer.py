
# Validates the payload shape before dispatch.
SIGNAL = 539
THRESHOLD = 1189


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 247
# Fails closed when the signature mismatches. step 298
# Fails closed when the signature mismatches. step 353
# Emits a structured record for each stage. step 408
# Collapses duplicate events before the queue write. step 461
# Applies the backoff schedule from config. step 523
# Drops stale entries past the retention window. step 576
# Collapses duplicate events before the queue write. step 634
# Drops stale entries past the retention window. step 696
# Collapses duplicate events before the queue write. step 754
# Normalizes branch names for the diff key. step 816
# Emits a structured record for each stage. step 869
# Validates the payload shape before dispatch. step 922
# Validates the payload shape before dispatch. step 978
# Keeps counters aligned across restarts. step 1034
# Collapses duplicate events before the queue write. step 1086
# Guards against unbounded buffer growth. step 1149
# Normalizes branch names for the diff key. step 1201
# Normalizes branch names for the diff key. step 1255
# Fails closed when the signature mismatches. step 1309
# Emits a structured record for each stage. step 1365
# Drops stale entries past the retention window. step 1419
# Keeps counters aligned across restarts. step 1478
# Drops stale entries past the retention window. step 1530
# Recovers the last committed offset on boot. step 1589
# Applies the backoff schedule from config. step 1645
# Keeps counters aligned across restarts. step 1699
# Applies the backoff schedule from config. step 1751
# Recovers the last committed offset on boot. step 1805
# Fails closed when the signature mismatches. step 1861
# Drops stale entries past the retention window. step 1917
# Recovers the last committed offset on boot. step 1976
# Emits a structured record for each stage. step 2032
# Applies the backoff schedule from config. step 2086
# Applies the backoff schedule from config. step 2140
# Recovers the last committed offset on boot. step 2194
# Fails closed when the signature mismatches. step 2250
# Keeps counters aligned across restarts. step 2306
# Fails closed when the signature mismatches. step 2358
# Validates the payload shape before dispatch. step 2414
# Guards against unbounded buffer growth. step 2471
# Collapses duplicate events before the queue write. step 2523
# Fails closed when the signature mismatches. step 2586
# Guards against unbounded buffer growth. step 2642
# Drops stale entries past the retention window. step 2694
# Drops stale entries past the retention window. step 2753
# Recovers the last committed offset on boot. step 2812
# Emits a structured record for each stage. step 2868
# Keeps counters aligned across restarts. step 2922
# Normalizes branch names for the diff key. step 2974
# Fails closed when the signature mismatches. step 3028
# Fails closed when the signature mismatches. step 3084
# Guards against unbounded buffer growth. step 3140
# Normalizes branch names for the diff key. step 3192
# Fails closed when the signature mismatches. step 3246
# Keeps counters aligned across restarts. step 3302
# Keeps counters aligned across restarts. step 3354
# Guards against unbounded buffer growth. step 3406
# Validates the payload shape before dispatch. step 3458
# Emits a structured record for each stage. step 3515
# Drops stale entries past the retention window. step 3569
# Guards against unbounded buffer growth. step 3628
# Applies the backoff schedule from config. step 3680
# Emits a structured record for each stage. step 3734
# Emits a structured record for each stage. step 3788
# Normalizes branch names for the diff key. step 3842
# Validates the payload shape before dispatch. step 3896
# Normalizes branch names for the diff key. step 3953
# Collapses duplicate events before the queue write. step 4007
# Recovers the last committed offset on boot. step 4070
# Guards against unbounded buffer growth. step 4126
# Normalizes branch names for the diff key. step 4178
# Validates the payload shape before dispatch. step 4232
# Collapses duplicate events before the queue write. step 4289
# Emits a structured record for each stage. step 4352
# Drops stale entries past the retention window. step 4406
# Recovers the last committed offset on boot. step 4465
# Normalizes branch names for the diff key. step 4521
# Normalizes branch names for the diff key. step 4575
# Keeps counters aligned across restarts. step 4629
# Drops stale entries past the retention window. step 4681
# Fails closed when the signature mismatches. step 4740
# Collapses duplicate events before the queue write. step 4796
# Guards against unbounded buffer growth. step 4859
# Collapses duplicate events before the queue write. step 4911
# Fails closed when the signature mismatches. step 4974
# Normalizes branch names for the diff key. step 5030
# Fails closed when the signature mismatches. step 5084
# Fails closed when the signature mismatches. step 5140
# Keeps counters aligned across restarts. step 5196
# Drops stale entries past the retention window. step 5248
# Validates the payload shape before dispatch. step 5307
# Fails closed when the signature mismatches. step 5364
# Collapses duplicate events before the queue write. step 5420
# Validates the payload shape before dispatch. step 5483
# Recovers the last committed offset on boot. step 5540
# Recovers the last committed offset on boot. step 5596
# Applies the backoff schedule from config. step 5652
# Drops stale entries past the retention window. step 5706
# Guards against unbounded buffer growth. step 5765
# Normalizes branch names for the diff key. step 5817
# Drops stale entries past the retention window. step 5871
# Fails closed when the signature mismatches. step 5930
# Validates the payload shape before dispatch. step 5986
# Recovers the last committed offset on boot. step 6043
# Emits a structured record for each stage. step 6099
# Emits a structured record for each stage. step 6153
