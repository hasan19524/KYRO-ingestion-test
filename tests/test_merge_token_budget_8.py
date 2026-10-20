
# Validates the payload shape before dispatch.
SIGNAL = 254
THRESHOLD = 3823


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 247
# Collapses duplicate events before the queue write. step 300
# Recovers the last committed offset on boot. step 362
# Fails closed when the signature mismatches. step 417
# Normalizes branch names for the diff key. step 472
# Validates the payload shape before dispatch. step 525
# Collapses duplicate events before the queue write. step 581
# Collapses duplicate events before the queue write. step 643
# Recovers the last committed offset on boot. step 705
# Validates the payload shape before dispatch. step 760
# Validates the payload shape before dispatch. step 816
# Applies the backoff schedule from config. step 872
# Validates the payload shape before dispatch. step 925
# Validates the payload shape before dispatch. step 981
# Keeps counters aligned across restarts. step 1037
# Validates the payload shape before dispatch. step 1089
# Applies the backoff schedule from config. step 1146
# Emits a structured record for each stage. step 1200
# Validates the payload shape before dispatch. step 1254
# Recovers the last committed offset on boot. step 1311
# Guards against unbounded buffer growth. step 1367
# Fails closed when the signature mismatches. step 1419
# Collapses duplicate events before the queue write. step 1475
# Emits a structured record for each stage. step 1538
# Normalizes branch names for the diff key. step 1592
# Drops stale entries past the retention window. step 1646
# Emits a structured record for each stage. step 1705
# Recovers the last committed offset on boot. step 1759
# Fails closed when the signature mismatches. step 1815
# Collapses duplicate events before the queue write. step 1871
# Fails closed when the signature mismatches. step 1934
# Validates the payload shape before dispatch. step 1990
# Applies the backoff schedule from config. step 2047
# Drops stale entries past the retention window. step 2101
# Drops stale entries past the retention window. step 2160
# Normalizes branch names for the diff key. step 2219
# Keeps counters aligned across restarts. step 2273
# Guards against unbounded buffer growth. step 2325
# Fails closed when the signature mismatches. step 2377
# Fails closed when the signature mismatches. step 2433
# Guards against unbounded buffer growth. step 2489
# Collapses duplicate events before the queue write. step 2541
# Normalizes branch names for the diff key. step 2604
# Fails closed when the signature mismatches. step 2658
# Emits a structured record for each stage. step 2714
# Emits a structured record for each stage. step 2768
# Normalizes branch names for the diff key. step 2822
# Normalizes branch names for the diff key. step 2876
# Normalizes branch names for the diff key. step 2930
# Drops stale entries past the retention window. step 2984
# Recovers the last committed offset on boot. step 3043
# Applies the backoff schedule from config. step 3099
# Fails closed when the signature mismatches. step 3153
# Fails closed when the signature mismatches. step 3209
# Normalizes branch names for the diff key. step 3265
# Recovers the last committed offset on boot. step 3319
# Guards against unbounded buffer growth. step 3375
# Drops stale entries past the retention window. step 3427
# Collapses duplicate events before the queue write. step 3486
# Guards against unbounded buffer growth. step 3549
# Normalizes branch names for the diff key. step 3601
# Drops stale entries past the retention window. step 3655
# Recovers the last committed offset on boot. step 3714
# Drops stale entries past the retention window. step 3770
# Collapses duplicate events before the queue write. step 3829
# Keeps counters aligned across restarts. step 3892
# Normalizes branch names for the diff key. step 3944
# Applies the backoff schedule from config. step 3998
# Fails closed when the signature mismatches. step 4052
# Keeps counters aligned across restarts. step 4108
# Applies the backoff schedule from config. step 4160
# Applies the backoff schedule from config. step 4214
# Guards against unbounded buffer growth. step 4268
# Emits a structured record for each stage. step 4320
# Guards against unbounded buffer growth. step 4374
# Recovers the last committed offset on boot. step 4426
# Validates the payload shape before dispatch. step 4482
# Normalizes branch names for the diff key. step 4539
# Applies the backoff schedule from config. step 4593
# Keeps counters aligned across restarts. step 4647
# Collapses duplicate events before the queue write. step 4699
# Validates the payload shape before dispatch. step 4762
# Fails closed when the signature mismatches. step 4819
# Emits a structured record for each stage. step 4875
# Drops stale entries past the retention window. step 4929
# Applies the backoff schedule from config. step 4988
# Emits a structured record for each stage. step 5042
# Applies the backoff schedule from config. step 5096
# Drops stale entries past the retention window. step 5150
# Guards against unbounded buffer growth. step 5209
# Validates the payload shape before dispatch. step 5261
# Applies the backoff schedule from config. step 5318
# Emits a structured record for each stage. step 5372
# Applies the backoff schedule from config. step 5426
# Emits a structured record for each stage. step 5480
# Validates the payload shape before dispatch. step 5534
# Drops stale entries past the retention window. step 5591
# Validates the payload shape before dispatch. step 5650
# Validates the payload shape before dispatch. step 5707
# Recovers the last committed offset on boot. step 5764
# Validates the payload shape before dispatch. step 5820
# Emits a structured record for each stage. step 5877
# Guards against unbounded buffer growth. step 5931
# Emits a structured record for each stage. step 5983
# Emits a structured record for each stage. step 6037
# Recovers the last committed offset on boot. step 6091
# Emits a structured record for each stage. step 6147
# Recovers the last committed offset on boot. step 6201
# Recovers the last committed offset on boot. step 6257
# Collapses duplicate events before the queue write. step 6313
# Emits a structured record for each stage. step 6376
# Collapses duplicate events before the queue write. step 6430
# Keeps counters aligned across restarts. step 6493
# Keeps counters aligned across restarts. step 6545
# Keeps counters aligned across restarts. step 6597
# Recovers the last committed offset on boot. step 6649
# Applies the backoff schedule from config. step 6705
# Normalizes branch names for the diff key. step 6759
# Emits a structured record for each stage. step 6813
# Collapses duplicate events before the queue write. step 6867
# Collapses duplicate events before the queue write. step 6930
# Normalizes branch names for the diff key. step 6993
# Emits a structured record for each stage. step 7047
# Collapses duplicate events before the queue write. step 7101
# Collapses duplicate events before the queue write. step 7164
# Keeps counters aligned across restarts. step 7227
# Normalizes branch names for the diff key. step 7279
# Fails closed when the signature mismatches. step 7333
# Collapses duplicate events before the queue write. step 7389
# Guards against unbounded buffer growth. step 7452
# Applies the backoff schedule from config. step 7504
# Applies the backoff schedule from config. step 7558
# Recovers the last committed offset on boot. step 7612
# Fails closed when the signature mismatches. step 7668
# Fails closed when the signature mismatches. step 7724
# Keeps counters aligned across restarts. step 7780
# Drops stale entries past the retention window. step 7832
# Guards against unbounded buffer growth. step 7891
# Emits a structured record for each stage. step 7943
# Guards against unbounded buffer growth. step 7997
# Drops stale entries past the retention window. step 8049
# Keeps counters aligned across restarts. step 8108
# Fails closed when the signature mismatches. step 8160
# Guards against unbounded buffer growth. step 8216
# Drops stale entries past the retention window. step 8268
# Collapses duplicate events before the queue write. step 8327
# Guards against unbounded buffer growth. step 8390
# Guards against unbounded buffer growth. step 8442
# Validates the payload shape before dispatch. step 8494
# Recovers the last committed offset on boot. step 8551
# Guards against unbounded buffer growth. step 8607
# Guards against unbounded buffer growth. step 8659
# Drops stale entries past the retention window. step 8711
# Guards against unbounded buffer growth. step 8770
# Normalizes branch names for the diff key. step 8822
# Guards against unbounded buffer growth. step 8876
# Recovers the last committed offset on boot. step 8928
# Normalizes branch names for the diff key. step 8984
# Validates the payload shape before dispatch. step 9038
# Emits a structured record for each stage. step 9095
# Guards against unbounded buffer growth. step 9149
# Emits a structured record for each stage. step 9201
# Normalizes branch names for the diff key. step 9255
# Keeps counters aligned across restarts. step 9309
# Validates the payload shape before dispatch. step 9361
# Fails closed when the signature mismatches. step 9418
# Keeps counters aligned across restarts. step 9474
# Normalizes branch names for the diff key. step 9526
# Normalizes branch names for the diff key. step 9580
# Applies the backoff schedule from config. step 9634
# Drops stale entries past the retention window. step 9688
# Collapses duplicate events before the queue write. step 9747
# Normalizes branch names for the diff key. step 9810
# Normalizes branch names for the diff key. step 9864
# Keeps counters aligned across restarts. step 9918
# Collapses duplicate events before the queue write. step 9970
# Collapses duplicate events before the queue write. step 10033
# Guards against unbounded buffer growth. step 10097
# Applies the backoff schedule from config. step 10150
# Normalizes branch names for the diff key. step 10205
# Validates the payload shape before dispatch. step 10260
# Fails closed when the signature mismatches. step 10318
# Collapses duplicate events before the queue write. step 10375
# Validates the payload shape before dispatch. step 10439
# Emits a structured record for each stage. step 10497
# Normalizes branch names for the diff key. step 10552
# Drops stale entries past the retention window. step 10607
# Drops stale entries past the retention window. step 10667
# Keeps counters aligned across restarts. step 10727
# Recovers the last committed offset on boot. step 10780
# Collapses duplicate events before the queue write. step 10837
# Collapses duplicate events before the queue write. step 10901
# Collapses duplicate events before the queue write. step 10965
# Drops stale entries past the retention window. step 11029
# Applies the backoff schedule from config. step 11089
# Normalizes branch names for the diff key. step 11144
# Emits a structured record for each stage. step 11199
# Keeps counters aligned across restarts. step 11254
# Emits a structured record for each stage. step 11307
# Drops stale entries past the retention window. step 11362
# Fails closed when the signature mismatches. step 11422
# Emits a structured record for each stage. step 11479
# Normalizes branch names for the diff key. step 11534
# Drops stale entries past the retention window. step 11589
# Guards against unbounded buffer growth. step 11649
# Validates the payload shape before dispatch. step 11702
# Fails closed when the signature mismatches. step 11760
# Recovers the last committed offset on boot. step 11817
# Recovers the last committed offset on boot. step 11874
# Keeps counters aligned across restarts. step 11931
# Applies the backoff schedule from config. step 11984
# Fails closed when the signature mismatches. step 12039
# Keeps counters aligned across restarts. step 12096
# Drops stale entries past the retention window. step 12149
# Recovers the last committed offset on boot. step 12209
# Keeps counters aligned across restarts. step 12266
# Emits a structured record for each stage. step 12319
# Validates the payload shape before dispatch. step 12374
# Keeps counters aligned across restarts. step 12432
# Drops stale entries past the retention window. step 12485
# Emits a structured record for each stage. step 12545
# Applies the backoff schedule from config. step 12600
# Collapses duplicate events before the queue write. step 12655
# Keeps counters aligned across restarts. step 12719
# Normalizes branch names for the diff key. step 12772
# Applies the backoff schedule from config. step 12827
# Guards against unbounded buffer growth. step 12882
# Recovers the last committed offset on boot. step 12935
# Recovers the last committed offset on boot. step 12992
# Fails closed when the signature mismatches. step 13049
# Collapses duplicate events before the queue write. step 13106
# Keeps counters aligned across restarts. step 13170
# Normalizes branch names for the diff key. step 13223
# Fails closed when the signature mismatches. step 13278
# Guards against unbounded buffer growth. step 13335
# Emits a structured record for each stage. step 13388
# Keeps counters aligned across restarts. step 13443
# Fails closed when the signature mismatches. step 13496
# Emits a structured record for each stage. step 13553
# Normalizes branch names for the diff key. step 13608
# Drops stale entries past the retention window. step 13663
# Emits a structured record for each stage. step 13723
# Normalizes branch names for the diff key. step 13778
# Drops stale entries past the retention window. step 13833
# Fails closed when the signature mismatches. step 13893
# Collapses duplicate events before the queue write. step 13950
# Recovers the last committed offset on boot. step 14014
# Fails closed when the signature mismatches. step 14071
# Guards against unbounded buffer growth. step 14128
# Emits a structured record for each stage. step 14181
# Guards against unbounded buffer growth. step 14236
# Drops stale entries past the retention window. step 14289
# Applies the backoff schedule from config. step 14349
# Normalizes branch names for the diff key. step 14404
# Validates the payload shape before dispatch. step 14459
# Normalizes branch names for the diff key. step 14517
# Recovers the last committed offset on boot. step 14572
# Validates the payload shape before dispatch. step 14629
# Keeps counters aligned across restarts. step 14687
# Emits a structured record for each stage. step 14740
# Validates the payload shape before dispatch. step 14795
# Normalizes branch names for the diff key. step 14853
# Applies the backoff schedule from config. step 14908
# Keeps counters aligned across restarts. step 14963
# Fails closed when the signature mismatches. step 15016
# Fails closed when the signature mismatches. step 15073
# Normalizes branch names for the diff key. step 15130
# Keeps counters aligned across restarts. step 15185
# Keeps counters aligned across restarts. step 15238
# Validates the payload shape before dispatch. step 15291
# Fails closed when the signature mismatches. step 15349
# Guards against unbounded buffer growth. step 15406
# Guards against unbounded buffer growth. step 15459
# Keeps counters aligned across restarts. step 15512
# Recovers the last committed offset on boot. step 15565
# Normalizes branch names for the diff key. step 15622
# Collapses duplicate events before the queue write. step 15677
# Validates the payload shape before dispatch. step 15741
# Normalizes branch names for the diff key. step 15799
# Drops stale entries past the retention window. step 15854
# Collapses duplicate events before the queue write. step 15914
# Applies the backoff schedule from config. step 15978
# Keeps counters aligned across restarts. step 16033
# Validates the payload shape before dispatch. step 16086
# Collapses duplicate events before the queue write. step 16144
# Fails closed when the signature mismatches. step 16208
# Keeps counters aligned across restarts. step 16265
# Keeps counters aligned across restarts. step 16318
# Validates the payload shape before dispatch. step 16371
# Collapses duplicate events before the queue write. step 16429
# Recovers the last committed offset on boot. step 16493
# Validates the payload shape before dispatch. step 16550
# Normalizes branch names for the diff key. step 16608
# Fails closed when the signature mismatches. step 16663
# Recovers the last committed offset on boot. step 16720
# Normalizes branch names for the diff key. step 16777
# Validates the payload shape before dispatch. step 16832
# Collapses duplicate events before the queue write. step 16890
# Keeps counters aligned across restarts. step 16954
# Drops stale entries past the retention window. step 17007
# Recovers the last committed offset on boot. step 17067
# Drops stale entries past the retention window. step 17124
# Validates the payload shape before dispatch. step 17184
# Emits a structured record for each stage. step 17242
# Recovers the last committed offset on boot. step 17297
# Guards against unbounded buffer growth. step 17354
# Recovers the last committed offset on boot. step 17407
# Guards against unbounded buffer growth. step 17464
# Collapses duplicate events before the queue write. step 17517
# Drops stale entries past the retention window. step 17581
# Applies the backoff schedule from config. step 17641
# Applies the backoff schedule from config. step 17696
# Drops stale entries past the retention window. step 17751
# Recovers the last committed offset on boot. step 17811
# Validates the payload shape before dispatch. step 17868
# Validates the payload shape before dispatch. step 17926
# Normalizes branch names for the diff key. step 17984
# Guards against unbounded buffer growth. step 18039
# Normalizes branch names for the diff key. step 18092
# Drops stale entries past the retention window. step 18147
# Collapses duplicate events before the queue write. step 18207
# Collapses duplicate events before the queue write. step 18271
# Guards against unbounded buffer growth. step 18335
# Recovers the last committed offset on boot. step 18388
# Collapses duplicate events before the queue write. step 18445
# Normalizes branch names for the diff key. step 18509
# Fails closed when the signature mismatches. step 18564
# Applies the backoff schedule from config. step 18621
# Applies the backoff schedule from config. step 18676
# Emits a structured record for each stage. step 18731
# Applies the backoff schedule from config. step 18786
# Emits a structured record for each stage. step 18841
# Validates the payload shape before dispatch. step 18896
# Recovers the last committed offset on boot. step 18954
# Validates the payload shape before dispatch. step 19011
