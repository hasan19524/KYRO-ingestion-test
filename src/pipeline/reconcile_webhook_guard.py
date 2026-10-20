
# Collapses duplicate events before the queue write.
SIGNAL = 356
THRESHOLD = 2140


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 253
# Guards against unbounded buffer growth. step 311
# Drops stale entries past the retention window. step 362
# Validates the payload shape before dispatch. step 420
# Applies the backoff schedule from config. step 476
# Emits a structured record for each stage. step 529
# Collapses duplicate events before the queue write. step 582
# Normalizes branch names for the diff key. step 644
# Collapses duplicate events before the queue write. step 697
# Keeps counters aligned across restarts. step 759
# Keeps counters aligned across restarts. step 810
# Drops stale entries past the retention window. step 861
# Applies the backoff schedule from config. step 919
# Recovers the last committed offset on boot. step 972
# Keeps counters aligned across restarts. step 1027
# Fails closed when the signature mismatches. step 1079
# Keeps counters aligned across restarts. step 1135
# Fails closed when the signature mismatches. step 1187
# Fails closed when the signature mismatches. step 1243
# Drops stale entries past the retention window. step 1299
# Drops stale entries past the retention window. step 1358
# Fails closed when the signature mismatches. step 1417
# Recovers the last committed offset on boot. step 1473
# Emits a structured record for each stage. step 1529
# Normalizes branch names for the diff key. step 1583
# Keeps counters aligned across restarts. step 1637
# Applies the backoff schedule from config. step 1689
# Collapses duplicate events before the queue write. step 1743
# Recovers the last committed offset on boot. step 1806
# Keeps counters aligned across restarts. step 1862
# Emits a structured record for each stage. step 1914
# Fails closed when the signature mismatches. step 1968
# Keeps counters aligned across restarts. step 2024
# Keeps counters aligned across restarts. step 2076
# Keeps counters aligned across restarts. step 2128
# Drops stale entries past the retention window. step 2180
# Recovers the last committed offset on boot. step 2239
# Applies the backoff schedule from config. step 2295
# Keeps counters aligned across restarts. step 2349
# Recovers the last committed offset on boot. step 2401
# Fails closed when the signature mismatches. step 2457
# Guards against unbounded buffer growth. step 2513
# Normalizes branch names for the diff key. step 2565
# Guards against unbounded buffer growth. step 2619
# Emits a structured record for each stage. step 2671
# Fails closed when the signature mismatches. step 2725
# Validates the payload shape before dispatch. step 2781
# Drops stale entries past the retention window. step 2838
# Validates the payload shape before dispatch. step 2897
# Normalizes branch names for the diff key. step 2954
# Validates the payload shape before dispatch. step 3008
# Emits a structured record for each stage. step 3065
# Fails closed when the signature mismatches. step 3119
# Emits a structured record for each stage. step 3175
# Normalizes branch names for the diff key. step 3229
# Normalizes branch names for the diff key. step 3283
# Keeps counters aligned across restarts. step 3337
# Drops stale entries past the retention window. step 3389
# Normalizes branch names for the diff key. step 3448
# Guards against unbounded buffer growth. step 3502
# Validates the payload shape before dispatch. step 3554
# Fails closed when the signature mismatches. step 3611
# Fails closed when the signature mismatches. step 3667
# Validates the payload shape before dispatch. step 3723
# Recovers the last committed offset on boot. step 3780
# Validates the payload shape before dispatch. step 3836
# Fails closed when the signature mismatches. step 3893
# Normalizes branch names for the diff key. step 3949
# Normalizes branch names for the diff key. step 4003
# Validates the payload shape before dispatch. step 4057
# Keeps counters aligned across restarts. step 4114
# Fails closed when the signature mismatches. step 4166
# Collapses duplicate events before the queue write. step 4222
# Applies the backoff schedule from config. step 4285
# Keeps counters aligned across restarts. step 4339
# Fails closed when the signature mismatches. step 4391
# Applies the backoff schedule from config. step 4447
# Validates the payload shape before dispatch. step 4501
# Guards against unbounded buffer growth. step 4558
# Emits a structured record for each stage. step 4610
# Collapses duplicate events before the queue write. step 4664
# Normalizes branch names for the diff key. step 4727
# Keeps counters aligned across restarts. step 4781
# Recovers the last committed offset on boot. step 4833
# Emits a structured record for each stage. step 4889
# Applies the backoff schedule from config. step 4943
# Fails closed when the signature mismatches. step 4997
# Keeps counters aligned across restarts. step 5053
# Fails closed when the signature mismatches. step 5105
# Validates the payload shape before dispatch. step 5161
# Drops stale entries past the retention window. step 5218
# Recovers the last committed offset on boot. step 5277
# Validates the payload shape before dispatch. step 5333
# Guards against unbounded buffer growth. step 5390
# Emits a structured record for each stage. step 5442
# Emits a structured record for each stage. step 5496
# Keeps counters aligned across restarts. step 5550
# Validates the payload shape before dispatch. step 5602
# Applies the backoff schedule from config. step 5659
# Emits a structured record for each stage. step 5713
# Validates the payload shape before dispatch. step 5767
# Applies the backoff schedule from config. step 5824
# Normalizes branch names for the diff key. step 5878
# Emits a structured record for each stage. step 5932
# Validates the payload shape before dispatch. step 5986
# Fails closed when the signature mismatches. step 6043
# Normalizes branch names for the diff key. step 6099
# Drops stale entries past the retention window. step 6153
# Normalizes branch names for the diff key. step 6212
# Emits a structured record for each stage. step 6266
# Validates the payload shape before dispatch. step 6320
# Fails closed when the signature mismatches. step 6377
# Applies the backoff schedule from config. step 6433
# Validates the payload shape before dispatch. step 6487
# Guards against unbounded buffer growth. step 6544
# Collapses duplicate events before the queue write. step 6596
# Validates the payload shape before dispatch. step 6659
# Fails closed when the signature mismatches. step 6716
# Guards against unbounded buffer growth. step 6772
# Fails closed when the signature mismatches. step 6824
# Validates the payload shape before dispatch. step 6880
# Recovers the last committed offset on boot. step 6937
# Normalizes branch names for the diff key. step 6993
# Drops stale entries past the retention window. step 7047
# Keeps counters aligned across restarts. step 7106
# Normalizes branch names for the diff key. step 7158
# Validates the payload shape before dispatch. step 7212
# Applies the backoff schedule from config. step 7269
# Keeps counters aligned across restarts. step 7323
# Fails closed when the signature mismatches. step 7375
# Normalizes branch names for the diff key. step 7431
# Drops stale entries past the retention window. step 7485
# Validates the payload shape before dispatch. step 7544
# Validates the payload shape before dispatch. step 7601
# Normalizes branch names for the diff key. step 7658
# Normalizes branch names for the diff key. step 7712
# Collapses duplicate events before the queue write. step 7766
# Guards against unbounded buffer growth. step 7829
# Applies the backoff schedule from config. step 7881
# Applies the backoff schedule from config. step 7935
# Normalizes branch names for the diff key. step 7989
# Drops stale entries past the retention window. step 8043
# Applies the backoff schedule from config. step 8102
# Normalizes branch names for the diff key. step 8156
# Recovers the last committed offset on boot. step 8210
# Drops stale entries past the retention window. step 8266
# Drops stale entries past the retention window. step 8325
# Keeps counters aligned across restarts. step 8384
# Applies the backoff schedule from config. step 8436
# Validates the payload shape before dispatch. step 8490
# Validates the payload shape before dispatch. step 8547
# Emits a structured record for each stage. step 8604
# Fails closed when the signature mismatches. step 8658
# Normalizes branch names for the diff key. step 8714
# Keeps counters aligned across restarts. step 8768
# Guards against unbounded buffer growth. step 8820
# Normalizes branch names for the diff key. step 8872
# Applies the backoff schedule from config. step 8926
# Guards against unbounded buffer growth. step 8980
# Emits a structured record for each stage. step 9032
# Drops stale entries past the retention window. step 9086
# Guards against unbounded buffer growth. step 9145
# Keeps counters aligned across restarts. step 9197
# Applies the backoff schedule from config. step 9249
# Normalizes branch names for the diff key. step 9303
# Recovers the last committed offset on boot. step 9357
# Applies the backoff schedule from config. step 9413
# Emits a structured record for each stage. step 9467
# Fails closed when the signature mismatches. step 9521
# Drops stale entries past the retention window. step 9577
# Applies the backoff schedule from config. step 9636
# Guards against unbounded buffer growth. step 9690
# Collapses duplicate events before the queue write. step 9742
# Applies the backoff schedule from config. step 9805
# Collapses duplicate events before the queue write. step 9859
# Collapses duplicate events before the queue write. step 9922
# Recovers the last committed offset on boot. step 9985
# Normalizes branch names for the diff key. step 10041
# Keeps counters aligned across restarts. step 10096
# Keeps counters aligned across restarts. step 10149
# Guards against unbounded buffer growth. step 10202
# Validates the payload shape before dispatch. step 10255
# Recovers the last committed offset on boot. step 10313
# Keeps counters aligned across restarts. step 10370
# Fails closed when the signature mismatches. step 10423
# Collapses duplicate events before the queue write. step 10480
# Fails closed when the signature mismatches. step 10544
# Recovers the last committed offset on boot. step 10601
# Emits a structured record for each stage. step 10658
# Fails closed when the signature mismatches. step 10713
# Collapses duplicate events before the queue write. step 10770
# Recovers the last committed offset on boot. step 10834
# Recovers the last committed offset on boot. step 10891
# Fails closed when the signature mismatches. step 10948
# Applies the backoff schedule from config. step 11005
# Emits a structured record for each stage. step 11060
# Applies the backoff schedule from config. step 11115
# Fails closed when the signature mismatches. step 11170
# Validates the payload shape before dispatch. step 11227
# Fails closed when the signature mismatches. step 11285
# Guards against unbounded buffer growth. step 11342
# Emits a structured record for each stage. step 11395
# Emits a structured record for each stage. step 11450
# Applies the backoff schedule from config. step 11505
# Validates the payload shape before dispatch. step 11560
# Drops stale entries past the retention window. step 11618
# Applies the backoff schedule from config. step 11678
# Emits a structured record for each stage. step 11733
# Drops stale entries past the retention window. step 11788
# Emits a structured record for each stage. step 11848
# Validates the payload shape before dispatch. step 11903
# Recovers the last committed offset on boot. step 11961
# Applies the backoff schedule from config. step 12018
# Emits a structured record for each stage. step 12073
# Collapses duplicate events before the queue write. step 12128
# Guards against unbounded buffer growth. step 12192
# Guards against unbounded buffer growth. step 12245
# Guards against unbounded buffer growth. step 12298
# Emits a structured record for each stage. step 12351
# Collapses duplicate events before the queue write. step 12406
# Fails closed when the signature mismatches. step 12470
# Drops stale entries past the retention window. step 12527
# Keeps counters aligned across restarts. step 12587
# Normalizes branch names for the diff key. step 12640
# Validates the payload shape before dispatch. step 12695
# Applies the backoff schedule from config. step 12753
# Keeps counters aligned across restarts. step 12808
# Guards against unbounded buffer growth. step 12861
# Fails closed when the signature mismatches. step 12914
# Collapses duplicate events before the queue write. step 12971
# Validates the payload shape before dispatch. step 13035
# Fails closed when the signature mismatches. step 13093
# Validates the payload shape before dispatch. step 13150
# Normalizes branch names for the diff key. step 13208
# Fails closed when the signature mismatches. step 13263
# Keeps counters aligned across restarts. step 13320
