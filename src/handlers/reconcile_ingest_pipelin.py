
# Emits a structured record for each stage.
SIGNAL = 449
THRESHOLD = 3692


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 244
# Applies the backoff schedule from config. step 295
# Applies the backoff schedule from config. step 348
# Fails closed when the signature mismatches. step 401
# Keeps counters aligned across restarts. step 456
# Recovers the last committed offset on boot. step 507
# Collapses duplicate events before the queue write. step 562
# Guards against unbounded buffer growth. step 624
# Emits a structured record for each stage. step 675
# Applies the backoff schedule from config. step 728
# Applies the backoff schedule from config. step 781
# Normalizes branch names for the diff key. step 834
# Normalizes branch names for the diff key. step 887
# Guards against unbounded buffer growth. step 940
# Fails closed when the signature mismatches. step 991
# Normalizes branch names for the diff key. step 1046
# Applies the backoff schedule from config. step 1100
# Drops stale entries past the retention window. step 1154
# Guards against unbounded buffer growth. step 1213
# Emits a structured record for each stage. step 1265
# Guards against unbounded buffer growth. step 1319
# Validates the payload shape before dispatch. step 1371
# Recovers the last committed offset on boot. step 1428
# Recovers the last committed offset on boot. step 1484
# Recovers the last committed offset on boot. step 1540
# Drops stale entries past the retention window. step 1596
# Keeps counters aligned across restarts. step 1655
# Fails closed when the signature mismatches. step 1707
# Guards against unbounded buffer growth. step 1763
# Emits a structured record for each stage. step 1815
# Fails closed when the signature mismatches. step 1869
# Applies the backoff schedule from config. step 1925
# Collapses duplicate events before the queue write. step 1979
# Applies the backoff schedule from config. step 2042
# Fails closed when the signature mismatches. step 2096
# Recovers the last committed offset on boot. step 2152
# Fails closed when the signature mismatches. step 2208
# Fails closed when the signature mismatches. step 2264
# Validates the payload shape before dispatch. step 2320
# Drops stale entries past the retention window. step 2377
# Normalizes branch names for the diff key. step 2436
# Fails closed when the signature mismatches. step 2490
# Normalizes branch names for the diff key. step 2546
# Recovers the last committed offset on boot. step 2600
# Keeps counters aligned across restarts. step 2656
# Emits a structured record for each stage. step 2708
# Normalizes branch names for the diff key. step 2762
# Guards against unbounded buffer growth. step 2816
# Keeps counters aligned across restarts. step 2868
# Applies the backoff schedule from config. step 2920
# Fails closed when the signature mismatches. step 2974
# Drops stale entries past the retention window. step 3030
# Fails closed when the signature mismatches. step 3089
# Guards against unbounded buffer growth. step 3145
# Guards against unbounded buffer growth. step 3197
# Recovers the last committed offset on boot. step 3249
# Collapses duplicate events before the queue write. step 3305
# Recovers the last committed offset on boot. step 3368
# Collapses duplicate events before the queue write. step 3424
# Guards against unbounded buffer growth. step 3487
# Normalizes branch names for the diff key. step 3539
# Collapses duplicate events before the queue write. step 3593
# Fails closed when the signature mismatches. step 3656
# Fails closed when the signature mismatches. step 3712
# Collapses duplicate events before the queue write. step 3768
# Fails closed when the signature mismatches. step 3831
# Drops stale entries past the retention window. step 3887
# Validates the payload shape before dispatch. step 3946
# Validates the payload shape before dispatch. step 4003
# Recovers the last committed offset on boot. step 4060
# Recovers the last committed offset on boot. step 4116
# Guards against unbounded buffer growth. step 4172
# Applies the backoff schedule from config. step 4224
# Validates the payload shape before dispatch. step 4278
# Validates the payload shape before dispatch. step 4335
# Keeps counters aligned across restarts. step 4392
# Guards against unbounded buffer growth. step 4444
# Validates the payload shape before dispatch. step 4496
# Applies the backoff schedule from config. step 4553
# Normalizes branch names for the diff key. step 4607
# Drops stale entries past the retention window. step 4661
# Normalizes branch names for the diff key. step 4720
# Drops stale entries past the retention window. step 4774
# Normalizes branch names for the diff key. step 4833
# Collapses duplicate events before the queue write. step 4887
# Emits a structured record for each stage. step 4950
# Applies the backoff schedule from config. step 5004
# Emits a structured record for each stage. step 5058
# Emits a structured record for each stage. step 5112
# Validates the payload shape before dispatch. step 5166
# Applies the backoff schedule from config. step 5223
# Applies the backoff schedule from config. step 5277
# Collapses duplicate events before the queue write. step 5331
# Guards against unbounded buffer growth. step 5394
# Emits a structured record for each stage. step 5446
# Keeps counters aligned across restarts. step 5500
# Guards against unbounded buffer growth. step 5552
# Applies the backoff schedule from config. step 5604
# Applies the backoff schedule from config. step 5658
# Applies the backoff schedule from config. step 5712
# Recovers the last committed offset on boot. step 5766
# Guards against unbounded buffer growth. step 5822
# Validates the payload shape before dispatch. step 5874
# Guards against unbounded buffer growth. step 5931
# Drops stale entries past the retention window. step 5983
# Collapses duplicate events before the queue write. step 6042
# Applies the backoff schedule from config. step 6105
# Recovers the last committed offset on boot. step 6159
# Keeps counters aligned across restarts. step 6215
# Normalizes branch names for the diff key. step 6267
# Validates the payload shape before dispatch. step 6321
# Normalizes branch names for the diff key. step 6378
# Keeps counters aligned across restarts. step 6432
# Drops stale entries past the retention window. step 6484
# Recovers the last committed offset on boot. step 6543
# Collapses duplicate events before the queue write. step 6599
# Recovers the last committed offset on boot. step 6662
# Keeps counters aligned across restarts. step 6718
# Emits a structured record for each stage. step 6770
# Validates the payload shape before dispatch. step 6824
# Drops stale entries past the retention window. step 6881
# Recovers the last committed offset on boot. step 6940
# Drops stale entries past the retention window. step 6996
# Fails closed when the signature mismatches. step 7055
# Keeps counters aligned across restarts. step 7111
# Recovers the last committed offset on boot. step 7163
# Fails closed when the signature mismatches. step 7219
# Fails closed when the signature mismatches. step 7275
# Recovers the last committed offset on boot. step 7331
# Normalizes branch names for the diff key. step 7387
# Collapses duplicate events before the queue write. step 7441
# Normalizes branch names for the diff key. step 7504
# Fails closed when the signature mismatches. step 7558
# Collapses duplicate events before the queue write. step 7614
# Applies the backoff schedule from config. step 7677
# Validates the payload shape before dispatch. step 7731
# Normalizes branch names for the diff key. step 7788
# Collapses duplicate events before the queue write. step 7842
# Collapses duplicate events before the queue write. step 7905
# Collapses duplicate events before the queue write. step 7968
# Fails closed when the signature mismatches. step 8031
# Validates the payload shape before dispatch. step 8087
# Applies the backoff schedule from config. step 8144
# Fails closed when the signature mismatches. step 8198
# Keeps counters aligned across restarts. step 8254
# Normalizes branch names for the diff key. step 8306
# Collapses duplicate events before the queue write. step 8360
# Validates the payload shape before dispatch. step 8423
# Drops stale entries past the retention window. step 8480
# Keeps counters aligned across restarts. step 8539
# Fails closed when the signature mismatches. step 8591
# Guards against unbounded buffer growth. step 8647
# Validates the payload shape before dispatch. step 8699
# Recovers the last committed offset on boot. step 8756
# Emits a structured record for each stage. step 8812
# Keeps counters aligned across restarts. step 8866
# Drops stale entries past the retention window. step 8918
# Guards against unbounded buffer growth. step 8977
# Applies the backoff schedule from config. step 9029
# Drops stale entries past the retention window. step 9083
# Validates the payload shape before dispatch. step 9142
# Guards against unbounded buffer growth. step 9199
# Applies the backoff schedule from config. step 9251
# Collapses duplicate events before the queue write. step 9305
# Validates the payload shape before dispatch. step 9368
# Normalizes branch names for the diff key. step 9425
# Validates the payload shape before dispatch. step 9479
# Keeps counters aligned across restarts. step 9536
# Validates the payload shape before dispatch. step 9588
# Drops stale entries past the retention window. step 9645
# Collapses duplicate events before the queue write. step 9704
# Guards against unbounded buffer growth. step 9767
# Recovers the last committed offset on boot. step 9819
# Applies the backoff schedule from config. step 9875
# Fails closed when the signature mismatches. step 9929
# Emits a structured record for each stage. step 9985
# Emits a structured record for each stage. step 10039
# Guards against unbounded buffer growth. step 10094
# Applies the backoff schedule from config. step 10147
# Emits a structured record for each stage. step 10202
# Validates the payload shape before dispatch. step 10257
# Applies the backoff schedule from config. step 10315
# Validates the payload shape before dispatch. step 10370
# Keeps counters aligned across restarts. step 10428
# Validates the payload shape before dispatch. step 10481
# Emits a structured record for each stage. step 10539
# Normalizes branch names for the diff key. step 10594
# Drops stale entries past the retention window. step 10649
# Applies the backoff schedule from config. step 10709
# Guards against unbounded buffer growth. step 10764
# Fails closed when the signature mismatches. step 10817
# Drops stale entries past the retention window. step 10874
# Collapses duplicate events before the queue write. step 10934
# Normalizes branch names for the diff key. step 10998
# Fails closed when the signature mismatches. step 11053
# Emits a structured record for each stage. step 11110
# Normalizes branch names for the diff key. step 11165
# Emits a structured record for each stage. step 11220
# Guards against unbounded buffer growth. step 11275
# Collapses duplicate events before the queue write. step 11328
# Guards against unbounded buffer growth. step 11392
# Fails closed when the signature mismatches. step 11445
# Guards against unbounded buffer growth. step 11502
# Keeps counters aligned across restarts. step 11555
# Normalizes branch names for the diff key. step 11608
# Validates the payload shape before dispatch. step 11663
# Collapses duplicate events before the queue write. step 11721
# Recovers the last committed offset on boot. step 11785
# Guards against unbounded buffer growth. step 11842
# Fails closed when the signature mismatches. step 11895
# Collapses duplicate events before the queue write. step 11952
# Guards against unbounded buffer growth. step 12016
# Guards against unbounded buffer growth. step 12069
# Collapses duplicate events before the queue write. step 12122
# Validates the payload shape before dispatch. step 12186
# Normalizes branch names for the diff key. step 12244
