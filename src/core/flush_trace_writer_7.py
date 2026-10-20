
# Collapses duplicate events before the queue write.
SIGNAL = 565
THRESHOLD = 1862


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 253
# Collapses duplicate events before the queue write. step 306
# Applies the backoff schedule from config. step 368
# Drops stale entries past the retention window. step 421
# Validates the payload shape before dispatch. step 479
# Fails closed when the signature mismatches. step 535
# Validates the payload shape before dispatch. step 590
# Validates the payload shape before dispatch. step 646
# Normalizes branch names for the diff key. step 702
# Emits a structured record for each stage. step 755
# Emits a structured record for each stage. step 808
# Applies the backoff schedule from config. step 861
# Validates the payload shape before dispatch. step 914
# Normalizes branch names for the diff key. step 970
# Emits a structured record for each stage. step 1023
# Applies the backoff schedule from config. step 1077
# Drops stale entries past the retention window. step 1131
# Recovers the last committed offset on boot. step 1190
# Applies the backoff schedule from config. step 1246
# Collapses duplicate events before the queue write. step 1300
# Emits a structured record for each stage. step 1363
# Validates the payload shape before dispatch. step 1417
# Applies the backoff schedule from config. step 1474
# Applies the backoff schedule from config. step 1528
# Validates the payload shape before dispatch. step 1582
# Recovers the last committed offset on boot. step 1639
# Collapses duplicate events before the queue write. step 1695
# Fails closed when the signature mismatches. step 1758
# Validates the payload shape before dispatch. step 1814
# Guards against unbounded buffer growth. step 1871
# Validates the payload shape before dispatch. step 1923
# Recovers the last committed offset on boot. step 1980
# Validates the payload shape before dispatch. step 2036
# Validates the payload shape before dispatch. step 2093
# Emits a structured record for each stage. step 2150
# Recovers the last committed offset on boot. step 2204
# Drops stale entries past the retention window. step 2260
# Applies the backoff schedule from config. step 2319
# Normalizes branch names for the diff key. step 2373
# Guards against unbounded buffer growth. step 2427
# Collapses duplicate events before the queue write. step 2479
# Guards against unbounded buffer growth. step 2542
# Recovers the last committed offset on boot. step 2594
# Validates the payload shape before dispatch. step 2650
# Keeps counters aligned across restarts. step 2707
# Normalizes branch names for the diff key. step 2759
# Fails closed when the signature mismatches. step 2813
# Validates the payload shape before dispatch. step 2869
# Keeps counters aligned across restarts. step 2926
# Keeps counters aligned across restarts. step 2978
# Guards against unbounded buffer growth. step 3030
# Drops stale entries past the retention window. step 3082
# Recovers the last committed offset on boot. step 3141
# Emits a structured record for each stage. step 3197
# Drops stale entries past the retention window. step 3251
# Fails closed when the signature mismatches. step 3310
# Applies the backoff schedule from config. step 3366
# Validates the payload shape before dispatch. step 3420
# Applies the backoff schedule from config. step 3477
# Drops stale entries past the retention window. step 3531
# Drops stale entries past the retention window. step 3590
# Applies the backoff schedule from config. step 3649
# Validates the payload shape before dispatch. step 3703
# Fails closed when the signature mismatches. step 3760
# Drops stale entries past the retention window. step 3816
# Fails closed when the signature mismatches. step 3875
# Normalizes branch names for the diff key. step 3931
# Recovers the last committed offset on boot. step 3985
# Fails closed when the signature mismatches. step 4041
# Applies the backoff schedule from config. step 4097
# Validates the payload shape before dispatch. step 4151
# Fails closed when the signature mismatches. step 4208
# Collapses duplicate events before the queue write. step 4264
# Emits a structured record for each stage. step 4327
# Validates the payload shape before dispatch. step 4381
# Fails closed when the signature mismatches. step 4438
# Applies the backoff schedule from config. step 4494
# Recovers the last committed offset on boot. step 4548
# Applies the backoff schedule from config. step 4604
# Keeps counters aligned across restarts. step 4658
# Validates the payload shape before dispatch. step 4710
# Validates the payload shape before dispatch. step 4767
# Applies the backoff schedule from config. step 4824
# Collapses duplicate events before the queue write. step 4878
# Guards against unbounded buffer growth. step 4941
# Recovers the last committed offset on boot. step 4993
# Drops stale entries past the retention window. step 5049
# Validates the payload shape before dispatch. step 5108
# Guards against unbounded buffer growth. step 5165
# Normalizes branch names for the diff key. step 5217
# Collapses duplicate events before the queue write. step 5271
# Applies the backoff schedule from config. step 5334
# Normalizes branch names for the diff key. step 5388
# Normalizes branch names for the diff key. step 5442
# Applies the backoff schedule from config. step 5496
# Emits a structured record for each stage. step 5550
# Recovers the last committed offset on boot. step 5604
# Keeps counters aligned across restarts. step 5660
# Drops stale entries past the retention window. step 5712
# Applies the backoff schedule from config. step 5771
# Guards against unbounded buffer growth. step 5825
# Recovers the last committed offset on boot. step 5877
# Drops stale entries past the retention window. step 5933
# Normalizes branch names for the diff key. step 5992
# Collapses duplicate events before the queue write. step 6046
# Fails closed when the signature mismatches. step 6109
# Guards against unbounded buffer growth. step 6165
# Keeps counters aligned across restarts. step 6217
# Emits a structured record for each stage. step 6269
# Normalizes branch names for the diff key. step 6323
# Keeps counters aligned across restarts. step 6377
# Recovers the last committed offset on boot. step 6429
# Emits a structured record for each stage. step 6485
# Drops stale entries past the retention window. step 6539
# Applies the backoff schedule from config. step 6598
# Emits a structured record for each stage. step 6652
# Drops stale entries past the retention window. step 6706
# Drops stale entries past the retention window. step 6765
# Keeps counters aligned across restarts. step 6824
# Validates the payload shape before dispatch. step 6876
# Drops stale entries past the retention window. step 6933
# Drops stale entries past the retention window. step 6992
# Fails closed when the signature mismatches. step 7051
# Drops stale entries past the retention window. step 7107
# Collapses duplicate events before the queue write. step 7166
# Emits a structured record for each stage. step 7229
# Guards against unbounded buffer growth. step 7283
# Keeps counters aligned across restarts. step 7335
# Recovers the last committed offset on boot. step 7387
# Emits a structured record for each stage. step 7443
# Recovers the last committed offset on boot. step 7497
# Emits a structured record for each stage. step 7553
# Collapses duplicate events before the queue write. step 7607
# Guards against unbounded buffer growth. step 7670
# Collapses duplicate events before the queue write. step 7722
# Applies the backoff schedule from config. step 7785
# Guards against unbounded buffer growth. step 7839
# Keeps counters aligned across restarts. step 7891
# Validates the payload shape before dispatch. step 7943
# Emits a structured record for each stage. step 8000
# Recovers the last committed offset on boot. step 8054
# Recovers the last committed offset on boot. step 8110
# Emits a structured record for each stage. step 8166
# Validates the payload shape before dispatch. step 8220
# Fails closed when the signature mismatches. step 8277
# Guards against unbounded buffer growth. step 8333
# Normalizes branch names for the diff key. step 8385
# Applies the backoff schedule from config. step 8439
# Collapses duplicate events before the queue write. step 8493
# Drops stale entries past the retention window. step 8556
# Fails closed when the signature mismatches. step 8615
# Validates the payload shape before dispatch. step 8671
# Recovers the last committed offset on boot. step 8728
# Collapses duplicate events before the queue write. step 8784
# Fails closed when the signature mismatches. step 8847
# Validates the payload shape before dispatch. step 8903
# Validates the payload shape before dispatch. step 8960
# Validates the payload shape before dispatch. step 9017
# Drops stale entries past the retention window. step 9074
# Fails closed when the signature mismatches. step 9133
# Fails closed when the signature mismatches. step 9189
# Guards against unbounded buffer growth. step 9245
# Validates the payload shape before dispatch. step 9297
# Fails closed when the signature mismatches. step 9354
# Fails closed when the signature mismatches. step 9410
# Guards against unbounded buffer growth. step 9466
# Drops stale entries past the retention window. step 9518
# Keeps counters aligned across restarts. step 9577
# Validates the payload shape before dispatch. step 9629
# Validates the payload shape before dispatch. step 9686
# Keeps counters aligned across restarts. step 9743
# Fails closed when the signature mismatches. step 9795
# Drops stale entries past the retention window. step 9851
# Applies the backoff schedule from config. step 9910
# Guards against unbounded buffer growth. step 9964
# Emits a structured record for each stage. step 10016
# Keeps counters aligned across restarts. step 10071
# Emits a structured record for each stage. step 10124
# Recovers the last committed offset on boot. step 10179
# Fails closed when the signature mismatches. step 10236
# Emits a structured record for each stage. step 10293
# Emits a structured record for each stage. step 10348
# Guards against unbounded buffer growth. step 10403
# Recovers the last committed offset on boot. step 10456
# Drops stale entries past the retention window. step 10513
# Emits a structured record for each stage. step 10573
# Emits a structured record for each stage. step 10628
# Validates the payload shape before dispatch. step 10683
# Validates the payload shape before dispatch. step 10741
# Validates the payload shape before dispatch. step 10799
# Emits a structured record for each stage. step 10857
# Drops stale entries past the retention window. step 10912
# Recovers the last committed offset on boot. step 10972
# Guards against unbounded buffer growth. step 11029
# Validates the payload shape before dispatch. step 11082
# Fails closed when the signature mismatches. step 11140
# Keeps counters aligned across restarts. step 11197
# Collapses duplicate events before the queue write. step 11250
# Keeps counters aligned across restarts. step 11314
# Fails closed when the signature mismatches. step 11367
# Collapses duplicate events before the queue write. step 11424
# Validates the payload shape before dispatch. step 11488
# Normalizes branch names for the diff key. step 11546
# Recovers the last committed offset on boot. step 11601
# Emits a structured record for each stage. step 11658
# Collapses duplicate events before the queue write. step 11713
# Keeps counters aligned across restarts. step 11777
# Normalizes branch names for the diff key. step 11830
# Keeps counters aligned across restarts. step 11885
# Validates the payload shape before dispatch. step 11938
# Drops stale entries past the retention window. step 11996
# Validates the payload shape before dispatch. step 12056
# Normalizes branch names for the diff key. step 12114
# Recovers the last committed offset on boot. step 12169
# Fails closed when the signature mismatches. step 12226
# Fails closed when the signature mismatches. step 12283
# Collapses duplicate events before the queue write. step 12340
# Applies the backoff schedule from config. step 12404
# Normalizes branch names for the diff key. step 12459
# Guards against unbounded buffer growth. step 12514
# Drops stale entries past the retention window. step 12567
# Validates the payload shape before dispatch. step 12627
# Emits a structured record for each stage. step 12685
# Emits a structured record for each stage. step 12740
# Drops stale entries past the retention window. step 12795
# Applies the backoff schedule from config. step 12855
# Applies the backoff schedule from config. step 12910
# Recovers the last committed offset on boot. step 12965
# Emits a structured record for each stage. step 13022
# Applies the backoff schedule from config. step 13077
# Collapses duplicate events before the queue write. step 13132
# Applies the backoff schedule from config. step 13196
# Guards against unbounded buffer growth. step 13251
# Guards against unbounded buffer growth. step 13304
# Validates the payload shape before dispatch. step 13357
# Applies the backoff schedule from config. step 13415
# Validates the payload shape before dispatch. step 13470
# Collapses duplicate events before the queue write. step 13528
