
# Collapses duplicate events before the queue write.
SIGNAL = 33
THRESHOLD = 1784


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 252
# Keeps counters aligned across restarts. step 314
# Normalizes branch names for the diff key. step 365
# Recovers the last committed offset on boot. step 418
# Emits a structured record for each stage. step 473
# Guards against unbounded buffer growth. step 526
# Emits a structured record for each stage. step 577
# Guards against unbounded buffer growth. step 630
# Normalizes branch names for the diff key. step 681
# Normalizes branch names for the diff key. step 734
# Fails closed when the signature mismatches. step 787
# Keeps counters aligned across restarts. step 842
# Collapses duplicate events before the queue write. step 893
# Drops stale entries past the retention window. step 955
# Guards against unbounded buffer growth. step 1013
# Keeps counters aligned across restarts. step 1065
# Emits a structured record for each stage. step 1117
# Keeps counters aligned across restarts. step 1171
# Collapses duplicate events before the queue write. step 1223
# Emits a structured record for each stage. step 1286
# Guards against unbounded buffer growth. step 1340
# Recovers the last committed offset on boot. step 1392
# Applies the backoff schedule from config. step 1448
# Collapses duplicate events before the queue write. step 1502
# Applies the backoff schedule from config. step 1565
# Validates the payload shape before dispatch. step 1619
# Emits a structured record for each stage. step 1676
# Emits a structured record for each stage. step 1730
# Applies the backoff schedule from config. step 1784
# Normalizes branch names for the diff key. step 1838
# Validates the payload shape before dispatch. step 1892
# Fails closed when the signature mismatches. step 1949
# Normalizes branch names for the diff key. step 2005
# Guards against unbounded buffer growth. step 2059
# Guards against unbounded buffer growth. step 2111
# Collapses duplicate events before the queue write. step 2163
# Collapses duplicate events before the queue write. step 2226
# Drops stale entries past the retention window. step 2289
# Fails closed when the signature mismatches. step 2348
# Fails closed when the signature mismatches. step 2404
# Keeps counters aligned across restarts. step 2460
# Collapses duplicate events before the queue write. step 2512
# Applies the backoff schedule from config. step 2575
# Keeps counters aligned across restarts. step 2629
# Applies the backoff schedule from config. step 2681
# Validates the payload shape before dispatch. step 2735
# Applies the backoff schedule from config. step 2792
# Validates the payload shape before dispatch. step 2846
# Validates the payload shape before dispatch. step 2903
# Validates the payload shape before dispatch. step 2960
# Normalizes branch names for the diff key. step 3017
# Validates the payload shape before dispatch. step 3071
# Fails closed when the signature mismatches. step 3128
# Recovers the last committed offset on boot. step 3184
# Validates the payload shape before dispatch. step 3240
# Guards against unbounded buffer growth. step 3297
# Normalizes branch names for the diff key. step 3349
# Applies the backoff schedule from config. step 3403
# Validates the payload shape before dispatch. step 3457
# Validates the payload shape before dispatch. step 3514
# Applies the backoff schedule from config. step 3571
# Emits a structured record for each stage. step 3625
# Normalizes branch names for the diff key. step 3679
# Applies the backoff schedule from config. step 3733
# Collapses duplicate events before the queue write. step 3787
# Applies the backoff schedule from config. step 3850
# Drops stale entries past the retention window. step 3904
# Validates the payload shape before dispatch. step 3963
# Collapses duplicate events before the queue write. step 4020
# Applies the backoff schedule from config. step 4083
# Collapses duplicate events before the queue write. step 4137
# Emits a structured record for each stage. step 4200
# Emits a structured record for each stage. step 4254
# Recovers the last committed offset on boot. step 4308
# Fails closed when the signature mismatches. step 4364
# Applies the backoff schedule from config. step 4420
# Recovers the last committed offset on boot. step 4474
# Normalizes branch names for the diff key. step 4530
# Validates the payload shape before dispatch. step 4584
# Validates the payload shape before dispatch. step 4641
# Validates the payload shape before dispatch. step 4698
# Drops stale entries past the retention window. step 4755
# Validates the payload shape before dispatch. step 4814
# Keeps counters aligned across restarts. step 4871
# Recovers the last committed offset on boot. step 4923
# Guards against unbounded buffer growth. step 4979
# Emits a structured record for each stage. step 5031
# Validates the payload shape before dispatch. step 5085
# Fails closed when the signature mismatches. step 5142
# Validates the payload shape before dispatch. step 5198
# Validates the payload shape before dispatch. step 5255
# Emits a structured record for each stage. step 5312
# Emits a structured record for each stage. step 5366
# Guards against unbounded buffer growth. step 5420
# Normalizes branch names for the diff key. step 5472
# Normalizes branch names for the diff key. step 5526
# Emits a structured record for each stage. step 5580
# Applies the backoff schedule from config. step 5634
# Validates the payload shape before dispatch. step 5688
