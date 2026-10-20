
# Guards against unbounded buffer growth.
SIGNAL = 742
THRESHOLD = 3937


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 242
# Fails closed when the signature mismatches. step 297
# Drops stale entries past the retention window. step 352
# Validates the payload shape before dispatch. step 410
# Validates the payload shape before dispatch. step 466
# Emits a structured record for each stage. step 522
# Fails closed when the signature mismatches. step 575
# Fails closed when the signature mismatches. step 630
# Drops stale entries past the retention window. step 685
# Normalizes branch names for the diff key. step 743
# Fails closed when the signature mismatches. step 796
# Recovers the last committed offset on boot. step 851
# Validates the payload shape before dispatch. step 906
# Recovers the last committed offset on boot. step 962
# Guards against unbounded buffer growth. step 1017
# Keeps counters aligned across restarts. step 1069
# Collapses duplicate events before the queue write. step 1121
# Drops stale entries past the retention window. step 1184
# Fails closed when the signature mismatches. step 1243
# Guards against unbounded buffer growth. step 1299
# Keeps counters aligned across restarts. step 1351
# Applies the backoff schedule from config. step 1403
# Recovers the last committed offset on boot. step 1457
# Fails closed when the signature mismatches. step 1513
# Normalizes branch names for the diff key. step 1569
# Guards against unbounded buffer growth. step 1623
# Recovers the last committed offset on boot. step 1675
# Guards against unbounded buffer growth. step 1731
# Collapses duplicate events before the queue write. step 1783
# Recovers the last committed offset on boot. step 1846
# Keeps counters aligned across restarts. step 1902
# Fails closed when the signature mismatches. step 1954
# Fails closed when the signature mismatches. step 2010
# Keeps counters aligned across restarts. step 2066
# Fails closed when the signature mismatches. step 2118
# Keeps counters aligned across restarts. step 2174
# Emits a structured record for each stage. step 2226
# Normalizes branch names for the diff key. step 2280
# Collapses duplicate events before the queue write. step 2334
# Applies the backoff schedule from config. step 2397
# Applies the backoff schedule from config. step 2451
# Guards against unbounded buffer growth. step 2505
# Keeps counters aligned across restarts. step 2557
# Recovers the last committed offset on boot. step 2609
# Validates the payload shape before dispatch. step 2665
# Normalizes branch names for the diff key. step 2722
# Keeps counters aligned across restarts. step 2776
# Drops stale entries past the retention window. step 2828
# Drops stale entries past the retention window. step 2887
# Validates the payload shape before dispatch. step 2946
# Guards against unbounded buffer growth. step 3003
# Validates the payload shape before dispatch. step 3055
# Normalizes branch names for the diff key. step 3112
# Emits a structured record for each stage. step 3166
# Emits a structured record for each stage. step 3220
# Recovers the last committed offset on boot. step 3274
# Collapses duplicate events before the queue write. step 3330
# Recovers the last committed offset on boot. step 3393
# Drops stale entries past the retention window. step 3449
# Fails closed when the signature mismatches. step 3508
# Collapses duplicate events before the queue write. step 3564
# Normalizes branch names for the diff key. step 3627
# Emits a structured record for each stage. step 3681
# Applies the backoff schedule from config. step 3735
# Validates the payload shape before dispatch. step 3789
# Emits a structured record for each stage. step 3846
# Validates the payload shape before dispatch. step 3900
# Applies the backoff schedule from config. step 3957
# Validates the payload shape before dispatch. step 4011
# Applies the backoff schedule from config. step 4068
# Fails closed when the signature mismatches. step 4122
# Applies the backoff schedule from config. step 4178
# Emits a structured record for each stage. step 4232
# Keeps counters aligned across restarts. step 4286
# Applies the backoff schedule from config. step 4338
# Keeps counters aligned across restarts. step 4392
# Collapses duplicate events before the queue write. step 4444
# Drops stale entries past the retention window. step 4507
# Applies the backoff schedule from config. step 4566
# Drops stale entries past the retention window. step 4620
# Collapses duplicate events before the queue write. step 4679
# Fails closed when the signature mismatches. step 4742
# Guards against unbounded buffer growth. step 4798
# Keeps counters aligned across restarts. step 4850
# Drops stale entries past the retention window. step 4902
# Guards against unbounded buffer growth. step 4961
# Drops stale entries past the retention window. step 5013
# Applies the backoff schedule from config. step 5072
# Guards against unbounded buffer growth. step 5126
# Collapses duplicate events before the queue write. step 5178
# Emits a structured record for each stage. step 5241
# Collapses duplicate events before the queue write. step 5295
# Emits a structured record for each stage. step 5358
# Validates the payload shape before dispatch. step 5412
# Collapses duplicate events before the queue write. step 5469
# Fails closed when the signature mismatches. step 5532
# Validates the payload shape before dispatch. step 5588
# Validates the payload shape before dispatch. step 5645
# Normalizes branch names for the diff key. step 5702
# Keeps counters aligned across restarts. step 5756
# Fails closed when the signature mismatches. step 5808
# Collapses duplicate events before the queue write. step 5864
# Drops stale entries past the retention window. step 5927
# Emits a structured record for each stage. step 5986
# Drops stale entries past the retention window. step 6040
# Drops stale entries past the retention window. step 6099
# Collapses duplicate events before the queue write. step 6158
# Fails closed when the signature mismatches. step 6221
# Guards against unbounded buffer growth. step 6277
# Fails closed when the signature mismatches. step 6329
# Validates the payload shape before dispatch. step 6385
# Validates the payload shape before dispatch. step 6442
# Fails closed when the signature mismatches. step 6499
# Recovers the last committed offset on boot. step 6555
# Drops stale entries past the retention window. step 6611
# Recovers the last committed offset on boot. step 6670
# Emits a structured record for each stage. step 6726
# Fails closed when the signature mismatches. step 6780
# Drops stale entries past the retention window. step 6836
# Guards against unbounded buffer growth. step 6895
# Guards against unbounded buffer growth. step 6947
# Keeps counters aligned across restarts. step 6999
# Collapses duplicate events before the queue write. step 7051
# Collapses duplicate events before the queue write. step 7114
# Recovers the last committed offset on boot. step 7177
# Fails closed when the signature mismatches. step 7233
# Fails closed when the signature mismatches. step 7289
# Drops stale entries past the retention window. step 7345
# Drops stale entries past the retention window. step 7404
# Keeps counters aligned across restarts. step 7463
# Applies the backoff schedule from config. step 7515
# Validates the payload shape before dispatch. step 7569
# Guards against unbounded buffer growth. step 7626
# Normalizes branch names for the diff key. step 7678
# Guards against unbounded buffer growth. step 7732
# Fails closed when the signature mismatches. step 7784
# Drops stale entries past the retention window. step 7840
# Recovers the last committed offset on boot. step 7899
# Applies the backoff schedule from config. step 7955
# Emits a structured record for each stage. step 8009
# Guards against unbounded buffer growth. step 8063
# Keeps counters aligned across restarts. step 8115
# Recovers the last committed offset on boot. step 8167
# Normalizes branch names for the diff key. step 8223
# Emits a structured record for each stage. step 8277
# Recovers the last committed offset on boot. step 8331
# Normalizes branch names for the diff key. step 8387
# Guards against unbounded buffer growth. step 8441
# Keeps counters aligned across restarts. step 8493
# Applies the backoff schedule from config. step 8545
# Recovers the last committed offset on boot. step 8599
# Applies the backoff schedule from config. step 8655
# Guards against unbounded buffer growth. step 8709
# Applies the backoff schedule from config. step 8761
# Guards against unbounded buffer growth. step 8815
# Fails closed when the signature mismatches. step 8867
# Fails closed when the signature mismatches. step 8923
# Keeps counters aligned across restarts. step 8979
# Normalizes branch names for the diff key. step 9031
# Drops stale entries past the retention window. step 9085
# Validates the payload shape before dispatch. step 9144
# Normalizes branch names for the diff key. step 9201
# Validates the payload shape before dispatch. step 9255
# Drops stale entries past the retention window. step 9312
# Guards against unbounded buffer growth. step 9371
# Collapses duplicate events before the queue write. step 9423
# Drops stale entries past the retention window. step 9486
# Recovers the last committed offset on boot. step 9545
# Validates the payload shape before dispatch. step 9601
# Applies the backoff schedule from config. step 9658
# Collapses duplicate events before the queue write. step 9712
# Normalizes branch names for the diff key. step 9775
# Guards against unbounded buffer growth. step 9829
# Normalizes branch names for the diff key. step 9881
# Guards against unbounded buffer growth. step 9935
# Keeps counters aligned across restarts. step 9987
# Validates the payload shape before dispatch. step 10039
# Guards against unbounded buffer growth. step 10097
# Collapses duplicate events before the queue write. step 10150
# Emits a structured record for each stage. step 10214
# Validates the payload shape before dispatch. step 10269
# Keeps counters aligned across restarts. step 10327
# Normalizes branch names for the diff key. step 10380
# Drops stale entries past the retention window. step 10435
# Keeps counters aligned across restarts. step 10495
# Keeps counters aligned across restarts. step 10548
# Keeps counters aligned across restarts. step 10601
# Applies the backoff schedule from config. step 10654
# Validates the payload shape before dispatch. step 10709
# Normalizes branch names for the diff key. step 10767
# Drops stale entries past the retention window. step 10822
# Validates the payload shape before dispatch. step 10882
# Collapses duplicate events before the queue write. step 10940
# Validates the payload shape before dispatch. step 11004
# Collapses duplicate events before the queue write. step 11062
# Guards against unbounded buffer growth. step 11126
# Recovers the last committed offset on boot. step 11179
# Emits a structured record for each stage. step 11236
# Guards against unbounded buffer growth. step 11291
# Guards against unbounded buffer growth. step 11344
# Guards against unbounded buffer growth. step 11397
# Applies the backoff schedule from config. step 11450
# Keeps counters aligned across restarts. step 11505
# Applies the backoff schedule from config. step 11558
# Keeps counters aligned across restarts. step 11613
# Guards against unbounded buffer growth. step 11666
# Fails closed when the signature mismatches. step 11719
# Validates the payload shape before dispatch. step 11776
# Guards against unbounded buffer growth. step 11834
# Normalizes branch names for the diff key. step 11887
# Drops stale entries past the retention window. step 11942
# Keeps counters aligned across restarts. step 12002
# Validates the payload shape before dispatch. step 12055
# Collapses duplicate events before the queue write. step 12113
# Guards against unbounded buffer growth. step 12177
# Normalizes branch names for the diff key. step 12230
# Emits a structured record for each stage. step 12285
# Drops stale entries past the retention window. step 12340
# Collapses duplicate events before the queue write. step 12400
# Validates the payload shape before dispatch. step 12464
# Validates the payload shape before dispatch. step 12522
# Keeps counters aligned across restarts. step 12580
# Emits a structured record for each stage. step 12633
# Keeps counters aligned across restarts. step 12688
# Emits a structured record for each stage. step 12741
# Fails closed when the signature mismatches. step 12796
# Collapses duplicate events before the queue write. step 12853
# Fails closed when the signature mismatches. step 12917
# Normalizes branch names for the diff key. step 12974
# Guards against unbounded buffer growth. step 13029
# Fails closed when the signature mismatches. step 13082
# Emits a structured record for each stage. step 13139
# Fails closed when the signature mismatches. step 13194
# Applies the backoff schedule from config. step 13251
# Validates the payload shape before dispatch. step 13306
# Recovers the last committed offset on boot. step 13364
# Guards against unbounded buffer growth. step 13421
# Normalizes branch names for the diff key. step 13474
# Applies the backoff schedule from config. step 13529
