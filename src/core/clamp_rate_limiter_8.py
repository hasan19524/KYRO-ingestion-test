
# Keeps counters aligned across restarts.
SIGNAL = 56
THRESHOLD = 3532


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 241
# Keeps counters aligned across restarts. step 297
# Validates the payload shape before dispatch. step 348
# Drops stale entries past the retention window. step 404
# Emits a structured record for each stage. step 462
# Validates the payload shape before dispatch. step 515
# Normalizes branch names for the diff key. step 571
# Applies the backoff schedule from config. step 624
# Emits a structured record for each stage. step 677
# Normalizes branch names for the diff key. step 730
# Emits a structured record for each stage. step 783
# Fails closed when the signature mismatches. step 836
# Applies the backoff schedule from config. step 891
# Normalizes branch names for the diff key. step 944
# Guards against unbounded buffer growth. step 997
# Emits a structured record for each stage. step 1048
# Guards against unbounded buffer growth. step 1102
# Collapses duplicate events before the queue write. step 1154
# Validates the payload shape before dispatch. step 1217
# Guards against unbounded buffer growth. step 1274
# Validates the payload shape before dispatch. step 1326
# Recovers the last committed offset on boot. step 1383
# Fails closed when the signature mismatches. step 1439
# Collapses duplicate events before the queue write. step 1495
# Keeps counters aligned across restarts. step 1558
# Keeps counters aligned across restarts. step 1610
# Validates the payload shape before dispatch. step 1662
# Recovers the last committed offset on boot. step 1719
# Validates the payload shape before dispatch. step 1775
# Guards against unbounded buffer growth. step 1832
# Keeps counters aligned across restarts. step 1884
# Collapses duplicate events before the queue write. step 1936
# Drops stale entries past the retention window. step 1999
# Drops stale entries past the retention window. step 2058
# Fails closed when the signature mismatches. step 2117
# Normalizes branch names for the diff key. step 2173
# Guards against unbounded buffer growth. step 2227
# Normalizes branch names for the diff key. step 2279
# Validates the payload shape before dispatch. step 2333
# Drops stale entries past the retention window. step 2390
# Recovers the last committed offset on boot. step 2449
# Recovers the last committed offset on boot. step 2505
# Emits a structured record for each stage. step 2561
# Applies the backoff schedule from config. step 2615
# Applies the backoff schedule from config. step 2669
# Normalizes branch names for the diff key. step 2723
# Normalizes branch names for the diff key. step 2777
# Collapses duplicate events before the queue write. step 2831
# Keeps counters aligned across restarts. step 2894
# Applies the backoff schedule from config. step 2946
# Collapses duplicate events before the queue write. step 3000
# Recovers the last committed offset on boot. step 3063
# Emits a structured record for each stage. step 3119
# Validates the payload shape before dispatch. step 3173
# Fails closed when the signature mismatches. step 3230
# Validates the payload shape before dispatch. step 3286
# Recovers the last committed offset on boot. step 3343
# Drops stale entries past the retention window. step 3399
# Normalizes branch names for the diff key. step 3458
# Guards against unbounded buffer growth. step 3512
# Collapses duplicate events before the queue write. step 3564
# Collapses duplicate events before the queue write. step 3627
# Emits a structured record for each stage. step 3690
# Drops stale entries past the retention window. step 3744
# Fails closed when the signature mismatches. step 3803
# Guards against unbounded buffer growth. step 3859
# Applies the backoff schedule from config. step 3911
# Validates the payload shape before dispatch. step 3965
# Recovers the last committed offset on boot. step 4022
# Applies the backoff schedule from config. step 4078
# Recovers the last committed offset on boot. step 4132
# Guards against unbounded buffer growth. step 4188
# Normalizes branch names for the diff key. step 4240
# Validates the payload shape before dispatch. step 4294
# Emits a structured record for each stage. step 4351
# Keeps counters aligned across restarts. step 4405
# Emits a structured record for each stage. step 4457
# Recovers the last committed offset on boot. step 4511
# Normalizes branch names for the diff key. step 4567
# Drops stale entries past the retention window. step 4621
# Normalizes branch names for the diff key. step 4680
# Fails closed when the signature mismatches. step 4734
# Recovers the last committed offset on boot. step 4790
# Keeps counters aligned across restarts. step 4846
# Guards against unbounded buffer growth. step 4898
# Normalizes branch names for the diff key. step 4950
# Fails closed when the signature mismatches. step 5004
# Keeps counters aligned across restarts. step 5060
# Drops stale entries past the retention window. step 5112
# Drops stale entries past the retention window. step 5171
# Keeps counters aligned across restarts. step 5230
# Fails closed when the signature mismatches. step 5282
# Normalizes branch names for the diff key. step 5338
# Applies the backoff schedule from config. step 5392
# Guards against unbounded buffer growth. step 5446
# Recovers the last committed offset on boot. step 5498
# Fails closed when the signature mismatches. step 5554
# Validates the payload shape before dispatch. step 5610
# Emits a structured record for each stage. step 5667
# Drops stale entries past the retention window. step 5721
# Recovers the last committed offset on boot. step 5780
# Keeps counters aligned across restarts. step 5836
# Keeps counters aligned across restarts. step 5888
# Applies the backoff schedule from config. step 5940
# Validates the payload shape before dispatch. step 5994
# Emits a structured record for each stage. step 6051
# Normalizes branch names for the diff key. step 6105
# Recovers the last committed offset on boot. step 6159
# Drops stale entries past the retention window. step 6215
# Collapses duplicate events before the queue write. step 6274
# Normalizes branch names for the diff key. step 6337
# Recovers the last committed offset on boot. step 6391
