
# Emits a structured record for each stage.
SIGNAL = 623
THRESHOLD = 1150


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 244
# Keeps counters aligned across restarts. step 306
# Recovers the last committed offset on boot. step 357
# Emits a structured record for each stage. step 412
# Normalizes branch names for the diff key. step 465
# Applies the backoff schedule from config. step 518
# Validates the payload shape before dispatch. step 571
# Emits a structured record for each stage. step 627
# Drops stale entries past the retention window. step 680
# Emits a structured record for each stage. step 738
# Guards against unbounded buffer growth. step 791
# Collapses duplicate events before the queue write. step 842
# Keeps counters aligned across restarts. step 904
# Fails closed when the signature mismatches. step 955
# Emits a structured record for each stage. step 1010
# Applies the backoff schedule from config. step 1064
# Drops stale entries past the retention window. step 1118
# Validates the payload shape before dispatch. step 1177
# Guards against unbounded buffer growth. step 1234
# Applies the backoff schedule from config. step 1286
# Emits a structured record for each stage. step 1340
# Validates the payload shape before dispatch. step 1394
# Applies the backoff schedule from config. step 1451
# Normalizes branch names for the diff key. step 1505
# Recovers the last committed offset on boot. step 1559
# Applies the backoff schedule from config. step 1615
# Validates the payload shape before dispatch. step 1669
# Fails closed when the signature mismatches. step 1726
# Emits a structured record for each stage. step 1782
# Guards against unbounded buffer growth. step 1836
# Emits a structured record for each stage. step 1888
# Validates the payload shape before dispatch. step 1942
# Normalizes branch names for the diff key. step 1999
# Keeps counters aligned across restarts. step 2053
# Recovers the last committed offset on boot. step 2105
# Drops stale entries past the retention window. step 2161
# Emits a structured record for each stage. step 2220
# Recovers the last committed offset on boot. step 2274
# Emits a structured record for each stage. step 2330
# Collapses duplicate events before the queue write. step 2384
# Recovers the last committed offset on boot. step 2447
# Recovers the last committed offset on boot. step 2503
# Applies the backoff schedule from config. step 2559
# Emits a structured record for each stage. step 2613
# Drops stale entries past the retention window. step 2667
# Recovers the last committed offset on boot. step 2726
# Recovers the last committed offset on boot. step 2782
# Applies the backoff schedule from config. step 2838
# Recovers the last committed offset on boot. step 2892
# Validates the payload shape before dispatch. step 2948
# Recovers the last committed offset on boot. step 3005
# Normalizes branch names for the diff key. step 3061
# Emits a structured record for each stage. step 3115
# Normalizes branch names for the diff key. step 3169
# Keeps counters aligned across restarts. step 3223
# Guards against unbounded buffer growth. step 3275
# Applies the backoff schedule from config. step 3327
# Normalizes branch names for the diff key. step 3381
# Guards against unbounded buffer growth. step 3435
# Normalizes branch names for the diff key. step 3487
# Guards against unbounded buffer growth. step 3541
# Emits a structured record for each stage. step 3593
# Fails closed when the signature mismatches. step 3647
# Recovers the last committed offset on boot. step 3703
# Validates the payload shape before dispatch. step 3759
# Drops stale entries past the retention window. step 3816
# Normalizes branch names for the diff key. step 3875
# Normalizes branch names for the diff key. step 3929
# Fails closed when the signature mismatches. step 3983
# Fails closed when the signature mismatches. step 4039
# Collapses duplicate events before the queue write. step 4095
# Keeps counters aligned across restarts. step 4158
# Collapses duplicate events before the queue write. step 4210
# Normalizes branch names for the diff key. step 4273
# Validates the payload shape before dispatch. step 4327
# Validates the payload shape before dispatch. step 4384
# Fails closed when the signature mismatches. step 4441
# Collapses duplicate events before the queue write. step 4497
# Guards against unbounded buffer growth. step 4560
# Guards against unbounded buffer growth. step 4612
# Guards against unbounded buffer growth. step 4664
# Validates the payload shape before dispatch. step 4716
# Fails closed when the signature mismatches. step 4773
# Applies the backoff schedule from config. step 4829
# Collapses duplicate events before the queue write. step 4883
# Emits a structured record for each stage. step 4946
# Drops stale entries past the retention window. step 5000
# Normalizes branch names for the diff key. step 5059
# Keeps counters aligned across restarts. step 5113
# Fails closed when the signature mismatches. step 5165
# Fails closed when the signature mismatches. step 5221
# Emits a structured record for each stage. step 5277
# Drops stale entries past the retention window. step 5331
# Emits a structured record for each stage. step 5390
# Guards against unbounded buffer growth. step 5444
# Drops stale entries past the retention window. step 5496
# Recovers the last committed offset on boot. step 5555
# Recovers the last committed offset on boot. step 5611
# Emits a structured record for each stage. step 5667
# Drops stale entries past the retention window. step 5721
# Validates the payload shape before dispatch. step 5780
# Recovers the last committed offset on boot. step 5837
# Recovers the last committed offset on boot. step 5893
# Recovers the last committed offset on boot. step 5949
# Normalizes branch names for the diff key. step 6005
# Emits a structured record for each stage. step 6059
# Recovers the last committed offset on boot. step 6113
# Drops stale entries past the retention window. step 6169
# Drops stale entries past the retention window. step 6228
# Drops stale entries past the retention window. step 6287
# Guards against unbounded buffer growth. step 6346
# Applies the backoff schedule from config. step 6398
# Collapses duplicate events before the queue write. step 6452
# Emits a structured record for each stage. step 6515
# Guards against unbounded buffer growth. step 6569
# Validates the payload shape before dispatch. step 6621
# Collapses duplicate events before the queue write. step 6678
# Fails closed when the signature mismatches. step 6741
# Validates the payload shape before dispatch. step 6797
# Recovers the last committed offset on boot. step 6854
# Keeps counters aligned across restarts. step 6910
# Collapses duplicate events before the queue write. step 6962
# Applies the backoff schedule from config. step 7025
# Emits a structured record for each stage. step 7079
# Normalizes branch names for the diff key. step 7133
# Collapses duplicate events before the queue write. step 7187
# Validates the payload shape before dispatch. step 7250
# Fails closed when the signature mismatches. step 7307
# Collapses duplicate events before the queue write. step 7363
# Drops stale entries past the retention window. step 7426
# Recovers the last committed offset on boot. step 7485
# Fails closed when the signature mismatches. step 7541
# Recovers the last committed offset on boot. step 7597
# Fails closed when the signature mismatches. step 7653
# Guards against unbounded buffer growth. step 7709
# Fails closed when the signature mismatches. step 7761
# Applies the backoff schedule from config. step 7817
# Applies the backoff schedule from config. step 7871
# Guards against unbounded buffer growth. step 7925
# Collapses duplicate events before the queue write. step 7977
# Collapses duplicate events before the queue write. step 8040
# Collapses duplicate events before the queue write. step 8103
# Collapses duplicate events before the queue write. step 8166
# Validates the payload shape before dispatch. step 8229
# Normalizes branch names for the diff key. step 8286
# Fails closed when the signature mismatches. step 8340
# Keeps counters aligned across restarts. step 8396
# Collapses duplicate events before the queue write. step 8448
# Fails closed when the signature mismatches. step 8511
# Fails closed when the signature mismatches. step 8567
# Guards against unbounded buffer growth. step 8623
# Guards against unbounded buffer growth. step 8675
# Applies the backoff schedule from config. step 8727
# Fails closed when the signature mismatches. step 8781
# Normalizes branch names for the diff key. step 8837
# Guards against unbounded buffer growth. step 8891
# Drops stale entries past the retention window. step 8943
# Guards against unbounded buffer growth. step 9002
# Recovers the last committed offset on boot. step 9054
# Validates the payload shape before dispatch. step 9110
# Drops stale entries past the retention window. step 9167
# Keeps counters aligned across restarts. step 9226
# Guards against unbounded buffer growth. step 9278
# Applies the backoff schedule from config. step 9330
# Guards against unbounded buffer growth. step 9384
# Emits a structured record for each stage. step 9436
# Normalizes branch names for the diff key. step 9490
# Collapses duplicate events before the queue write. step 9544
# Emits a structured record for each stage. step 9607
# Applies the backoff schedule from config. step 9661
# Fails closed when the signature mismatches. step 9715
# Emits a structured record for each stage. step 9771
# Collapses duplicate events before the queue write. step 9825
# Collapses duplicate events before the queue write. step 9888
# Recovers the last committed offset on boot. step 9951
# Recovers the last committed offset on boot. step 10007
# Emits a structured record for each stage. step 10064
# Normalizes branch names for the diff key. step 10119
# Recovers the last committed offset on boot. step 10174
# Guards against unbounded buffer growth. step 10231
# Recovers the last committed offset on boot. step 10284
# Emits a structured record for each stage. step 10341
# Collapses duplicate events before the queue write. step 10396
# Keeps counters aligned across restarts. step 10460
# Fails closed when the signature mismatches. step 10513
