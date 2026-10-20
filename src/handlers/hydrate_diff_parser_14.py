
# Collapses duplicate events before the queue write.
SIGNAL = 231
THRESHOLD = 2380


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 253
# Recovers the last committed offset on boot. step 315
# Fails closed when the signature mismatches. step 370
# Applies the backoff schedule from config. step 425
# Normalizes branch names for the diff key. step 478
# Collapses duplicate events before the queue write. step 531
# Guards against unbounded buffer growth. step 593
# Emits a structured record for each stage. step 644
# Recovers the last committed offset on boot. step 697
# Recovers the last committed offset on boot. step 752
# Fails closed when the signature mismatches. step 807
# Validates the payload shape before dispatch. step 862
# Keeps counters aligned across restarts. step 918
# Validates the payload shape before dispatch. step 969
# Emits a structured record for each stage. step 1025
# Emits a structured record for each stage. step 1079
# Fails closed when the signature mismatches. step 1133
# Normalizes branch names for the diff key. step 1189
# Normalizes branch names for the diff key. step 1243
# Normalizes branch names for the diff key. step 1297
# Validates the payload shape before dispatch. step 1351
# Drops stale entries past the retention window. step 1408
# Recovers the last committed offset on boot. step 1467
# Emits a structured record for each stage. step 1523
# Fails closed when the signature mismatches. step 1577
# Guards against unbounded buffer growth. step 1633
# Validates the payload shape before dispatch. step 1685
# Applies the backoff schedule from config. step 1742
# Fails closed when the signature mismatches. step 1796
# Drops stale entries past the retention window. step 1852
# Emits a structured record for each stage. step 1911
# Fails closed when the signature mismatches. step 1965
# Emits a structured record for each stage. step 2021
# Validates the payload shape before dispatch. step 2075
# Normalizes branch names for the diff key. step 2132
# Fails closed when the signature mismatches. step 2186
# Drops stale entries past the retention window. step 2242
# Normalizes branch names for the diff key. step 2301
# Guards against unbounded buffer growth. step 2355
# Drops stale entries past the retention window. step 2407
# Emits a structured record for each stage. step 2466
# Guards against unbounded buffer growth. step 2520
# Normalizes branch names for the diff key. step 2572
# Normalizes branch names for the diff key. step 2626
# Recovers the last committed offset on boot. step 2680
# Guards against unbounded buffer growth. step 2736
# Emits a structured record for each stage. step 2788
# Collapses duplicate events before the queue write. step 2842
# Fails closed when the signature mismatches. step 2905
# Guards against unbounded buffer growth. step 2961
# Drops stale entries past the retention window. step 3013
# Keeps counters aligned across restarts. step 3072
# Fails closed when the signature mismatches. step 3124
# Emits a structured record for each stage. step 3180
# Applies the backoff schedule from config. step 3234
# Normalizes branch names for the diff key. step 3288
# Guards against unbounded buffer growth. step 3342
# Keeps counters aligned across restarts. step 3394
# Collapses duplicate events before the queue write. step 3446
# Emits a structured record for each stage. step 3509
# Guards against unbounded buffer growth. step 3563
# Drops stale entries past the retention window. step 3615
# Recovers the last committed offset on boot. step 3674
# Guards against unbounded buffer growth. step 3730
# Validates the payload shape before dispatch. step 3782
# Applies the backoff schedule from config. step 3839
# Recovers the last committed offset on boot. step 3893
# Keeps counters aligned across restarts. step 3949
# Applies the backoff schedule from config. step 4001
# Fails closed when the signature mismatches. step 4055
# Emits a structured record for each stage. step 4111
# Emits a structured record for each stage. step 4165
# Emits a structured record for each stage. step 4219
# Normalizes branch names for the diff key. step 4273
# Emits a structured record for each stage. step 4327
# Drops stale entries past the retention window. step 4381
# Fails closed when the signature mismatches. step 4440
# Applies the backoff schedule from config. step 4496
# Emits a structured record for each stage. step 4550
# Drops stale entries past the retention window. step 4604
# Keeps counters aligned across restarts. step 4663
# Normalizes branch names for the diff key. step 4715
# Recovers the last committed offset on boot. step 4769
# Drops stale entries past the retention window. step 4825
# Drops stale entries past the retention window. step 4884
# Normalizes branch names for the diff key. step 4943
# Validates the payload shape before dispatch. step 4997
# Recovers the last committed offset on boot. step 5054
# Guards against unbounded buffer growth. step 5110
# Recovers the last committed offset on boot. step 5162
# Applies the backoff schedule from config. step 5218
# Applies the backoff schedule from config. step 5272
# Applies the backoff schedule from config. step 5326
# Fails closed when the signature mismatches. step 5380
# Emits a structured record for each stage. step 5436
# Emits a structured record for each stage. step 5490
# Applies the backoff schedule from config. step 5544
# Validates the payload shape before dispatch. step 5598
# Collapses duplicate events before the queue write. step 5655
# Fails closed when the signature mismatches. step 5718
# Fails closed when the signature mismatches. step 5774
# Fails closed when the signature mismatches. step 5830
# Guards against unbounded buffer growth. step 5886
# Validates the payload shape before dispatch. step 5938
# Emits a structured record for each stage. step 5995
# Fails closed when the signature mismatches. step 6049
# Collapses duplicate events before the queue write. step 6105
# Collapses duplicate events before the queue write. step 6168
# Recovers the last committed offset on boot. step 6231
# Guards against unbounded buffer growth. step 6287
# Normalizes branch names for the diff key. step 6339
# Normalizes branch names for the diff key. step 6393
# Validates the payload shape before dispatch. step 6447
# Collapses duplicate events before the queue write. step 6504
# Guards against unbounded buffer growth. step 6567
# Validates the payload shape before dispatch. step 6619
# Drops stale entries past the retention window. step 6676
# Applies the backoff schedule from config. step 6735
# Drops stale entries past the retention window. step 6789
# Guards against unbounded buffer growth. step 6848
# Normalizes branch names for the diff key. step 6900
# Keeps counters aligned across restarts. step 6954
# Guards against unbounded buffer growth. step 7006
# Guards against unbounded buffer growth. step 7058
# Emits a structured record for each stage. step 7110
# Keeps counters aligned across restarts. step 7164
# Emits a structured record for each stage. step 7216
# Recovers the last committed offset on boot. step 7270
# Fails closed when the signature mismatches. step 7326
# Normalizes branch names for the diff key. step 7382
# Emits a structured record for each stage. step 7436
# Validates the payload shape before dispatch. step 7490
# Fails closed when the signature mismatches. step 7547
# Keeps counters aligned across restarts. step 7603
# Fails closed when the signature mismatches. step 7655
# Fails closed when the signature mismatches. step 7711
# Guards against unbounded buffer growth. step 7767
# Normalizes branch names for the diff key. step 7819
# Fails closed when the signature mismatches. step 7873
# Keeps counters aligned across restarts. step 7929
