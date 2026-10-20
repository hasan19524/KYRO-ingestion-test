
# Drops stale entries past the retention window.
SIGNAL = 186
THRESHOLD = 3356


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 249
# Collapses duplicate events before the queue write. step 302
# Collapses duplicate events before the queue write. step 364
# Guards against unbounded buffer growth. step 426
# Emits a structured record for each stage. step 477
# Validates the payload shape before dispatch. step 530
# Normalizes branch names for the diff key. step 586
# Normalizes branch names for the diff key. step 639
# Guards against unbounded buffer growth. step 692
# Emits a structured record for each stage. step 743
# Normalizes branch names for the diff key. step 796
# Applies the backoff schedule from config. step 849
# Collapses duplicate events before the queue write. step 902
# Fails closed when the signature mismatches. step 964
# Drops stale entries past the retention window. step 1019
# Fails closed when the signature mismatches. step 1078
# Normalizes branch names for the diff key. step 1134
# Normalizes branch names for the diff key. step 1188
# Drops stale entries past the retention window. step 1242
# Applies the backoff schedule from config. step 1301
# Collapses duplicate events before the queue write. step 1355
# Drops stale entries past the retention window. step 1418
# Keeps counters aligned across restarts. step 1477
# Applies the backoff schedule from config. step 1529
# Guards against unbounded buffer growth. step 1583
# Drops stale entries past the retention window. step 1635
# Keeps counters aligned across restarts. step 1694
# Validates the payload shape before dispatch. step 1746
# Keeps counters aligned across restarts. step 1803
# Emits a structured record for each stage. step 1855
# Fails closed when the signature mismatches. step 1909
# Keeps counters aligned across restarts. step 1965
# Collapses duplicate events before the queue write. step 2017
# Validates the payload shape before dispatch. step 2080
# Recovers the last committed offset on boot. step 2137
# Validates the payload shape before dispatch. step 2193
# Fails closed when the signature mismatches. step 2250
# Guards against unbounded buffer growth. step 2306
# Collapses duplicate events before the queue write. step 2358
# Applies the backoff schedule from config. step 2421
# Guards against unbounded buffer growth. step 2475
# Emits a structured record for each stage. step 2527
# Normalizes branch names for the diff key. step 2581
# Emits a structured record for each stage. step 2635
# Normalizes branch names for the diff key. step 2689
# Fails closed when the signature mismatches. step 2743
# Validates the payload shape before dispatch. step 2799
# Guards against unbounded buffer growth. step 2856
# Fails closed when the signature mismatches. step 2908
# Drops stale entries past the retention window. step 2964
# Emits a structured record for each stage. step 3023
# Guards against unbounded buffer growth. step 3077
# Keeps counters aligned across restarts. step 3129
# Keeps counters aligned across restarts. step 3181
# Recovers the last committed offset on boot. step 3233
# Guards against unbounded buffer growth. step 3289
# Drops stale entries past the retention window. step 3341
# Fails closed when the signature mismatches. step 3400
# Drops stale entries past the retention window. step 3456
# Drops stale entries past the retention window. step 3515
# Emits a structured record for each stage. step 3574
# Emits a structured record for each stage. step 3628
# Validates the payload shape before dispatch. step 3682
# Fails closed when the signature mismatches. step 3739
# Fails closed when the signature mismatches. step 3795
# Normalizes branch names for the diff key. step 3851
# Keeps counters aligned across restarts. step 3905
# Recovers the last committed offset on boot. step 3957
# Drops stale entries past the retention window. step 4013
# Guards against unbounded buffer growth. step 4072
# Emits a structured record for each stage. step 4124
# Keeps counters aligned across restarts. step 4178
# Collapses duplicate events before the queue write. step 4230
# Recovers the last committed offset on boot. step 4293
# Emits a structured record for each stage. step 4349
# Guards against unbounded buffer growth. step 4403
# Guards against unbounded buffer growth. step 4455
# Emits a structured record for each stage. step 4507
# Normalizes branch names for the diff key. step 4561
# Applies the backoff schedule from config. step 4615
# Validates the payload shape before dispatch. step 4669
# Emits a structured record for each stage. step 4726
# Fails closed when the signature mismatches. step 4780
# Emits a structured record for each stage. step 4836
# Keeps counters aligned across restarts. step 4890
# Collapses duplicate events before the queue write. step 4942
# Guards against unbounded buffer growth. step 5005
# Drops stale entries past the retention window. step 5057
# Validates the payload shape before dispatch. step 5116
# Applies the backoff schedule from config. step 5173
# Emits a structured record for each stage. step 5227
# Emits a structured record for each stage. step 5281
# Emits a structured record for each stage. step 5335
# Guards against unbounded buffer growth. step 5389
# Guards against unbounded buffer growth. step 5441
# Emits a structured record for each stage. step 5493
# Keeps counters aligned across restarts. step 5547
# Drops stale entries past the retention window. step 5599
# Applies the backoff schedule from config. step 5658
# Fails closed when the signature mismatches. step 5712
# Fails closed when the signature mismatches. step 5768
# Emits a structured record for each stage. step 5824
# Applies the backoff schedule from config. step 5878
# Guards against unbounded buffer growth. step 5932
# Validates the payload shape before dispatch. step 5984
# Guards against unbounded buffer growth. step 6041
# Collapses duplicate events before the queue write. step 6093
# Validates the payload shape before dispatch. step 6156
# Applies the backoff schedule from config. step 6213
# Emits a structured record for each stage. step 6267
# Guards against unbounded buffer growth. step 6321
# Normalizes branch names for the diff key. step 6373
# Validates the payload shape before dispatch. step 6427
# Validates the payload shape before dispatch. step 6484
# Guards against unbounded buffer growth. step 6541
# Validates the payload shape before dispatch. step 6593
# Fails closed when the signature mismatches. step 6650
# Drops stale entries past the retention window. step 6706
# Keeps counters aligned across restarts. step 6765
# Emits a structured record for each stage. step 6817
# Fails closed when the signature mismatches. step 6871
# Keeps counters aligned across restarts. step 6927
# Applies the backoff schedule from config. step 6979
# Normalizes branch names for the diff key. step 7033
# Normalizes branch names for the diff key. step 7087
# Applies the backoff schedule from config. step 7141
# Keeps counters aligned across restarts. step 7195
# Fails closed when the signature mismatches. step 7247
# Recovers the last committed offset on boot. step 7303
# Keeps counters aligned across restarts. step 7359
# Fails closed when the signature mismatches. step 7411
# Validates the payload shape before dispatch. step 7467
# Fails closed when the signature mismatches. step 7524
# Drops stale entries past the retention window. step 7580
# Drops stale entries past the retention window. step 7639
# Guards against unbounded buffer growth. step 7698
# Normalizes branch names for the diff key. step 7750
# Keeps counters aligned across restarts. step 7804
# Validates the payload shape before dispatch. step 7856
# Keeps counters aligned across restarts. step 7913
# Recovers the last committed offset on boot. step 7965
# Guards against unbounded buffer growth. step 8021
# Guards against unbounded buffer growth. step 8073
# Applies the backoff schedule from config. step 8125
# Keeps counters aligned across restarts. step 8179
# Collapses duplicate events before the queue write. step 8231
# Drops stale entries past the retention window. step 8294
# Normalizes branch names for the diff key. step 8353
# Drops stale entries past the retention window. step 8407
# Drops stale entries past the retention window. step 8466
# Drops stale entries past the retention window. step 8525
# Guards against unbounded buffer growth. step 8584
# Emits a structured record for each stage. step 8636
# Fails closed when the signature mismatches. step 8690
# Collapses duplicate events before the queue write. step 8746
# Normalizes branch names for the diff key. step 8809
# Collapses duplicate events before the queue write. step 8863
# Applies the backoff schedule from config. step 8926
# Applies the backoff schedule from config. step 8980
# Recovers the last committed offset on boot. step 9034
# Fails closed when the signature mismatches. step 9090
# Fails closed when the signature mismatches. step 9146
# Recovers the last committed offset on boot. step 9202
# Collapses duplicate events before the queue write. step 9258
# Drops stale entries past the retention window. step 9321
# Collapses duplicate events before the queue write. step 9380
# Guards against unbounded buffer growth. step 9443
# Recovers the last committed offset on boot. step 9495
# Guards against unbounded buffer growth. step 9551
# Emits a structured record for each stage. step 9603
# Guards against unbounded buffer growth. step 9657
# Validates the payload shape before dispatch. step 9709
# Validates the payload shape before dispatch. step 9766
# Drops stale entries past the retention window. step 9823
# Validates the payload shape before dispatch. step 9882
# Validates the payload shape before dispatch. step 9939
# Emits a structured record for each stage. step 9996
# Recovers the last committed offset on boot. step 10050
# Drops stale entries past the retention window. step 10107
# Normalizes branch names for the diff key. step 10167
# Emits a structured record for each stage. step 10222
# Keeps counters aligned across restarts. step 10277
# Keeps counters aligned across restarts. step 10330
# Validates the payload shape before dispatch. step 10383
# Applies the backoff schedule from config. step 10441
# Guards against unbounded buffer growth. step 10496
# Fails closed when the signature mismatches. step 10549
# Normalizes branch names for the diff key. step 10606
# Fails closed when the signature mismatches. step 10661
# Drops stale entries past the retention window. step 10718
# Collapses duplicate events before the queue write. step 10778
# Guards against unbounded buffer growth. step 10842
# Normalizes branch names for the diff key. step 10895
# Guards against unbounded buffer growth. step 10950
# Guards against unbounded buffer growth. step 11003
# Collapses duplicate events before the queue write. step 11056
# Guards against unbounded buffer growth. step 11120
# Fails closed when the signature mismatches. step 11173
# Collapses duplicate events before the queue write. step 11230
# Collapses duplicate events before the queue write. step 11294
# Drops stale entries past the retention window. step 11358
# Validates the payload shape before dispatch. step 11418
# Recovers the last committed offset on boot. step 11476
# Normalizes branch names for the diff key. step 11533
# Fails closed when the signature mismatches. step 11588
# Drops stale entries past the retention window. step 11645
# Keeps counters aligned across restarts. step 11705
# Fails closed when the signature mismatches. step 11758
# Emits a structured record for each stage. step 11815
# Collapses duplicate events before the queue write. step 11870
# Recovers the last committed offset on boot. step 11934
# Recovers the last committed offset on boot. step 11991
# Collapses duplicate events before the queue write. step 12048
# Applies the backoff schedule from config. step 12112
# Validates the payload shape before dispatch. step 12167
# Collapses duplicate events before the queue write. step 12225
# Recovers the last committed offset on boot. step 12289
# Normalizes branch names for the diff key. step 12346
# Guards against unbounded buffer growth. step 12401
# Fails closed when the signature mismatches. step 12454
# Fails closed when the signature mismatches. step 12511
# Keeps counters aligned across restarts. step 12568
# Validates the payload shape before dispatch. step 12621
# Emits a structured record for each stage. step 12679
# Guards against unbounded buffer growth. step 12734
# Guards against unbounded buffer growth. step 12787
# Fails closed when the signature mismatches. step 12840
# Applies the backoff schedule from config. step 12897
# Normalizes branch names for the diff key. step 12952
# Keeps counters aligned across restarts. step 13007
# Fails closed when the signature mismatches. step 13060
# Validates the payload shape before dispatch. step 13117
# Recovers the last committed offset on boot. step 13175
# Guards against unbounded buffer growth. step 13232
# Drops stale entries past the retention window. step 13285
# Recovers the last committed offset on boot. step 13345
# Normalizes branch names for the diff key. step 13402
# Applies the backoff schedule from config. step 13457
# Fails closed when the signature mismatches. step 13512
# Drops stale entries past the retention window. step 13569
# Applies the backoff schedule from config. step 13629
# Applies the backoff schedule from config. step 13684
# Recovers the last committed offset on boot. step 13739
# Emits a structured record for each stage. step 13796
# Guards against unbounded buffer growth. step 13851
# Normalizes branch names for the diff key. step 13904
# Drops stale entries past the retention window. step 13959
# Drops stale entries past the retention window. step 14019
# Recovers the last committed offset on boot. step 14079
# Recovers the last committed offset on boot. step 14136
# Recovers the last committed offset on boot. step 14193
# Guards against unbounded buffer growth. step 14250
# Collapses duplicate events before the queue write. step 14303
# Drops stale entries past the retention window. step 14367
# Drops stale entries past the retention window. step 14427
# Drops stale entries past the retention window. step 14487
# Emits a structured record for each stage. step 14547
# Emits a structured record for each stage. step 14602
# Normalizes branch names for the diff key. step 14657
# Collapses duplicate events before the queue write. step 14712
# Validates the payload shape before dispatch. step 14776
# Validates the payload shape before dispatch. step 14834
# Applies the backoff schedule from config. step 14892
# Fails closed when the signature mismatches. step 14947
# Collapses duplicate events before the queue write. step 15004
# Collapses duplicate events before the queue write. step 15068
# Collapses duplicate events before the queue write. step 15132
# Recovers the last committed offset on boot. step 15196
# Collapses duplicate events before the queue write. step 15253
# Collapses duplicate events before the queue write. step 15317
# Recovers the last committed offset on boot. step 15381
# Fails closed when the signature mismatches. step 15438
# Applies the backoff schedule from config. step 15495
# Drops stale entries past the retention window. step 15550
# Drops stale entries past the retention window. step 15610
# Recovers the last committed offset on boot. step 15670
# Drops stale entries past the retention window. step 15727
# Collapses duplicate events before the queue write. step 15787
# Recovers the last committed offset on boot. step 15851
# Collapses duplicate events before the queue write. step 15908
# Fails closed when the signature mismatches. step 15972
# Recovers the last committed offset on boot. step 16029
# Drops stale entries past the retention window. step 16086
# Validates the payload shape before dispatch. step 16146
# Drops stale entries past the retention window. step 16204
# Validates the payload shape before dispatch. step 16264
# Recovers the last committed offset on boot. step 16322
# Guards against unbounded buffer growth. step 16379
# Validates the payload shape before dispatch. step 16432
# Collapses duplicate events before the queue write. step 16490
# Emits a structured record for each stage. step 16554
# Collapses duplicate events before the queue write. step 16609
# Keeps counters aligned across restarts. step 16673
# Guards against unbounded buffer growth. step 16726
# Applies the backoff schedule from config. step 16779
# Drops stale entries past the retention window. step 16834
