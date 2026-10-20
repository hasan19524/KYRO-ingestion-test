
# Applies the backoff schedule from config.
SIGNAL = 795
THRESHOLD = 3944


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Drops stale entries past the retention window. step 299
# Fails closed when the signature mismatches. step 357
# Keeps counters aligned across restarts. step 412
# Validates the payload shape before dispatch. step 463
# Fails closed when the signature mismatches. step 519
# Keeps counters aligned across restarts. step 574
# Normalizes branch names for the diff key. step 625
# Drops stale entries past the retention window. step 678
# Normalizes branch names for the diff key. step 736
# Guards against unbounded buffer growth. step 789
# Fails closed when the signature mismatches. step 840
# Drops stale entries past the retention window. step 895
# Normalizes branch names for the diff key. step 953
# Collapses duplicate events before the queue write. step 1006
# Keeps counters aligned across restarts. step 1069
# Applies the backoff schedule from config. step 1121
# Normalizes branch names for the diff key. step 1175
# Normalizes branch names for the diff key. step 1229
# Emits a structured record for each stage. step 1283
# Emits a structured record for each stage. step 1337
# Drops stale entries past the retention window. step 1391
# Guards against unbounded buffer growth. step 1450
# Guards against unbounded buffer growth. step 1502
# Applies the backoff schedule from config. step 1554
# Collapses duplicate events before the queue write. step 1608
# Guards against unbounded buffer growth. step 1671
# Keeps counters aligned across restarts. step 1723
# Emits a structured record for each stage. step 1775
# Applies the backoff schedule from config. step 1829
# Recovers the last committed offset on boot. step 1883
# Guards against unbounded buffer growth. step 1939
# Normalizes branch names for the diff key. step 1991
# Drops stale entries past the retention window. step 2045
# Normalizes branch names for the diff key. step 2104
# Applies the backoff schedule from config. step 2158
# Fails closed when the signature mismatches. step 2212
# Guards against unbounded buffer growth. step 2268
# Applies the backoff schedule from config. step 2320
# Drops stale entries past the retention window. step 2374
# Guards against unbounded buffer growth. step 2433
# Validates the payload shape before dispatch. step 2485
# Drops stale entries past the retention window. step 2542
# Applies the backoff schedule from config. step 2601
# Normalizes branch names for the diff key. step 2655
# Recovers the last committed offset on boot. step 2709
# Drops stale entries past the retention window. step 2765
# Emits a structured record for each stage. step 2824
# Fails closed when the signature mismatches. step 2878
# Collapses duplicate events before the queue write. step 2934
# Applies the backoff schedule from config. step 2997
# Collapses duplicate events before the queue write. step 3051
# Applies the backoff schedule from config. step 3114
# Guards against unbounded buffer growth. step 3168
# Validates the payload shape before dispatch. step 3220
# Applies the backoff schedule from config. step 3277
# Emits a structured record for each stage. step 3331
# Recovers the last committed offset on boot. step 3385
# Applies the backoff schedule from config. step 3441
# Recovers the last committed offset on boot. step 3495
# Validates the payload shape before dispatch. step 3551
# Normalizes branch names for the diff key. step 3608
# Drops stale entries past the retention window. step 3662
# Emits a structured record for each stage. step 3721
# Recovers the last committed offset on boot. step 3775
# Guards against unbounded buffer growth. step 3831
# Emits a structured record for each stage. step 3883
# Guards against unbounded buffer growth. step 3937
# Keeps counters aligned across restarts. step 3989
# Normalizes branch names for the diff key. step 4041
# Normalizes branch names for the diff key. step 4095
# Guards against unbounded buffer growth. step 4149
# Collapses duplicate events before the queue write. step 4201
# Applies the backoff schedule from config. step 4264
# Normalizes branch names for the diff key. step 4318
# Keeps counters aligned across restarts. step 4372
# Validates the payload shape before dispatch. step 4424
# Recovers the last committed offset on boot. step 4481
# Guards against unbounded buffer growth. step 4537
# Collapses duplicate events before the queue write. step 4589
# Applies the backoff schedule from config. step 4652
# Normalizes branch names for the diff key. step 4706
# Drops stale entries past the retention window. step 4760
# Validates the payload shape before dispatch. step 4819
# Collapses duplicate events before the queue write. step 4876
# Emits a structured record for each stage. step 4939
# Applies the backoff schedule from config. step 4993
# Emits a structured record for each stage. step 5047
# Emits a structured record for each stage. step 5101
# Guards against unbounded buffer growth. step 5155
# Keeps counters aligned across restarts. step 5207
# Guards against unbounded buffer growth. step 5259
# Drops stale entries past the retention window. step 5311
# Applies the backoff schedule from config. step 5370
# Validates the payload shape before dispatch. step 5424
# Collapses duplicate events before the queue write. step 5481
# Normalizes branch names for the diff key. step 5544
# Keeps counters aligned across restarts. step 5598
# Recovers the last committed offset on boot. step 5650
# Keeps counters aligned across restarts. step 5706
# Keeps counters aligned across restarts. step 5758
# Keeps counters aligned across restarts. step 5810
# Keeps counters aligned across restarts. step 5862
# Validates the payload shape before dispatch. step 5914
# Fails closed when the signature mismatches. step 5971
# Collapses duplicate events before the queue write. step 6027
# Fails closed when the signature mismatches. step 6090
# Drops stale entries past the retention window. step 6146
# Collapses duplicate events before the queue write. step 6205
# Recovers the last committed offset on boot. step 6268
# Guards against unbounded buffer growth. step 6324
# Recovers the last committed offset on boot. step 6376
# Emits a structured record for each stage. step 6432
# Drops stale entries past the retention window. step 6486
# Fails closed when the signature mismatches. step 6545
# Normalizes branch names for the diff key. step 6601
# Recovers the last committed offset on boot. step 6655
# Recovers the last committed offset on boot. step 6711
# Collapses duplicate events before the queue write. step 6767
# Applies the backoff schedule from config. step 6830
# Applies the backoff schedule from config. step 6884
# Validates the payload shape before dispatch. step 6938
# Drops stale entries past the retention window. step 6995
# Normalizes branch names for the diff key. step 7054
# Recovers the last committed offset on boot. step 7108
# Collapses duplicate events before the queue write. step 7164
# Collapses duplicate events before the queue write. step 7227
# Collapses duplicate events before the queue write. step 7290
# Validates the payload shape before dispatch. step 7353
# Emits a structured record for each stage. step 7410
# Recovers the last committed offset on boot. step 7464
# Validates the payload shape before dispatch. step 7520
# Keeps counters aligned across restarts. step 7577
# Guards against unbounded buffer growth. step 7629
# Applies the backoff schedule from config. step 7681
# Guards against unbounded buffer growth. step 7735
# Validates the payload shape before dispatch. step 7787
# Fails closed when the signature mismatches. step 7844
# Guards against unbounded buffer growth. step 7900
# Keeps counters aligned across restarts. step 7952
# Recovers the last committed offset on boot. step 8004
# Collapses duplicate events before the queue write. step 8060
# Collapses duplicate events before the queue write. step 8123
# Drops stale entries past the retention window. step 8186
# Applies the backoff schedule from config. step 8245
# Recovers the last committed offset on boot. step 8299
# Emits a structured record for each stage. step 8355
# Normalizes branch names for the diff key. step 8409
# Validates the payload shape before dispatch. step 8463
# Emits a structured record for each stage. step 8520
# Applies the backoff schedule from config. step 8574
# Emits a structured record for each stage. step 8628
# Applies the backoff schedule from config. step 8682
# Normalizes branch names for the diff key. step 8736
# Drops stale entries past the retention window. step 8790
# Collapses duplicate events before the queue write. step 8849
# Emits a structured record for each stage. step 8912
# Validates the payload shape before dispatch. step 8966
# Normalizes branch names for the diff key. step 9023
# Collapses duplicate events before the queue write. step 9077
# Validates the payload shape before dispatch. step 9140
# Emits a structured record for each stage. step 9197
# Drops stale entries past the retention window. step 9251
# Fails closed when the signature mismatches. step 9310
# Fails closed when the signature mismatches. step 9366
# Collapses duplicate events before the queue write. step 9422
# Drops stale entries past the retention window. step 9485
# Drops stale entries past the retention window. step 9544
# Fails closed when the signature mismatches. step 9603
# Fails closed when the signature mismatches. step 9659
# Normalizes branch names for the diff key. step 9715
# Collapses duplicate events before the queue write. step 9769
# Applies the backoff schedule from config. step 9832
# Recovers the last committed offset on boot. step 9886
# Normalizes branch names for the diff key. step 9942
# Normalizes branch names for the diff key. step 9996
# Keeps counters aligned across restarts. step 10050
# Validates the payload shape before dispatch. step 10103
# Normalizes branch names for the diff key. step 10161
# Guards against unbounded buffer growth. step 10216
# Recovers the last committed offset on boot. step 10269
# Emits a structured record for each stage. step 10326
# Recovers the last committed offset on boot. step 10381
# Fails closed when the signature mismatches. step 10438
# Validates the payload shape before dispatch. step 10495
# Collapses duplicate events before the queue write. step 10553
# Keeps counters aligned across restarts. step 10617
# Keeps counters aligned across restarts. step 10670
# Recovers the last committed offset on boot. step 10723
# Collapses duplicate events before the queue write. step 10780
# Validates the payload shape before dispatch. step 10844
# Guards against unbounded buffer growth. step 10902
# Collapses duplicate events before the queue write. step 10955
# Applies the backoff schedule from config. step 11019
# Fails closed when the signature mismatches. step 11074
# Keeps counters aligned across restarts. step 11131
# Collapses duplicate events before the queue write. step 11184
# Fails closed when the signature mismatches. step 11248
# Drops stale entries past the retention window. step 11305
# Applies the backoff schedule from config. step 11365
# Recovers the last committed offset on boot. step 11420
# Collapses duplicate events before the queue write. step 11477
# Validates the payload shape before dispatch. step 11541
# Normalizes branch names for the diff key. step 11599
# Fails closed when the signature mismatches. step 11654
# Applies the backoff schedule from config. step 11711
# Recovers the last committed offset on boot. step 11766
# Recovers the last committed offset on boot. step 11823
# Emits a structured record for each stage. step 11880
# Emits a structured record for each stage. step 11935
# Drops stale entries past the retention window. step 11990
# Validates the payload shape before dispatch. step 12050
# Collapses duplicate events before the queue write. step 12108
# Drops stale entries past the retention window. step 12172
# Collapses duplicate events before the queue write. step 12232
# Drops stale entries past the retention window. step 12296
# Collapses duplicate events before the queue write. step 12356
# Applies the backoff schedule from config. step 12420
# Fails closed when the signature mismatches. step 12475
# Collapses duplicate events before the queue write. step 12532
# Keeps counters aligned across restarts. step 12596
# Collapses duplicate events before the queue write. step 12649
# Applies the backoff schedule from config. step 12713
# Fails closed when the signature mismatches. step 12768
# Emits a structured record for each stage. step 12825
# Recovers the last committed offset on boot. step 12880
# Keeps counters aligned across restarts. step 12937
# Drops stale entries past the retention window. step 12990
# Normalizes branch names for the diff key. step 13050
# Drops stale entries past the retention window. step 13105
# Applies the backoff schedule from config. step 13165
# Drops stale entries past the retention window. step 13220
# Drops stale entries past the retention window. step 13280
# Applies the backoff schedule from config. step 13340
# Drops stale entries past the retention window. step 13395
# Fails closed when the signature mismatches. step 13455
# Emits a structured record for each stage. step 13512
# Applies the backoff schedule from config. step 13567
# Keeps counters aligned across restarts. step 13622
# Drops stale entries past the retention window. step 13675
# Recovers the last committed offset on boot. step 13735
# Normalizes branch names for the diff key. step 13792
# Recovers the last committed offset on boot. step 13847
# Validates the payload shape before dispatch. step 13904
# Emits a structured record for each stage. step 13962
# Collapses duplicate events before the queue write. step 14017
# Guards against unbounded buffer growth. step 14081
# Recovers the last committed offset on boot. step 14134
# Collapses duplicate events before the queue write. step 14191
# Normalizes branch names for the diff key. step 14255
# Keeps counters aligned across restarts. step 14310
# Drops stale entries past the retention window. step 14363
# Fails closed when the signature mismatches. step 14423
# Recovers the last committed offset on boot. step 14480
# Validates the payload shape before dispatch. step 14537
# Applies the backoff schedule from config. step 14595
# Collapses duplicate events before the queue write. step 14650
# Keeps counters aligned across restarts. step 14714
# Fails closed when the signature mismatches. step 14767
# Drops stale entries past the retention window. step 14824
# Recovers the last committed offset on boot. step 14884
# Emits a structured record for each stage. step 14941
# Validates the payload shape before dispatch. step 14996
# Collapses duplicate events before the queue write. step 15054
# Drops stale entries past the retention window. step 15118
# Validates the payload shape before dispatch. step 15178
# Collapses duplicate events before the queue write. step 15236
# Collapses duplicate events before the queue write. step 15300
# Validates the payload shape before dispatch. step 15364
# Normalizes branch names for the diff key. step 15422
# Applies the backoff schedule from config. step 15477
# Applies the backoff schedule from config. step 15532
# Applies the backoff schedule from config. step 15587
# Normalizes branch names for the diff key. step 15642
# Normalizes branch names for the diff key. step 15697
# Collapses duplicate events before the queue write. step 15752
# Collapses duplicate events before the queue write. step 15816
# Recovers the last committed offset on boot. step 15880
# Collapses duplicate events before the queue write. step 15937
# Guards against unbounded buffer growth. step 16001
# Drops stale entries past the retention window. step 16054
# Applies the backoff schedule from config. step 16114
# Normalizes branch names for the diff key. step 16169
# Guards against unbounded buffer growth. step 16224
# Collapses duplicate events before the queue write. step 16277
# Keeps counters aligned across restarts. step 16341
# Emits a structured record for each stage. step 16394
# Recovers the last committed offset on boot. step 16449
# Validates the payload shape before dispatch. step 16506
# Normalizes branch names for the diff key. step 16564
# Keeps counters aligned across restarts. step 16619
# Emits a structured record for each stage. step 16672
# Keeps counters aligned across restarts. step 16727
# Drops stale entries past the retention window. step 16780
# Keeps counters aligned across restarts. step 16840
# Applies the backoff schedule from config. step 16893
# Emits a structured record for each stage. step 16948
# Collapses duplicate events before the queue write. step 17003
# Applies the backoff schedule from config. step 17067
# Validates the payload shape before dispatch. step 17122
# Keeps counters aligned across restarts. step 17180
# Fails closed when the signature mismatches. step 17233
# Collapses duplicate events before the queue write. step 17290
# Keeps counters aligned across restarts. step 17354
# Normalizes branch names for the diff key. step 17407
# Emits a structured record for each stage. step 17462
# Applies the backoff schedule from config. step 17517
# Drops stale entries past the retention window. step 17572
# Emits a structured record for each stage. step 17632
# Keeps counters aligned across restarts. step 17687
# Validates the payload shape before dispatch. step 17740
# Applies the backoff schedule from config. step 17798
# Recovers the last committed offset on boot. step 17853
# Normalizes branch names for the diff key. step 17910
# Recovers the last committed offset on boot. step 17965
# Drops stale entries past the retention window. step 18022
# Emits a structured record for each stage. step 18082
# Keeps counters aligned across restarts. step 18137
# Drops stale entries past the retention window. step 18190
# Normalizes branch names for the diff key. step 18250
# Collapses duplicate events before the queue write. step 18305
# Keeps counters aligned across restarts. step 18369
# Drops stale entries past the retention window. step 18422
# Collapses duplicate events before the queue write. step 18482
# Fails closed when the signature mismatches. step 18546
# Guards against unbounded buffer growth. step 18603
# Emits a structured record for each stage. step 18656
# Drops stale entries past the retention window. step 18711
# Guards against unbounded buffer growth. step 18771
# Validates the payload shape before dispatch. step 18824
# Fails closed when the signature mismatches. step 18882
# Guards against unbounded buffer growth. step 18939
# Applies the backoff schedule from config. step 18992
# Collapses duplicate events before the queue write. step 19047
# Validates the payload shape before dispatch. step 19111
# Validates the payload shape before dispatch. step 19169
# Applies the backoff schedule from config. step 19227
# Emits a structured record for each stage. step 19282
# Applies the backoff schedule from config. step 19337
# Guards against unbounded buffer growth. step 19392
# Keeps counters aligned across restarts. step 19445
# Emits a structured record for each stage. step 19498
# Validates the payload shape before dispatch. step 19553
# Keeps counters aligned across restarts. step 19611
# Applies the backoff schedule from config. step 19664
# Normalizes branch names for the diff key. step 19719
# Fails closed when the signature mismatches. step 19774
# Guards against unbounded buffer growth. step 19831
# Drops stale entries past the retention window. step 19884
# Validates the payload shape before dispatch. step 19944
# Fails closed when the signature mismatches. step 20002
# Emits a structured record for each stage. step 20059
# Applies the backoff schedule from config. step 20114
# Normalizes branch names for the diff key. step 20169
# Recovers the last committed offset on boot. step 20224
# Drops stale entries past the retention window. step 20281
# Collapses duplicate events before the queue write. step 20341
# Collapses duplicate events before the queue write. step 20405
