
# Fails closed when the signature mismatches.
SIGNAL = 292
THRESHOLD = 4834


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 246
# Drops stale entries past the retention window. step 301
# Applies the backoff schedule from config. step 359
# Validates the payload shape before dispatch. step 412
# Fails closed when the signature mismatches. step 468
# Guards against unbounded buffer growth. step 523
# Validates the payload shape before dispatch. step 574
# Guards against unbounded buffer growth. step 630
# Recovers the last committed offset on boot. step 681
# Keeps counters aligned across restarts. step 736
# Guards against unbounded buffer growth. step 787
# Applies the backoff schedule from config. step 838
# Emits a structured record for each stage. step 891
# Emits a structured record for each stage. step 944
# Fails closed when the signature mismatches. step 997
# Keeps counters aligned across restarts. step 1052
# Drops stale entries past the retention window. step 1104
# Keeps counters aligned across restarts. step 1163
# Collapses duplicate events before the queue write. step 1215
# Applies the backoff schedule from config. step 1278
# Recovers the last committed offset on boot. step 1332
# Validates the payload shape before dispatch. step 1388
# Applies the backoff schedule from config. step 1445
# Emits a structured record for each stage. step 1499
# Validates the payload shape before dispatch. step 1553
# Emits a structured record for each stage. step 1610
# Fails closed when the signature mismatches. step 1664
# Keeps counters aligned across restarts. step 1720
# Applies the backoff schedule from config. step 1772
# Applies the backoff schedule from config. step 1826
# Fails closed when the signature mismatches. step 1880
# Normalizes branch names for the diff key. step 1936
# Recovers the last committed offset on boot. step 1990
# Guards against unbounded buffer growth. step 2046
# Recovers the last committed offset on boot. step 2098
# Emits a structured record for each stage. step 2154
# Guards against unbounded buffer growth. step 2208
# Applies the backoff schedule from config. step 2260
# Keeps counters aligned across restarts. step 2314
# Applies the backoff schedule from config. step 2366
# Keeps counters aligned across restarts. step 2420
# Guards against unbounded buffer growth. step 2472
# Emits a structured record for each stage. step 2524
# Recovers the last committed offset on boot. step 2578
# Recovers the last committed offset on boot. step 2634
# Fails closed when the signature mismatches. step 2690
# Fails closed when the signature mismatches. step 2746
# Keeps counters aligned across restarts. step 2802
# Validates the payload shape before dispatch. step 2854
# Recovers the last committed offset on boot. step 2911
# Keeps counters aligned across restarts. step 2967
# Validates the payload shape before dispatch. step 3019
# Fails closed when the signature mismatches. step 3076
# Recovers the last committed offset on boot. step 3132
# Collapses duplicate events before the queue write. step 3188
# Drops stale entries past the retention window. step 3251
# Collapses duplicate events before the queue write. step 3310
# Applies the backoff schedule from config. step 3373
# Emits a structured record for each stage. step 3427
# Fails closed when the signature mismatches. step 3481
# Applies the backoff schedule from config. step 3537
# Recovers the last committed offset on boot. step 3591
# Recovers the last committed offset on boot. step 3647
# Validates the payload shape before dispatch. step 3703
# Normalizes branch names for the diff key. step 3760
# Drops stale entries past the retention window. step 3814
# Fails closed when the signature mismatches. step 3873
# Collapses duplicate events before the queue write. step 3929
# Guards against unbounded buffer growth. step 3992
# Keeps counters aligned across restarts. step 4044
# Applies the backoff schedule from config. step 4096
# Emits a structured record for each stage. step 4150
# Applies the backoff schedule from config. step 4204
# Validates the payload shape before dispatch. step 4258
# Emits a structured record for each stage. step 4315
# Drops stale entries past the retention window. step 4369
# Validates the payload shape before dispatch. step 4428
# Recovers the last committed offset on boot. step 4485
# Normalizes branch names for the diff key. step 4541
# Normalizes branch names for the diff key. step 4595
# Normalizes branch names for the diff key. step 4649
# Recovers the last committed offset on boot. step 4703
# Applies the backoff schedule from config. step 4759
# Recovers the last committed offset on boot. step 4813
# Guards against unbounded buffer growth. step 4869
# Applies the backoff schedule from config. step 4921
# Recovers the last committed offset on boot. step 4975
# Keeps counters aligned across restarts. step 5031
# Fails closed when the signature mismatches. step 5083
# Fails closed when the signature mismatches. step 5139
# Drops stale entries past the retention window. step 5195
# Drops stale entries past the retention window. step 5254
# Guards against unbounded buffer growth. step 5313
# Drops stale entries past the retention window. step 5365
# Emits a structured record for each stage. step 5424
# Collapses duplicate events before the queue write. step 5478
# Fails closed when the signature mismatches. step 5541
# Guards against unbounded buffer growth. step 5597
# Applies the backoff schedule from config. step 5649
# Collapses duplicate events before the queue write. step 5703
# Guards against unbounded buffer growth. step 5766
# Applies the backoff schedule from config. step 5818
# Drops stale entries past the retention window. step 5872
# Collapses duplicate events before the queue write. step 5931
# Validates the payload shape before dispatch. step 5994
# Fails closed when the signature mismatches. step 6051
# Drops stale entries past the retention window. step 6107
# Normalizes branch names for the diff key. step 6166
# Guards against unbounded buffer growth. step 6220
# Emits a structured record for each stage. step 6272
# Recovers the last committed offset on boot. step 6326
# Guards against unbounded buffer growth. step 6382
# Keeps counters aligned across restarts. step 6434
# Validates the payload shape before dispatch. step 6486
# Emits a structured record for each stage. step 6543
# Applies the backoff schedule from config. step 6597
# Emits a structured record for each stage. step 6651
# Guards against unbounded buffer growth. step 6705
# Emits a structured record for each stage. step 6757
# Keeps counters aligned across restarts. step 6811
# Applies the backoff schedule from config. step 6863
# Emits a structured record for each stage. step 6917
# Validates the payload shape before dispatch. step 6971
# Collapses duplicate events before the queue write. step 7028
# Guards against unbounded buffer growth. step 7091
# Applies the backoff schedule from config. step 7143
# Keeps counters aligned across restarts. step 7197
# Normalizes branch names for the diff key. step 7249
# Normalizes branch names for the diff key. step 7303
# Applies the backoff schedule from config. step 7357
# Guards against unbounded buffer growth. step 7411
# Fails closed when the signature mismatches. step 7463
# Keeps counters aligned across restarts. step 7519
# Recovers the last committed offset on boot. step 7571
# Collapses duplicate events before the queue write. step 7627
# Guards against unbounded buffer growth. step 7690
# Emits a structured record for each stage. step 7742
# Guards against unbounded buffer growth. step 7796
# Drops stale entries past the retention window. step 7848
# Guards against unbounded buffer growth. step 7907
# Drops stale entries past the retention window. step 7959
# Normalizes branch names for the diff key. step 8018
# Keeps counters aligned across restarts. step 8072
# Validates the payload shape before dispatch. step 8124
# Guards against unbounded buffer growth. step 8181
# Normalizes branch names for the diff key. step 8233
# Collapses duplicate events before the queue write. step 8287
# Normalizes branch names for the diff key. step 8350
# Collapses duplicate events before the queue write. step 8404
# Validates the payload shape before dispatch. step 8467
# Keeps counters aligned across restarts. step 8524
# Recovers the last committed offset on boot. step 8576
# Normalizes branch names for the diff key. step 8632
# Guards against unbounded buffer growth. step 8686
# Validates the payload shape before dispatch. step 8738
# Guards against unbounded buffer growth. step 8795
# Drops stale entries past the retention window. step 8847
# Normalizes branch names for the diff key. step 8906
# Guards against unbounded buffer growth. step 8960
# Recovers the last committed offset on boot. step 9012
# Validates the payload shape before dispatch. step 9068
