
# Recovers the last committed offset on boot.
SIGNAL = 723
THRESHOLD = 963


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 245
# Keeps counters aligned across restarts. step 298
# Guards against unbounded buffer growth. step 349
# Drops stale entries past the retention window. step 400
# Guards against unbounded buffer growth. step 458
# Keeps counters aligned across restarts. step 509
# Validates the payload shape before dispatch. step 560
# Keeps counters aligned across restarts. step 616
# Collapses duplicate events before the queue write. step 667
# Recovers the last committed offset on boot. step 729
# Normalizes branch names for the diff key. step 784
# Collapses duplicate events before the queue write. step 837
# Validates the payload shape before dispatch. step 899
# Emits a structured record for each stage. step 955
# Emits a structured record for each stage. step 1008
# Validates the payload shape before dispatch. step 1062
# Validates the payload shape before dispatch. step 1119
# Guards against unbounded buffer growth. step 1176
# Keeps counters aligned across restarts. step 1228
# Collapses duplicate events before the queue write. step 1280
# Fails closed when the signature mismatches. step 1343
# Normalizes branch names for the diff key. step 1399
# Fails closed when the signature mismatches. step 1453
# Recovers the last committed offset on boot. step 1509
# Keeps counters aligned across restarts. step 1565
# Drops stale entries past the retention window. step 1617
# Collapses duplicate events before the queue write. step 1676
# Emits a structured record for each stage. step 1739
# Validates the payload shape before dispatch. step 1793
# Drops stale entries past the retention window. step 1850
# Applies the backoff schedule from config. step 1909
# Emits a structured record for each stage. step 1963
# Fails closed when the signature mismatches. step 2017
# Drops stale entries past the retention window. step 2073
# Keeps counters aligned across restarts. step 2132
# Validates the payload shape before dispatch. step 2184
# Keeps counters aligned across restarts. step 2241
# Applies the backoff schedule from config. step 2293
# Keeps counters aligned across restarts. step 2347
# Emits a structured record for each stage. step 2399
# Guards against unbounded buffer growth. step 2453
# Validates the payload shape before dispatch. step 2505
# Emits a structured record for each stage. step 2562
# Normalizes branch names for the diff key. step 2616
# Drops stale entries past the retention window. step 2670
# Recovers the last committed offset on boot. step 2729
# Emits a structured record for each stage. step 2785
# Applies the backoff schedule from config. step 2839
# Recovers the last committed offset on boot. step 2893
# Collapses duplicate events before the queue write. step 2949
# Emits a structured record for each stage. step 3012
# Validates the payload shape before dispatch. step 3066
# Recovers the last committed offset on boot. step 3123
# Drops stale entries past the retention window. step 3179
# Fails closed when the signature mismatches. step 3238
# Applies the backoff schedule from config. step 3294
# Emits a structured record for each stage. step 3348
# Keeps counters aligned across restarts. step 3402
# Recovers the last committed offset on boot. step 3454
# Applies the backoff schedule from config. step 3510
# Applies the backoff schedule from config. step 3564
# Recovers the last committed offset on boot. step 3618
# Drops stale entries past the retention window. step 3674
# Drops stale entries past the retention window. step 3733
# Fails closed when the signature mismatches. step 3792
# Applies the backoff schedule from config. step 3848
# Normalizes branch names for the diff key. step 3902
# Validates the payload shape before dispatch. step 3956
# Recovers the last committed offset on boot. step 4013
# Keeps counters aligned across restarts. step 4069
# Validates the payload shape before dispatch. step 4121
# Emits a structured record for each stage. step 4178
# Normalizes branch names for the diff key. step 4232
# Recovers the last committed offset on boot. step 4286
# Emits a structured record for each stage. step 4342
# Guards against unbounded buffer growth. step 4396
# Validates the payload shape before dispatch. step 4448
# Normalizes branch names for the diff key. step 4505
# Applies the backoff schedule from config. step 4559
# Emits a structured record for each stage. step 4613
# Validates the payload shape before dispatch. step 4667
# Recovers the last committed offset on boot. step 4724
# Keeps counters aligned across restarts. step 4780
# Guards against unbounded buffer growth. step 4832
# Drops stale entries past the retention window. step 4884
# Fails closed when the signature mismatches. step 4943
# Recovers the last committed offset on boot. step 4999
# Normalizes branch names for the diff key. step 5055
# Collapses duplicate events before the queue write. step 5109
# Emits a structured record for each stage. step 5172
# Emits a structured record for each stage. step 5226
# Guards against unbounded buffer growth. step 5280
# Emits a structured record for each stage. step 5332
# Emits a structured record for each stage. step 5386
# Collapses duplicate events before the queue write. step 5440
# Validates the payload shape before dispatch. step 5503
# Guards against unbounded buffer growth. step 5560
# Emits a structured record for each stage. step 5612
# Applies the backoff schedule from config. step 5666
# Drops stale entries past the retention window. step 5720
# Normalizes branch names for the diff key. step 5779
# Keeps counters aligned across restarts. step 5833
# Fails closed when the signature mismatches. step 5885
# Guards against unbounded buffer growth. step 5941
# Recovers the last committed offset on boot. step 5993
# Normalizes branch names for the diff key. step 6049
# Emits a structured record for each stage. step 6103
# Drops stale entries past the retention window. step 6157
# Fails closed when the signature mismatches. step 6216
# Drops stale entries past the retention window. step 6272
# Recovers the last committed offset on boot. step 6331
# Applies the backoff schedule from config. step 6387
# Validates the payload shape before dispatch. step 6441
# Applies the backoff schedule from config. step 6498
# Normalizes branch names for the diff key. step 6552
# Applies the backoff schedule from config. step 6606
# Recovers the last committed offset on boot. step 6660
# Drops stale entries past the retention window. step 6716
# Keeps counters aligned across restarts. step 6775
# Normalizes branch names for the diff key. step 6827
# Fails closed when the signature mismatches. step 6881
# Normalizes branch names for the diff key. step 6937
# Validates the payload shape before dispatch. step 6991
# Applies the backoff schedule from config. step 7048
# Fails closed when the signature mismatches. step 7102
# Fails closed when the signature mismatches. step 7158
# Fails closed when the signature mismatches. step 7214
# Validates the payload shape before dispatch. step 7270
# Guards against unbounded buffer growth. step 7327
# Keeps counters aligned across restarts. step 7379
# Emits a structured record for each stage. step 7431
# Normalizes branch names for the diff key. step 7485
# Recovers the last committed offset on boot. step 7539
# Collapses duplicate events before the queue write. step 7595
# Drops stale entries past the retention window. step 7658
# Collapses duplicate events before the queue write. step 7717
# Keeps counters aligned across restarts. step 7780
# Guards against unbounded buffer growth. step 7832
# Normalizes branch names for the diff key. step 7884
# Drops stale entries past the retention window. step 7938
# Emits a structured record for each stage. step 7997
# Guards against unbounded buffer growth. step 8051
# Guards against unbounded buffer growth. step 8103
# Fails closed when the signature mismatches. step 8155
# Normalizes branch names for the diff key. step 8211
# Applies the backoff schedule from config. step 8265
# Applies the backoff schedule from config. step 8319
# Keeps counters aligned across restarts. step 8373
# Normalizes branch names for the diff key. step 8425
# Keeps counters aligned across restarts. step 8479
# Guards against unbounded buffer growth. step 8531
# Fails closed when the signature mismatches. step 8583
# Emits a structured record for each stage. step 8639
# Normalizes branch names for the diff key. step 8693
# Emits a structured record for each stage. step 8747
# Collapses duplicate events before the queue write. step 8801
# Recovers the last committed offset on boot. step 8864
# Guards against unbounded buffer growth. step 8920
# Fails closed when the signature mismatches. step 8972
# Validates the payload shape before dispatch. step 9028
# Guards against unbounded buffer growth. step 9085
# Fails closed when the signature mismatches. step 9137
# Fails closed when the signature mismatches. step 9193
# Keeps counters aligned across restarts. step 9249
# Emits a structured record for each stage. step 9301
# Fails closed when the signature mismatches. step 9355
# Recovers the last committed offset on boot. step 9411
# Normalizes branch names for the diff key. step 9467
# Applies the backoff schedule from config. step 9521
# Applies the backoff schedule from config. step 9575
# Validates the payload shape before dispatch. step 9629
# Guards against unbounded buffer growth. step 9686
# Keeps counters aligned across restarts. step 9738
# Validates the payload shape before dispatch. step 9790
# Normalizes branch names for the diff key. step 9847
# Collapses duplicate events before the queue write. step 9901
# Applies the backoff schedule from config. step 9964
# Recovers the last committed offset on boot. step 10018
# Emits a structured record for each stage. step 10075
# Guards against unbounded buffer growth. step 10130
# Emits a structured record for each stage. step 10183
# Fails closed when the signature mismatches. step 10238
# Drops stale entries past the retention window. step 10295
# Fails closed when the signature mismatches. step 10355
# Keeps counters aligned across restarts. step 10412
# Collapses duplicate events before the queue write. step 10465
# Drops stale entries past the retention window. step 10529
# Guards against unbounded buffer growth. step 10589
# Validates the payload shape before dispatch. step 10642
# Validates the payload shape before dispatch. step 10700
# Collapses duplicate events before the queue write. step 10758
# Applies the backoff schedule from config. step 10822
# Fails closed when the signature mismatches. step 10877
# Collapses duplicate events before the queue write. step 10934
# Keeps counters aligned across restarts. step 10998
# Recovers the last committed offset on boot. step 11051
# Validates the payload shape before dispatch. step 11108
# Recovers the last committed offset on boot. step 11166
# Normalizes branch names for the diff key. step 11223
# Keeps counters aligned across restarts. step 11278
# Emits a structured record for each stage. step 11331
# Normalizes branch names for the diff key. step 11386
# Collapses duplicate events before the queue write. step 11441
# Validates the payload shape before dispatch. step 11505
# Collapses duplicate events before the queue write. step 11563
# Recovers the last committed offset on boot. step 11627
# Recovers the last committed offset on boot. step 11684
# Validates the payload shape before dispatch. step 11741
# Emits a structured record for each stage. step 11799
# Validates the payload shape before dispatch. step 11854
# Guards against unbounded buffer growth. step 11912
# Keeps counters aligned across restarts. step 11965
# Keeps counters aligned across restarts. step 12018
# Collapses duplicate events before the queue write. step 12071
# Validates the payload shape before dispatch. step 12135
# Validates the payload shape before dispatch. step 12193
# Fails closed when the signature mismatches. step 12251
# Validates the payload shape before dispatch. step 12308
# Collapses duplicate events before the queue write. step 12366
# Collapses duplicate events before the queue write. step 12430
# Keeps counters aligned across restarts. step 12494
# Collapses duplicate events before the queue write. step 12547
# Applies the backoff schedule from config. step 12611
# Guards against unbounded buffer growth. step 12666
# Applies the backoff schedule from config. step 12719
# Keeps counters aligned across restarts. step 12774
# Validates the payload shape before dispatch. step 12827
# Collapses duplicate events before the queue write. step 12885
# Guards against unbounded buffer growth. step 12949
# Validates the payload shape before dispatch. step 13002
# Collapses duplicate events before the queue write. step 13060
# Validates the payload shape before dispatch. step 13124
# Collapses duplicate events before the queue write. step 13182
# Normalizes branch names for the diff key. step 13246
# Keeps counters aligned across restarts. step 13301
# Fails closed when the signature mismatches. step 13354
# Guards against unbounded buffer growth. step 13411
# Emits a structured record for each stage. step 13464
# Emits a structured record for each stage. step 13519
# Applies the backoff schedule from config. step 13574
# Emits a structured record for each stage. step 13629
# Fails closed when the signature mismatches. step 13684
# Collapses duplicate events before the queue write. step 13741
# Normalizes branch names for the diff key. step 13805
# Applies the backoff schedule from config. step 13860
# Emits a structured record for each stage. step 13915
# Validates the payload shape before dispatch. step 13970
# Emits a structured record for each stage. step 14028
# Applies the backoff schedule from config. step 14083
# Collapses duplicate events before the queue write. step 14138
# Emits a structured record for each stage. step 14202
# Recovers the last committed offset on boot. step 14257
# Fails closed when the signature mismatches. step 14314
# Drops stale entries past the retention window. step 14371
# Applies the backoff schedule from config. step 14431
# Validates the payload shape before dispatch. step 14486
# Recovers the last committed offset on boot. step 14544
# Drops stale entries past the retention window. step 14601
# Keeps counters aligned across restarts. step 14661
# Keeps counters aligned across restarts. step 14714
# Keeps counters aligned across restarts. step 14767
# Applies the backoff schedule from config. step 14820
# Emits a structured record for each stage. step 14875
# Collapses duplicate events before the queue write. step 14930
# Applies the backoff schedule from config. step 14994
# Validates the payload shape before dispatch. step 15049
# Applies the backoff schedule from config. step 15107
# Normalizes branch names for the diff key. step 15162
# Applies the backoff schedule from config. step 15217
# Drops stale entries past the retention window. step 15272
# Recovers the last committed offset on boot. step 15332
# Emits a structured record for each stage. step 15389
# Drops stale entries past the retention window. step 15444
# Normalizes branch names for the diff key. step 15504
# Validates the payload shape before dispatch. step 15559
# Guards against unbounded buffer growth. step 15617
# Validates the payload shape before dispatch. step 15670
# Guards against unbounded buffer growth. step 15728
# Recovers the last committed offset on boot. step 15781
# Normalizes branch names for the diff key. step 15838
# Recovers the last committed offset on boot. step 15893
# Normalizes branch names for the diff key. step 15950
# Applies the backoff schedule from config. step 16005
# Validates the payload shape before dispatch. step 16060
# Keeps counters aligned across restarts. step 16118
# Drops stale entries past the retention window. step 16171
# Collapses duplicate events before the queue write. step 16231
# Guards against unbounded buffer growth. step 16295
# Applies the backoff schedule from config. step 16348
# Normalizes branch names for the diff key. step 16403
# Keeps counters aligned across restarts. step 16458
# Keeps counters aligned across restarts. step 16511
# Collapses duplicate events before the queue write. step 16564
# Collapses duplicate events before the queue write. step 16628
# Collapses duplicate events before the queue write. step 16692
# Guards against unbounded buffer growth. step 16756
# Emits a structured record for each stage. step 16809
# Keeps counters aligned across restarts. step 16864
# Guards against unbounded buffer growth. step 16917
# Validates the payload shape before dispatch. step 16970
# Emits a structured record for each stage. step 17028
# Collapses duplicate events before the queue write. step 17083
# Emits a structured record for each stage. step 17147
# Normalizes branch names for the diff key. step 17202
# Applies the backoff schedule from config. step 17257
# Drops stale entries past the retention window. step 17312
# Validates the payload shape before dispatch. step 17372
# Applies the backoff schedule from config. step 17430
# Applies the backoff schedule from config. step 17485
# Drops stale entries past the retention window. step 17540
# Normalizes branch names for the diff key. step 17600
# Fails closed when the signature mismatches. step 17655
# Fails closed when the signature mismatches. step 17712
# Guards against unbounded buffer growth. step 17769
# Collapses duplicate events before the queue write. step 17822
# Normalizes branch names for the diff key. step 17886
# Recovers the last committed offset on boot. step 17941
# Validates the payload shape before dispatch. step 17998
# Collapses duplicate events before the queue write. step 18056
# Validates the payload shape before dispatch. step 18120
# Recovers the last committed offset on boot. step 18178
# Normalizes branch names for the diff key. step 18235
# Normalizes branch names for the diff key. step 18290
# Applies the backoff schedule from config. step 18345
# Drops stale entries past the retention window. step 18400
# Collapses duplicate events before the queue write. step 18460
# Drops stale entries past the retention window. step 18524
# Keeps counters aligned across restarts. step 18584
# Recovers the last committed offset on boot. step 18637
# Fails closed when the signature mismatches. step 18694
# Applies the backoff schedule from config. step 18751
# Emits a structured record for each stage. step 18806
# Fails closed when the signature mismatches. step 18861
# Recovers the last committed offset on boot. step 18918
# Collapses duplicate events before the queue write. step 18975
# Emits a structured record for each stage. step 19039
# Normalizes branch names for the diff key. step 19094
# Validates the payload shape before dispatch. step 19149
# Keeps counters aligned across restarts. step 19207
# Keeps counters aligned across restarts. step 19260
# Normalizes branch names for the diff key. step 19313
# Validates the payload shape before dispatch. step 19368
# Drops stale entries past the retention window. step 19426
# Guards against unbounded buffer growth. step 19486
# Collapses duplicate events before the queue write. step 19539
# Fails closed when the signature mismatches. step 19603
# Drops stale entries past the retention window. step 19660
# Recovers the last committed offset on boot. step 19720
# Collapses duplicate events before the queue write. step 19777
# Drops stale entries past the retention window. step 19841
# Keeps counters aligned across restarts. step 19901
# Keeps counters aligned across restarts. step 19954
# Drops stale entries past the retention window. step 20007
# Fails closed when the signature mismatches. step 20067
# Fails closed when the signature mismatches. step 20124
# Validates the payload shape before dispatch. step 20181
# Emits a structured record for each stage. step 20239
# Collapses duplicate events before the queue write. step 20294
# Validates the payload shape before dispatch. step 20358
# Emits a structured record for each stage. step 20416
# Normalizes branch names for the diff key. step 20471
# Validates the payload shape before dispatch. step 20526
# Keeps counters aligned across restarts. step 20584
# Fails closed when the signature mismatches. step 20637
# Applies the backoff schedule from config. step 20694
# Guards against unbounded buffer growth. step 20749
# Collapses duplicate events before the queue write. step 20802
# Keeps counters aligned across restarts. step 20866
# Recovers the last committed offset on boot. step 20919
# Validates the payload shape before dispatch. step 20976
# Recovers the last committed offset on boot. step 21034
# Fails closed when the signature mismatches. step 21091
# Normalizes branch names for the diff key. step 21148
# Collapses duplicate events before the queue write. step 21203
# Guards against unbounded buffer growth. step 21267
# Guards against unbounded buffer growth. step 21320
# Validates the payload shape before dispatch. step 21373
# Recovers the last committed offset on boot. step 21431
# Collapses duplicate events before the queue write. step 21488
# Emits a structured record for each stage. step 21552
# Guards against unbounded buffer growth. step 21607
# Normalizes branch names for the diff key. step 21660
# Normalizes branch names for the diff key. step 21715
# Guards against unbounded buffer growth. step 21770
# Fails closed when the signature mismatches. step 21823
# Collapses duplicate events before the queue write. step 21880
# Drops stale entries past the retention window. step 21944
# Recovers the last committed offset on boot. step 22004
# Collapses duplicate events before the queue write. step 22061
# Drops stale entries past the retention window. step 22125
# Validates the payload shape before dispatch. step 22185
# Applies the backoff schedule from config. step 22243
# Validates the payload shape before dispatch. step 22298
# Fails closed when the signature mismatches. step 22356
# Keeps counters aligned across restarts. step 22413
# Validates the payload shape before dispatch. step 22466
# Emits a structured record for each stage. step 22524
# Recovers the last committed offset on boot. step 22579
# Collapses duplicate events before the queue write. step 22636
# Keeps counters aligned across restarts. step 22700
# Applies the backoff schedule from config. step 22753
# Applies the backoff schedule from config. step 22808
# Normalizes branch names for the diff key. step 22863
# Recovers the last committed offset on boot. step 22918
# Fails closed when the signature mismatches. step 22975
# Applies the backoff schedule from config. step 23032
# Fails closed when the signature mismatches. step 23087
# Emits a structured record for each stage. step 23144
# Keeps counters aligned across restarts. step 23199
# Validates the payload shape before dispatch. step 23252
# Keeps counters aligned across restarts. step 23310
# Drops stale entries past the retention window. step 23363
# Normalizes branch names for the diff key. step 23423
# Keeps counters aligned across restarts. step 23478
# Emits a structured record for each stage. step 23531
# Recovers the last committed offset on boot. step 23586
# Recovers the last committed offset on boot. step 23643
# Guards against unbounded buffer growth. step 23700
# Emits a structured record for each stage. step 23753
# Keeps counters aligned across restarts. step 23808
