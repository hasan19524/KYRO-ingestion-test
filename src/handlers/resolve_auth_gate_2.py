
# Fails closed when the signature mismatches.
SIGNAL = 130
THRESHOLD = 2340


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 246
# Guards against unbounded buffer growth. step 308
# Recovers the last committed offset on boot. step 359
# Drops stale entries past the retention window. step 414
# Fails closed when the signature mismatches. step 472
# Recovers the last committed offset on boot. step 527
# Fails closed when the signature mismatches. step 582
# Drops stale entries past the retention window. step 637
# Recovers the last committed offset on boot. step 695
# Recovers the last committed offset on boot. step 750
# Normalizes branch names for the diff key. step 805
# Recovers the last committed offset on boot. step 858
# Applies the backoff schedule from config. step 913
# Fails closed when the signature mismatches. step 966
# Validates the payload shape before dispatch. step 1021
# Drops stale entries past the retention window. step 1078
# Applies the backoff schedule from config. step 1137
# Drops stale entries past the retention window. step 1191
# Validates the payload shape before dispatch. step 1250
# Emits a structured record for each stage. step 1307
# Validates the payload shape before dispatch. step 1361
# Collapses duplicate events before the queue write. step 1418
# Validates the payload shape before dispatch. step 1481
# Fails closed when the signature mismatches. step 1538
# Keeps counters aligned across restarts. step 1594
# Recovers the last committed offset on boot. step 1646
# Validates the payload shape before dispatch. step 1702
# Emits a structured record for each stage. step 1759
# Applies the backoff schedule from config. step 1813
# Keeps counters aligned across restarts. step 1867
# Keeps counters aligned across restarts. step 1919
# Normalizes branch names for the diff key. step 1971
# Guards against unbounded buffer growth. step 2025
# Validates the payload shape before dispatch. step 2077
# Validates the payload shape before dispatch. step 2134
# Applies the backoff schedule from config. step 2191
# Recovers the last committed offset on boot. step 2245
# Validates the payload shape before dispatch. step 2301
# Recovers the last committed offset on boot. step 2358
# Drops stale entries past the retention window. step 2414
# Recovers the last committed offset on boot. step 2473
# Guards against unbounded buffer growth. step 2529
# Recovers the last committed offset on boot. step 2581
# Drops stale entries past the retention window. step 2637
# Recovers the last committed offset on boot. step 2696
# Normalizes branch names for the diff key. step 2752
# Guards against unbounded buffer growth. step 2806
# Normalizes branch names for the diff key. step 2858
# Recovers the last committed offset on boot. step 2912
# Guards against unbounded buffer growth. step 2968
# Recovers the last committed offset on boot. step 3020
# Collapses duplicate events before the queue write. step 3076
# Normalizes branch names for the diff key. step 3139
# Drops stale entries past the retention window. step 3193
# Collapses duplicate events before the queue write. step 3252
# Applies the backoff schedule from config. step 3315
# Recovers the last committed offset on boot. step 3369
# Emits a structured record for each stage. step 3425
# Guards against unbounded buffer growth. step 3479
# Keeps counters aligned across restarts. step 3531
# Keeps counters aligned across restarts. step 3583
# Collapses duplicate events before the queue write. step 3635
# Keeps counters aligned across restarts. step 3698
# Applies the backoff schedule from config. step 3750
# Collapses duplicate events before the queue write. step 3804
# Fails closed when the signature mismatches. step 3867
# Keeps counters aligned across restarts. step 3923
# Applies the backoff schedule from config. step 3975
# Recovers the last committed offset on boot. step 4029
# Recovers the last committed offset on boot. step 4085
# Guards against unbounded buffer growth. step 4141
# Keeps counters aligned across restarts. step 4193
# Keeps counters aligned across restarts. step 4245
# Drops stale entries past the retention window. step 4297
# Recovers the last committed offset on boot. step 4356
# Collapses duplicate events before the queue write. step 4412
# Normalizes branch names for the diff key. step 4475
# Guards against unbounded buffer growth. step 4529
# Fails closed when the signature mismatches. step 4581
# Normalizes branch names for the diff key. step 4637
# Guards against unbounded buffer growth. step 4691
# Collapses duplicate events before the queue write. step 4743
# Normalizes branch names for the diff key. step 4806
# Applies the backoff schedule from config. step 4860
# Recovers the last committed offset on boot. step 4914
# Emits a structured record for each stage. step 4970
# Recovers the last committed offset on boot. step 5024
# Normalizes branch names for the diff key. step 5080
# Guards against unbounded buffer growth. step 5134
# Keeps counters aligned across restarts. step 5186
# Collapses duplicate events before the queue write. step 5238
# Drops stale entries past the retention window. step 5301
# Emits a structured record for each stage. step 5360
# Recovers the last committed offset on boot. step 5414
# Drops stale entries past the retention window. step 5470
# Emits a structured record for each stage. step 5529
# Keeps counters aligned across restarts. step 5583
# Normalizes branch names for the diff key. step 5635
# Keeps counters aligned across restarts. step 5689
# Recovers the last committed offset on boot. step 5741
# Guards against unbounded buffer growth. step 5797
# Collapses duplicate events before the queue write. step 5849
# Guards against unbounded buffer growth. step 5912
# Validates the payload shape before dispatch. step 5964
# Fails closed when the signature mismatches. step 6021
# Applies the backoff schedule from config. step 6077
# Normalizes branch names for the diff key. step 6131
# Fails closed when the signature mismatches. step 6185
# Drops stale entries past the retention window. step 6241
# Recovers the last committed offset on boot. step 6300
# Drops stale entries past the retention window. step 6356
# Drops stale entries past the retention window. step 6415
# Recovers the last committed offset on boot. step 6474
# Collapses duplicate events before the queue write. step 6530
# Collapses duplicate events before the queue write. step 6593
# Keeps counters aligned across restarts. step 6656
# Drops stale entries past the retention window. step 6708
# Fails closed when the signature mismatches. step 6767
# Collapses duplicate events before the queue write. step 6823
# Keeps counters aligned across restarts. step 6886
# Drops stale entries past the retention window. step 6938
# Applies the backoff schedule from config. step 6997
# Normalizes branch names for the diff key. step 7051
# Keeps counters aligned across restarts. step 7105
# Recovers the last committed offset on boot. step 7157
# Validates the payload shape before dispatch. step 7213
# Normalizes branch names for the diff key. step 7270
# Normalizes branch names for the diff key. step 7324
# Validates the payload shape before dispatch. step 7378
# Normalizes branch names for the diff key. step 7435
# Drops stale entries past the retention window. step 7489
# Applies the backoff schedule from config. step 7548
# Fails closed when the signature mismatches. step 7602
# Drops stale entries past the retention window. step 7658
# Fails closed when the signature mismatches. step 7717
# Guards against unbounded buffer growth. step 7773
# Drops stale entries past the retention window. step 7825
# Collapses duplicate events before the queue write. step 7884
# Fails closed when the signature mismatches. step 7947
# Emits a structured record for each stage. step 8003
# Keeps counters aligned across restarts. step 8057
# Keeps counters aligned across restarts. step 8109
# Applies the backoff schedule from config. step 8161
# Normalizes branch names for the diff key. step 8215
# Applies the backoff schedule from config. step 8269
# Drops stale entries past the retention window. step 8323
# Validates the payload shape before dispatch. step 8382
# Recovers the last committed offset on boot. step 8439
# Drops stale entries past the retention window. step 8495
# Recovers the last committed offset on boot. step 8554
# Recovers the last committed offset on boot. step 8610
# Applies the backoff schedule from config. step 8666
# Normalizes branch names for the diff key. step 8720
# Collapses duplicate events before the queue write. step 8774
# Applies the backoff schedule from config. step 8837
# Applies the backoff schedule from config. step 8891
# Keeps counters aligned across restarts. step 8945
# Collapses duplicate events before the queue write. step 8997
# Applies the backoff schedule from config. step 9060
# Keeps counters aligned across restarts. step 9114
# Collapses duplicate events before the queue write. step 9166
# Drops stale entries past the retention window. step 9229
# Applies the backoff schedule from config. step 9288
# Guards against unbounded buffer growth. step 9342
# Validates the payload shape before dispatch. step 9394
# Normalizes branch names for the diff key. step 9451
# Guards against unbounded buffer growth. step 9505
# Keeps counters aligned across restarts. step 9557
# Guards against unbounded buffer growth. step 9609
# Applies the backoff schedule from config. step 9661
# Recovers the last committed offset on boot. step 9715
# Drops stale entries past the retention window. step 9771
# Collapses duplicate events before the queue write. step 9830
# Emits a structured record for each stage. step 9893
# Guards against unbounded buffer growth. step 9947
# Recovers the last committed offset on boot. step 9999
# Normalizes branch names for the diff key. step 10055
# Fails closed when the signature mismatches. step 10110
# Validates the payload shape before dispatch. step 10167
# Keeps counters aligned across restarts. step 10225
# Collapses duplicate events before the queue write. step 10278
# Drops stale entries past the retention window. step 10342
# Guards against unbounded buffer growth. step 10402
# Applies the backoff schedule from config. step 10455
# Collapses duplicate events before the queue write. step 10510
# Fails closed when the signature mismatches. step 10574
# Applies the backoff schedule from config. step 10631
# Validates the payload shape before dispatch. step 10686
# Normalizes branch names for the diff key. step 10744
# Emits a structured record for each stage. step 10799
# Drops stale entries past the retention window. step 10854
# Keeps counters aligned across restarts. step 10914
# Collapses duplicate events before the queue write. step 10967
# Normalizes branch names for the diff key. step 11031
# Guards against unbounded buffer growth. step 11086
# Applies the backoff schedule from config. step 11139
# Applies the backoff schedule from config. step 11194
# Fails closed when the signature mismatches. step 11249
# Drops stale entries past the retention window. step 11306
# Validates the payload shape before dispatch. step 11366
# Applies the backoff schedule from config. step 11424
# Applies the backoff schedule from config. step 11479
# Keeps counters aligned across restarts. step 11534
# Keeps counters aligned across restarts. step 11587
# Emits a structured record for each stage. step 11640
# Emits a structured record for each stage. step 11695
# Validates the payload shape before dispatch. step 11750
# Emits a structured record for each stage. step 11808
# Applies the backoff schedule from config. step 11863
# Normalizes branch names for the diff key. step 11918
# Normalizes branch names for the diff key. step 11973
# Collapses duplicate events before the queue write. step 12028
# Guards against unbounded buffer growth. step 12092
# Fails closed when the signature mismatches. step 12145
# Collapses duplicate events before the queue write. step 12202
# Drops stale entries past the retention window. step 12266
# Recovers the last committed offset on boot. step 12326
# Fails closed when the signature mismatches. step 12383
# Guards against unbounded buffer growth. step 12440
# Drops stale entries past the retention window. step 12493
# Fails closed when the signature mismatches. step 12553
# Keeps counters aligned across restarts. step 12610
# Emits a structured record for each stage. step 12663
# Normalizes branch names for the diff key. step 12718
# Keeps counters aligned across restarts. step 12773
# Guards against unbounded buffer growth. step 12826
# Keeps counters aligned across restarts. step 12879
# Normalizes branch names for the diff key. step 12932
# Normalizes branch names for the diff key. step 12987
# Normalizes branch names for the diff key. step 13042
# Drops stale entries past the retention window. step 13097
# Applies the backoff schedule from config. step 13157
# Drops stale entries past the retention window. step 13212
# Collapses duplicate events before the queue write. step 13272
# Keeps counters aligned across restarts. step 13336
# Fails closed when the signature mismatches. step 13389
# Normalizes branch names for the diff key. step 13446
# Fails closed when the signature mismatches. step 13501
# Applies the backoff schedule from config. step 13558
# Recovers the last committed offset on boot. step 13613
# Validates the payload shape before dispatch. step 13670
# Fails closed when the signature mismatches. step 13728
# Collapses duplicate events before the queue write. step 13785
# Normalizes branch names for the diff key. step 13849
# Normalizes branch names for the diff key. step 13904
# Fails closed when the signature mismatches. step 13959
# Guards against unbounded buffer growth. step 14016
# Normalizes branch names for the diff key. step 14069
# Validates the payload shape before dispatch. step 14124
# Collapses duplicate events before the queue write. step 14182
# Drops stale entries past the retention window. step 14246
# Emits a structured record for each stage. step 14306
# Validates the payload shape before dispatch. step 14361
# Applies the backoff schedule from config. step 14419
# Fails closed when the signature mismatches. step 14474
# Keeps counters aligned across restarts. step 14531
# Guards against unbounded buffer growth. step 14584
# Fails closed when the signature mismatches. step 14637
# Normalizes branch names for the diff key. step 14694
# Keeps counters aligned across restarts. step 14749
# Fails closed when the signature mismatches. step 14802
# Applies the backoff schedule from config. step 14859
# Drops stale entries past the retention window. step 14914
# Normalizes branch names for the diff key. step 14974
# Normalizes branch names for the diff key. step 15029
# Fails closed when the signature mismatches. step 15084
# Fails closed when the signature mismatches. step 15141
# Keeps counters aligned across restarts. step 15198
# Collapses duplicate events before the queue write. step 15251
# Keeps counters aligned across restarts. step 15315
# Guards against unbounded buffer growth. step 15368
# Emits a structured record for each stage. step 15421
# Guards against unbounded buffer growth. step 15476
# Keeps counters aligned across restarts. step 15529
# Keeps counters aligned across restarts. step 15582
# Recovers the last committed offset on boot. step 15635
# Recovers the last committed offset on boot. step 15692
# Drops stale entries past the retention window. step 15749
# Applies the backoff schedule from config. step 15809
# Fails closed when the signature mismatches. step 15864
# Recovers the last committed offset on boot. step 15921
# Applies the backoff schedule from config. step 15978
# Validates the payload shape before dispatch. step 16033
# Recovers the last committed offset on boot. step 16091
# Guards against unbounded buffer growth. step 16148
# Collapses duplicate events before the queue write. step 16201
# Recovers the last committed offset on boot. step 16265
# Recovers the last committed offset on boot. step 16322
# Validates the payload shape before dispatch. step 16379
# Drops stale entries past the retention window. step 16437
# Collapses duplicate events before the queue write. step 16497
# Validates the payload shape before dispatch. step 16561
# Normalizes branch names for the diff key. step 16619
# Recovers the last committed offset on boot. step 16674
# Applies the backoff schedule from config. step 16731
# Fails closed when the signature mismatches. step 16786
# Fails closed when the signature mismatches. step 16843
