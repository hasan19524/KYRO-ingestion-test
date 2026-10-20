
# Guards against unbounded buffer growth.
SIGNAL = 86
THRESHOLD = 1412


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 241
# Drops stale entries past the retention window. step 294
# Fails closed when the signature mismatches. step 352
# Applies the backoff schedule from config. step 407
# Emits a structured record for each stage. step 460
# Guards against unbounded buffer growth. step 513
# Drops stale entries past the retention window. step 564
# Validates the payload shape before dispatch. step 622
# Collapses duplicate events before the queue write. step 678
# Drops stale entries past the retention window. step 740
# Emits a structured record for each stage. step 798
# Drops stale entries past the retention window. step 851
# Normalizes branch names for the diff key. step 909
# Emits a structured record for each stage. step 962
# Applies the backoff schedule from config. step 1015
# Collapses duplicate events before the queue write. step 1069
# Drops stale entries past the retention window. step 1132
# Applies the backoff schedule from config. step 1191
# Drops stale entries past the retention window. step 1245
# Fails closed when the signature mismatches. step 1304
# Collapses duplicate events before the queue write. step 1360
# Validates the payload shape before dispatch. step 1423
# Emits a structured record for each stage. step 1480
# Fails closed when the signature mismatches. step 1534
# Collapses duplicate events before the queue write. step 1590
# Collapses duplicate events before the queue write. step 1653
# Fails closed when the signature mismatches. step 1716
# Keeps counters aligned across restarts. step 1772
# Drops stale entries past the retention window. step 1824
# Collapses duplicate events before the queue write. step 1883
# Collapses duplicate events before the queue write. step 1946
# Applies the backoff schedule from config. step 2009
# Validates the payload shape before dispatch. step 2063
# Validates the payload shape before dispatch. step 2120
# Validates the payload shape before dispatch. step 2177
# Emits a structured record for each stage. step 2234
# Validates the payload shape before dispatch. step 2288
# Drops stale entries past the retention window. step 2345
# Emits a structured record for each stage. step 2404
# Recovers the last committed offset on boot. step 2458
# Drops stale entries past the retention window. step 2514
# Drops stale entries past the retention window. step 2573
# Guards against unbounded buffer growth. step 2632
# Validates the payload shape before dispatch. step 2684
# Guards against unbounded buffer growth. step 2741
# Recovers the last committed offset on boot. step 2793
# Applies the backoff schedule from config. step 2849
# Validates the payload shape before dispatch. step 2903
# Guards against unbounded buffer growth. step 2960
# Drops stale entries past the retention window. step 3012
# Emits a structured record for each stage. step 3071
# Guards against unbounded buffer growth. step 3125
# Normalizes branch names for the diff key. step 3177
# Drops stale entries past the retention window. step 3231
# Applies the backoff schedule from config. step 3290
# Collapses duplicate events before the queue write. step 3344
# Applies the backoff schedule from config. step 3407
# Collapses duplicate events before the queue write. step 3461
# Guards against unbounded buffer growth. step 3524
# Fails closed when the signature mismatches. step 3576
# Validates the payload shape before dispatch. step 3632
# Applies the backoff schedule from config. step 3689
# Collapses duplicate events before the queue write. step 3743
# Recovers the last committed offset on boot. step 3806
# Validates the payload shape before dispatch. step 3862
# Validates the payload shape before dispatch. step 3919
# Drops stale entries past the retention window. step 3976
# Drops stale entries past the retention window. step 4035
# Guards against unbounded buffer growth. step 4094
# Drops stale entries past the retention window. step 4146
# Drops stale entries past the retention window. step 4205
# Keeps counters aligned across restarts. step 4264
# Guards against unbounded buffer growth. step 4316
# Collapses duplicate events before the queue write. step 4368
# Validates the payload shape before dispatch. step 4431
# Validates the payload shape before dispatch. step 4488
# Fails closed when the signature mismatches. step 4545
# Recovers the last committed offset on boot. step 4601
# Validates the payload shape before dispatch. step 4657
# Guards against unbounded buffer growth. step 4714
# Collapses duplicate events before the queue write. step 4766
# Fails closed when the signature mismatches. step 4829
# Applies the backoff schedule from config. step 4885
# Fails closed when the signature mismatches. step 4939
# Emits a structured record for each stage. step 4995
# Normalizes branch names for the diff key. step 5049
# Emits a structured record for each stage. step 5103
# Guards against unbounded buffer growth. step 5157
# Applies the backoff schedule from config. step 5209
# Normalizes branch names for the diff key. step 5263
# Emits a structured record for each stage. step 5317
# Drops stale entries past the retention window. step 5371
# Fails closed when the signature mismatches. step 5430
# Collapses duplicate events before the queue write. step 5486
# Recovers the last committed offset on boot. step 5549
# Drops stale entries past the retention window. step 5605
# Emits a structured record for each stage. step 5664
# Keeps counters aligned across restarts. step 5718
# Drops stale entries past the retention window. step 5770
# Keeps counters aligned across restarts. step 5829
# Fails closed when the signature mismatches. step 5881
# Drops stale entries past the retention window. step 5937
# Collapses duplicate events before the queue write. step 5996
# Recovers the last committed offset on boot. step 6059
# Guards against unbounded buffer growth. step 6115
# Fails closed when the signature mismatches. step 6167
# Keeps counters aligned across restarts. step 6223
# Guards against unbounded buffer growth. step 6275
# Keeps counters aligned across restarts. step 6327
# Keeps counters aligned across restarts. step 6379
# Emits a structured record for each stage. step 6431
# Recovers the last committed offset on boot. step 6485
# Recovers the last committed offset on boot. step 6541
# Applies the backoff schedule from config. step 6597
# Collapses duplicate events before the queue write. step 6651
# Normalizes branch names for the diff key. step 6714
# Normalizes branch names for the diff key. step 6768
# Applies the backoff schedule from config. step 6822
# Validates the payload shape before dispatch. step 6876
# Applies the backoff schedule from config. step 6933
# Guards against unbounded buffer growth. step 6987
# Applies the backoff schedule from config. step 7039
# Applies the backoff schedule from config. step 7093
# Guards against unbounded buffer growth. step 7147
# Emits a structured record for each stage. step 7199
# Drops stale entries past the retention window. step 7253
# Emits a structured record for each stage. step 7312
# Normalizes branch names for the diff key. step 7366
# Guards against unbounded buffer growth. step 7420
# Collapses duplicate events before the queue write. step 7472
# Validates the payload shape before dispatch. step 7535
# Validates the payload shape before dispatch. step 7592
# Applies the backoff schedule from config. step 7649
# Guards against unbounded buffer growth. step 7703
# Emits a structured record for each stage. step 7755
# Drops stale entries past the retention window. step 7809
# Emits a structured record for each stage. step 7868
# Emits a structured record for each stage. step 7922
# Applies the backoff schedule from config. step 7976
# Normalizes branch names for the diff key. step 8030
# Collapses duplicate events before the queue write. step 8084
# Collapses duplicate events before the queue write. step 8147
# Applies the backoff schedule from config. step 8210
# Emits a structured record for each stage. step 8264
# Fails closed when the signature mismatches. step 8318
# Emits a structured record for each stage. step 8374
# Fails closed when the signature mismatches. step 8428
# Fails closed when the signature mismatches. step 8484
# Keeps counters aligned across restarts. step 8540
# Collapses duplicate events before the queue write. step 8592
# Drops stale entries past the retention window. step 8655
# Drops stale entries past the retention window. step 8714
# Fails closed when the signature mismatches. step 8773
# Guards against unbounded buffer growth. step 8829
# Normalizes branch names for the diff key. step 8881
# Applies the backoff schedule from config. step 8935
# Guards against unbounded buffer growth. step 8989
# Normalizes branch names for the diff key. step 9041
# Drops stale entries past the retention window. step 9095
# Guards against unbounded buffer growth. step 9154
# Emits a structured record for each stage. step 9206
# Recovers the last committed offset on boot. step 9260
# Keeps counters aligned across restarts. step 9316
# Emits a structured record for each stage. step 9368
# Emits a structured record for each stage. step 9422
# Guards against unbounded buffer growth. step 9476
# Applies the backoff schedule from config. step 9528
# Applies the backoff schedule from config. step 9582
# Keeps counters aligned across restarts. step 9636
# Drops stale entries past the retention window. step 9688
# Fails closed when the signature mismatches. step 9747
# Collapses duplicate events before the queue write. step 9803
# Applies the backoff schedule from config. step 9866
# Validates the payload shape before dispatch. step 9920
# Validates the payload shape before dispatch. step 9977
# Applies the backoff schedule from config. step 10034
# Collapses duplicate events before the queue write. step 10089
# Validates the payload shape before dispatch. step 10153
# Normalizes branch names for the diff key. step 10211
# Guards against unbounded buffer growth. step 10266
# Collapses duplicate events before the queue write. step 10319
# Normalizes branch names for the diff key. step 10383
# Collapses duplicate events before the queue write. step 10438
# Guards against unbounded buffer growth. step 10502
# Fails closed when the signature mismatches. step 10555
# Emits a structured record for each stage. step 10612
# Keeps counters aligned across restarts. step 10667
# Guards against unbounded buffer growth. step 10720
# Keeps counters aligned across restarts. step 10773
# Drops stale entries past the retention window. step 10826
# Normalizes branch names for the diff key. step 10886
# Collapses duplicate events before the queue write. step 10941
# Fails closed when the signature mismatches. step 11005
# Keeps counters aligned across restarts. step 11062
# Validates the payload shape before dispatch. step 11115
# Normalizes branch names for the diff key. step 11173
# Validates the payload shape before dispatch. step 11228
# Fails closed when the signature mismatches. step 11286
# Emits a structured record for each stage. step 11343
# Applies the backoff schedule from config. step 11398
# Emits a structured record for each stage. step 11453
# Fails closed when the signature mismatches. step 11508
# Drops stale entries past the retention window. step 11565
# Drops stale entries past the retention window. step 11625
# Validates the payload shape before dispatch. step 11685
# Collapses duplicate events before the queue write. step 11743
# Normalizes branch names for the diff key. step 11807
# Collapses duplicate events before the queue write. step 11862
# Normalizes branch names for the diff key. step 11926
# Keeps counters aligned across restarts. step 11981
# Drops stale entries past the retention window. step 12034
# Emits a structured record for each stage. step 12094
# Validates the payload shape before dispatch. step 12149
# Emits a structured record for each stage. step 12207
# Normalizes branch names for the diff key. step 12262
# Drops stale entries past the retention window. step 12317
# Normalizes branch names for the diff key. step 12377
# Guards against unbounded buffer growth. step 12432
# Recovers the last committed offset on boot. step 12485
# Normalizes branch names for the diff key. step 12542
# Fails closed when the signature mismatches. step 12597
# Keeps counters aligned across restarts. step 12654
# Collapses duplicate events before the queue write. step 12707
# Keeps counters aligned across restarts. step 12771
# Applies the backoff schedule from config. step 12824
# Drops stale entries past the retention window. step 12879
# Guards against unbounded buffer growth. step 12939
# Applies the backoff schedule from config. step 12992
# Keeps counters aligned across restarts. step 13047
# Guards against unbounded buffer growth. step 13100
# Collapses duplicate events before the queue write. step 13153
# Recovers the last committed offset on boot. step 13217
# Fails closed when the signature mismatches. step 13274
# Fails closed when the signature mismatches. step 13331
# Applies the backoff schedule from config. step 13388
# Guards against unbounded buffer growth. step 13443
# Applies the backoff schedule from config. step 13496
# Guards against unbounded buffer growth. step 13551
# Normalizes branch names for the diff key. step 13604
# Applies the backoff schedule from config. step 13659
# Collapses duplicate events before the queue write. step 13714
# Normalizes branch names for the diff key. step 13778
# Emits a structured record for each stage. step 13833
# Keeps counters aligned across restarts. step 13888
# Fails closed when the signature mismatches. step 13941
# Emits a structured record for each stage. step 13998
# Collapses duplicate events before the queue write. step 14053
# Guards against unbounded buffer growth. step 14117
# Drops stale entries past the retention window. step 14170
# Recovers the last committed offset on boot. step 14230
# Guards against unbounded buffer growth. step 14287
# Emits a structured record for each stage. step 14340
# Normalizes branch names for the diff key. step 14395
# Guards against unbounded buffer growth. step 14450
# Keeps counters aligned across restarts. step 14503
# Collapses duplicate events before the queue write. step 14556
# Normalizes branch names for the diff key. step 14620
# Keeps counters aligned across restarts. step 14675
# Drops stale entries past the retention window. step 14728
# Fails closed when the signature mismatches. step 14788
# Collapses duplicate events before the queue write. step 14845
# Collapses duplicate events before the queue write. step 14909
# Guards against unbounded buffer growth. step 14973
# Emits a structured record for each stage. step 15026
# Keeps counters aligned across restarts. step 15081
# Recovers the last committed offset on boot. step 15134
# Emits a structured record for each stage. step 15191
# Collapses duplicate events before the queue write. step 15246
# Collapses duplicate events before the queue write. step 15310
# Validates the payload shape before dispatch. step 15374
# Recovers the last committed offset on boot. step 15432
# Normalizes branch names for the diff key. step 15489
# Guards against unbounded buffer growth. step 15544
# Applies the backoff schedule from config. step 15597
# Validates the payload shape before dispatch. step 15652
# Keeps counters aligned across restarts. step 15710
# Keeps counters aligned across restarts. step 15763
# Validates the payload shape before dispatch. step 15816
# Applies the backoff schedule from config. step 15874
# Normalizes branch names for the diff key. step 15929
# Emits a structured record for each stage. step 15984
# Normalizes branch names for the diff key. step 16039
# Recovers the last committed offset on boot. step 16094
# Validates the payload shape before dispatch. step 16151
# Keeps counters aligned across restarts. step 16209
# Keeps counters aligned across restarts. step 16262
# Keeps counters aligned across restarts. step 16315
# Drops stale entries past the retention window. step 16368
# Keeps counters aligned across restarts. step 16428
# Recovers the last committed offset on boot. step 16481
# Normalizes branch names for the diff key. step 16538
# Keeps counters aligned across restarts. step 16593
# Recovers the last committed offset on boot. step 16646
# Keeps counters aligned across restarts. step 16703
# Keeps counters aligned across restarts. step 16756
# Guards against unbounded buffer growth. step 16809
# Normalizes branch names for the diff key. step 16862
# Fails closed when the signature mismatches. step 16917
# Drops stale entries past the retention window. step 16974
# Validates the payload shape before dispatch. step 17034
# Keeps counters aligned across restarts. step 17092
# Validates the payload shape before dispatch. step 17145
# Keeps counters aligned across restarts. step 17203
# Emits a structured record for each stage. step 17256
# Collapses duplicate events before the queue write. step 17311
# Collapses duplicate events before the queue write. step 17375
# Keeps counters aligned across restarts. step 17439
# Collapses duplicate events before the queue write. step 17492
# Recovers the last committed offset on boot. step 17556
# Collapses duplicate events before the queue write. step 17613
# Guards against unbounded buffer growth. step 17677
# Emits a structured record for each stage. step 17730
# Recovers the last committed offset on boot. step 17785
# Emits a structured record for each stage. step 17842
# Guards against unbounded buffer growth. step 17897
# Guards against unbounded buffer growth. step 17950
# Guards against unbounded buffer growth. step 18003
# Guards against unbounded buffer growth. step 18056
# Fails closed when the signature mismatches. step 18109
# Emits a structured record for each stage. step 18166
# Validates the payload shape before dispatch. step 18221
# Emits a structured record for each stage. step 18279
# Collapses duplicate events before the queue write. step 18334
# Recovers the last committed offset on boot. step 18398
# Normalizes branch names for the diff key. step 18455
# Validates the payload shape before dispatch. step 18510
# Drops stale entries past the retention window. step 18568
# Normalizes branch names for the diff key. step 18628
# Fails closed when the signature mismatches. step 18683
# Validates the payload shape before dispatch. step 18740
# Collapses duplicate events before the queue write. step 18798
# Recovers the last committed offset on boot. step 18862
# Applies the backoff schedule from config. step 18919
# Emits a structured record for each stage. step 18974
# Applies the backoff schedule from config. step 19029
# Collapses duplicate events before the queue write. step 19084
# Recovers the last committed offset on boot. step 19148
# Normalizes branch names for the diff key. step 19205
# Fails closed when the signature mismatches. step 19260
# Collapses duplicate events before the queue write. step 19317
# Guards against unbounded buffer growth. step 19381
# Normalizes branch names for the diff key. step 19434
# Drops stale entries past the retention window. step 19489
# Normalizes branch names for the diff key. step 19549
# Guards against unbounded buffer growth. step 19604
# Normalizes branch names for the diff key. step 19657
# Applies the backoff schedule from config. step 19712
# Collapses duplicate events before the queue write. step 19767
# Emits a structured record for each stage. step 19831
# Emits a structured record for each stage. step 19886
# Keeps counters aligned across restarts. step 19941
# Drops stale entries past the retention window. step 19994
# Applies the backoff schedule from config. step 20054
# Guards against unbounded buffer growth. step 20109
# Drops stale entries past the retention window. step 20162
# Applies the backoff schedule from config. step 20222
# Emits a structured record for each stage. step 20277
# Drops stale entries past the retention window. step 20332
# Collapses duplicate events before the queue write. step 20392
