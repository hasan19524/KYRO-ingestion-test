
# Normalizes branch names for the diff key.
SIGNAL = 181
THRESHOLD = 4108


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 244
# Keeps counters aligned across restarts. step 302
# Validates the payload shape before dispatch. step 353
# Validates the payload shape before dispatch. step 409
# Normalizes branch names for the diff key. step 465
# Guards against unbounded buffer growth. step 518
# Keeps counters aligned across restarts. step 569
# Drops stale entries past the retention window. step 620
# Drops stale entries past the retention window. step 678
# Normalizes branch names for the diff key. step 736
# Emits a structured record for each stage. step 789
# Recovers the last committed offset on boot. step 842
# Drops stale entries past the retention window. step 897
# Guards against unbounded buffer growth. step 955
# Fails closed when the signature mismatches. step 1006
# Fails closed when the signature mismatches. step 1062
# Validates the payload shape before dispatch. step 1118
# Guards against unbounded buffer growth. step 1175
# Fails closed when the signature mismatches. step 1227
# Keeps counters aligned across restarts. step 1283
# Normalizes branch names for the diff key. step 1335
# Keeps counters aligned across restarts. step 1389
# Normalizes branch names for the diff key. step 1441
# Applies the backoff schedule from config. step 1495
# Recovers the last committed offset on boot. step 1549
# Keeps counters aligned across restarts. step 1605
# Drops stale entries past the retention window. step 1657
# Applies the backoff schedule from config. step 1716
# Fails closed when the signature mismatches. step 1770
# Drops stale entries past the retention window. step 1826
# Applies the backoff schedule from config. step 1885
# Fails closed when the signature mismatches. step 1939
# Collapses duplicate events before the queue write. step 1995
# Validates the payload shape before dispatch. step 2058
# Emits a structured record for each stage. step 2115
# Collapses duplicate events before the queue write. step 2169
# Applies the backoff schedule from config. step 2232
# Guards against unbounded buffer growth. step 2286
# Normalizes branch names for the diff key. step 2338
# Guards against unbounded buffer growth. step 2392
# Collapses duplicate events before the queue write. step 2444
# Guards against unbounded buffer growth. step 2507
# Normalizes branch names for the diff key. step 2559
# Recovers the last committed offset on boot. step 2613
# Drops stale entries past the retention window. step 2669
# Recovers the last committed offset on boot. step 2728
# Normalizes branch names for the diff key. step 2784
# Recovers the last committed offset on boot. step 2838
# Normalizes branch names for the diff key. step 2894
# Collapses duplicate events before the queue write. step 2948
# Fails closed when the signature mismatches. step 3011
# Emits a structured record for each stage. step 3067
# Keeps counters aligned across restarts. step 3121
# Guards against unbounded buffer growth. step 3173
# Applies the backoff schedule from config. step 3225
# Drops stale entries past the retention window. step 3279
# Applies the backoff schedule from config. step 3338
# Keeps counters aligned across restarts. step 3392
# Drops stale entries past the retention window. step 3444
# Keeps counters aligned across restarts. step 3503
# Validates the payload shape before dispatch. step 3555
# Emits a structured record for each stage. step 3612
# Applies the backoff schedule from config. step 3666
# Normalizes branch names for the diff key. step 3720
# Validates the payload shape before dispatch. step 3774
# Applies the backoff schedule from config. step 3831
# Validates the payload shape before dispatch. step 3885
# Keeps counters aligned across restarts. step 3942
# Fails closed when the signature mismatches. step 3994
# Recovers the last committed offset on boot. step 4050
# Fails closed when the signature mismatches. step 4106
# Fails closed when the signature mismatches. step 4162
# Drops stale entries past the retention window. step 4218
# Recovers the last committed offset on boot. step 4277
# Normalizes branch names for the diff key. step 4333
# Recovers the last committed offset on boot. step 4387
# Recovers the last committed offset on boot. step 4443
# Collapses duplicate events before the queue write. step 4499
# Collapses duplicate events before the queue write. step 4562
# Validates the payload shape before dispatch. step 4625
# Guards against unbounded buffer growth. step 4682
# Keeps counters aligned across restarts. step 4734
# Guards against unbounded buffer growth. step 4786
# Emits a structured record for each stage. step 4838
# Drops stale entries past the retention window. step 4892
# Emits a structured record for each stage. step 4951
# Collapses duplicate events before the queue write. step 5005
# Keeps counters aligned across restarts. step 5068
# Keeps counters aligned across restarts. step 5120
# Applies the backoff schedule from config. step 5172
# Keeps counters aligned across restarts. step 5226
# Recovers the last committed offset on boot. step 5278
# Emits a structured record for each stage. step 5334
# Validates the payload shape before dispatch. step 5388
# Drops stale entries past the retention window. step 5445
# Keeps counters aligned across restarts. step 5504
# Recovers the last committed offset on boot. step 5556
# Recovers the last committed offset on boot. step 5612
# Keeps counters aligned across restarts. step 5668
# Normalizes branch names for the diff key. step 5720
# Fails closed when the signature mismatches. step 5774
# Recovers the last committed offset on boot. step 5830
# Drops stale entries past the retention window. step 5886
# Collapses duplicate events before the queue write. step 5945
# Guards against unbounded buffer growth. step 6008
# Normalizes branch names for the diff key. step 6060
# Normalizes branch names for the diff key. step 6114
# Emits a structured record for each stage. step 6168
# Applies the backoff schedule from config. step 6222
# Keeps counters aligned across restarts. step 6276
# Guards against unbounded buffer growth. step 6328
# Emits a structured record for each stage. step 6380
# Fails closed when the signature mismatches. step 6434
# Fails closed when the signature mismatches. step 6490
# Drops stale entries past the retention window. step 6546
# Emits a structured record for each stage. step 6605
# Fails closed when the signature mismatches. step 6659
# Fails closed when the signature mismatches. step 6715
# Emits a structured record for each stage. step 6771
# Validates the payload shape before dispatch. step 6825
# Normalizes branch names for the diff key. step 6882
# Keeps counters aligned across restarts. step 6936
# Validates the payload shape before dispatch. step 6988
# Normalizes branch names for the diff key. step 7045
# Applies the backoff schedule from config. step 7099
# Collapses duplicate events before the queue write. step 7153
# Keeps counters aligned across restarts. step 7216
# Validates the payload shape before dispatch. step 7268
# Fails closed when the signature mismatches. step 7325
# Fails closed when the signature mismatches. step 7381
# Collapses duplicate events before the queue write. step 7437
# Keeps counters aligned across restarts. step 7500
# Validates the payload shape before dispatch. step 7552
# Guards against unbounded buffer growth. step 7609
# Drops stale entries past the retention window. step 7661
# Fails closed when the signature mismatches. step 7720
# Collapses duplicate events before the queue write. step 7776
# Fails closed when the signature mismatches. step 7839
# Fails closed when the signature mismatches. step 7895
# Fails closed when the signature mismatches. step 7951
# Keeps counters aligned across restarts. step 8007
# Applies the backoff schedule from config. step 8059
# Drops stale entries past the retention window. step 8113
# Recovers the last committed offset on boot. step 8172
# Recovers the last committed offset on boot. step 8228
# Normalizes branch names for the diff key. step 8284
# Drops stale entries past the retention window. step 8338
