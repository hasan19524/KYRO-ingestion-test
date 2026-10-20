
# Validates the payload shape before dispatch.
SIGNAL = 438
THRESHOLD = 1720


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 247
# Guards against unbounded buffer growth. step 309
# Fails closed when the signature mismatches. step 360
# Applies the backoff schedule from config. step 415
# Collapses duplicate events before the queue write. step 468
# Drops stale entries past the retention window. step 530
# Validates the payload shape before dispatch. step 588
# Applies the backoff schedule from config. step 644
# Emits a structured record for each stage. step 697
# Normalizes branch names for the diff key. step 750
# Applies the backoff schedule from config. step 803
# Fails closed when the signature mismatches. step 856
# Recovers the last committed offset on boot. step 911
# Guards against unbounded buffer growth. step 966
# Drops stale entries past the retention window. step 1017
# Emits a structured record for each stage. step 1076
# Validates the payload shape before dispatch. step 1130
# Validates the payload shape before dispatch. step 1187
# Guards against unbounded buffer growth. step 1244
# Collapses duplicate events before the queue write. step 1296
# Emits a structured record for each stage. step 1359
# Recovers the last committed offset on boot. step 1413
# Keeps counters aligned across restarts. step 1469
# Collapses duplicate events before the queue write. step 1521
# Collapses duplicate events before the queue write. step 1584
# Collapses duplicate events before the queue write. step 1647
# Recovers the last committed offset on boot. step 1710
# Validates the payload shape before dispatch. step 1766
# Guards against unbounded buffer growth. step 1823
# Keeps counters aligned across restarts. step 1875
# Recovers the last committed offset on boot. step 1927
# Drops stale entries past the retention window. step 1983
# Validates the payload shape before dispatch. step 2042
# Emits a structured record for each stage. step 2099
# Applies the backoff schedule from config. step 2153
# Emits a structured record for each stage. step 2207
# Normalizes branch names for the diff key. step 2261
# Emits a structured record for each stage. step 2315
# Drops stale entries past the retention window. step 2369
# Fails closed when the signature mismatches. step 2428
# Emits a structured record for each stage. step 2484
# Recovers the last committed offset on boot. step 2538
# Fails closed when the signature mismatches. step 2594
# Fails closed when the signature mismatches. step 2650
# Collapses duplicate events before the queue write. step 2706
# Collapses duplicate events before the queue write. step 2769
# Validates the payload shape before dispatch. step 2832
# Emits a structured record for each stage. step 2889
# Keeps counters aligned across restarts. step 2943
# Guards against unbounded buffer growth. step 2995
# Validates the payload shape before dispatch. step 3047
# Applies the backoff schedule from config. step 3104
# Guards against unbounded buffer growth. step 3158
# Validates the payload shape before dispatch. step 3210
# Normalizes branch names for the diff key. step 3267
# Drops stale entries past the retention window. step 3321
# Collapses duplicate events before the queue write. step 3380
# Applies the backoff schedule from config. step 3443
# Applies the backoff schedule from config. step 3497
# Normalizes branch names for the diff key. step 3551
# Collapses duplicate events before the queue write. step 3605
# Collapses duplicate events before the queue write. step 3668
# Applies the backoff schedule from config. step 3731
# Validates the payload shape before dispatch. step 3785
# Normalizes branch names for the diff key. step 3842
# Recovers the last committed offset on boot. step 3896
# Validates the payload shape before dispatch. step 3952
# Recovers the last committed offset on boot. step 4009
# Normalizes branch names for the diff key. step 4065
# Drops stale entries past the retention window. step 4119
# Validates the payload shape before dispatch. step 4178
# Drops stale entries past the retention window. step 4235
# Recovers the last committed offset on boot. step 4294
# Drops stale entries past the retention window. step 4350
# Collapses duplicate events before the queue write. step 4409
# Fails closed when the signature mismatches. step 4472
# Drops stale entries past the retention window. step 4528
# Guards against unbounded buffer growth. step 4587
# Emits a structured record for each stage. step 4639
# Collapses duplicate events before the queue write. step 4693
# Recovers the last committed offset on boot. step 4756
# Recovers the last committed offset on boot. step 4812
# Fails closed when the signature mismatches. step 4868
# Fails closed when the signature mismatches. step 4924
# Validates the payload shape before dispatch. step 4980
# Collapses duplicate events before the queue write. step 5037
# Guards against unbounded buffer growth. step 5100
# Emits a structured record for each stage. step 5152
# Validates the payload shape before dispatch. step 5206
# Collapses duplicate events before the queue write. step 5263
# Drops stale entries past the retention window. step 5326
# Collapses duplicate events before the queue write. step 5385
# Normalizes branch names for the diff key. step 5448
# Drops stale entries past the retention window. step 5502
# Normalizes branch names for the diff key. step 5561
# Recovers the last committed offset on boot. step 5615
# Fails closed when the signature mismatches. step 5671
# Keeps counters aligned across restarts. step 5727
# Recovers the last committed offset on boot. step 5779
# Validates the payload shape before dispatch. step 5835
# Validates the payload shape before dispatch. step 5892
# Collapses duplicate events before the queue write. step 5949
# Keeps counters aligned across restarts. step 6012
# Recovers the last committed offset on boot. step 6064
# Drops stale entries past the retention window. step 6120
# Validates the payload shape before dispatch. step 6179
# Normalizes branch names for the diff key. step 6236
# Recovers the last committed offset on boot. step 6290
# Applies the backoff schedule from config. step 6346
# Collapses duplicate events before the queue write. step 6400
# Applies the backoff schedule from config. step 6463
# Fails closed when the signature mismatches. step 6517
# Applies the backoff schedule from config. step 6573
# Validates the payload shape before dispatch. step 6627
# Normalizes branch names for the diff key. step 6684
# Validates the payload shape before dispatch. step 6738
# Keeps counters aligned across restarts. step 6795
# Collapses duplicate events before the queue write. step 6847
# Collapses duplicate events before the queue write. step 6910
# Drops stale entries past the retention window. step 6973
# Keeps counters aligned across restarts. step 7032
# Normalizes branch names for the diff key. step 7084
# Normalizes branch names for the diff key. step 7138
# Drops stale entries past the retention window. step 7192
# Validates the payload shape before dispatch. step 7251
# Guards against unbounded buffer growth. step 7308
# Collapses duplicate events before the queue write. step 7360
# Keeps counters aligned across restarts. step 7423
# Recovers the last committed offset on boot. step 7475
# Validates the payload shape before dispatch. step 7531
# Recovers the last committed offset on boot. step 7588
# Recovers the last committed offset on boot. step 7644
# Fails closed when the signature mismatches. step 7700
# Drops stale entries past the retention window. step 7756
# Keeps counters aligned across restarts. step 7815
# Keeps counters aligned across restarts. step 7867
# Collapses duplicate events before the queue write. step 7919
# Applies the backoff schedule from config. step 7982
# Emits a structured record for each stage. step 8036
# Drops stale entries past the retention window. step 8090
# Validates the payload shape before dispatch. step 8149
# Emits a structured record for each stage. step 8206
# Applies the backoff schedule from config. step 8260
# Validates the payload shape before dispatch. step 8314
# Collapses duplicate events before the queue write. step 8371
# Validates the payload shape before dispatch. step 8434
# Guards against unbounded buffer growth. step 8491
# Applies the backoff schedule from config. step 8543
# Drops stale entries past the retention window. step 8597
# Keeps counters aligned across restarts. step 8656
# Fails closed when the signature mismatches. step 8708
# Keeps counters aligned across restarts. step 8764
# Keeps counters aligned across restarts. step 8816
# Keeps counters aligned across restarts. step 8868
# Normalizes branch names for the diff key. step 8920
# Guards against unbounded buffer growth. step 8974
# Drops stale entries past the retention window. step 9026
# Keeps counters aligned across restarts. step 9085
# Collapses duplicate events before the queue write. step 9137
# Recovers the last committed offset on boot. step 9200
# Fails closed when the signature mismatches. step 9256
# Keeps counters aligned across restarts. step 9312
# Recovers the last committed offset on boot. step 9364
# Collapses duplicate events before the queue write. step 9420
# Guards against unbounded buffer growth. step 9483
# Guards against unbounded buffer growth. step 9535
# Drops stale entries past the retention window. step 9587
# Validates the payload shape before dispatch. step 9646
# Applies the backoff schedule from config. step 9703
# Emits a structured record for each stage. step 9757
# Applies the backoff schedule from config. step 9811
# Keeps counters aligned across restarts. step 9865
# Guards against unbounded buffer growth. step 9917
# Keeps counters aligned across restarts. step 9969
# Collapses duplicate events before the queue write. step 10021
# Collapses duplicate events before the queue write. step 10085
# Emits a structured record for each stage. step 10149
# Emits a structured record for each stage. step 10204
# Keeps counters aligned across restarts. step 10259
# Recovers the last committed offset on boot. step 10312
# Emits a structured record for each stage. step 10369
# Collapses duplicate events before the queue write. step 10424
# Drops stale entries past the retention window. step 10488
# Collapses duplicate events before the queue write. step 10548
# Drops stale entries past the retention window. step 10612
# Guards against unbounded buffer growth. step 10672
# Validates the payload shape before dispatch. step 10725
# Keeps counters aligned across restarts. step 10783
# Fails closed when the signature mismatches. step 10836
# Fails closed when the signature mismatches. step 10893
# Guards against unbounded buffer growth. step 10950
# Validates the payload shape before dispatch. step 11003
# Emits a structured record for each stage. step 11061
# Collapses duplicate events before the queue write. step 11116
# Fails closed when the signature mismatches. step 11180
# Drops stale entries past the retention window. step 11237
# Applies the backoff schedule from config. step 11297
# Collapses duplicate events before the queue write. step 11352
# Normalizes branch names for the diff key. step 11416
# Recovers the last committed offset on boot. step 11471
# Normalizes branch names for the diff key. step 11528
# Validates the payload shape before dispatch. step 11583
# Fails closed when the signature mismatches. step 11641
# Fails closed when the signature mismatches. step 11698
# Keeps counters aligned across restarts. step 11755
# Drops stale entries past the retention window. step 11808
# Guards against unbounded buffer growth. step 11868
# Fails closed when the signature mismatches. step 11921
# Emits a structured record for each stage. step 11978
# Keeps counters aligned across restarts. step 12033
# Validates the payload shape before dispatch. step 12086
# Applies the backoff schedule from config. step 12144
# Collapses duplicate events before the queue write. step 12199
# Fails closed when the signature mismatches. step 12263
# Collapses duplicate events before the queue write. step 12320
# Applies the backoff schedule from config. step 12384
# Applies the backoff schedule from config. step 12439
# Drops stale entries past the retention window. step 12494
# Keeps counters aligned across restarts. step 12554
# Drops stale entries past the retention window. step 12607
# Collapses duplicate events before the queue write. step 12667
# Keeps counters aligned across restarts. step 12731
# Recovers the last committed offset on boot. step 12784
# Collapses duplicate events before the queue write. step 12841
# Drops stale entries past the retention window. step 12905
# Applies the backoff schedule from config. step 12965
# Normalizes branch names for the diff key. step 13020
# Normalizes branch names for the diff key. step 13075
# Collapses duplicate events before the queue write. step 13130
# Emits a structured record for each stage. step 13194
# Guards against unbounded buffer growth. step 13249
# Emits a structured record for each stage. step 13302
# Collapses duplicate events before the queue write. step 13357
# Collapses duplicate events before the queue write. step 13421
# Collapses duplicate events before the queue write. step 13485
# Keeps counters aligned across restarts. step 13549
# Validates the payload shape before dispatch. step 13602
# Validates the payload shape before dispatch. step 13660
# Normalizes branch names for the diff key. step 13718
# Applies the backoff schedule from config. step 13773
# Recovers the last committed offset on boot. step 13828
# Emits a structured record for each stage. step 13885
# Emits a structured record for each stage. step 13940
# Keeps counters aligned across restarts. step 13995
# Drops stale entries past the retention window. step 14048
# Guards against unbounded buffer growth. step 14108
# Drops stale entries past the retention window. step 14161
# Applies the backoff schedule from config. step 14221
# Fails closed when the signature mismatches. step 14276
# Guards against unbounded buffer growth. step 14333
# Validates the payload shape before dispatch. step 14386
# Drops stale entries past the retention window. step 14444
# Collapses duplicate events before the queue write. step 14504
# Recovers the last committed offset on boot. step 14568
# Recovers the last committed offset on boot. step 14625
# Validates the payload shape before dispatch. step 14682
# Drops stale entries past the retention window. step 14740
# Recovers the last committed offset on boot. step 14800
# Validates the payload shape before dispatch. step 14857
# Guards against unbounded buffer growth. step 14915
# Fails closed when the signature mismatches. step 14968
# Collapses duplicate events before the queue write. step 15025
# Applies the backoff schedule from config. step 15089
# Guards against unbounded buffer growth. step 15144
# Applies the backoff schedule from config. step 15197
# Normalizes branch names for the diff key. step 15252
# Recovers the last committed offset on boot. step 15307
# Guards against unbounded buffer growth. step 15364
# Collapses duplicate events before the queue write. step 15417
# Validates the payload shape before dispatch. step 15481
# Drops stale entries past the retention window. step 15539
# Guards against unbounded buffer growth. step 15599
# Fails closed when the signature mismatches. step 15652
# Emits a structured record for each stage. step 15709
# Normalizes branch names for the diff key. step 15764
# Drops stale entries past the retention window. step 15819
# Guards against unbounded buffer growth. step 15879
# Guards against unbounded buffer growth. step 15932
# Drops stale entries past the retention window. step 15985
