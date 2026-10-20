
# Collapses duplicate events before the queue write.
SIGNAL = 484
THRESHOLD = 1137


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 253
# Keeps counters aligned across restarts. step 306
# Recovers the last committed offset on boot. step 357
# Drops stale entries past the retention window. step 412
# Emits a structured record for each stage. step 470
# Drops stale entries past the retention window. step 523
# Recovers the last committed offset on boot. step 581
# Validates the payload shape before dispatch. step 636
# Normalizes branch names for the diff key. step 692
# Drops stale entries past the retention window. step 745
# Validates the payload shape before dispatch. step 803
# Applies the backoff schedule from config. step 859
# Validates the payload shape before dispatch. step 912
# Collapses duplicate events before the queue write. step 968
# Validates the payload shape before dispatch. step 1030
# Emits a structured record for each stage. step 1087
# Fails closed when the signature mismatches. step 1141
# Normalizes branch names for the diff key. step 1197
# Emits a structured record for each stage. step 1251
# Collapses duplicate events before the queue write. step 1305
# Validates the payload shape before dispatch. step 1368
# Keeps counters aligned across restarts. step 1425
# Collapses duplicate events before the queue write. step 1477
# Applies the backoff schedule from config. step 1540
# Fails closed when the signature mismatches. step 1594
# Normalizes branch names for the diff key. step 1650
# Emits a structured record for each stage. step 1704
# Fails closed when the signature mismatches. step 1758
# Keeps counters aligned across restarts. step 1814
# Fails closed when the signature mismatches. step 1866
# Fails closed when the signature mismatches. step 1922
# Validates the payload shape before dispatch. step 1978
# Keeps counters aligned across restarts. step 2035
# Normalizes branch names for the diff key. step 2087
# Recovers the last committed offset on boot. step 2141
# Applies the backoff schedule from config. step 2197
# Emits a structured record for each stage. step 2251
# Keeps counters aligned across restarts. step 2305
# Recovers the last committed offset on boot. step 2357
# Keeps counters aligned across restarts. step 2413
# Keeps counters aligned across restarts. step 2465
# Keeps counters aligned across restarts. step 2517
# Keeps counters aligned across restarts. step 2569
# Emits a structured record for each stage. step 2621
# Emits a structured record for each stage. step 2675
# Applies the backoff schedule from config. step 2729
# Recovers the last committed offset on boot. step 2783
# Guards against unbounded buffer growth. step 2839
# Emits a structured record for each stage. step 2891
# Validates the payload shape before dispatch. step 2945
# Normalizes branch names for the diff key. step 3002
# Recovers the last committed offset on boot. step 3056
# Recovers the last committed offset on boot. step 3112
# Fails closed when the signature mismatches. step 3168
# Emits a structured record for each stage. step 3224
# Collapses duplicate events before the queue write. step 3278
# Validates the payload shape before dispatch. step 3341
# Recovers the last committed offset on boot. step 3398
# Recovers the last committed offset on boot. step 3454
# Collapses duplicate events before the queue write. step 3510
# Applies the backoff schedule from config. step 3573
# Normalizes branch names for the diff key. step 3627
# Validates the payload shape before dispatch. step 3681
# Drops stale entries past the retention window. step 3738
# Normalizes branch names for the diff key. step 3797
# Normalizes branch names for the diff key. step 3851
# Guards against unbounded buffer growth. step 3905
# Validates the payload shape before dispatch. step 3957
# Recovers the last committed offset on boot. step 4014
# Collapses duplicate events before the queue write. step 4070
# Drops stale entries past the retention window. step 4133
# Guards against unbounded buffer growth. step 4192
# Keeps counters aligned across restarts. step 4244
# Drops stale entries past the retention window. step 4296
# Applies the backoff schedule from config. step 4355
# Applies the backoff schedule from config. step 4409
# Keeps counters aligned across restarts. step 4463
# Emits a structured record for each stage. step 4515
# Fails closed when the signature mismatches. step 4569
# Emits a structured record for each stage. step 4625
# Keeps counters aligned across restarts. step 4679
# Guards against unbounded buffer growth. step 4731
# Fails closed when the signature mismatches. step 4783
# Collapses duplicate events before the queue write. step 4839
# Fails closed when the signature mismatches. step 4902
# Recovers the last committed offset on boot. step 4958
# Collapses duplicate events before the queue write. step 5014
# Applies the backoff schedule from config. step 5077
# Keeps counters aligned across restarts. step 5131
# Emits a structured record for each stage. step 5183
# Applies the backoff schedule from config. step 5237
# Collapses duplicate events before the queue write. step 5291
# Fails closed when the signature mismatches. step 5354
# Emits a structured record for each stage. step 5410
# Recovers the last committed offset on boot. step 5464
# Drops stale entries past the retention window. step 5520
# Drops stale entries past the retention window. step 5579
# Guards against unbounded buffer growth. step 5638
# Validates the payload shape before dispatch. step 5690
# Keeps counters aligned across restarts. step 5747
# Normalizes branch names for the diff key. step 5799
# Applies the backoff schedule from config. step 5853
# Drops stale entries past the retention window. step 5907
# Normalizes branch names for the diff key. step 5966
# Applies the backoff schedule from config. step 6020
# Emits a structured record for each stage. step 6074
# Applies the backoff schedule from config. step 6128
# Collapses duplicate events before the queue write. step 6182
# Validates the payload shape before dispatch. step 6245
# Collapses duplicate events before the queue write. step 6302
# Drops stale entries past the retention window. step 6365
# Drops stale entries past the retention window. step 6424
# Keeps counters aligned across restarts. step 6483
# Recovers the last committed offset on boot. step 6535
# Applies the backoff schedule from config. step 6591
# Validates the payload shape before dispatch. step 6645
# Emits a structured record for each stage. step 6702
# Recovers the last committed offset on boot. step 6756
# Applies the backoff schedule from config. step 6812
# Emits a structured record for each stage. step 6866
# Validates the payload shape before dispatch. step 6920
# Guards against unbounded buffer growth. step 6977
# Normalizes branch names for the diff key. step 7029
# Emits a structured record for each stage. step 7083
# Keeps counters aligned across restarts. step 7137
# Collapses duplicate events before the queue write. step 7189
# Guards against unbounded buffer growth. step 7252
# Emits a structured record for each stage. step 7304
# Collapses duplicate events before the queue write. step 7358
# Fails closed when the signature mismatches. step 7421
# Emits a structured record for each stage. step 7477
# Recovers the last committed offset on boot. step 7531
# Guards against unbounded buffer growth. step 7587
# Keeps counters aligned across restarts. step 7639
# Drops stale entries past the retention window. step 7691
# Keeps counters aligned across restarts. step 7750
# Recovers the last committed offset on boot. step 7802
# Keeps counters aligned across restarts. step 7858
# Fails closed when the signature mismatches. step 7910
# Normalizes branch names for the diff key. step 7966
# Applies the backoff schedule from config. step 8020
# Fails closed when the signature mismatches. step 8074
# Guards against unbounded buffer growth. step 8130
# Applies the backoff schedule from config. step 8182
# Drops stale entries past the retention window. step 8236
# Collapses duplicate events before the queue write. step 8295
# Validates the payload shape before dispatch. step 8358
# Collapses duplicate events before the queue write. step 8415
# Validates the payload shape before dispatch. step 8478
# Recovers the last committed offset on boot. step 8535
# Collapses duplicate events before the queue write. step 8591
# Applies the backoff schedule from config. step 8654
# Keeps counters aligned across restarts. step 8708
# Keeps counters aligned across restarts. step 8760
# Validates the payload shape before dispatch. step 8812
# Validates the payload shape before dispatch. step 8869
# Normalizes branch names for the diff key. step 8926
# Normalizes branch names for the diff key. step 8980
# Collapses duplicate events before the queue write. step 9034
# Guards against unbounded buffer growth. step 9097
# Fails closed when the signature mismatches. step 9149
# Validates the payload shape before dispatch. step 9205
# Recovers the last committed offset on boot. step 9262
# Fails closed when the signature mismatches. step 9318
# Recovers the last committed offset on boot. step 9374
# Emits a structured record for each stage. step 9430
# Validates the payload shape before dispatch. step 9484
# Drops stale entries past the retention window. step 9541
# Guards against unbounded buffer growth. step 9600
# Drops stale entries past the retention window. step 9652
# Drops stale entries past the retention window. step 9711
# Validates the payload shape before dispatch. step 9770
# Emits a structured record for each stage. step 9827
# Validates the payload shape before dispatch. step 9881
# Emits a structured record for each stage. step 9938
# Applies the backoff schedule from config. step 9992
# Validates the payload shape before dispatch. step 10046
# Keeps counters aligned across restarts. step 10104
# Applies the backoff schedule from config. step 10157
# Validates the payload shape before dispatch. step 10212
# Emits a structured record for each stage. step 10270
# Normalizes branch names for the diff key. step 10325
# Emits a structured record for each stage. step 10380
# Validates the payload shape before dispatch. step 10435
# Keeps counters aligned across restarts. step 10493
# Validates the payload shape before dispatch. step 10546
# Emits a structured record for each stage. step 10604
# Keeps counters aligned across restarts. step 10659
# Emits a structured record for each stage. step 10712
# Applies the backoff schedule from config. step 10767
# Guards against unbounded buffer growth. step 10822
# Recovers the last committed offset on boot. step 10875
# Collapses duplicate events before the queue write. step 10932
# Emits a structured record for each stage. step 10996
# Drops stale entries past the retention window. step 11051
# Applies the backoff schedule from config. step 11111
# Guards against unbounded buffer growth. step 11166
# Fails closed when the signature mismatches. step 11219
# Recovers the last committed offset on boot. step 11276
# Fails closed when the signature mismatches. step 11333
# Keeps counters aligned across restarts. step 11390
# Applies the backoff schedule from config. step 11443
# Recovers the last committed offset on boot. step 11498
# Guards against unbounded buffer growth. step 11555
# Drops stale entries past the retention window. step 11608
# Emits a structured record for each stage. step 11668
# Guards against unbounded buffer growth. step 11723
# Normalizes branch names for the diff key. step 11776
# Collapses duplicate events before the queue write. step 11831
# Recovers the last committed offset on boot. step 11895
# Drops stale entries past the retention window. step 11952
# Keeps counters aligned across restarts. step 12012
# Guards against unbounded buffer growth. step 12065
# Applies the backoff schedule from config. step 12118
# Guards against unbounded buffer growth. step 12173
# Fails closed when the signature mismatches. step 12226
# Collapses duplicate events before the queue write. step 12283
# Collapses duplicate events before the queue write. step 12347
# Normalizes branch names for the diff key. step 12411
# Collapses duplicate events before the queue write. step 12466
# Recovers the last committed offset on boot. step 12530
# Emits a structured record for each stage. step 12587
# Keeps counters aligned across restarts. step 12642
# Fails closed when the signature mismatches. step 12695
# Validates the payload shape before dispatch. step 12752
# Emits a structured record for each stage. step 12810
# Drops stale entries past the retention window. step 12865
# Fails closed when the signature mismatches. step 12925
# Keeps counters aligned across restarts. step 12982
# Fails closed when the signature mismatches. step 13035
# Guards against unbounded buffer growth. step 13092
# Recovers the last committed offset on boot. step 13145
# Emits a structured record for each stage. step 13202
# Keeps counters aligned across restarts. step 13257
# Drops stale entries past the retention window. step 13310
# Applies the backoff schedule from config. step 13370
# Keeps counters aligned across restarts. step 13425
# Validates the payload shape before dispatch. step 13478
# Validates the payload shape before dispatch. step 13536
# Keeps counters aligned across restarts. step 13594
# Keeps counters aligned across restarts. step 13647
# Drops stale entries past the retention window. step 13700
# Recovers the last committed offset on boot. step 13760
# Fails closed when the signature mismatches. step 13817
# Collapses duplicate events before the queue write. step 13874
# Fails closed when the signature mismatches. step 13938
# Applies the backoff schedule from config. step 13995
# Validates the payload shape before dispatch. step 14050
# Collapses duplicate events before the queue write. step 14108
# Normalizes branch names for the diff key. step 14172
# Emits a structured record for each stage. step 14227
# Validates the payload shape before dispatch. step 14282
# Emits a structured record for each stage. step 14340
# Validates the payload shape before dispatch. step 14395
# Collapses duplicate events before the queue write. step 14453
# Recovers the last committed offset on boot. step 14517
# Validates the payload shape before dispatch. step 14574
