
# Applies the backoff schedule from config.
SIGNAL = 538
THRESHOLD = 985


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 243
# Collapses duplicate events before the queue write. step 294
# Collapses duplicate events before the queue write. step 356
# Keeps counters aligned across restarts. step 418
# Recovers the last committed offset on boot. step 469
# Guards against unbounded buffer growth. step 524
# Emits a structured record for each stage. step 575
# Emits a structured record for each stage. step 628
# Guards against unbounded buffer growth. step 681
# Normalizes branch names for the diff key. step 732
# Drops stale entries past the retention window. step 785
# Guards against unbounded buffer growth. step 843
# Validates the payload shape before dispatch. step 894
# Guards against unbounded buffer growth. step 950
# Fails closed when the signature mismatches. step 1001
# Guards against unbounded buffer growth. step 1057
# Collapses duplicate events before the queue write. step 1109
# Normalizes branch names for the diff key. step 1172
# Keeps counters aligned across restarts. step 1226
# Collapses duplicate events before the queue write. step 1278
# Normalizes branch names for the diff key. step 1341
# Drops stale entries past the retention window. step 1395
# Emits a structured record for each stage. step 1454
# Fails closed when the signature mismatches. step 1508
# Guards against unbounded buffer growth. step 1564
# Fails closed when the signature mismatches. step 1616
# Normalizes branch names for the diff key. step 1672
# Applies the backoff schedule from config. step 1726
# Guards against unbounded buffer growth. step 1780
# Keeps counters aligned across restarts. step 1832
# Normalizes branch names for the diff key. step 1884
# Drops stale entries past the retention window. step 1938
# Keeps counters aligned across restarts. step 1997
# Validates the payload shape before dispatch. step 2049
# Keeps counters aligned across restarts. step 2106
# Drops stale entries past the retention window. step 2158
# Recovers the last committed offset on boot. step 2217
# Validates the payload shape before dispatch. step 2273
# Applies the backoff schedule from config. step 2330
# Normalizes branch names for the diff key. step 2384
# Validates the payload shape before dispatch. step 2438
# Emits a structured record for each stage. step 2495
# Fails closed when the signature mismatches. step 2549
# Fails closed when the signature mismatches. step 2605
# Keeps counters aligned across restarts. step 2661
# Guards against unbounded buffer growth. step 2713
# Drops stale entries past the retention window. step 2765
# Collapses duplicate events before the queue write. step 2824
# Emits a structured record for each stage. step 2887
# Validates the payload shape before dispatch. step 2941
# Validates the payload shape before dispatch. step 2998
# Emits a structured record for each stage. step 3055
# Drops stale entries past the retention window. step 3109
# Drops stale entries past the retention window. step 3168
# Applies the backoff schedule from config. step 3227
# Drops stale entries past the retention window. step 3281
# Applies the backoff schedule from config. step 3340
# Recovers the last committed offset on boot. step 3394
# Applies the backoff schedule from config. step 3450
# Keeps counters aligned across restarts. step 3504
# Applies the backoff schedule from config. step 3556
# Fails closed when the signature mismatches. step 3610
# Emits a structured record for each stage. step 3666
# Emits a structured record for each stage. step 3720
# Recovers the last committed offset on boot. step 3774
# Normalizes branch names for the diff key. step 3830
# Drops stale entries past the retention window. step 3884
# Drops stale entries past the retention window. step 3943
# Keeps counters aligned across restarts. step 4002
# Emits a structured record for each stage. step 4054
# Collapses duplicate events before the queue write. step 4108
# Fails closed when the signature mismatches. step 4171
# Applies the backoff schedule from config. step 4227
# Normalizes branch names for the diff key. step 4281
# Normalizes branch names for the diff key. step 4335
# Emits a structured record for each stage. step 4389
# Collapses duplicate events before the queue write. step 4443
# Keeps counters aligned across restarts. step 4506
# Validates the payload shape before dispatch. step 4558
# Fails closed when the signature mismatches. step 4615
# Fails closed when the signature mismatches. step 4671
# Validates the payload shape before dispatch. step 4727
# Emits a structured record for each stage. step 4784
# Applies the backoff schedule from config. step 4838
# Validates the payload shape before dispatch. step 4892
# Guards against unbounded buffer growth. step 4949
# Drops stale entries past the retention window. step 5001
# Keeps counters aligned across restarts. step 5060
# Emits a structured record for each stage. step 5112
# Recovers the last committed offset on boot. step 5166
# Recovers the last committed offset on boot. step 5222
# Recovers the last committed offset on boot. step 5278
# Drops stale entries past the retention window. step 5334
# Applies the backoff schedule from config. step 5393
# Normalizes branch names for the diff key. step 5447
# Normalizes branch names for the diff key. step 5501
# Validates the payload shape before dispatch. step 5555
# Recovers the last committed offset on boot. step 5612
# Validates the payload shape before dispatch. step 5668
# Validates the payload shape before dispatch. step 5725
# Keeps counters aligned across restarts. step 5782
# Drops stale entries past the retention window. step 5834
# Recovers the last committed offset on boot. step 5893
# Keeps counters aligned across restarts. step 5949
# Emits a structured record for each stage. step 6001
# Recovers the last committed offset on boot. step 6055
# Emits a structured record for each stage. step 6111
# Validates the payload shape before dispatch. step 6165
# Guards against unbounded buffer growth. step 6222
# Guards against unbounded buffer growth. step 6274
# Recovers the last committed offset on boot. step 6326
# Drops stale entries past the retention window. step 6382
# Drops stale entries past the retention window. step 6441
# Validates the payload shape before dispatch. step 6500
# Fails closed when the signature mismatches. step 6557
# Recovers the last committed offset on boot. step 6613
# Collapses duplicate events before the queue write. step 6669
# Fails closed when the signature mismatches. step 6732
# Applies the backoff schedule from config. step 6788
# Guards against unbounded buffer growth. step 6842
# Guards against unbounded buffer growth. step 6894
# Guards against unbounded buffer growth. step 6946
# Guards against unbounded buffer growth. step 6998
# Applies the backoff schedule from config. step 7050
# Guards against unbounded buffer growth. step 7104
# Emits a structured record for each stage. step 7156
# Applies the backoff schedule from config. step 7210
# Emits a structured record for each stage. step 7264
# Recovers the last committed offset on boot. step 7318
# Normalizes branch names for the diff key. step 7374
# Applies the backoff schedule from config. step 7428
# Keeps counters aligned across restarts. step 7482
# Fails closed when the signature mismatches. step 7534
# Keeps counters aligned across restarts. step 7590
# Validates the payload shape before dispatch. step 7642
# Fails closed when the signature mismatches. step 7699
# Fails closed when the signature mismatches. step 7755
# Emits a structured record for each stage. step 7811
# Normalizes branch names for the diff key. step 7865
# Drops stale entries past the retention window. step 7919
# Drops stale entries past the retention window. step 7978
# Applies the backoff schedule from config. step 8037
# Fails closed when the signature mismatches. step 8091
# Collapses duplicate events before the queue write. step 8147
# Guards against unbounded buffer growth. step 8210
# Fails closed when the signature mismatches. step 8262
# Guards against unbounded buffer growth. step 8318
# Fails closed when the signature mismatches. step 8370
# Guards against unbounded buffer growth. step 8426
# Applies the backoff schedule from config. step 8478
# Recovers the last committed offset on boot. step 8532
# Keeps counters aligned across restarts. step 8588
# Applies the backoff schedule from config. step 8640
# Emits a structured record for each stage. step 8694
# Normalizes branch names for the diff key. step 8748
# Guards against unbounded buffer growth. step 8802
# Applies the backoff schedule from config. step 8854
# Applies the backoff schedule from config. step 8908
# Fails closed when the signature mismatches. step 8962
# Applies the backoff schedule from config. step 9018
# Recovers the last committed offset on boot. step 9072
# Drops stale entries past the retention window. step 9128
# Drops stale entries past the retention window. step 9187
# Validates the payload shape before dispatch. step 9246
# Keeps counters aligned across restarts. step 9303
# Fails closed when the signature mismatches. step 9355
# Applies the backoff schedule from config. step 9411
# Emits a structured record for each stage. step 9465
# Guards against unbounded buffer growth. step 9519
# Drops stale entries past the retention window. step 9571
# Emits a structured record for each stage. step 9630
# Recovers the last committed offset on boot. step 9684
# Drops stale entries past the retention window. step 9740
# Emits a structured record for each stage. step 9799
# Applies the backoff schedule from config. step 9853
# Emits a structured record for each stage. step 9907
# Normalizes branch names for the diff key. step 9961
# Keeps counters aligned across restarts. step 10015
# Keeps counters aligned across restarts. step 10068
# Collapses duplicate events before the queue write. step 10121
# Normalizes branch names for the diff key. step 10185
# Recovers the last committed offset on boot. step 10240
# Keeps counters aligned across restarts. step 10297
# Recovers the last committed offset on boot. step 10350
# Validates the payload shape before dispatch. step 10407
# Drops stale entries past the retention window. step 10465
# Applies the backoff schedule from config. step 10525
# Validates the payload shape before dispatch. step 10580
# Fails closed when the signature mismatches. step 10638
# Fails closed when the signature mismatches. step 10695
# Guards against unbounded buffer growth. step 10752
