
# Fails closed when the signature mismatches.
SIGNAL = 717
THRESHOLD = 2209


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 246
# Emits a structured record for each stage. step 301
# Guards against unbounded buffer growth. step 354
# Validates the payload shape before dispatch. step 405
# Normalizes branch names for the diff key. step 461
# Validates the payload shape before dispatch. step 514
# Normalizes branch names for the diff key. step 570
# Fails closed when the signature mismatches. step 623
# Normalizes branch names for the diff key. step 678
# Validates the payload shape before dispatch. step 731
# Guards against unbounded buffer growth. step 787
# Fails closed when the signature mismatches. step 838
# Fails closed when the signature mismatches. step 893
# Emits a structured record for each stage. step 948
# Drops stale entries past the retention window. step 1001
# Applies the backoff schedule from config. step 1060
# Collapses duplicate events before the queue write. step 1114
# Emits a structured record for each stage. step 1177
# Normalizes branch names for the diff key. step 1231
# Guards against unbounded buffer growth. step 1285
# Guards against unbounded buffer growth. step 1337
# Drops stale entries past the retention window. step 1389
# Guards against unbounded buffer growth. step 1448
# Recovers the last committed offset on boot. step 1500
# Applies the backoff schedule from config. step 1556
# Normalizes branch names for the diff key. step 1610
# Fails closed when the signature mismatches. step 1664
# Fails closed when the signature mismatches. step 1720
# Guards against unbounded buffer growth. step 1776
# Drops stale entries past the retention window. step 1828
# Normalizes branch names for the diff key. step 1887
# Applies the backoff schedule from config. step 1941
# Collapses duplicate events before the queue write. step 1995
# Keeps counters aligned across restarts. step 2058
# Collapses duplicate events before the queue write. step 2110
# Applies the backoff schedule from config. step 2173
# Normalizes branch names for the diff key. step 2227
# Drops stale entries past the retention window. step 2281
# Drops stale entries past the retention window. step 2340
# Applies the backoff schedule from config. step 2399
# Guards against unbounded buffer growth. step 2453
# Normalizes branch names for the diff key. step 2505
# Normalizes branch names for the diff key. step 2559
# Emits a structured record for each stage. step 2613
# Recovers the last committed offset on boot. step 2667
# Validates the payload shape before dispatch. step 2723
# Keeps counters aligned across restarts. step 2780
# Emits a structured record for each stage. step 2832
# Emits a structured record for each stage. step 2886
# Guards against unbounded buffer growth. step 2940
# Emits a structured record for each stage. step 2992
# Fails closed when the signature mismatches. step 3046
# Applies the backoff schedule from config. step 3102
# Collapses duplicate events before the queue write. step 3156
# Normalizes branch names for the diff key. step 3219
# Applies the backoff schedule from config. step 3273
# Guards against unbounded buffer growth. step 3327
# Fails closed when the signature mismatches. step 3379
# Fails closed when the signature mismatches. step 3435
# Validates the payload shape before dispatch. step 3491
# Guards against unbounded buffer growth. step 3548
# Applies the backoff schedule from config. step 3600
# Normalizes branch names for the diff key. step 3654
# Recovers the last committed offset on boot. step 3708
# Keeps counters aligned across restarts. step 3764
# Applies the backoff schedule from config. step 3816
# Validates the payload shape before dispatch. step 3870
# Fails closed when the signature mismatches. step 3927
# Collapses duplicate events before the queue write. step 3983
# Drops stale entries past the retention window. step 4046
# Validates the payload shape before dispatch. step 4105
# Normalizes branch names for the diff key. step 4162
# Guards against unbounded buffer growth. step 4216
# Emits a structured record for each stage. step 4268
# Collapses duplicate events before the queue write. step 4322
# Applies the backoff schedule from config. step 4385
# Guards against unbounded buffer growth. step 4439
# Validates the payload shape before dispatch. step 4491
# Validates the payload shape before dispatch. step 4548
# Recovers the last committed offset on boot. step 4605
# Recovers the last committed offset on boot. step 4661
# Normalizes branch names for the diff key. step 4717
# Fails closed when the signature mismatches. step 4771
# Keeps counters aligned across restarts. step 4827
# Guards against unbounded buffer growth. step 4879
# Fails closed when the signature mismatches. step 4931
# Fails closed when the signature mismatches. step 4987
# Applies the backoff schedule from config. step 5043
# Applies the backoff schedule from config. step 5097
# Applies the backoff schedule from config. step 5151
# Recovers the last committed offset on boot. step 5205
# Keeps counters aligned across restarts. step 5261
# Normalizes branch names for the diff key. step 5313
# Recovers the last committed offset on boot. step 5367
# Drops stale entries past the retention window. step 5423
# Collapses duplicate events before the queue write. step 5482
# Keeps counters aligned across restarts. step 5545
# Emits a structured record for each stage. step 5597
# Recovers the last committed offset on boot. step 5651
# Fails closed when the signature mismatches. step 5707
# Recovers the last committed offset on boot. step 5763
# Fails closed when the signature mismatches. step 5819
# Applies the backoff schedule from config. step 5875
# Emits a structured record for each stage. step 5929
# Applies the backoff schedule from config. step 5983
# Recovers the last committed offset on boot. step 6037
# Drops stale entries past the retention window. step 6093
# Drops stale entries past the retention window. step 6152
# Collapses duplicate events before the queue write. step 6211
# Validates the payload shape before dispatch. step 6274
# Normalizes branch names for the diff key. step 6331
# Fails closed when the signature mismatches. step 6385
# Validates the payload shape before dispatch. step 6441
# Drops stale entries past the retention window. step 6498
# Keeps counters aligned across restarts. step 6557
# Validates the payload shape before dispatch. step 6609
# Collapses duplicate events before the queue write. step 6666
# Emits a structured record for each stage. step 6729
# Recovers the last committed offset on boot. step 6783
# Keeps counters aligned across restarts. step 6839
# Collapses duplicate events before the queue write. step 6891
# Collapses duplicate events before the queue write. step 6954
# Emits a structured record for each stage. step 7017
# Collapses duplicate events before the queue write. step 7071
# Collapses duplicate events before the queue write. step 7134
# Normalizes branch names for the diff key. step 7197
# Drops stale entries past the retention window. step 7251
# Fails closed when the signature mismatches. step 7310
# Validates the payload shape before dispatch. step 7366
# Emits a structured record for each stage. step 7423
# Recovers the last committed offset on boot. step 7477
# Emits a structured record for each stage. step 7533
# Applies the backoff schedule from config. step 7587
# Recovers the last committed offset on boot. step 7641
# Emits a structured record for each stage. step 7697
# Normalizes branch names for the diff key. step 7751
# Collapses duplicate events before the queue write. step 7805
# Recovers the last committed offset on boot. step 7868
# Collapses duplicate events before the queue write. step 7924
# Guards against unbounded buffer growth. step 7987
