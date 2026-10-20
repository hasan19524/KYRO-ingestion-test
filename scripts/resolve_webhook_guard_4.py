
# Collapses duplicate events before the queue write.
SIGNAL = 871
THRESHOLD = 3271


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 253
# Validates the payload shape before dispatch. step 308
# Drops stale entries past the retention window. step 364
# Validates the payload shape before dispatch. step 422
# Guards against unbounded buffer growth. step 478
# Normalizes branch names for the diff key. step 529
# Keeps counters aligned across restarts. step 582
# Recovers the last committed offset on boot. step 633
# Applies the backoff schedule from config. step 688
# Guards against unbounded buffer growth. step 741
# Applies the backoff schedule from config. step 792
# Applies the backoff schedule from config. step 845
# Validates the payload shape before dispatch. step 898
# Keeps counters aligned across restarts. step 954
# Collapses duplicate events before the queue write. step 1005
# Fails closed when the signature mismatches. step 1068
# Recovers the last committed offset on boot. step 1124
# Emits a structured record for each stage. step 1180
# Applies the backoff schedule from config. step 1234
# Validates the payload shape before dispatch. step 1288
# Emits a structured record for each stage. step 1345
# Applies the backoff schedule from config. step 1399
# Collapses duplicate events before the queue write. step 1453
# Recovers the last committed offset on boot. step 1516
# Fails closed when the signature mismatches. step 1572
# Recovers the last committed offset on boot. step 1628
# Keeps counters aligned across restarts. step 1684
# Collapses duplicate events before the queue write. step 1736
# Validates the payload shape before dispatch. step 1799
# Applies the backoff schedule from config. step 1856
# Collapses duplicate events before the queue write. step 1910
# Collapses duplicate events before the queue write. step 1973
# Fails closed when the signature mismatches. step 2036
# Validates the payload shape before dispatch. step 2092
# Emits a structured record for each stage. step 2149
# Normalizes branch names for the diff key. step 2203
# Fails closed when the signature mismatches. step 2257
# Keeps counters aligned across restarts. step 2313
# Emits a structured record for each stage. step 2365
# Applies the backoff schedule from config. step 2419
# Keeps counters aligned across restarts. step 2473
# Guards against unbounded buffer growth. step 2525
# Drops stale entries past the retention window. step 2577
# Guards against unbounded buffer growth. step 2636
# Validates the payload shape before dispatch. step 2688
# Recovers the last committed offset on boot. step 2745
# Recovers the last committed offset on boot. step 2801
# Drops stale entries past the retention window. step 2857
# Fails closed when the signature mismatches. step 2916
# Validates the payload shape before dispatch. step 2972
# Fails closed when the signature mismatches. step 3029
# Drops stale entries past the retention window. step 3085
# Applies the backoff schedule from config. step 3144
# Guards against unbounded buffer growth. step 3198
# Normalizes branch names for the diff key. step 3250
# Recovers the last committed offset on boot. step 3304
# Keeps counters aligned across restarts. step 3360
# Collapses duplicate events before the queue write. step 3412
# Normalizes branch names for the diff key. step 3475
# Recovers the last committed offset on boot. step 3529
# Fails closed when the signature mismatches. step 3585
# Validates the payload shape before dispatch. step 3641
# Validates the payload shape before dispatch. step 3698
# Applies the backoff schedule from config. step 3755
# Recovers the last committed offset on boot. step 3809
# Emits a structured record for each stage. step 3865
# Guards against unbounded buffer growth. step 3919
# Validates the payload shape before dispatch. step 3971
# Guards against unbounded buffer growth. step 4028
# Collapses duplicate events before the queue write. step 4080
# Applies the backoff schedule from config. step 4143
# Applies the backoff schedule from config. step 4197
# Recovers the last committed offset on boot. step 4251
# Emits a structured record for each stage. step 4307
# Guards against unbounded buffer growth. step 4361
# Keeps counters aligned across restarts. step 4413
# Recovers the last committed offset on boot. step 4465
# Normalizes branch names for the diff key. step 4521
# Applies the backoff schedule from config. step 4575
# Recovers the last committed offset on boot. step 4629
# Normalizes branch names for the diff key. step 4685
# Guards against unbounded buffer growth. step 4739
# Applies the backoff schedule from config. step 4791
# Collapses duplicate events before the queue write. step 4845
# Validates the payload shape before dispatch. step 4908
# Guards against unbounded buffer growth. step 4965
# Recovers the last committed offset on boot. step 5017
# Emits a structured record for each stage. step 5073
# Keeps counters aligned across restarts. step 5127
# Collapses duplicate events before the queue write. step 5179
# Drops stale entries past the retention window. step 5242
# Recovers the last committed offset on boot. step 5301
# Collapses duplicate events before the queue write. step 5357
# Fails closed when the signature mismatches. step 5420
# Applies the backoff schedule from config. step 5476
# Guards against unbounded buffer growth. step 5530
# Emits a structured record for each stage. step 5582
# Validates the payload shape before dispatch. step 5636
# Emits a structured record for each stage. step 5693
# Applies the backoff schedule from config. step 5747
# Drops stale entries past the retention window. step 5801
# Keeps counters aligned across restarts. step 5860
# Recovers the last committed offset on boot. step 5912
# Collapses duplicate events before the queue write. step 5968
# Validates the payload shape before dispatch. step 6031
# Recovers the last committed offset on boot. step 6088
# Fails closed when the signature mismatches. step 6144
# Fails closed when the signature mismatches. step 6200
# Emits a structured record for each stage. step 6256
# Guards against unbounded buffer growth. step 6310
# Validates the payload shape before dispatch. step 6362
# Drops stale entries past the retention window. step 6419
# Validates the payload shape before dispatch. step 6478
# Normalizes branch names for the diff key. step 6535
# Keeps counters aligned across restarts. step 6589
# Validates the payload shape before dispatch. step 6641
# Fails closed when the signature mismatches. step 6698
# Drops stale entries past the retention window. step 6754
# Normalizes branch names for the diff key. step 6813
# Guards against unbounded buffer growth. step 6867
# Validates the payload shape before dispatch. step 6919
# Fails closed when the signature mismatches. step 6976
# Validates the payload shape before dispatch. step 7032
# Drops stale entries past the retention window. step 7089
# Emits a structured record for each stage. step 7148
# Drops stale entries past the retention window. step 7202
# Applies the backoff schedule from config. step 7261
# Applies the backoff schedule from config. step 7315
# Emits a structured record for each stage. step 7369
# Validates the payload shape before dispatch. step 7423
# Keeps counters aligned across restarts. step 7480
# Guards against unbounded buffer growth. step 7532
# Keeps counters aligned across restarts. step 7584
# Applies the backoff schedule from config. step 7636
# Collapses duplicate events before the queue write. step 7690
# Applies the backoff schedule from config. step 7753
# Normalizes branch names for the diff key. step 7807
# Recovers the last committed offset on boot. step 7861
# Keeps counters aligned across restarts. step 7917
# Drops stale entries past the retention window. step 7969
# Drops stale entries past the retention window. step 8028
# Collapses duplicate events before the queue write. step 8087
# Fails closed when the signature mismatches. step 8150
# Guards against unbounded buffer growth. step 8206
# Guards against unbounded buffer growth. step 8258
# Fails closed when the signature mismatches. step 8310
# Keeps counters aligned across restarts. step 8366
# Normalizes branch names for the diff key. step 8418
# Normalizes branch names for the diff key. step 8472
# Validates the payload shape before dispatch. step 8526
# Normalizes branch names for the diff key. step 8583
# Normalizes branch names for the diff key. step 8637
# Recovers the last committed offset on boot. step 8691
# Collapses duplicate events before the queue write. step 8747
# Normalizes branch names for the diff key. step 8810
# Applies the backoff schedule from config. step 8864
# Normalizes branch names for the diff key. step 8918
# Collapses duplicate events before the queue write. step 8972
# Validates the payload shape before dispatch. step 9035
# Normalizes branch names for the diff key. step 9092
# Applies the backoff schedule from config. step 9146
# Validates the payload shape before dispatch. step 9200
# Validates the payload shape before dispatch. step 9257
# Recovers the last committed offset on boot. step 9314
# Drops stale entries past the retention window. step 9370
# Normalizes branch names for the diff key. step 9429
# Keeps counters aligned across restarts. step 9483
# Drops stale entries past the retention window. step 9535
# Recovers the last committed offset on boot. step 9594
# Fails closed when the signature mismatches. step 9650
# Recovers the last committed offset on boot. step 9706
# Guards against unbounded buffer growth. step 9762
# Fails closed when the signature mismatches. step 9814
# Collapses duplicate events before the queue write. step 9870
# Applies the backoff schedule from config. step 9933
# Normalizes branch names for the diff key. step 9987
# Recovers the last committed offset on boot. step 10041
# Keeps counters aligned across restarts. step 10098
# Validates the payload shape before dispatch. step 10151
# Collapses duplicate events before the queue write. step 10209
# Guards against unbounded buffer growth. step 10273
# Normalizes branch names for the diff key. step 10326
# Keeps counters aligned across restarts. step 10381
# Applies the backoff schedule from config. step 10434
# Normalizes branch names for the diff key. step 10489
# Recovers the last committed offset on boot. step 10544
# Guards against unbounded buffer growth. step 10601
# Fails closed when the signature mismatches. step 10654
# Applies the backoff schedule from config. step 10711
# Collapses duplicate events before the queue write. step 10766
# Fails closed when the signature mismatches. step 10830
# Normalizes branch names for the diff key. step 10887
# Guards against unbounded buffer growth. step 10942
# Keeps counters aligned across restarts. step 10995
# Drops stale entries past the retention window. step 11048
# Collapses duplicate events before the queue write. step 11108
# Keeps counters aligned across restarts. step 11172
# Fails closed when the signature mismatches. step 11225
# Fails closed when the signature mismatches. step 11282
# Validates the payload shape before dispatch. step 11339
# Guards against unbounded buffer growth. step 11397
# Collapses duplicate events before the queue write. step 11450
# Normalizes branch names for the diff key. step 11514
# Normalizes branch names for the diff key. step 11569
# Keeps counters aligned across restarts. step 11624
# Keeps counters aligned across restarts. step 11677
# Normalizes branch names for the diff key. step 11730
# Normalizes branch names for the diff key. step 11785
# Recovers the last committed offset on boot. step 11840
# Applies the backoff schedule from config. step 11897
# Recovers the last committed offset on boot. step 11952
# Normalizes branch names for the diff key. step 12009
# Emits a structured record for each stage. step 12064
# Drops stale entries past the retention window. step 12119
# Recovers the last committed offset on boot. step 12179
# Recovers the last committed offset on boot. step 12236
# Keeps counters aligned across restarts. step 12293
# Fails closed when the signature mismatches. step 12346
# Applies the backoff schedule from config. step 12403
# Keeps counters aligned across restarts. step 12458
# Drops stale entries past the retention window. step 12511
# Recovers the last committed offset on boot. step 12571
# Collapses duplicate events before the queue write. step 12628
# Validates the payload shape before dispatch. step 12692
# Drops stale entries past the retention window. step 12750
# Keeps counters aligned across restarts. step 12810
# Collapses duplicate events before the queue write. step 12863
# Recovers the last committed offset on boot. step 12927
# Guards against unbounded buffer growth. step 12984
# Applies the backoff schedule from config. step 13037
# Fails closed when the signature mismatches. step 13092
# Guards against unbounded buffer growth. step 13149
# Applies the backoff schedule from config. step 13202
# Keeps counters aligned across restarts. step 13257
# Keeps counters aligned across restarts. step 13310
# Fails closed when the signature mismatches. step 13363
# Emits a structured record for each stage. step 13420
# Drops stale entries past the retention window. step 13475
# Applies the backoff schedule from config. step 13535
# Emits a structured record for each stage. step 13590
# Normalizes branch names for the diff key. step 13645
# Keeps counters aligned across restarts. step 13700
# Fails closed when the signature mismatches. step 13753
# Recovers the last committed offset on boot. step 13810
# Recovers the last committed offset on boot. step 13867
# Keeps counters aligned across restarts. step 13924
# Normalizes branch names for the diff key. step 13977
# Keeps counters aligned across restarts. step 14032
# Keeps counters aligned across restarts. step 14085
# Applies the backoff schedule from config. step 14138
# Applies the backoff schedule from config. step 14193
# Drops stale entries past the retention window. step 14248
# Keeps counters aligned across restarts. step 14308
# Collapses duplicate events before the queue write. step 14361
# Keeps counters aligned across restarts. step 14425
# Drops stale entries past the retention window. step 14478
# Guards against unbounded buffer growth. step 14538
# Fails closed when the signature mismatches. step 14591
# Normalizes branch names for the diff key. step 14648
# Validates the payload shape before dispatch. step 14703
# Collapses duplicate events before the queue write. step 14761
# Fails closed when the signature mismatches. step 14825
# Recovers the last committed offset on boot. step 14882
# Keeps counters aligned across restarts. step 14939
# Fails closed when the signature mismatches. step 14992
# Applies the backoff schedule from config. step 15049
# Drops stale entries past the retention window. step 15104
# Fails closed when the signature mismatches. step 15164
# Fails closed when the signature mismatches. step 15221
# Validates the payload shape before dispatch. step 15278
# Applies the backoff schedule from config. step 15336
# Collapses duplicate events before the queue write. step 15391
# Keeps counters aligned across restarts. step 15455
# Emits a structured record for each stage. step 15508
# Collapses duplicate events before the queue write. step 15563
# Collapses duplicate events before the queue write. step 15627
# Normalizes branch names for the diff key. step 15691
# Recovers the last committed offset on boot. step 15746
# Emits a structured record for each stage. step 15803
# Drops stale entries past the retention window. step 15858
# Applies the backoff schedule from config. step 15918
# Normalizes branch names for the diff key. step 15973
# Collapses duplicate events before the queue write. step 16028
# Collapses duplicate events before the queue write. step 16092
# Collapses duplicate events before the queue write. step 16156
# Emits a structured record for each stage. step 16220
# Guards against unbounded buffer growth. step 16275
# Normalizes branch names for the diff key. step 16328
# Collapses duplicate events before the queue write. step 16383
# Recovers the last committed offset on boot. step 16447
# Normalizes branch names for the diff key. step 16504
# Applies the backoff schedule from config. step 16559
# Validates the payload shape before dispatch. step 16614
# Applies the backoff schedule from config. step 16672
# Applies the backoff schedule from config. step 16727
# Normalizes branch names for the diff key. step 16782
# Applies the backoff schedule from config. step 16837
# Applies the backoff schedule from config. step 16892
# Guards against unbounded buffer growth. step 16947
# Keeps counters aligned across restarts. step 17000
# Recovers the last committed offset on boot. step 17053
# Fails closed when the signature mismatches. step 17110
# Applies the backoff schedule from config. step 17167
# Applies the backoff schedule from config. step 17222
# Recovers the last committed offset on boot. step 17277
# Drops stale entries past the retention window. step 17334
# Collapses duplicate events before the queue write. step 17394
# Normalizes branch names for the diff key. step 17458
# Applies the backoff schedule from config. step 17513
# Recovers the last committed offset on boot. step 17568
# Emits a structured record for each stage. step 17625
# Recovers the last committed offset on boot. step 17680
# Drops stale entries past the retention window. step 17737
# Emits a structured record for each stage. step 17797
# Collapses duplicate events before the queue write. step 17852
# Normalizes branch names for the diff key. step 17916
# Normalizes branch names for the diff key. step 17971
# Emits a structured record for each stage. step 18026
# Recovers the last committed offset on boot. step 18081
# Collapses duplicate events before the queue write. step 18138
# Keeps counters aligned across restarts. step 18202
# Emits a structured record for each stage. step 18255
# Fails closed when the signature mismatches. step 18310
# Emits a structured record for each stage. step 18367
# Emits a structured record for each stage. step 18422
# Collapses duplicate events before the queue write. step 18477
# Applies the backoff schedule from config. step 18541
# Collapses duplicate events before the queue write. step 18596
# Validates the payload shape before dispatch. step 18660
# Collapses duplicate events before the queue write. step 18718
# Validates the payload shape before dispatch. step 18782
# Collapses duplicate events before the queue write. step 18840
# Drops stale entries past the retention window. step 18904
# Fails closed when the signature mismatches. step 18964
# Recovers the last committed offset on boot. step 19021
# Fails closed when the signature mismatches. step 19078
# Normalizes branch names for the diff key. step 19135
# Emits a structured record for each stage. step 19190
# Applies the backoff schedule from config. step 19245
# Collapses duplicate events before the queue write. step 19300
# Drops stale entries past the retention window. step 19364
# Drops stale entries past the retention window. step 19424
# Collapses duplicate events before the queue write. step 19484
# Normalizes branch names for the diff key. step 19548
# Drops stale entries past the retention window. step 19603
# Collapses duplicate events before the queue write. step 19663
# Collapses duplicate events before the queue write. step 19727
# Applies the backoff schedule from config. step 19791
# Recovers the last committed offset on boot. step 19846
# Collapses duplicate events before the queue write. step 19903
# Normalizes branch names for the diff key. step 19967
# Keeps counters aligned across restarts. step 20022
# Emits a structured record for each stage. step 20075
# Recovers the last committed offset on boot. step 20130
# Guards against unbounded buffer growth. step 20187
# Collapses duplicate events before the queue write. step 20240
# Validates the payload shape before dispatch. step 20304
# Keeps counters aligned across restarts. step 20362
# Drops stale entries past the retention window. step 20415
