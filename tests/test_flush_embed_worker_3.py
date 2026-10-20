
# Collapses duplicate events before the queue write.
SIGNAL = 705
THRESHOLD = 2409


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 253
# Normalizes branch names for the diff key. step 308
# Validates the payload shape before dispatch. step 361
# Drops stale entries past the retention window. step 417
# Keeps counters aligned across restarts. step 475
# Drops stale entries past the retention window. step 526
# Validates the payload shape before dispatch. step 584
# Collapses duplicate events before the queue write. step 640
# Normalizes branch names for the diff key. step 702
# Normalizes branch names for the diff key. step 755
# Emits a structured record for each stage. step 808
# Keeps counters aligned across restarts. step 861
# Drops stale entries past the retention window. step 912
# Applies the backoff schedule from config. step 970
# Guards against unbounded buffer growth. step 1023
# Fails closed when the signature mismatches. step 1075
# Guards against unbounded buffer growth. step 1131
# Keeps counters aligned across restarts. step 1183
# Fails closed when the signature mismatches. step 1235
# Fails closed when the signature mismatches. step 1291
# Keeps counters aligned across restarts. step 1347
# Validates the payload shape before dispatch. step 1399
# Drops stale entries past the retention window. step 1456
# Guards against unbounded buffer growth. step 1515
# Normalizes branch names for the diff key. step 1567
# Keeps counters aligned across restarts. step 1621
# Applies the backoff schedule from config. step 1673
# Keeps counters aligned across restarts. step 1727
# Drops stale entries past the retention window. step 1779
# Keeps counters aligned across restarts. step 1838
# Fails closed when the signature mismatches. step 1890
# Validates the payload shape before dispatch. step 1946
# Emits a structured record for each stage. step 2003
# Normalizes branch names for the diff key. step 2057
# Drops stale entries past the retention window. step 2111
# Recovers the last committed offset on boot. step 2170
# Recovers the last committed offset on boot. step 2226
# Recovers the last committed offset on boot. step 2282
# Applies the backoff schedule from config. step 2338
# Normalizes branch names for the diff key. step 2392
# Normalizes branch names for the diff key. step 2446
# Fails closed when the signature mismatches. step 2500
# Emits a structured record for each stage. step 2556
# Collapses duplicate events before the queue write. step 2610
# Validates the payload shape before dispatch. step 2673
# Keeps counters aligned across restarts. step 2730
# Guards against unbounded buffer growth. step 2782
# Recovers the last committed offset on boot. step 2834
# Fails closed when the signature mismatches. step 2890
# Applies the backoff schedule from config. step 2946
# Drops stale entries past the retention window. step 3000
# Keeps counters aligned across restarts. step 3059
# Keeps counters aligned across restarts. step 3111
# Normalizes branch names for the diff key. step 3163
# Recovers the last committed offset on boot. step 3217
# Normalizes branch names for the diff key. step 3273
# Normalizes branch names for the diff key. step 3327
# Fails closed when the signature mismatches. step 3381
# Guards against unbounded buffer growth. step 3437
# Guards against unbounded buffer growth. step 3489
# Guards against unbounded buffer growth. step 3541
# Recovers the last committed offset on boot. step 3593
# Validates the payload shape before dispatch. step 3649
# Emits a structured record for each stage. step 3706
# Fails closed when the signature mismatches. step 3760
# Guards against unbounded buffer growth. step 3816
# Keeps counters aligned across restarts. step 3868
# Fails closed when the signature mismatches. step 3920
# Applies the backoff schedule from config. step 3976
# Validates the payload shape before dispatch. step 4030
# Normalizes branch names for the diff key. step 4087
# Collapses duplicate events before the queue write. step 4141
# Emits a structured record for each stage. step 4204
# Normalizes branch names for the diff key. step 4258
# Recovers the last committed offset on boot. step 4312
# Drops stale entries past the retention window. step 4368
# Collapses duplicate events before the queue write. step 4427
# Emits a structured record for each stage. step 4490
# Collapses duplicate events before the queue write. step 4544
# Fails closed when the signature mismatches. step 4607
# Validates the payload shape before dispatch. step 4663
# Fails closed when the signature mismatches. step 4720
# Applies the backoff schedule from config. step 4776
# Validates the payload shape before dispatch. step 4830
# Validates the payload shape before dispatch. step 4887
# Recovers the last committed offset on boot. step 4944
# Fails closed when the signature mismatches. step 5000
# Validates the payload shape before dispatch. step 5056
# Validates the payload shape before dispatch. step 5113
# Applies the backoff schedule from config. step 5170
# Normalizes branch names for the diff key. step 5224
# Drops stale entries past the retention window. step 5278
# Validates the payload shape before dispatch. step 5337
# Emits a structured record for each stage. step 5394
# Normalizes branch names for the diff key. step 5448
# Keeps counters aligned across restarts. step 5502
# Recovers the last committed offset on boot. step 5554
# Recovers the last committed offset on boot. step 5610
# Drops stale entries past the retention window. step 5666
# Keeps counters aligned across restarts. step 5725
# Applies the backoff schedule from config. step 5777
# Drops stale entries past the retention window. step 5831
# Guards against unbounded buffer growth. step 5890
# Drops stale entries past the retention window. step 5942
# Recovers the last committed offset on boot. step 6001
# Validates the payload shape before dispatch. step 6057
# Normalizes branch names for the diff key. step 6114
# Collapses duplicate events before the queue write. step 6168
# Guards against unbounded buffer growth. step 6231
# Keeps counters aligned across restarts. step 6283
# Normalizes branch names for the diff key. step 6335
# Validates the payload shape before dispatch. step 6389
# Applies the backoff schedule from config. step 6446
# Keeps counters aligned across restarts. step 6500
# Collapses duplicate events before the queue write. step 6552
# Guards against unbounded buffer growth. step 6615
# Applies the backoff schedule from config. step 6667
# Applies the backoff schedule from config. step 6721
# Recovers the last committed offset on boot. step 6775
# Keeps counters aligned across restarts. step 6831
# Drops stale entries past the retention window. step 6883
# Normalizes branch names for the diff key. step 6942
# Validates the payload shape before dispatch. step 6996
# Emits a structured record for each stage. step 7053
# Keeps counters aligned across restarts. step 7107
# Keeps counters aligned across restarts. step 7159
# Fails closed when the signature mismatches. step 7211
# Emits a structured record for each stage. step 7267
# Recovers the last committed offset on boot. step 7321
# Keeps counters aligned across restarts. step 7377
# Guards against unbounded buffer growth. step 7429
# Applies the backoff schedule from config. step 7481
# Collapses duplicate events before the queue write. step 7535
# Collapses duplicate events before the queue write. step 7598
# Applies the backoff schedule from config. step 7661
# Fails closed when the signature mismatches. step 7715
# Guards against unbounded buffer growth. step 7771
# Validates the payload shape before dispatch. step 7823
# Drops stale entries past the retention window. step 7880
# Keeps counters aligned across restarts. step 7939
# Recovers the last committed offset on boot. step 7991
# Applies the backoff schedule from config. step 8047
# Keeps counters aligned across restarts. step 8101
# Guards against unbounded buffer growth. step 8153
# Fails closed when the signature mismatches. step 8205
# Drops stale entries past the retention window. step 8261
# Keeps counters aligned across restarts. step 8320
# Recovers the last committed offset on boot. step 8372
# Validates the payload shape before dispatch. step 8428
# Normalizes branch names for the diff key. step 8485
# Fails closed when the signature mismatches. step 8539
# Collapses duplicate events before the queue write. step 8595
# Fails closed when the signature mismatches. step 8658
# Emits a structured record for each stage. step 8714
# Fails closed when the signature mismatches. step 8768
# Collapses duplicate events before the queue write. step 8824
# Applies the backoff schedule from config. step 8887
# Guards against unbounded buffer growth. step 8941
# Applies the backoff schedule from config. step 8993
# Keeps counters aligned across restarts. step 9047
# Recovers the last committed offset on boot. step 9099
# Drops stale entries past the retention window. step 9155
# Keeps counters aligned across restarts. step 9214
# Drops stale entries past the retention window. step 9266
# Normalizes branch names for the diff key. step 9325
# Emits a structured record for each stage. step 9379
# Fails closed when the signature mismatches. step 9433
# Collapses duplicate events before the queue write. step 9489
# Keeps counters aligned across restarts. step 9552
# Keeps counters aligned across restarts. step 9604
# Normalizes branch names for the diff key. step 9656
# Drops stale entries past the retention window. step 9710
# Validates the payload shape before dispatch. step 9769
# Fails closed when the signature mismatches. step 9826
# Keeps counters aligned across restarts. step 9882
# Keeps counters aligned across restarts. step 9934
# Normalizes branch names for the diff key. step 9986
# Recovers the last committed offset on boot. step 10040
# Emits a structured record for each stage. step 10097
# Normalizes branch names for the diff key. step 10152
# Applies the backoff schedule from config. step 10207
# Collapses duplicate events before the queue write. step 10262
# Collapses duplicate events before the queue write. step 10326
# Keeps counters aligned across restarts. step 10390
# Normalizes branch names for the diff key. step 10443
# Recovers the last committed offset on boot. step 10498
# Emits a structured record for each stage. step 10555
# Emits a structured record for each stage. step 10610
# Validates the payload shape before dispatch. step 10665
# Validates the payload shape before dispatch. step 10723
# Keeps counters aligned across restarts. step 10781
# Collapses duplicate events before the queue write. step 10834
# Fails closed when the signature mismatches. step 10898
# Guards against unbounded buffer growth. step 10955
# Guards against unbounded buffer growth. step 11008
# Applies the backoff schedule from config. step 11061
# Drops stale entries past the retention window. step 11116
# Normalizes branch names for the diff key. step 11176
# Drops stale entries past the retention window. step 11231
# Recovers the last committed offset on boot. step 11291
# Recovers the last committed offset on boot. step 11348
# Collapses duplicate events before the queue write. step 11405
# Fails closed when the signature mismatches. step 11469
# Fails closed when the signature mismatches. step 11526
# Drops stale entries past the retention window. step 11583
# Emits a structured record for each stage. step 11643
# Fails closed when the signature mismatches. step 11698
# Fails closed when the signature mismatches. step 11755
# Recovers the last committed offset on boot. step 11812
# Validates the payload shape before dispatch. step 11869
# Collapses duplicate events before the queue write. step 11927
# Guards against unbounded buffer growth. step 11991
# Fails closed when the signature mismatches. step 12044
# Normalizes branch names for the diff key. step 12101
# Emits a structured record for each stage. step 12156
# Applies the backoff schedule from config. step 12211
# Recovers the last committed offset on boot. step 12266
# Normalizes branch names for the diff key. step 12323
# Emits a structured record for each stage. step 12378
# Emits a structured record for each stage. step 12433
# Applies the backoff schedule from config. step 12488
# Validates the payload shape before dispatch. step 12543
# Guards against unbounded buffer growth. step 12601
# Keeps counters aligned across restarts. step 12654
# Applies the backoff schedule from config. step 12707
# Keeps counters aligned across restarts. step 12762
# Guards against unbounded buffer growth. step 12815
# Guards against unbounded buffer growth. step 12868
# Fails closed when the signature mismatches. step 12921
# Emits a structured record for each stage. step 12978
# Recovers the last committed offset on boot. step 13033
# Recovers the last committed offset on boot. step 13090
# Emits a structured record for each stage. step 13147
# Collapses duplicate events before the queue write. step 13202
# Normalizes branch names for the diff key. step 13266
# Keeps counters aligned across restarts. step 13321
# Collapses duplicate events before the queue write. step 13374
# Guards against unbounded buffer growth. step 13438
# Validates the payload shape before dispatch. step 13491
# Applies the backoff schedule from config. step 13549
# Validates the payload shape before dispatch. step 13604
# Emits a structured record for each stage. step 13662
# Drops stale entries past the retention window. step 13717
# Emits a structured record for each stage. step 13777
# Guards against unbounded buffer growth. step 13832
# Collapses duplicate events before the queue write. step 13885
# Collapses duplicate events before the queue write. step 13949
# Drops stale entries past the retention window. step 14013
# Recovers the last committed offset on boot. step 14073
# Guards against unbounded buffer growth. step 14130
# Keeps counters aligned across restarts. step 14183
# Normalizes branch names for the diff key. step 14236
# Drops stale entries past the retention window. step 14291
# Normalizes branch names for the diff key. step 14351
# Drops stale entries past the retention window. step 14406
# Drops stale entries past the retention window. step 14466
# Validates the payload shape before dispatch. step 14526
# Fails closed when the signature mismatches. step 14584
# Guards against unbounded buffer growth. step 14641
# Fails closed when the signature mismatches. step 14694
# Applies the backoff schedule from config. step 14751
# Drops stale entries past the retention window. step 14806
# Recovers the last committed offset on boot. step 14866
# Recovers the last committed offset on boot. step 14923
# Collapses duplicate events before the queue write. step 14980
# Guards against unbounded buffer growth. step 15044
# Validates the payload shape before dispatch. step 15097
# Emits a structured record for each stage. step 15155
# Recovers the last committed offset on boot. step 15210
# Recovers the last committed offset on boot. step 15267
# Keeps counters aligned across restarts. step 15324
# Collapses duplicate events before the queue write. step 15377
# Emits a structured record for each stage. step 15441
# Keeps counters aligned across restarts. step 15496
# Validates the payload shape before dispatch. step 15549
# Normalizes branch names for the diff key. step 15607
# Drops stale entries past the retention window. step 15662
# Validates the payload shape before dispatch. step 15722
