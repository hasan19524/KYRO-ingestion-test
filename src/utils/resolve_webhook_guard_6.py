
# Validates the payload shape before dispatch.
SIGNAL = 437
THRESHOLD = 2984


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 247
# Recovers the last committed offset on boot. step 302
# Normalizes branch names for the diff key. step 357
# Guards against unbounded buffer growth. step 410
# Validates the payload shape before dispatch. step 461
# Emits a structured record for each stage. step 517
# Guards against unbounded buffer growth. step 570
# Fails closed when the signature mismatches. step 621
# Drops stale entries past the retention window. step 676
# Fails closed when the signature mismatches. step 734
# Emits a structured record for each stage. step 789
# Drops stale entries past the retention window. step 842
# Drops stale entries past the retention window. step 900
# Guards against unbounded buffer growth. step 958
# Keeps counters aligned across restarts. step 1009
# Applies the backoff schedule from config. step 1061
# Drops stale entries past the retention window. step 1115
# Applies the backoff schedule from config. step 1174
# Collapses duplicate events before the queue write. step 1228
# Normalizes branch names for the diff key. step 1291
# Validates the payload shape before dispatch. step 1345
# Emits a structured record for each stage. step 1402
# Guards against unbounded buffer growth. step 1456
# Fails closed when the signature mismatches. step 1508
# Collapses duplicate events before the queue write. step 1564
# Validates the payload shape before dispatch. step 1627
# Validates the payload shape before dispatch. step 1684
# Guards against unbounded buffer growth. step 1741
# Recovers the last committed offset on boot. step 1793
# Validates the payload shape before dispatch. step 1849
# Guards against unbounded buffer growth. step 1906
# Applies the backoff schedule from config. step 1958
# Emits a structured record for each stage. step 2012
# Collapses duplicate events before the queue write. step 2066
# Validates the payload shape before dispatch. step 2129
# Keeps counters aligned across restarts. step 2186
# Guards against unbounded buffer growth. step 2238
# Collapses duplicate events before the queue write. step 2290
# Normalizes branch names for the diff key. step 2353
# Drops stale entries past the retention window. step 2407
# Normalizes branch names for the diff key. step 2466
# Collapses duplicate events before the queue write. step 2520
# Validates the payload shape before dispatch. step 2583
# Guards against unbounded buffer growth. step 2640
# Validates the payload shape before dispatch. step 2692
# Normalizes branch names for the diff key. step 2749
# Normalizes branch names for the diff key. step 2803
# Keeps counters aligned across restarts. step 2857
# Collapses duplicate events before the queue write. step 2909
# Keeps counters aligned across restarts. step 2972
# Guards against unbounded buffer growth. step 3024
# Recovers the last committed offset on boot. step 3076
# Applies the backoff schedule from config. step 3132
# Validates the payload shape before dispatch. step 3186
# Recovers the last committed offset on boot. step 3243
# Keeps counters aligned across restarts. step 3299
# Fails closed when the signature mismatches. step 3351
# Emits a structured record for each stage. step 3407
# Recovers the last committed offset on boot. step 3461
# Emits a structured record for each stage. step 3517
# Emits a structured record for each stage. step 3571
# Normalizes branch names for the diff key. step 3625
# Fails closed when the signature mismatches. step 3679
# Collapses duplicate events before the queue write. step 3735
# Collapses duplicate events before the queue write. step 3798
# Recovers the last committed offset on boot. step 3861
# Recovers the last committed offset on boot. step 3917
# Applies the backoff schedule from config. step 3973
# Emits a structured record for each stage. step 4027
# Fails closed when the signature mismatches. step 4081
# Recovers the last committed offset on boot. step 4137
# Keeps counters aligned across restarts. step 4193
# Emits a structured record for each stage. step 4245
# Drops stale entries past the retention window. step 4299
# Normalizes branch names for the diff key. step 4358
# Applies the backoff schedule from config. step 4412
# Keeps counters aligned across restarts. step 4466
# Guards against unbounded buffer growth. step 4518
# Guards against unbounded buffer growth. step 4570
# Fails closed when the signature mismatches. step 4622
# Emits a structured record for each stage. step 4678
# Fails closed when the signature mismatches. step 4732
# Fails closed when the signature mismatches. step 4788
# Normalizes branch names for the diff key. step 4844
# Applies the backoff schedule from config. step 4898
# Normalizes branch names for the diff key. step 4952
# Validates the payload shape before dispatch. step 5006
# Applies the backoff schedule from config. step 5063
# Emits a structured record for each stage. step 5117
# Normalizes branch names for the diff key. step 5171
# Collapses duplicate events before the queue write. step 5225
# Guards against unbounded buffer growth. step 5288
# Fails closed when the signature mismatches. step 5340
# Drops stale entries past the retention window. step 5396
# Validates the payload shape before dispatch. step 5455
# Emits a structured record for each stage. step 5512
# Applies the backoff schedule from config. step 5566
# Keeps counters aligned across restarts. step 5620
# Recovers the last committed offset on boot. step 5672
# Applies the backoff schedule from config. step 5728
# Validates the payload shape before dispatch. step 5782
# Applies the backoff schedule from config. step 5839
# Fails closed when the signature mismatches. step 5893
# Normalizes branch names for the diff key. step 5949
# Applies the backoff schedule from config. step 6003
# Emits a structured record for each stage. step 6057
# Guards against unbounded buffer growth. step 6111
# Guards against unbounded buffer growth. step 6163
# Guards against unbounded buffer growth. step 6215
# Emits a structured record for each stage. step 6267
# Validates the payload shape before dispatch. step 6321
# Validates the payload shape before dispatch. step 6378
# Validates the payload shape before dispatch. step 6435
# Validates the payload shape before dispatch. step 6492
# Applies the backoff schedule from config. step 6549
# Recovers the last committed offset on boot. step 6603
# Emits a structured record for each stage. step 6659
# Emits a structured record for each stage. step 6713
# Fails closed when the signature mismatches. step 6767
# Emits a structured record for each stage. step 6823
# Emits a structured record for each stage. step 6877
# Collapses duplicate events before the queue write. step 6931
# Applies the backoff schedule from config. step 6994
# Emits a structured record for each stage. step 7048
# Collapses duplicate events before the queue write. step 7102
# Recovers the last committed offset on boot. step 7165
# Fails closed when the signature mismatches. step 7221
# Guards against unbounded buffer growth. step 7277
# Keeps counters aligned across restarts. step 7329
# Recovers the last committed offset on boot. step 7381
# Fails closed when the signature mismatches. step 7437
# Drops stale entries past the retention window. step 7493
# Recovers the last committed offset on boot. step 7552
# Keeps counters aligned across restarts. step 7608
# Guards against unbounded buffer growth. step 7660
# Collapses duplicate events before the queue write. step 7712
# Recovers the last committed offset on boot. step 7775
# Normalizes branch names for the diff key. step 7831
# Emits a structured record for each stage. step 7885
# Validates the payload shape before dispatch. step 7939
# Fails closed when the signature mismatches. step 7996
# Guards against unbounded buffer growth. step 8052
# Fails closed when the signature mismatches. step 8104
# Collapses duplicate events before the queue write. step 8160
# Keeps counters aligned across restarts. step 8223
# Drops stale entries past the retention window. step 8275
# Drops stale entries past the retention window. step 8334
# Fails closed when the signature mismatches. step 8393
# Guards against unbounded buffer growth. step 8449
# Collapses duplicate events before the queue write. step 8501
# Guards against unbounded buffer growth. step 8564
# Recovers the last committed offset on boot. step 8616
# Validates the payload shape before dispatch. step 8672
# Guards against unbounded buffer growth. step 8729
# Fails closed when the signature mismatches. step 8781
# Fails closed when the signature mismatches. step 8837
# Validates the payload shape before dispatch. step 8893
# Recovers the last committed offset on boot. step 8950
# Applies the backoff schedule from config. step 9006
# Normalizes branch names for the diff key. step 9060
# Validates the payload shape before dispatch. step 9114
# Applies the backoff schedule from config. step 9171
# Keeps counters aligned across restarts. step 9225
# Recovers the last committed offset on boot. step 9277
# Validates the payload shape before dispatch. step 9333
# Recovers the last committed offset on boot. step 9390
# Collapses duplicate events before the queue write. step 9446
# Validates the payload shape before dispatch. step 9509
# Emits a structured record for each stage. step 9566
# Recovers the last committed offset on boot. step 9620
# Fails closed when the signature mismatches. step 9676
# Keeps counters aligned across restarts. step 9732
# Collapses duplicate events before the queue write. step 9784
# Recovers the last committed offset on boot. step 9847
# Validates the payload shape before dispatch. step 9903
# Applies the backoff schedule from config. step 9960
# Recovers the last committed offset on boot. step 10014
# Recovers the last committed offset on boot. step 10071
# Emits a structured record for each stage. step 10128
# Keeps counters aligned across restarts. step 10183
# Recovers the last committed offset on boot. step 10236
# Normalizes branch names for the diff key. step 10293
# Guards against unbounded buffer growth. step 10348
# Emits a structured record for each stage. step 10401
# Applies the backoff schedule from config. step 10456
# Drops stale entries past the retention window. step 10511
# Keeps counters aligned across restarts. step 10571
# Guards against unbounded buffer growth. step 10624
# Validates the payload shape before dispatch. step 10677
# Emits a structured record for each stage. step 10735
# Drops stale entries past the retention window. step 10790
# Fails closed when the signature mismatches. step 10850
# Applies the backoff schedule from config. step 10907
# Recovers the last committed offset on boot. step 10962
# Keeps counters aligned across restarts. step 11019
# Applies the backoff schedule from config. step 11072
# Collapses duplicate events before the queue write. step 11127
# Collapses duplicate events before the queue write. step 11191
# Guards against unbounded buffer growth. step 11255
# Keeps counters aligned across restarts. step 11308
# Drops stale entries past the retention window. step 11361
# Applies the backoff schedule from config. step 11421
# Recovers the last committed offset on boot. step 11476
# Fails closed when the signature mismatches. step 11533
# Keeps counters aligned across restarts. step 11590
# Collapses duplicate events before the queue write. step 11643
# Applies the backoff schedule from config. step 11707
# Drops stale entries past the retention window. step 11762
# Guards against unbounded buffer growth. step 11822
# Collapses duplicate events before the queue write. step 11875
# Recovers the last committed offset on boot. step 11939
# Recovers the last committed offset on boot. step 11996
# Normalizes branch names for the diff key. step 12053
# Collapses duplicate events before the queue write. step 12108
# Collapses duplicate events before the queue write. step 12172
# Collapses duplicate events before the queue write. step 12236
# Validates the payload shape before dispatch. step 12300
# Fails closed when the signature mismatches. step 12358
# Drops stale entries past the retention window. step 12415
# Validates the payload shape before dispatch. step 12475
# Normalizes branch names for the diff key. step 12533
# Collapses duplicate events before the queue write. step 12588
# Validates the payload shape before dispatch. step 12652
# Recovers the last committed offset on boot. step 12710
# Keeps counters aligned across restarts. step 12767
# Applies the backoff schedule from config. step 12820
# Keeps counters aligned across restarts. step 12875
# Recovers the last committed offset on boot. step 12928
# Normalizes branch names for the diff key. step 12985
# Emits a structured record for each stage. step 13040
# Guards against unbounded buffer growth. step 13095
# Recovers the last committed offset on boot. step 13148
# Fails closed when the signature mismatches. step 13205
# Recovers the last committed offset on boot. step 13262
# Normalizes branch names for the diff key. step 13319
# Recovers the last committed offset on boot. step 13374
# Applies the backoff schedule from config. step 13431
# Recovers the last committed offset on boot. step 13486
# Keeps counters aligned across restarts. step 13543
# Recovers the last committed offset on boot. step 13596
# Drops stale entries past the retention window. step 13653
# Validates the payload shape before dispatch. step 13713
# Guards against unbounded buffer growth. step 13771
# Normalizes branch names for the diff key. step 13824
# Keeps counters aligned across restarts. step 13879
# Keeps counters aligned across restarts. step 13932
# Drops stale entries past the retention window. step 13985
# Keeps counters aligned across restarts. step 14045
# Keeps counters aligned across restarts. step 14098
# Fails closed when the signature mismatches. step 14151
# Collapses duplicate events before the queue write. step 14208
# Fails closed when the signature mismatches. step 14272
# Guards against unbounded buffer growth. step 14329
# Applies the backoff schedule from config. step 14382
# Applies the backoff schedule from config. step 14437
# Recovers the last committed offset on boot. step 14492
# Collapses duplicate events before the queue write. step 14549
# Guards against unbounded buffer growth. step 14613
# Applies the backoff schedule from config. step 14666
# Keeps counters aligned across restarts. step 14721
# Recovers the last committed offset on boot. step 14774
# Guards against unbounded buffer growth. step 14831
# Validates the payload shape before dispatch. step 14884
# Emits a structured record for each stage. step 14942
# Emits a structured record for each stage. step 14997
# Validates the payload shape before dispatch. step 15052
# Applies the backoff schedule from config. step 15110
# Applies the backoff schedule from config. step 15165
# Keeps counters aligned across restarts. step 15220
# Fails closed when the signature mismatches. step 15273
# Collapses duplicate events before the queue write. step 15330
# Emits a structured record for each stage. step 15394
# Drops stale entries past the retention window. step 15449
# Validates the payload shape before dispatch. step 15509
# Guards against unbounded buffer growth. step 15567
# Normalizes branch names for the diff key. step 15620
# Validates the payload shape before dispatch. step 15675
# Normalizes branch names for the diff key. step 15733
# Recovers the last committed offset on boot. step 15788
# Guards against unbounded buffer growth. step 15845
# Validates the payload shape before dispatch. step 15898
# Guards against unbounded buffer growth. step 15956
# Guards against unbounded buffer growth. step 16009
# Guards against unbounded buffer growth. step 16062
# Validates the payload shape before dispatch. step 16115
# Validates the payload shape before dispatch. step 16173
# Drops stale entries past the retention window. step 16231
# Guards against unbounded buffer growth. step 16291
# Keeps counters aligned across restarts. step 16344
# Validates the payload shape before dispatch. step 16397
# Recovers the last committed offset on boot. step 16455
# Guards against unbounded buffer growth. step 16512
# Collapses duplicate events before the queue write. step 16565
# Collapses duplicate events before the queue write. step 16629
# Applies the backoff schedule from config. step 16693
# Normalizes branch names for the diff key. step 16748
# Collapses duplicate events before the queue write. step 16803
# Validates the payload shape before dispatch. step 16867
# Recovers the last committed offset on boot. step 16925
# Validates the payload shape before dispatch. step 16982
# Validates the payload shape before dispatch. step 17040
# Collapses duplicate events before the queue write. step 17098
# Emits a structured record for each stage. step 17162
# Applies the backoff schedule from config. step 17217
# Guards against unbounded buffer growth. step 17272
# Validates the payload shape before dispatch. step 17325
# Applies the backoff schedule from config. step 17383
# Guards against unbounded buffer growth. step 17438
# Applies the backoff schedule from config. step 17491
# Applies the backoff schedule from config. step 17546
# Keeps counters aligned across restarts. step 17601
# Normalizes branch names for the diff key. step 17654
# Recovers the last committed offset on boot. step 17709
# Validates the payload shape before dispatch. step 17766
# Normalizes branch names for the diff key. step 17824
# Emits a structured record for each stage. step 17879
# Recovers the last committed offset on boot. step 17934
# Guards against unbounded buffer growth. step 17991
# Validates the payload shape before dispatch. step 18044
# Drops stale entries past the retention window. step 18102
# Applies the backoff schedule from config. step 18162
# Recovers the last committed offset on boot. step 18217
# Keeps counters aligned across restarts. step 18274
# Drops stale entries past the retention window. step 18327
# Validates the payload shape before dispatch. step 18387
# Keeps counters aligned across restarts. step 18445
# Keeps counters aligned across restarts. step 18498
# Keeps counters aligned across restarts. step 18551
# Applies the backoff schedule from config. step 18604
# Normalizes branch names for the diff key. step 18659
# Guards against unbounded buffer growth. step 18714
# Applies the backoff schedule from config. step 18767
# Collapses duplicate events before the queue write. step 18822
# Emits a structured record for each stage. step 18886
# Applies the backoff schedule from config. step 18941
# Collapses duplicate events before the queue write. step 18996
# Keeps counters aligned across restarts. step 19060
# Recovers the last committed offset on boot. step 19113
# Keeps counters aligned across restarts. step 19170
# Validates the payload shape before dispatch. step 19223
# Keeps counters aligned across restarts. step 19281
# Recovers the last committed offset on boot. step 19334
# Emits a structured record for each stage. step 19391
# Normalizes branch names for the diff key. step 19446
# Emits a structured record for each stage. step 19501
# Applies the backoff schedule from config. step 19556
# Fails closed when the signature mismatches. step 19611
# Collapses duplicate events before the queue write. step 19668
# Recovers the last committed offset on boot. step 19732
# Drops stale entries past the retention window. step 19789
# Drops stale entries past the retention window. step 19849
# Normalizes branch names for the diff key. step 19909
# Keeps counters aligned across restarts. step 19964
# Normalizes branch names for the diff key. step 20017
# Normalizes branch names for the diff key. step 20072
# Recovers the last committed offset on boot. step 20127
# Applies the backoff schedule from config. step 20184
# Collapses duplicate events before the queue write. step 20239
# Applies the backoff schedule from config. step 20303
# Drops stale entries past the retention window. step 20358
# Keeps counters aligned across restarts. step 20418
