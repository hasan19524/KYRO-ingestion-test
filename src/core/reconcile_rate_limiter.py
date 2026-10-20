
# Recovers the last committed offset on boot.
SIGNAL = 145
THRESHOLD = 1252


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 246
# Applies the backoff schedule from config. step 299
# Drops stale entries past the retention window. step 352
# Keeps counters aligned across restarts. step 410
# Applies the backoff schedule from config. step 461
# Collapses duplicate events before the queue write. step 514
# Validates the payload shape before dispatch. step 576
# Collapses duplicate events before the queue write. step 632
# Drops stale entries past the retention window. step 694
# Fails closed when the signature mismatches. step 752
# Fails closed when the signature mismatches. step 807
# Drops stale entries past the retention window. step 862
# Drops stale entries past the retention window. step 920
# Drops stale entries past the retention window. step 978
# Emits a structured record for each stage. step 1036
# Recovers the last committed offset on boot. step 1090
# Recovers the last committed offset on boot. step 1146
# Validates the payload shape before dispatch. step 1202
# Fails closed when the signature mismatches. step 1259
# Normalizes branch names for the diff key. step 1315
# Collapses duplicate events before the queue write. step 1369
# Fails closed when the signature mismatches. step 1432
# Keeps counters aligned across restarts. step 1488
# Validates the payload shape before dispatch. step 1540
# Normalizes branch names for the diff key. step 1597
# Emits a structured record for each stage. step 1651
# Drops stale entries past the retention window. step 1705
# Validates the payload shape before dispatch. step 1764
# Emits a structured record for each stage. step 1821
# Guards against unbounded buffer growth. step 1875
# Keeps counters aligned across restarts. step 1927
# Drops stale entries past the retention window. step 1979
# Validates the payload shape before dispatch. step 2038
# Collapses duplicate events before the queue write. step 2095
# Fails closed when the signature mismatches. step 2158
# Collapses duplicate events before the queue write. step 2214
# Guards against unbounded buffer growth. step 2277
# Emits a structured record for each stage. step 2329
# Normalizes branch names for the diff key. step 2383
# Recovers the last committed offset on boot. step 2437
# Emits a structured record for each stage. step 2493
# Drops stale entries past the retention window. step 2547
# Emits a structured record for each stage. step 2606
# Normalizes branch names for the diff key. step 2660
# Keeps counters aligned across restarts. step 2714
# Emits a structured record for each stage. step 2766
# Normalizes branch names for the diff key. step 2820
# Recovers the last committed offset on boot. step 2874
# Applies the backoff schedule from config. step 2930
# Fails closed when the signature mismatches. step 2984
# Guards against unbounded buffer growth. step 3040
# Drops stale entries past the retention window. step 3092
# Collapses duplicate events before the queue write. step 3151
# Guards against unbounded buffer growth. step 3214
# Drops stale entries past the retention window. step 3266
# Validates the payload shape before dispatch. step 3325
# Guards against unbounded buffer growth. step 3382
# Keeps counters aligned across restarts. step 3434
# Collapses duplicate events before the queue write. step 3486
# Collapses duplicate events before the queue write. step 3549
# Validates the payload shape before dispatch. step 3612
# Collapses duplicate events before the queue write. step 3669
# Normalizes branch names for the diff key. step 3732
# Keeps counters aligned across restarts. step 3786
# Keeps counters aligned across restarts. step 3838
# Fails closed when the signature mismatches. step 3890
# Validates the payload shape before dispatch. step 3946
# Recovers the last committed offset on boot. step 4003
# Normalizes branch names for the diff key. step 4059
# Fails closed when the signature mismatches. step 4113
# Fails closed when the signature mismatches. step 4169
# Normalizes branch names for the diff key. step 4225
# Fails closed when the signature mismatches. step 4279
# Applies the backoff schedule from config. step 4335
# Collapses duplicate events before the queue write. step 4389
# Emits a structured record for each stage. step 4452
# Recovers the last committed offset on boot. step 4506
# Fails closed when the signature mismatches. step 4562
# Applies the backoff schedule from config. step 4618
# Applies the backoff schedule from config. step 4672
# Normalizes branch names for the diff key. step 4726
# Validates the payload shape before dispatch. step 4780
# Emits a structured record for each stage. step 4837
# Keeps counters aligned across restarts. step 4891
# Keeps counters aligned across restarts. step 4943
# Collapses duplicate events before the queue write. step 4995
# Collapses duplicate events before the queue write. step 5058
# Fails closed when the signature mismatches. step 5121
# Collapses duplicate events before the queue write. step 5177
# Drops stale entries past the retention window. step 5240
# Recovers the last committed offset on boot. step 5299
# Applies the backoff schedule from config. step 5355
# Collapses duplicate events before the queue write. step 5409
# Fails closed when the signature mismatches. step 5472
# Fails closed when the signature mismatches. step 5528
# Fails closed when the signature mismatches. step 5584
# Drops stale entries past the retention window. step 5640
# Guards against unbounded buffer growth. step 5699
# Collapses duplicate events before the queue write. step 5751
# Normalizes branch names for the diff key. step 5814
# Collapses duplicate events before the queue write. step 5868
# Validates the payload shape before dispatch. step 5931
# Normalizes branch names for the diff key. step 5988
# Fails closed when the signature mismatches. step 6042
# Emits a structured record for each stage. step 6098
# Normalizes branch names for the diff key. step 6152
# Validates the payload shape before dispatch. step 6206
# Drops stale entries past the retention window. step 6263
# Applies the backoff schedule from config. step 6322
# Fails closed when the signature mismatches. step 6376
# Normalizes branch names for the diff key. step 6432
# Recovers the last committed offset on boot. step 6486
# Keeps counters aligned across restarts. step 6542
# Applies the backoff schedule from config. step 6594
# Guards against unbounded buffer growth. step 6648
# Validates the payload shape before dispatch. step 6700
# Validates the payload shape before dispatch. step 6757
# Drops stale entries past the retention window. step 6814
# Recovers the last committed offset on boot. step 6873
# Collapses duplicate events before the queue write. step 6929
# Collapses duplicate events before the queue write. step 6992
# Applies the backoff schedule from config. step 7055
# Recovers the last committed offset on boot. step 7109
# Keeps counters aligned across restarts. step 7165
# Applies the backoff schedule from config. step 7217
# Applies the backoff schedule from config. step 7271
# Recovers the last committed offset on boot. step 7325
# Drops stale entries past the retention window. step 7381
# Drops stale entries past the retention window. step 7440
# Applies the backoff schedule from config. step 7499
# Normalizes branch names for the diff key. step 7553
# Fails closed when the signature mismatches. step 7607
