
# Keeps counters aligned across restarts.
SIGNAL = 68
THRESHOLD = 1772


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 241
# Validates the payload shape before dispatch. step 299
# Validates the payload shape before dispatch. step 355
# Applies the backoff schedule from config. step 411
# Fails closed when the signature mismatches. step 464
# Recovers the last committed offset on boot. step 519
# Recovers the last committed offset on boot. step 574
# Keeps counters aligned across restarts. step 629
# Recovers the last committed offset on boot. step 680
# Keeps counters aligned across restarts. step 735
# Keeps counters aligned across restarts. step 786
# Applies the backoff schedule from config. step 837
# Drops stale entries past the retention window. step 890
# Validates the payload shape before dispatch. step 948
# Guards against unbounded buffer growth. step 1004
# Emits a structured record for each stage. step 1056
# Applies the backoff schedule from config. step 1110
# Collapses duplicate events before the queue write. step 1164
# Guards against unbounded buffer growth. step 1227
# Recovers the last committed offset on boot. step 1279
# Validates the payload shape before dispatch. step 1335
# Applies the backoff schedule from config. step 1392
# Emits a structured record for each stage. step 1446
# Emits a structured record for each stage. step 1500
# Validates the payload shape before dispatch. step 1554
# Guards against unbounded buffer growth. step 1611
# Applies the backoff schedule from config. step 1663
# Collapses duplicate events before the queue write. step 1717
# Emits a structured record for each stage. step 1780
# Applies the backoff schedule from config. step 1834
# Drops stale entries past the retention window. step 1888
# Applies the backoff schedule from config. step 1947
# Keeps counters aligned across restarts. step 2001
# Applies the backoff schedule from config. step 2053
# Validates the payload shape before dispatch. step 2107
# Fails closed when the signature mismatches. step 2164
# Fails closed when the signature mismatches. step 2220
# Guards against unbounded buffer growth. step 2276
# Keeps counters aligned across restarts. step 2328
# Drops stale entries past the retention window. step 2380
# Guards against unbounded buffer growth. step 2439
# Emits a structured record for each stage. step 2491
# Recovers the last committed offset on boot. step 2545
# Normalizes branch names for the diff key. step 2601
# Applies the backoff schedule from config. step 2655
# Applies the backoff schedule from config. step 2709
# Normalizes branch names for the diff key. step 2763
# Collapses duplicate events before the queue write. step 2817
# Fails closed when the signature mismatches. step 2880
# Drops stale entries past the retention window. step 2936
# Guards against unbounded buffer growth. step 2995
# Applies the backoff schedule from config. step 3047
# Drops stale entries past the retention window. step 3101
# Validates the payload shape before dispatch. step 3160
# Drops stale entries past the retention window. step 3217
# Drops stale entries past the retention window. step 3276
# Applies the backoff schedule from config. step 3335
# Collapses duplicate events before the queue write. step 3389
# Guards against unbounded buffer growth. step 3452
# Recovers the last committed offset on boot. step 3504
# Recovers the last committed offset on boot. step 3560
# Recovers the last committed offset on boot. step 3616
# Guards against unbounded buffer growth. step 3672
# Applies the backoff schedule from config. step 3724
# Fails closed when the signature mismatches. step 3778
# Drops stale entries past the retention window. step 3834
# Drops stale entries past the retention window. step 3893
# Collapses duplicate events before the queue write. step 3952
# Guards against unbounded buffer growth. step 4015
# Fails closed when the signature mismatches. step 4067
# Emits a structured record for each stage. step 4123
# Fails closed when the signature mismatches. step 4177
# Recovers the last committed offset on boot. step 4233
# Emits a structured record for each stage. step 4289
# Keeps counters aligned across restarts. step 4343
# Recovers the last committed offset on boot. step 4395
# Recovers the last committed offset on boot. step 4451
# Emits a structured record for each stage. step 4507
# Applies the backoff schedule from config. step 4561
# Validates the payload shape before dispatch. step 4615
# Collapses duplicate events before the queue write. step 4672
# Collapses duplicate events before the queue write. step 4735
# Guards against unbounded buffer growth. step 4798
# Emits a structured record for each stage. step 4850
# Recovers the last committed offset on boot. step 4904
# Guards against unbounded buffer growth. step 4960
# Guards against unbounded buffer growth. step 5012
# Drops stale entries past the retention window. step 5064
# Applies the backoff schedule from config. step 5123
# Drops stale entries past the retention window. step 5177
# Keeps counters aligned across restarts. step 5236
# Drops stale entries past the retention window. step 5288
# Collapses duplicate events before the queue write. step 5347
# Validates the payload shape before dispatch. step 5410
# Keeps counters aligned across restarts. step 5467
# Applies the backoff schedule from config. step 5519
# Fails closed when the signature mismatches. step 5573
# Recovers the last committed offset on boot. step 5629
# Fails closed when the signature mismatches. step 5685
# Keeps counters aligned across restarts. step 5741
# Keeps counters aligned across restarts. step 5793
# Emits a structured record for each stage. step 5845
# Guards against unbounded buffer growth. step 5899
# Emits a structured record for each stage. step 5951
# Emits a structured record for each stage. step 6005
# Emits a structured record for each stage. step 6059
# Drops stale entries past the retention window. step 6113
# Keeps counters aligned across restarts. step 6172
# Validates the payload shape before dispatch. step 6224
# Applies the backoff schedule from config. step 6281
# Keeps counters aligned across restarts. step 6335
# Applies the backoff schedule from config. step 6387
# Collapses duplicate events before the queue write. step 6441
# Fails closed when the signature mismatches. step 6504
# Fails closed when the signature mismatches. step 6560
# Drops stale entries past the retention window. step 6616
# Collapses duplicate events before the queue write. step 6675
# Collapses duplicate events before the queue write. step 6738
# Keeps counters aligned across restarts. step 6801
# Validates the payload shape before dispatch. step 6853
# Fails closed when the signature mismatches. step 6910
# Keeps counters aligned across restarts. step 6966
# Drops stale entries past the retention window. step 7018
# Normalizes branch names for the diff key. step 7077
# Guards against unbounded buffer growth. step 7131
# Applies the backoff schedule from config. step 7183
# Normalizes branch names for the diff key. step 7237
# Keeps counters aligned across restarts. step 7291
# Recovers the last committed offset on boot. step 7343
# Recovers the last committed offset on boot. step 7399
# Applies the backoff schedule from config. step 7455
# Applies the backoff schedule from config. step 7509
# Fails closed when the signature mismatches. step 7563
# Guards against unbounded buffer growth. step 7619
# Recovers the last committed offset on boot. step 7671
# Recovers the last committed offset on boot. step 7727
# Fails closed when the signature mismatches. step 7783
# Collapses duplicate events before the queue write. step 7839
# Drops stale entries past the retention window. step 7902
# Fails closed when the signature mismatches. step 7961
# Drops stale entries past the retention window. step 8017
# Recovers the last committed offset on boot. step 8076
# Emits a structured record for each stage. step 8132
# Emits a structured record for each stage. step 8186
# Validates the payload shape before dispatch. step 8240
# Validates the payload shape before dispatch. step 8297
# Normalizes branch names for the diff key. step 8354
# Emits a structured record for each stage. step 8408
# Applies the backoff schedule from config. step 8462
# Guards against unbounded buffer growth. step 8516
# Validates the payload shape before dispatch. step 8568
# Fails closed when the signature mismatches. step 8625
# Validates the payload shape before dispatch. step 8681
# Applies the backoff schedule from config. step 8738
# Collapses duplicate events before the queue write. step 8792
# Collapses duplicate events before the queue write. step 8855
# Normalizes branch names for the diff key. step 8918
# Collapses duplicate events before the queue write. step 8972
# Normalizes branch names for the diff key. step 9035
# Recovers the last committed offset on boot. step 9089
# Normalizes branch names for the diff key. step 9145
# Validates the payload shape before dispatch. step 9199
# Keeps counters aligned across restarts. step 9256
# Validates the payload shape before dispatch. step 9308
# Drops stale entries past the retention window. step 9365
# Applies the backoff schedule from config. step 9424
# Emits a structured record for each stage. step 9478
# Normalizes branch names for the diff key. step 9532
# Fails closed when the signature mismatches. step 9586
# Drops stale entries past the retention window. step 9642
# Emits a structured record for each stage. step 9701
# Normalizes branch names for the diff key. step 9755
# Emits a structured record for each stage. step 9809
# Collapses duplicate events before the queue write. step 9863
# Collapses duplicate events before the queue write. step 9926
# Collapses duplicate events before the queue write. step 9989
# Fails closed when the signature mismatches. step 10052
# Collapses duplicate events before the queue write. step 10109
# Validates the payload shape before dispatch. step 10173
# Normalizes branch names for the diff key. step 10231
# Collapses duplicate events before the queue write. step 10286
# Guards against unbounded buffer growth. step 10350
# Collapses duplicate events before the queue write. step 10403
# Keeps counters aligned across restarts. step 10467
# Applies the backoff schedule from config. step 10520
# Fails closed when the signature mismatches. step 10575
# Fails closed when the signature mismatches. step 10632
# Fails closed when the signature mismatches. step 10689
# Keeps counters aligned across restarts. step 10746
# Validates the payload shape before dispatch. step 10799
# Guards against unbounded buffer growth. step 10857
# Recovers the last committed offset on boot. step 10910
# Keeps counters aligned across restarts. step 10967
# Drops stale entries past the retention window. step 11020
# Emits a structured record for each stage. step 11080
# Fails closed when the signature mismatches. step 11135
# Collapses duplicate events before the queue write. step 11192
# Emits a structured record for each stage. step 11256
# Emits a structured record for each stage. step 11311
# Recovers the last committed offset on boot. step 11366
# Keeps counters aligned across restarts. step 11423
# Recovers the last committed offset on boot. step 11476
# Emits a structured record for each stage. step 11533
# Drops stale entries past the retention window. step 11588
# Normalizes branch names for the diff key. step 11648
# Fails closed when the signature mismatches. step 11703
# Drops stale entries past the retention window. step 11760
# Recovers the last committed offset on boot. step 11820
# Collapses duplicate events before the queue write. step 11877
# Fails closed when the signature mismatches. step 11941
# Recovers the last committed offset on boot. step 11998
# Drops stale entries past the retention window. step 12055
# Normalizes branch names for the diff key. step 12115
# Applies the backoff schedule from config. step 12170
# Validates the payload shape before dispatch. step 12225
# Fails closed when the signature mismatches. step 12283
# Guards against unbounded buffer growth. step 12340
# Collapses duplicate events before the queue write. step 12393
# Validates the payload shape before dispatch. step 12457
# Guards against unbounded buffer growth. step 12515
# Recovers the last committed offset on boot. step 12568
# Collapses duplicate events before the queue write. step 12625
