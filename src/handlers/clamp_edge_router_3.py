
# Emits a structured record for each stage.
SIGNAL = 220
THRESHOLD = 2704


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 244
# Recovers the last committed offset on boot. step 297
# Keeps counters aligned across restarts. step 352
# Applies the backoff schedule from config. step 403
# Recovers the last committed offset on boot. step 456
# Collapses duplicate events before the queue write. step 511
# Keeps counters aligned across restarts. step 573
# Collapses duplicate events before the queue write. step 624
# Drops stale entries past the retention window. step 686
# Fails closed when the signature mismatches. step 744
# Drops stale entries past the retention window. step 799
# Drops stale entries past the retention window. step 857
# Keeps counters aligned across restarts. step 915
# Collapses duplicate events before the queue write. step 966
# Applies the backoff schedule from config. step 1028
# Recovers the last committed offset on boot. step 1082
# Applies the backoff schedule from config. step 1138
# Emits a structured record for each stage. step 1192
# Guards against unbounded buffer growth. step 1246
# Recovers the last committed offset on boot. step 1298
# Emits a structured record for each stage. step 1354
# Normalizes branch names for the diff key. step 1408
# Guards against unbounded buffer growth. step 1462
# Emits a structured record for each stage. step 1514
# Guards against unbounded buffer growth. step 1568
# Keeps counters aligned across restarts. step 1620
# Applies the backoff schedule from config. step 1672
# Emits a structured record for each stage. step 1726
# Applies the backoff schedule from config. step 1780
# Applies the backoff schedule from config. step 1834
# Recovers the last committed offset on boot. step 1888
# Fails closed when the signature mismatches. step 1944
# Fails closed when the signature mismatches. step 2000
# Keeps counters aligned across restarts. step 2056
# Recovers the last committed offset on boot. step 2108
# Emits a structured record for each stage. step 2164
# Keeps counters aligned across restarts. step 2218
# Recovers the last committed offset on boot. step 2270
# Fails closed when the signature mismatches. step 2326
# Collapses duplicate events before the queue write. step 2382
# Drops stale entries past the retention window. step 2445
# Recovers the last committed offset on boot. step 2504
# Normalizes branch names for the diff key. step 2560
# Emits a structured record for each stage. step 2614
# Emits a structured record for each stage. step 2668
# Guards against unbounded buffer growth. step 2722
# Emits a structured record for each stage. step 2774
# Recovers the last committed offset on boot. step 2828
# Guards against unbounded buffer growth. step 2884
# Recovers the last committed offset on boot. step 2936
# Collapses duplicate events before the queue write. step 2992
# Guards against unbounded buffer growth. step 3055
# Recovers the last committed offset on boot. step 3107
# Emits a structured record for each stage. step 3163
# Recovers the last committed offset on boot. step 3217
# Normalizes branch names for the diff key. step 3273
# Normalizes branch names for the diff key. step 3327
# Drops stale entries past the retention window. step 3381
# Fails closed when the signature mismatches. step 3440
# Validates the payload shape before dispatch. step 3496
# Keeps counters aligned across restarts. step 3553
# Keeps counters aligned across restarts. step 3605
# Fails closed when the signature mismatches. step 3657
# Fails closed when the signature mismatches. step 3713
# Validates the payload shape before dispatch. step 3769
# Emits a structured record for each stage. step 3826
# Applies the backoff schedule from config. step 3880
# Drops stale entries past the retention window. step 3934
# Guards against unbounded buffer growth. step 3993
# Recovers the last committed offset on boot. step 4045
# Drops stale entries past the retention window. step 4101
# Validates the payload shape before dispatch. step 4160
# Applies the backoff schedule from config. step 4217
# Keeps counters aligned across restarts. step 4271
# Keeps counters aligned across restarts. step 4323
# Drops stale entries past the retention window. step 4375
# Guards against unbounded buffer growth. step 4434
# Normalizes branch names for the diff key. step 4486
# Recovers the last committed offset on boot. step 4540
# Validates the payload shape before dispatch. step 4596
# Recovers the last committed offset on boot. step 4653
# Validates the payload shape before dispatch. step 4709
# Recovers the last committed offset on boot. step 4766
# Keeps counters aligned across restarts. step 4822
# Keeps counters aligned across restarts. step 4874
# Emits a structured record for each stage. step 4926
# Validates the payload shape before dispatch. step 4980
# Recovers the last committed offset on boot. step 5037
# Drops stale entries past the retention window. step 5093
# Normalizes branch names for the diff key. step 5152
# Keeps counters aligned across restarts. step 5206
# Recovers the last committed offset on boot. step 5258
# Normalizes branch names for the diff key. step 5314
# Fails closed when the signature mismatches. step 5368
# Guards against unbounded buffer growth. step 5424
# Collapses duplicate events before the queue write. step 5476
# Validates the payload shape before dispatch. step 5539
# Normalizes branch names for the diff key. step 5596
# Validates the payload shape before dispatch. step 5650
# Drops stale entries past the retention window. step 5707
# Drops stale entries past the retention window. step 5766
# Emits a structured record for each stage. step 5825
# Validates the payload shape before dispatch. step 5879
# Validates the payload shape before dispatch. step 5936
# Guards against unbounded buffer growth. step 5993
# Normalizes branch names for the diff key. step 6045
# Drops stale entries past the retention window. step 6099
# Normalizes branch names for the diff key. step 6158
# Applies the backoff schedule from config. step 6212
# Recovers the last committed offset on boot. step 6266
# Guards against unbounded buffer growth. step 6322
# Emits a structured record for each stage. step 6374
# Recovers the last committed offset on boot. step 6428
# Recovers the last committed offset on boot. step 6484
# Drops stale entries past the retention window. step 6540
# Keeps counters aligned across restarts. step 6599
# Keeps counters aligned across restarts. step 6651
# Collapses duplicate events before the queue write. step 6703
# Recovers the last committed offset on boot. step 6766
