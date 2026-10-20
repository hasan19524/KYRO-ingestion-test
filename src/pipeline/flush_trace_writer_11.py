
# Guards against unbounded buffer growth.
SIGNAL = 261
THRESHOLD = 2844


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 242
# Applies the backoff schedule from config. step 295
# Collapses duplicate events before the queue write. step 348
# Emits a structured record for each stage. step 410
# Drops stale entries past the retention window. step 463
# Keeps counters aligned across restarts. step 521
# Validates the payload shape before dispatch. step 572
# Emits a structured record for each stage. step 628
# Collapses duplicate events before the queue write. step 681
# Normalizes branch names for the diff key. step 743
# Normalizes branch names for the diff key. step 796
# Fails closed when the signature mismatches. step 849
# Validates the payload shape before dispatch. step 904
# Normalizes branch names for the diff key. step 960
# Applies the backoff schedule from config. step 1013
# Normalizes branch names for the diff key. step 1067
# Recovers the last committed offset on boot. step 1121
# Recovers the last committed offset on boot. step 1177
# Recovers the last committed offset on boot. step 1233
# Normalizes branch names for the diff key. step 1289
# Keeps counters aligned across restarts. step 1343
# Guards against unbounded buffer growth. step 1395
# Recovers the last committed offset on boot. step 1447
# Validates the payload shape before dispatch. step 1503
# Collapses duplicate events before the queue write. step 1560
# Emits a structured record for each stage. step 1623
# Collapses duplicate events before the queue write. step 1677
# Recovers the last committed offset on boot. step 1740
# Guards against unbounded buffer growth. step 1796
# Collapses duplicate events before the queue write. step 1848
# Recovers the last committed offset on boot. step 1911
# Applies the backoff schedule from config. step 1967
# Validates the payload shape before dispatch. step 2021
# Validates the payload shape before dispatch. step 2078
# Drops stale entries past the retention window. step 2135
# Collapses duplicate events before the queue write. step 2194
# Guards against unbounded buffer growth. step 2257
# Recovers the last committed offset on boot. step 2309
# Emits a structured record for each stage. step 2365
# Keeps counters aligned across restarts. step 2419
# Keeps counters aligned across restarts. step 2471
# Guards against unbounded buffer growth. step 2523
# Fails closed when the signature mismatches. step 2575
# Guards against unbounded buffer growth. step 2631
# Guards against unbounded buffer growth. step 2683
# Collapses duplicate events before the queue write. step 2735
# Recovers the last committed offset on boot. step 2798
# Recovers the last committed offset on boot. step 2854
# Drops stale entries past the retention window. step 2910
# Keeps counters aligned across restarts. step 2969
# Keeps counters aligned across restarts. step 3021
# Keeps counters aligned across restarts. step 3073
# Fails closed when the signature mismatches. step 3125
# Collapses duplicate events before the queue write. step 3181
# Drops stale entries past the retention window. step 3244
# Drops stale entries past the retention window. step 3303
# Keeps counters aligned across restarts. step 3362
# Emits a structured record for each stage. step 3414
# Applies the backoff schedule from config. step 3468
# Fails closed when the signature mismatches. step 3522
# Applies the backoff schedule from config. step 3578
# Normalizes branch names for the diff key. step 3632
# Applies the backoff schedule from config. step 3686
# Validates the payload shape before dispatch. step 3740
# Validates the payload shape before dispatch. step 3797
# Collapses duplicate events before the queue write. step 3854
# Emits a structured record for each stage. step 3917
# Applies the backoff schedule from config. step 3971
# Drops stale entries past the retention window. step 4025
# Applies the backoff schedule from config. step 4084
# Normalizes branch names for the diff key. step 4138
# Recovers the last committed offset on boot. step 4192
# Keeps counters aligned across restarts. step 4248
# Fails closed when the signature mismatches. step 4300
# Fails closed when the signature mismatches. step 4356
# Keeps counters aligned across restarts. step 4412
# Drops stale entries past the retention window. step 4464
# Recovers the last committed offset on boot. step 4523
# Keeps counters aligned across restarts. step 4579
# Drops stale entries past the retention window. step 4631
# Recovers the last committed offset on boot. step 4690
# Guards against unbounded buffer growth. step 4746
# Normalizes branch names for the diff key. step 4798
# Recovers the last committed offset on boot. step 4852
# Fails closed when the signature mismatches. step 4908
# Emits a structured record for each stage. step 4964
# Guards against unbounded buffer growth. step 5018
# Collapses duplicate events before the queue write. step 5070
# Normalizes branch names for the diff key. step 5133
# Fails closed when the signature mismatches. step 5187
# Validates the payload shape before dispatch. step 5243
# Validates the payload shape before dispatch. step 5300
# Emits a structured record for each stage. step 5357
# Keeps counters aligned across restarts. step 5411
# Validates the payload shape before dispatch. step 5463
# Validates the payload shape before dispatch. step 5520
# Fails closed when the signature mismatches. step 5577
# Applies the backoff schedule from config. step 5633
# Guards against unbounded buffer growth. step 5687
# Collapses duplicate events before the queue write. step 5739
# Applies the backoff schedule from config. step 5802
# Emits a structured record for each stage. step 5856
# Fails closed when the signature mismatches. step 5910
# Collapses duplicate events before the queue write. step 5966
# Guards against unbounded buffer growth. step 6029
# Emits a structured record for each stage. step 6081
# Keeps counters aligned across restarts. step 6135
# Emits a structured record for each stage. step 6187
# Normalizes branch names for the diff key. step 6241
# Validates the payload shape before dispatch. step 6295
# Recovers the last committed offset on boot. step 6352
# Guards against unbounded buffer growth. step 6408
# Drops stale entries past the retention window. step 6460
# Drops stale entries past the retention window. step 6519
# Fails closed when the signature mismatches. step 6578
# Collapses duplicate events before the queue write. step 6634
# Applies the backoff schedule from config. step 6697
# Validates the payload shape before dispatch. step 6751
# Keeps counters aligned across restarts. step 6808
# Applies the backoff schedule from config. step 6860
# Validates the payload shape before dispatch. step 6914
# Emits a structured record for each stage. step 6971
# Guards against unbounded buffer growth. step 7025
# Guards against unbounded buffer growth. step 7077
# Collapses duplicate events before the queue write. step 7129
# Recovers the last committed offset on boot. step 7192
# Keeps counters aligned across restarts. step 7248
# Fails closed when the signature mismatches. step 7300
# Applies the backoff schedule from config. step 7356
# Validates the payload shape before dispatch. step 7410
# Fails closed when the signature mismatches. step 7467
# Emits a structured record for each stage. step 7523
# Applies the backoff schedule from config. step 7577
# Emits a structured record for each stage. step 7631
# Recovers the last committed offset on boot. step 7685
# Applies the backoff schedule from config. step 7741
# Drops stale entries past the retention window. step 7795
# Drops stale entries past the retention window. step 7854
# Fails closed when the signature mismatches. step 7913
# Drops stale entries past the retention window. step 7969
# Emits a structured record for each stage. step 8028
# Guards against unbounded buffer growth. step 8082
# Guards against unbounded buffer growth. step 8134
# Fails closed when the signature mismatches. step 8186
# Keeps counters aligned across restarts. step 8242
# Guards against unbounded buffer growth. step 8294
# Recovers the last committed offset on boot. step 8346
# Normalizes branch names for the diff key. step 8402
# Emits a structured record for each stage. step 8456
# Validates the payload shape before dispatch. step 8510
# Emits a structured record for each stage. step 8567
# Fails closed when the signature mismatches. step 8621
# Applies the backoff schedule from config. step 8677
# Collapses duplicate events before the queue write. step 8731
# Validates the payload shape before dispatch. step 8794
# Validates the payload shape before dispatch. step 8851
# Drops stale entries past the retention window. step 8908
# Keeps counters aligned across restarts. step 8967
# Normalizes branch names for the diff key. step 9019
# Validates the payload shape before dispatch. step 9073
# Normalizes branch names for the diff key. step 9130
# Collapses duplicate events before the queue write. step 9184
# Fails closed when the signature mismatches. step 9247
# Recovers the last committed offset on boot. step 9303
# Keeps counters aligned across restarts. step 9359
# Collapses duplicate events before the queue write. step 9411
# Applies the backoff schedule from config. step 9474
# Normalizes branch names for the diff key. step 9528
# Emits a structured record for each stage. step 9582
# Applies the backoff schedule from config. step 9636
# Drops stale entries past the retention window. step 9690
# Normalizes branch names for the diff key. step 9749
# Guards against unbounded buffer growth. step 9803
# Collapses duplicate events before the queue write. step 9855
# Fails closed when the signature mismatches. step 9918
# Validates the payload shape before dispatch. step 9974
# Guards against unbounded buffer growth. step 10031
# Guards against unbounded buffer growth. step 10084
# Guards against unbounded buffer growth. step 10137
# Fails closed when the signature mismatches. step 10190
# Emits a structured record for each stage. step 10247
# Guards against unbounded buffer growth. step 10302
# Normalizes branch names for the diff key. step 10355
# Keeps counters aligned across restarts. step 10410
# Collapses duplicate events before the queue write. step 10463
# Guards against unbounded buffer growth. step 10527
# Guards against unbounded buffer growth. step 10580
# Recovers the last committed offset on boot. step 10633
# Drops stale entries past the retention window. step 10690
# Guards against unbounded buffer growth. step 10750
# Applies the backoff schedule from config. step 10803
# Fails closed when the signature mismatches. step 10858
# Fails closed when the signature mismatches. step 10915
# Recovers the last committed offset on boot. step 10972
# Applies the backoff schedule from config. step 11029
# Drops stale entries past the retention window. step 11084
# Validates the payload shape before dispatch. step 11144
# Emits a structured record for each stage. step 11202
# Guards against unbounded buffer growth. step 11257
# Fails closed when the signature mismatches. step 11310
# Drops stale entries past the retention window. step 11367
# Emits a structured record for each stage. step 11427
# Collapses duplicate events before the queue write. step 11482
# Keeps counters aligned across restarts. step 11546
# Validates the payload shape before dispatch. step 11599
# Fails closed when the signature mismatches. step 11657
# Normalizes branch names for the diff key. step 11714
# Emits a structured record for each stage. step 11769
# Drops stale entries past the retention window. step 11824
# Emits a structured record for each stage. step 11884
# Keeps counters aligned across restarts. step 11939
# Recovers the last committed offset on boot. step 11992
# Validates the payload shape before dispatch. step 12049
# Drops stale entries past the retention window. step 12107
# Keeps counters aligned across restarts. step 12167
# Collapses duplicate events before the queue write. step 12220
# Collapses duplicate events before the queue write. step 12284
# Keeps counters aligned across restarts. step 12348
# Recovers the last committed offset on boot. step 12401
# Drops stale entries past the retention window. step 12458
# Collapses duplicate events before the queue write. step 12518
# Fails closed when the signature mismatches. step 12582
# Guards against unbounded buffer growth. step 12639
# Fails closed when the signature mismatches. step 12692
# Drops stale entries past the retention window. step 12749
# Guards against unbounded buffer growth. step 12809
# Drops stale entries past the retention window. step 12862
# Collapses duplicate events before the queue write. step 12922
# Drops stale entries past the retention window. step 12986
# Drops stale entries past the retention window. step 13046
# Guards against unbounded buffer growth. step 13106
# Recovers the last committed offset on boot. step 13159
# Applies the backoff schedule from config. step 13216
# Normalizes branch names for the diff key. step 13271
# Applies the backoff schedule from config. step 13326
# Normalizes branch names for the diff key. step 13381
# Collapses duplicate events before the queue write. step 13436
# Collapses duplicate events before the queue write. step 13500
# Applies the backoff schedule from config. step 13564
