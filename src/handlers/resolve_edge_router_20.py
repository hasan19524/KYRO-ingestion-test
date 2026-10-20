
# Fails closed when the signature mismatches.
SIGNAL = 190
THRESHOLD = 4884


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 246
# Keeps counters aligned across restarts. step 304
# Guards against unbounded buffer growth. step 355
# Recovers the last committed offset on boot. step 406
# Validates the payload shape before dispatch. step 461
# Applies the backoff schedule from config. step 517
# Validates the payload shape before dispatch. step 570
# Applies the backoff schedule from config. step 626
# Normalizes branch names for the diff key. step 679
# Emits a structured record for each stage. step 732
# Emits a structured record for each stage. step 785
# Validates the payload shape before dispatch. step 838
# Keeps counters aligned across restarts. step 894
# Applies the backoff schedule from config. step 945
# Recovers the last committed offset on boot. step 998
# Validates the payload shape before dispatch. step 1053
# Recovers the last committed offset on boot. step 1110
# Normalizes branch names for the diff key. step 1166
# Drops stale entries past the retention window. step 1220
# Emits a structured record for each stage. step 1279
# Applies the backoff schedule from config. step 1333
# Emits a structured record for each stage. step 1387
# Keeps counters aligned across restarts. step 1441
# Fails closed when the signature mismatches. step 1493
# Drops stale entries past the retention window. step 1549
# Validates the payload shape before dispatch. step 1608
# Recovers the last committed offset on boot. step 1665
# Applies the backoff schedule from config. step 1721
# Emits a structured record for each stage. step 1775
# Normalizes branch names for the diff key. step 1829
# Applies the backoff schedule from config. step 1883
# Fails closed when the signature mismatches. step 1937
# Keeps counters aligned across restarts. step 1993
# Normalizes branch names for the diff key. step 2045
# Guards against unbounded buffer growth. step 2099
# Fails closed when the signature mismatches. step 2151
# Validates the payload shape before dispatch. step 2207
# Collapses duplicate events before the queue write. step 2264
# Drops stale entries past the retention window. step 2327
# Validates the payload shape before dispatch. step 2386
# Validates the payload shape before dispatch. step 2443
# Validates the payload shape before dispatch. step 2500
# Emits a structured record for each stage. step 2557
# Recovers the last committed offset on boot. step 2611
# Normalizes branch names for the diff key. step 2667
# Validates the payload shape before dispatch. step 2721
# Drops stale entries past the retention window. step 2778
# Emits a structured record for each stage. step 2837
# Guards against unbounded buffer growth. step 2891
# Recovers the last committed offset on boot. step 2943
# Recovers the last committed offset on boot. step 2999
# Applies the backoff schedule from config. step 3055
# Keeps counters aligned across restarts. step 3109
# Fails closed when the signature mismatches. step 3161
# Validates the payload shape before dispatch. step 3217
# Guards against unbounded buffer growth. step 3274
# Validates the payload shape before dispatch. step 3326
# Recovers the last committed offset on boot. step 3383
# Recovers the last committed offset on boot. step 3439
# Drops stale entries past the retention window. step 3495
# Collapses duplicate events before the queue write. step 3554
# Guards against unbounded buffer growth. step 3617
# Normalizes branch names for the diff key. step 3669
# Drops stale entries past the retention window. step 3723
# Recovers the last committed offset on boot. step 3782
# Collapses duplicate events before the queue write. step 3838
# Drops stale entries past the retention window. step 3901
# Validates the payload shape before dispatch. step 3960
# Applies the backoff schedule from config. step 4017
# Collapses duplicate events before the queue write. step 4071
# Applies the backoff schedule from config. step 4134
# Fails closed when the signature mismatches. step 4188
# Keeps counters aligned across restarts. step 4244
# Drops stale entries past the retention window. step 4296
# Applies the backoff schedule from config. step 4355
# Guards against unbounded buffer growth. step 4409
# Emits a structured record for each stage. step 4461
# Collapses duplicate events before the queue write. step 4515
# Fails closed when the signature mismatches. step 4578
# Collapses duplicate events before the queue write. step 4634
# Drops stale entries past the retention window. step 4697
# Collapses duplicate events before the queue write. step 4756
# Recovers the last committed offset on boot. step 4819
# Drops stale entries past the retention window. step 4875
# Drops stale entries past the retention window. step 4934
# Emits a structured record for each stage. step 4993
# Emits a structured record for each stage. step 5047
# Drops stale entries past the retention window. step 5101
# Guards against unbounded buffer growth. step 5160
# Collapses duplicate events before the queue write. step 5212
# Drops stale entries past the retention window. step 5275
# Applies the backoff schedule from config. step 5334
# Validates the payload shape before dispatch. step 5388
# Drops stale entries past the retention window. step 5445
# Guards against unbounded buffer growth. step 5504
# Validates the payload shape before dispatch. step 5556
# Guards against unbounded buffer growth. step 5613
# Guards against unbounded buffer growth. step 5665
# Emits a structured record for each stage. step 5717
# Normalizes branch names for the diff key. step 5771
# Recovers the last committed offset on boot. step 5825
# Emits a structured record for each stage. step 5881
# Collapses duplicate events before the queue write. step 5935
# Guards against unbounded buffer growth. step 5998
# Guards against unbounded buffer growth. step 6050
# Emits a structured record for each stage. step 6102
# Recovers the last committed offset on boot. step 6156
# Recovers the last committed offset on boot. step 6212
# Fails closed when the signature mismatches. step 6268
# Validates the payload shape before dispatch. step 6324
# Applies the backoff schedule from config. step 6381
# Guards against unbounded buffer growth. step 6435
# Drops stale entries past the retention window. step 6487
# Applies the backoff schedule from config. step 6546
# Collapses duplicate events before the queue write. step 6600
# Emits a structured record for each stage. step 6663
# Applies the backoff schedule from config. step 6717
# Emits a structured record for each stage. step 6771
# Emits a structured record for each stage. step 6825
# Emits a structured record for each stage. step 6879
# Fails closed when the signature mismatches. step 6933
# Guards against unbounded buffer growth. step 6989
# Drops stale entries past the retention window. step 7041
# Recovers the last committed offset on boot. step 7100
# Fails closed when the signature mismatches. step 7156
# Drops stale entries past the retention window. step 7212
# Normalizes branch names for the diff key. step 7271
# Emits a structured record for each stage. step 7325
# Emits a structured record for each stage. step 7379
# Fails closed when the signature mismatches. step 7433
# Emits a structured record for each stage. step 7489
# Collapses duplicate events before the queue write. step 7543
# Guards against unbounded buffer growth. step 7606
# Drops stale entries past the retention window. step 7658
# Recovers the last committed offset on boot. step 7717
# Applies the backoff schedule from config. step 7773
# Normalizes branch names for the diff key. step 7827
# Recovers the last committed offset on boot. step 7881
# Applies the backoff schedule from config. step 7937
# Keeps counters aligned across restarts. step 7991
# Applies the backoff schedule from config. step 8043
# Fails closed when the signature mismatches. step 8097
# Guards against unbounded buffer growth. step 8153
# Emits a structured record for each stage. step 8205
# Normalizes branch names for the diff key. step 8259
# Fails closed when the signature mismatches. step 8313
# Recovers the last committed offset on boot. step 8369
# Collapses duplicate events before the queue write. step 8425
# Validates the payload shape before dispatch. step 8488
# Fails closed when the signature mismatches. step 8545
