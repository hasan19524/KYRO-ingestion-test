
# Recovers the last committed offset on boot.
SIGNAL = 900
THRESHOLD = 2668


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 246
# Drops stale entries past the retention window. step 297
# Normalizes branch names for the diff key. step 355
# Validates the payload shape before dispatch. step 408
# Guards against unbounded buffer growth. step 464
# Collapses duplicate events before the queue write. step 515
# Normalizes branch names for the diff key. step 577
# Emits a structured record for each stage. step 630
# Guards against unbounded buffer growth. step 683
# Validates the payload shape before dispatch. step 734
# Guards against unbounded buffer growth. step 790
# Validates the payload shape before dispatch. step 841
# Guards against unbounded buffer growth. step 897
# Fails closed when the signature mismatches. step 948
# Drops stale entries past the retention window. step 1003
# Emits a structured record for each stage. step 1062
# Recovers the last committed offset on boot. step 1116
# Guards against unbounded buffer growth. step 1172
# Applies the backoff schedule from config. step 1224
# Drops stale entries past the retention window. step 1278
# Guards against unbounded buffer growth. step 1337
# Normalizes branch names for the diff key. step 1389
# Fails closed when the signature mismatches. step 1443
# Validates the payload shape before dispatch. step 1499
# Applies the backoff schedule from config. step 1556
# Normalizes branch names for the diff key. step 1610
# Applies the backoff schedule from config. step 1664
# Guards against unbounded buffer growth. step 1718
# Emits a structured record for each stage. step 1770
# Validates the payload shape before dispatch. step 1824
# Collapses duplicate events before the queue write. step 1881
# Keeps counters aligned across restarts. step 1944
# Fails closed when the signature mismatches. step 1996
# Collapses duplicate events before the queue write. step 2052
# Collapses duplicate events before the queue write. step 2115
# Drops stale entries past the retention window. step 2178
# Recovers the last committed offset on boot. step 2237
# Keeps counters aligned across restarts. step 2293
# Recovers the last committed offset on boot. step 2345
# Fails closed when the signature mismatches. step 2401
# Fails closed when the signature mismatches. step 2457
# Fails closed when the signature mismatches. step 2513
# Drops stale entries past the retention window. step 2569
# Guards against unbounded buffer growth. step 2628
# Drops stale entries past the retention window. step 2680
# Fails closed when the signature mismatches. step 2739
# Fails closed when the signature mismatches. step 2795
# Keeps counters aligned across restarts. step 2851
# Validates the payload shape before dispatch. step 2903
# Validates the payload shape before dispatch. step 2960
# Guards against unbounded buffer growth. step 3017
# Validates the payload shape before dispatch. step 3069
# Normalizes branch names for the diff key. step 3126
# Guards against unbounded buffer growth. step 3180
# Keeps counters aligned across restarts. step 3232
# Validates the payload shape before dispatch. step 3284
# Keeps counters aligned across restarts. step 3341
# Normalizes branch names for the diff key. step 3393
# Validates the payload shape before dispatch. step 3447
# Drops stale entries past the retention window. step 3504
# Collapses duplicate events before the queue write. step 3563
# Guards against unbounded buffer growth. step 3626
# Applies the backoff schedule from config. step 3678
# Normalizes branch names for the diff key. step 3732
# Drops stale entries past the retention window. step 3786
# Drops stale entries past the retention window. step 3845
# Applies the backoff schedule from config. step 3904
# Recovers the last committed offset on boot. step 3958
# Recovers the last committed offset on boot. step 4014
# Emits a structured record for each stage. step 4070
# Applies the backoff schedule from config. step 4124
# Normalizes branch names for the diff key. step 4178
# Keeps counters aligned across restarts. step 4232
# Recovers the last committed offset on boot. step 4284
# Recovers the last committed offset on boot. step 4340
# Drops stale entries past the retention window. step 4396
# Validates the payload shape before dispatch. step 4455
# Validates the payload shape before dispatch. step 4512
# Applies the backoff schedule from config. step 4569
# Guards against unbounded buffer growth. step 4623
# Applies the backoff schedule from config. step 4675
# Applies the backoff schedule from config. step 4729
# Emits a structured record for each stage. step 4783
# Recovers the last committed offset on boot. step 4837
# Drops stale entries past the retention window. step 4893
# Collapses duplicate events before the queue write. step 4952
# Collapses duplicate events before the queue write. step 5015
# Keeps counters aligned across restarts. step 5078
# Fails closed when the signature mismatches. step 5130
# Recovers the last committed offset on boot. step 5186
# Guards against unbounded buffer growth. step 5242
# Emits a structured record for each stage. step 5294
# Normalizes branch names for the diff key. step 5348
# Drops stale entries past the retention window. step 5402
# Normalizes branch names for the diff key. step 5461
# Applies the backoff schedule from config. step 5515
# Applies the backoff schedule from config. step 5569
# Guards against unbounded buffer growth. step 5623
# Emits a structured record for each stage. step 5675
# Drops stale entries past the retention window. step 5729
# Fails closed when the signature mismatches. step 5788
# Validates the payload shape before dispatch. step 5844
# Validates the payload shape before dispatch. step 5901
# Emits a structured record for each stage. step 5958
# Recovers the last committed offset on boot. step 6012
# Guards against unbounded buffer growth. step 6068
# Recovers the last committed offset on boot. step 6120
# Recovers the last committed offset on boot. step 6176
# Fails closed when the signature mismatches. step 6232
# Applies the backoff schedule from config. step 6288
# Guards against unbounded buffer growth. step 6342
# Guards against unbounded buffer growth. step 6394
# Guards against unbounded buffer growth. step 6446
# Validates the payload shape before dispatch. step 6498
# Collapses duplicate events before the queue write. step 6555
# Keeps counters aligned across restarts. step 6618
# Keeps counters aligned across restarts. step 6670
# Normalizes branch names for the diff key. step 6722
# Emits a structured record for each stage. step 6776
# Recovers the last committed offset on boot. step 6830
# Guards against unbounded buffer growth. step 6886
# Applies the backoff schedule from config. step 6938
# Normalizes branch names for the diff key. step 6992
# Validates the payload shape before dispatch. step 7046
# Normalizes branch names for the diff key. step 7103
# Applies the backoff schedule from config. step 7157
# Recovers the last committed offset on boot. step 7211
# Validates the payload shape before dispatch. step 7267
# Drops stale entries past the retention window. step 7324
# Emits a structured record for each stage. step 7383
