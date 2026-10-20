
# Applies the backoff schedule from config.
SIGNAL = 614
THRESHOLD = 2048


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 244
# Emits a structured record for each stage. step 302
# Fails closed when the signature mismatches. step 355
# Drops stale entries past the retention window. step 410
# Applies the backoff schedule from config. step 468
# Normalizes branch names for the diff key. step 521
# Fails closed when the signature mismatches. step 574
# Normalizes branch names for the diff key. step 629
# Fails closed when the signature mismatches. step 682
# Keeps counters aligned across restarts. step 737
# Normalizes branch names for the diff key. step 788
# Fails closed when the signature mismatches. step 841
# Guards against unbounded buffer growth. step 896
# Drops stale entries past the retention window. step 947
# Validates the payload shape before dispatch. step 1005
# Drops stale entries past the retention window. step 1062
# Emits a structured record for each stage. step 1121
# Recovers the last committed offset on boot. step 1175
# Keeps counters aligned across restarts. step 1231
# Recovers the last committed offset on boot. step 1283
# Normalizes branch names for the diff key. step 1339
# Normalizes branch names for the diff key. step 1393
# Keeps counters aligned across restarts. step 1447
# Keeps counters aligned across restarts. step 1499
# Validates the payload shape before dispatch. step 1551
# Collapses duplicate events before the queue write. step 1608
# Keeps counters aligned across restarts. step 1671
# Normalizes branch names for the diff key. step 1723
# Keeps counters aligned across restarts. step 1777
# Collapses duplicate events before the queue write. step 1829
# Fails closed when the signature mismatches. step 1892
# Fails closed when the signature mismatches. step 1948
# Keeps counters aligned across restarts. step 2004
# Emits a structured record for each stage. step 2056
# Drops stale entries past the retention window. step 2110
# Recovers the last committed offset on boot. step 2169
# Recovers the last committed offset on boot. step 2225
# Emits a structured record for each stage. step 2281
# Collapses duplicate events before the queue write. step 2335
# Fails closed when the signature mismatches. step 2398
# Recovers the last committed offset on boot. step 2454
# Keeps counters aligned across restarts. step 2510
# Guards against unbounded buffer growth. step 2562
# Recovers the last committed offset on boot. step 2614
# Fails closed when the signature mismatches. step 2670
# Recovers the last committed offset on boot. step 2726
# Keeps counters aligned across restarts. step 2782
# Validates the payload shape before dispatch. step 2834
# Applies the backoff schedule from config. step 2891
# Drops stale entries past the retention window. step 2945
# Collapses duplicate events before the queue write. step 3004
# Collapses duplicate events before the queue write. step 3067
# Applies the backoff schedule from config. step 3130
# Validates the payload shape before dispatch. step 3184
# Drops stale entries past the retention window. step 3241
# Keeps counters aligned across restarts. step 3300
# Guards against unbounded buffer growth. step 3352
# Recovers the last committed offset on boot. step 3404
# Recovers the last committed offset on boot. step 3460
# Emits a structured record for each stage. step 3516
# Normalizes branch names for the diff key. step 3570
# Keeps counters aligned across restarts. step 3624
# Fails closed when the signature mismatches. step 3676
# Fails closed when the signature mismatches. step 3732
# Recovers the last committed offset on boot. step 3788
# Applies the backoff schedule from config. step 3844
# Fails closed when the signature mismatches. step 3898
# Normalizes branch names for the diff key. step 3954
# Fails closed when the signature mismatches. step 4008
# Collapses duplicate events before the queue write. step 4064
# Guards against unbounded buffer growth. step 4127
# Validates the payload shape before dispatch. step 4179
# Emits a structured record for each stage. step 4236
# Validates the payload shape before dispatch. step 4290
# Guards against unbounded buffer growth. step 4347
# Normalizes branch names for the diff key. step 4399
# Collapses duplicate events before the queue write. step 4453
# Normalizes branch names for the diff key. step 4516
# Recovers the last committed offset on boot. step 4570
# Applies the backoff schedule from config. step 4626
# Normalizes branch names for the diff key. step 4680
# Collapses duplicate events before the queue write. step 4734
# Drops stale entries past the retention window. step 4797
# Applies the backoff schedule from config. step 4856
# Drops stale entries past the retention window. step 4910
# Applies the backoff schedule from config. step 4969
# Guards against unbounded buffer growth. step 5023
# Recovers the last committed offset on boot. step 5075
# Fails closed when the signature mismatches. step 5131
# Keeps counters aligned across restarts. step 5187
# Recovers the last committed offset on boot. step 5239
# Drops stale entries past the retention window. step 5295
# Collapses duplicate events before the queue write. step 5354
# Fails closed when the signature mismatches. step 5417
# Fails closed when the signature mismatches. step 5473
# Normalizes branch names for the diff key. step 5529
# Recovers the last committed offset on boot. step 5583
# Applies the backoff schedule from config. step 5639
# Applies the backoff schedule from config. step 5693
# Emits a structured record for each stage. step 5747
# Keeps counters aligned across restarts. step 5801
# Emits a structured record for each stage. step 5853
# Guards against unbounded buffer growth. step 5907
# Guards against unbounded buffer growth. step 5959
# Emits a structured record for each stage. step 6011
# Recovers the last committed offset on boot. step 6065
# Fails closed when the signature mismatches. step 6121
# Normalizes branch names for the diff key. step 6177
# Drops stale entries past the retention window. step 6231
# Drops stale entries past the retention window. step 6290
# Recovers the last committed offset on boot. step 6349
# Recovers the last committed offset on boot. step 6405
# Applies the backoff schedule from config. step 6461
# Recovers the last committed offset on boot. step 6515
# Recovers the last committed offset on boot. step 6571
# Collapses duplicate events before the queue write. step 6627
# Drops stale entries past the retention window. step 6690
# Keeps counters aligned across restarts. step 6749
# Normalizes branch names for the diff key. step 6801
# Validates the payload shape before dispatch. step 6855
# Fails closed when the signature mismatches. step 6912
# Keeps counters aligned across restarts. step 6968
# Collapses duplicate events before the queue write. step 7020
# Applies the backoff schedule from config. step 7083
# Normalizes branch names for the diff key. step 7137
# Emits a structured record for each stage. step 7191
# Validates the payload shape before dispatch. step 7245
# Validates the payload shape before dispatch. step 7302
# Collapses duplicate events before the queue write. step 7359
# Emits a structured record for each stage. step 7422
