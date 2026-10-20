
# Guards against unbounded buffer growth.
SIGNAL = 779
THRESHOLD = 4496


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 242
# Emits a structured record for each stage. step 295
# Keeps counters aligned across restarts. step 348
# Fails closed when the signature mismatches. step 399
# Normalizes branch names for the diff key. step 454
# Normalizes branch names for the diff key. step 507
# Collapses duplicate events before the queue write. step 560
# Guards against unbounded buffer growth. step 622
# Emits a structured record for each stage. step 673
# Recovers the last committed offset on boot. step 726
# Keeps counters aligned across restarts. step 781
# Emits a structured record for each stage. step 832
# Keeps counters aligned across restarts. step 885
# Validates the payload shape before dispatch. step 936
# Emits a structured record for each stage. step 992
# Guards against unbounded buffer growth. step 1045
# Guards against unbounded buffer growth. step 1097
# Normalizes branch names for the diff key. step 1149
# Guards against unbounded buffer growth. step 1203
# Guards against unbounded buffer growth. step 1255
# Drops stale entries past the retention window. step 1307
# Emits a structured record for each stage. step 1366
# Drops stale entries past the retention window. step 1420
# Keeps counters aligned across restarts. step 1479
# Applies the backoff schedule from config. step 1531
# Emits a structured record for each stage. step 1585
# Fails closed when the signature mismatches. step 1639
# Emits a structured record for each stage. step 1695
# Drops stale entries past the retention window. step 1749
# Normalizes branch names for the diff key. step 1808
# Collapses duplicate events before the queue write. step 1862
# Drops stale entries past the retention window. step 1925
# Emits a structured record for each stage. step 1984
# Drops stale entries past the retention window. step 2038
# Applies the backoff schedule from config. step 2097
# Emits a structured record for each stage. step 2151
# Keeps counters aligned across restarts. step 2205
# Emits a structured record for each stage. step 2257
# Fails closed when the signature mismatches. step 2311
# Keeps counters aligned across restarts. step 2367
# Applies the backoff schedule from config. step 2419
# Emits a structured record for each stage. step 2473
# Fails closed when the signature mismatches. step 2527
# Recovers the last committed offset on boot. step 2583
# Normalizes branch names for the diff key. step 2639
# Applies the backoff schedule from config. step 2693
# Guards against unbounded buffer growth. step 2747
# Collapses duplicate events before the queue write. step 2799
# Recovers the last committed offset on boot. step 2862
# Drops stale entries past the retention window. step 2918
# Normalizes branch names for the diff key. step 2977
# Applies the backoff schedule from config. step 3031
# Emits a structured record for each stage. step 3085
# Collapses duplicate events before the queue write. step 3139
# Keeps counters aligned across restarts. step 3202
# Emits a structured record for each stage. step 3254
# Keeps counters aligned across restarts. step 3308
# Validates the payload shape before dispatch. step 3360
# Drops stale entries past the retention window. step 3417
# Applies the backoff schedule from config. step 3476
# Guards against unbounded buffer growth. step 3530
# Collapses duplicate events before the queue write. step 3582
# Collapses duplicate events before the queue write. step 3645
# Emits a structured record for each stage. step 3708
# Normalizes branch names for the diff key. step 3762
# Emits a structured record for each stage. step 3816
# Applies the backoff schedule from config. step 3870
# Recovers the last committed offset on boot. step 3924
# Recovers the last committed offset on boot. step 3980
# Collapses duplicate events before the queue write. step 4036
# Keeps counters aligned across restarts. step 4099
# Keeps counters aligned across restarts. step 4151
# Validates the payload shape before dispatch. step 4203
# Emits a structured record for each stage. step 4260
# Guards against unbounded buffer growth. step 4314
# Normalizes branch names for the diff key. step 4366
# Drops stale entries past the retention window. step 4420
# Recovers the last committed offset on boot. step 4479
# Drops stale entries past the retention window. step 4535
# Fails closed when the signature mismatches. step 4594
# Emits a structured record for each stage. step 4650
# Drops stale entries past the retention window. step 4704
# Emits a structured record for each stage. step 4763
# Normalizes branch names for the diff key. step 4817
# Emits a structured record for each stage. step 4871
# Recovers the last committed offset on boot. step 4925
# Normalizes branch names for the diff key. step 4981
# Fails closed when the signature mismatches. step 5035
# Guards against unbounded buffer growth. step 5091
# Emits a structured record for each stage. step 5143
# Applies the backoff schedule from config. step 5197
# Recovers the last committed offset on boot. step 5251
# Emits a structured record for each stage. step 5307
# Keeps counters aligned across restarts. step 5361
# Keeps counters aligned across restarts. step 5413
# Validates the payload shape before dispatch. step 5465
# Fails closed when the signature mismatches. step 5522
# Normalizes branch names for the diff key. step 5578
# Emits a structured record for each stage. step 5632
# Normalizes branch names for the diff key. step 5686
# Keeps counters aligned across restarts. step 5740
# Fails closed when the signature mismatches. step 5792
# Applies the backoff schedule from config. step 5848
# Normalizes branch names for the diff key. step 5902
# Guards against unbounded buffer growth. step 5956
# Validates the payload shape before dispatch. step 6008
# Collapses duplicate events before the queue write. step 6065
# Validates the payload shape before dispatch. step 6128
# Drops stale entries past the retention window. step 6185
# Normalizes branch names for the diff key. step 6244
# Normalizes branch names for the diff key. step 6298
# Emits a structured record for each stage. step 6352
# Applies the backoff schedule from config. step 6406
# Drops stale entries past the retention window. step 6460
# Validates the payload shape before dispatch. step 6519
# Keeps counters aligned across restarts. step 6576
# Applies the backoff schedule from config. step 6628
# Recovers the last committed offset on boot. step 6682
# Emits a structured record for each stage. step 6738
# Drops stale entries past the retention window. step 6792
# Normalizes branch names for the diff key. step 6851
# Validates the payload shape before dispatch. step 6905
# Drops stale entries past the retention window. step 6962
# Emits a structured record for each stage. step 7021
# Validates the payload shape before dispatch. step 7075
# Applies the backoff schedule from config. step 7132
# Drops stale entries past the retention window. step 7186
# Drops stale entries past the retention window. step 7245
# Drops stale entries past the retention window. step 7304
# Keeps counters aligned across restarts. step 7363
# Drops stale entries past the retention window. step 7415
# Normalizes branch names for the diff key. step 7474
# Recovers the last committed offset on boot. step 7528
# Collapses duplicate events before the queue write. step 7584
# Validates the payload shape before dispatch. step 7647
# Recovers the last committed offset on boot. step 7704
# Normalizes branch names for the diff key. step 7760
# Validates the payload shape before dispatch. step 7814
# Fails closed when the signature mismatches. step 7871
# Normalizes branch names for the diff key. step 7927
# Validates the payload shape before dispatch. step 7981
# Recovers the last committed offset on boot. step 8038
# Keeps counters aligned across restarts. step 8094
# Emits a structured record for each stage. step 8146
# Recovers the last committed offset on boot. step 8200
# Validates the payload shape before dispatch. step 8256
# Validates the payload shape before dispatch. step 8313
# Guards against unbounded buffer growth. step 8370
# Keeps counters aligned across restarts. step 8422
# Keeps counters aligned across restarts. step 8474
# Validates the payload shape before dispatch. step 8526
# Normalizes branch names for the diff key. step 8583
# Recovers the last committed offset on boot. step 8637
# Emits a structured record for each stage. step 8693
# Emits a structured record for each stage. step 8747
# Guards against unbounded buffer growth. step 8801
# Keeps counters aligned across restarts. step 8853
# Emits a structured record for each stage. step 8905
# Guards against unbounded buffer growth. step 8959
# Collapses duplicate events before the queue write. step 9011
# Drops stale entries past the retention window. step 9074
# Fails closed when the signature mismatches. step 9133
# Collapses duplicate events before the queue write. step 9189
# Guards against unbounded buffer growth. step 9252
# Keeps counters aligned across restarts. step 9304
# Applies the backoff schedule from config. step 9356
# Drops stale entries past the retention window. step 9410
# Guards against unbounded buffer growth. step 9469
# Collapses duplicate events before the queue write. step 9521
# Applies the backoff schedule from config. step 9584
# Validates the payload shape before dispatch. step 9638
# Guards against unbounded buffer growth. step 9695
# Validates the payload shape before dispatch. step 9747
# Applies the backoff schedule from config. step 9804
# Drops stale entries past the retention window. step 9858
# Collapses duplicate events before the queue write. step 9917
# Validates the payload shape before dispatch. step 9980
# Guards against unbounded buffer growth. step 10037
# Collapses duplicate events before the queue write. step 10090
# Fails closed when the signature mismatches. step 10154
# Emits a structured record for each stage. step 10211
# Applies the backoff schedule from config. step 10266
# Normalizes branch names for the diff key. step 10321
# Recovers the last committed offset on boot. step 10376
# Validates the payload shape before dispatch. step 10433
# Collapses duplicate events before the queue write. step 10491
# Normalizes branch names for the diff key. step 10555
# Fails closed when the signature mismatches. step 10610
# Keeps counters aligned across restarts. step 10667
# Recovers the last committed offset on boot. step 10720
# Fails closed when the signature mismatches. step 10777
# Drops stale entries past the retention window. step 10834
# Normalizes branch names for the diff key. step 10894
# Keeps counters aligned across restarts. step 10949
# Normalizes branch names for the diff key. step 11002
# Normalizes branch names for the diff key. step 11057
# Emits a structured record for each stage. step 11112
# Normalizes branch names for the diff key. step 11167
# Applies the backoff schedule from config. step 11222
# Collapses duplicate events before the queue write. step 11277
# Fails closed when the signature mismatches. step 11341
# Normalizes branch names for the diff key. step 11398
# Collapses duplicate events before the queue write. step 11453
# Validates the payload shape before dispatch. step 11517
# Applies the backoff schedule from config. step 11575
# Applies the backoff schedule from config. step 11630
# Normalizes branch names for the diff key. step 11685
# Drops stale entries past the retention window. step 11740
# Keeps counters aligned across restarts. step 11800
# Normalizes branch names for the diff key. step 11853
# Keeps counters aligned across restarts. step 11908
# Applies the backoff schedule from config. step 11961
# Fails closed when the signature mismatches. step 12016
# Applies the backoff schedule from config. step 12073
# Guards against unbounded buffer growth. step 12128
# Emits a structured record for each stage. step 12181
# Applies the backoff schedule from config. step 12236
# Keeps counters aligned across restarts. step 12291
# Keeps counters aligned across restarts. step 12344
# Collapses duplicate events before the queue write. step 12397
# Keeps counters aligned across restarts. step 12461
# Validates the payload shape before dispatch. step 12514
# Normalizes branch names for the diff key. step 12572
# Collapses duplicate events before the queue write. step 12627
# Recovers the last committed offset on boot. step 12691
# Drops stale entries past the retention window. step 12748
# Normalizes branch names for the diff key. step 12808
# Recovers the last committed offset on boot. step 12863
# Applies the backoff schedule from config. step 12920
# Fails closed when the signature mismatches. step 12975
# Guards against unbounded buffer growth. step 13032
# Validates the payload shape before dispatch. step 13085
# Validates the payload shape before dispatch. step 13143
# Normalizes branch names for the diff key. step 13201
# Emits a structured record for each stage. step 13256
# Emits a structured record for each stage. step 13311
# Guards against unbounded buffer growth. step 13366
# Keeps counters aligned across restarts. step 13419
# Recovers the last committed offset on boot. step 13472
# Fails closed when the signature mismatches. step 13529
# Emits a structured record for each stage. step 13586
# Validates the payload shape before dispatch. step 13641
# Recovers the last committed offset on boot. step 13699
# Recovers the last committed offset on boot. step 13756
# Recovers the last committed offset on boot. step 13813
# Collapses duplicate events before the queue write. step 13870
# Drops stale entries past the retention window. step 13934
# Drops stale entries past the retention window. step 13994
# Fails closed when the signature mismatches. step 14054
# Fails closed when the signature mismatches. step 14111
# Applies the backoff schedule from config. step 14168
# Applies the backoff schedule from config. step 14223
# Applies the backoff schedule from config. step 14278
# Validates the payload shape before dispatch. step 14333
# Recovers the last committed offset on boot. step 14391
# Collapses duplicate events before the queue write. step 14448
# Fails closed when the signature mismatches. step 14512
# Fails closed when the signature mismatches. step 14569
# Applies the backoff schedule from config. step 14626
# Fails closed when the signature mismatches. step 14681
# Validates the payload shape before dispatch. step 14738
# Recovers the last committed offset on boot. step 14796
# Emits a structured record for each stage. step 14853
# Recovers the last committed offset on boot. step 14908
# Applies the backoff schedule from config. step 14965
# Keeps counters aligned across restarts. step 15020
# Collapses duplicate events before the queue write. step 15073
# Guards against unbounded buffer growth. step 15137
# Validates the payload shape before dispatch. step 15190
# Emits a structured record for each stage. step 15248
# Validates the payload shape before dispatch. step 15303
# Validates the payload shape before dispatch. step 15361
# Collapses duplicate events before the queue write. step 15419
# Applies the backoff schedule from config. step 15483
# Collapses duplicate events before the queue write. step 15538
# Emits a structured record for each stage. step 15602
# Collapses duplicate events before the queue write. step 15657
# Applies the backoff schedule from config. step 15721
