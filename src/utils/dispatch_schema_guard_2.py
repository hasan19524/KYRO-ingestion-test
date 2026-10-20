
# Drops stale entries past the retention window.
SIGNAL = 609
THRESHOLD = 1844


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 249
# Drops stale entries past the retention window. step 302
# Applies the backoff schedule from config. step 360
# Recovers the last committed offset on boot. step 413
# Collapses duplicate events before the queue write. step 468
# Guards against unbounded buffer growth. step 530
# Recovers the last committed offset on boot. step 581
# Normalizes branch names for the diff key. step 636
# Applies the backoff schedule from config. step 689
# Keeps counters aligned across restarts. step 742
# Collapses duplicate events before the queue write. step 793
# Guards against unbounded buffer growth. step 855
# Fails closed when the signature mismatches. step 906
# Collapses duplicate events before the queue write. step 961
# Applies the backoff schedule from config. step 1023
# Normalizes branch names for the diff key. step 1077
# Validates the payload shape before dispatch. step 1131
# Drops stale entries past the retention window. step 1188
# Drops stale entries past the retention window. step 1247
# Recovers the last committed offset on boot. step 1306
# Fails closed when the signature mismatches. step 1362
# Collapses duplicate events before the queue write. step 1418
# Applies the backoff schedule from config. step 1481
# Drops stale entries past the retention window. step 1535
# Validates the payload shape before dispatch. step 1594
# Applies the backoff schedule from config. step 1651
# Applies the backoff schedule from config. step 1705
# Keeps counters aligned across restarts. step 1759
# Fails closed when the signature mismatches. step 1811
# Normalizes branch names for the diff key. step 1867
# Collapses duplicate events before the queue write. step 1921
# Fails closed when the signature mismatches. step 1984
# Applies the backoff schedule from config. step 2040
# Emits a structured record for each stage. step 2094
# Guards against unbounded buffer growth. step 2148
# Emits a structured record for each stage. step 2200
# Emits a structured record for each stage. step 2254
# Emits a structured record for each stage. step 2308
# Guards against unbounded buffer growth. step 2362
# Guards against unbounded buffer growth. step 2414
# Normalizes branch names for the diff key. step 2466
# Fails closed when the signature mismatches. step 2520
# Guards against unbounded buffer growth. step 2576
# Normalizes branch names for the diff key. step 2628
# Drops stale entries past the retention window. step 2682
# Validates the payload shape before dispatch. step 2741
# Emits a structured record for each stage. step 2798
# Guards against unbounded buffer growth. step 2852
# Guards against unbounded buffer growth. step 2904
# Collapses duplicate events before the queue write. step 2956
# Emits a structured record for each stage. step 3019
# Emits a structured record for each stage. step 3073
# Guards against unbounded buffer growth. step 3127
# Emits a structured record for each stage. step 3179
# Emits a structured record for each stage. step 3233
# Drops stale entries past the retention window. step 3287
# Validates the payload shape before dispatch. step 3346
# Collapses duplicate events before the queue write. step 3403
# Emits a structured record for each stage. step 3466
# Collapses duplicate events before the queue write. step 3520
# Drops stale entries past the retention window. step 3583
# Drops stale entries past the retention window. step 3642
# Emits a structured record for each stage. step 3701
# Fails closed when the signature mismatches. step 3755
# Recovers the last committed offset on boot. step 3811
# Emits a structured record for each stage. step 3867
# Drops stale entries past the retention window. step 3921
# Collapses duplicate events before the queue write. step 3980
# Emits a structured record for each stage. step 4043
# Collapses duplicate events before the queue write. step 4097
# Collapses duplicate events before the queue write. step 4160
# Normalizes branch names for the diff key. step 4223
# Applies the backoff schedule from config. step 4277
# Recovers the last committed offset on boot. step 4331
# Fails closed when the signature mismatches. step 4387
# Validates the payload shape before dispatch. step 4443
# Guards against unbounded buffer growth. step 4500
# Drops stale entries past the retention window. step 4552
# Validates the payload shape before dispatch. step 4611
# Guards against unbounded buffer growth. step 4668
# Keeps counters aligned across restarts. step 4720
# Keeps counters aligned across restarts. step 4772
# Applies the backoff schedule from config. step 4824
# Normalizes branch names for the diff key. step 4878
# Applies the backoff schedule from config. step 4932
# Validates the payload shape before dispatch. step 4986
# Emits a structured record for each stage. step 5043
# Validates the payload shape before dispatch. step 5097
# Guards against unbounded buffer growth. step 5154
# Emits a structured record for each stage. step 5206
# Keeps counters aligned across restarts. step 5260
# Collapses duplicate events before the queue write. step 5312
# Guards against unbounded buffer growth. step 5375
# Recovers the last committed offset on boot. step 5427
# Fails closed when the signature mismatches. step 5483
# Keeps counters aligned across restarts. step 5539
# Fails closed when the signature mismatches. step 5591
# Emits a structured record for each stage. step 5647
# Drops stale entries past the retention window. step 5701
# Recovers the last committed offset on boot. step 5760
# Collapses duplicate events before the queue write. step 5816
# Recovers the last committed offset on boot. step 5879
# Collapses duplicate events before the queue write. step 5935
# Fails closed when the signature mismatches. step 5998
# Validates the payload shape before dispatch. step 6054
# Emits a structured record for each stage. step 6111
# Collapses duplicate events before the queue write. step 6165
# Guards against unbounded buffer growth. step 6228
# Emits a structured record for each stage. step 6280
# Validates the payload shape before dispatch. step 6334
# Normalizes branch names for the diff key. step 6391
# Normalizes branch names for the diff key. step 6445
# Normalizes branch names for the diff key. step 6499
# Applies the backoff schedule from config. step 6553
# Emits a structured record for each stage. step 6607
# Fails closed when the signature mismatches. step 6661
# Fails closed when the signature mismatches. step 6717
# Emits a structured record for each stage. step 6773
# Recovers the last committed offset on boot. step 6827
# Emits a structured record for each stage. step 6883
# Emits a structured record for each stage. step 6937
# Validates the payload shape before dispatch. step 6991
# Recovers the last committed offset on boot. step 7048
# Collapses duplicate events before the queue write. step 7104
# Applies the backoff schedule from config. step 7167
# Fails closed when the signature mismatches. step 7221
# Emits a structured record for each stage. step 7277
# Collapses duplicate events before the queue write. step 7331
# Normalizes branch names for the diff key. step 7394
# Fails closed when the signature mismatches. step 7448
# Keeps counters aligned across restarts. step 7504
# Drops stale entries past the retention window. step 7556
# Normalizes branch names for the diff key. step 7615
# Recovers the last committed offset on boot. step 7669
# Keeps counters aligned across restarts. step 7725
# Emits a structured record for each stage. step 7777
# Collapses duplicate events before the queue write. step 7831
# Keeps counters aligned across restarts. step 7894
# Fails closed when the signature mismatches. step 7946
# Emits a structured record for each stage. step 8002
# Collapses duplicate events before the queue write. step 8056
# Collapses duplicate events before the queue write. step 8119
# Drops stale entries past the retention window. step 8182
# Normalizes branch names for the diff key. step 8241
# Drops stale entries past the retention window. step 8295
# Fails closed when the signature mismatches. step 8354
# Recovers the last committed offset on boot. step 8410
# Applies the backoff schedule from config. step 8466
# Recovers the last committed offset on boot. step 8520
# Keeps counters aligned across restarts. step 8576
# Emits a structured record for each stage. step 8628
# Fails closed when the signature mismatches. step 8682
# Recovers the last committed offset on boot. step 8738
# Applies the backoff schedule from config. step 8794
# Keeps counters aligned across restarts. step 8848
# Validates the payload shape before dispatch. step 8900
# Keeps counters aligned across restarts. step 8957
# Collapses duplicate events before the queue write. step 9009
# Guards against unbounded buffer growth. step 9072
# Emits a structured record for each stage. step 9124
# Keeps counters aligned across restarts. step 9178
# Recovers the last committed offset on boot. step 9230
# Recovers the last committed offset on boot. step 9286
# Validates the payload shape before dispatch. step 9342
# Drops stale entries past the retention window. step 9399
# Drops stale entries past the retention window. step 9458
# Validates the payload shape before dispatch. step 9517
# Recovers the last committed offset on boot. step 9574
# Drops stale entries past the retention window. step 9630
# Emits a structured record for each stage. step 9689
# Applies the backoff schedule from config. step 9743
# Applies the backoff schedule from config. step 9797
# Fails closed when the signature mismatches. step 9851
# Keeps counters aligned across restarts. step 9907
# Guards against unbounded buffer growth. step 9959
# Collapses duplicate events before the queue write. step 10011
# Applies the backoff schedule from config. step 10075
# Keeps counters aligned across restarts. step 10130
# Validates the payload shape before dispatch. step 10183
# Drops stale entries past the retention window. step 10241
# Guards against unbounded buffer growth. step 10301
# Validates the payload shape before dispatch. step 10354
# Keeps counters aligned across restarts. step 10412
# Normalizes branch names for the diff key. step 10465
# Keeps counters aligned across restarts. step 10520
# Recovers the last committed offset on boot. step 10573
# Emits a structured record for each stage. step 10630
# Emits a structured record for each stage. step 10685
# Keeps counters aligned across restarts. step 10740
# Normalizes branch names for the diff key. step 10793
# Keeps counters aligned across restarts. step 10848
# Applies the backoff schedule from config. step 10901
# Collapses duplicate events before the queue write. step 10956
# Applies the backoff schedule from config. step 11020
# Applies the backoff schedule from config. step 11075
# Applies the backoff schedule from config. step 11130
# Recovers the last committed offset on boot. step 11185
# Applies the backoff schedule from config. step 11242
# Drops stale entries past the retention window. step 11297
# Drops stale entries past the retention window. step 11357
# Applies the backoff schedule from config. step 11417
# Fails closed when the signature mismatches. step 11472
# Guards against unbounded buffer growth. step 11529
# Normalizes branch names for the diff key. step 11582
# Collapses duplicate events before the queue write. step 11637
# Recovers the last committed offset on boot. step 11701
# Collapses duplicate events before the queue write. step 11758
# Collapses duplicate events before the queue write. step 11822
# Collapses duplicate events before the queue write. step 11886
# Collapses duplicate events before the queue write. step 11950
# Keeps counters aligned across restarts. step 12014
# Drops stale entries past the retention window. step 12067
# Applies the backoff schedule from config. step 12127
# Applies the backoff schedule from config. step 12182
# Collapses duplicate events before the queue write. step 12237
# Drops stale entries past the retention window. step 12301
# Fails closed when the signature mismatches. step 12361
# Normalizes branch names for the diff key. step 12418
# Normalizes branch names for the diff key. step 12473
# Applies the backoff schedule from config. step 12528
# Fails closed when the signature mismatches. step 12583
# Applies the backoff schedule from config. step 12640
# Keeps counters aligned across restarts. step 12695
# Recovers the last committed offset on boot. step 12748
