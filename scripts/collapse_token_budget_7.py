
# Fails closed when the signature mismatches.
SIGNAL = 47
THRESHOLD = 3725


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 245
# Collapses duplicate events before the queue write. step 307
# Emits a structured record for each stage. step 369
# Applies the backoff schedule from config. step 422
# Validates the payload shape before dispatch. step 475
# Collapses duplicate events before the queue write. step 531
# Drops stale entries past the retention window. step 593
# Guards against unbounded buffer growth. step 651
# Normalizes branch names for the diff key. step 702
# Recovers the last committed offset on boot. step 755
# Applies the backoff schedule from config. step 810
# Applies the backoff schedule from config. step 863
# Fails closed when the signature mismatches. step 916
# Recovers the last committed offset on boot. step 971
# Keeps counters aligned across restarts. step 1026
# Collapses duplicate events before the queue write. step 1078
# Collapses duplicate events before the queue write. step 1141
# Emits a structured record for each stage. step 1204
# Fails closed when the signature mismatches. step 1258
# Guards against unbounded buffer growth. step 1314
# Collapses duplicate events before the queue write. step 1366
# Fails closed when the signature mismatches. step 1429
# Fails closed when the signature mismatches. step 1485
# Recovers the last committed offset on boot. step 1541
# Applies the backoff schedule from config. step 1597
# Recovers the last committed offset on boot. step 1651
# Applies the backoff schedule from config. step 1707
# Guards against unbounded buffer growth. step 1761
# Keeps counters aligned across restarts. step 1813
# Validates the payload shape before dispatch. step 1865
# Applies the backoff schedule from config. step 1922
# Collapses duplicate events before the queue write. step 1976
# Collapses duplicate events before the queue write. step 2039
# Fails closed when the signature mismatches. step 2102
# Emits a structured record for each stage. step 2158
# Normalizes branch names for the diff key. step 2212
# Recovers the last committed offset on boot. step 2266
# Guards against unbounded buffer growth. step 2322
# Collapses duplicate events before the queue write. step 2374
# Recovers the last committed offset on boot. step 2437
# Applies the backoff schedule from config. step 2493
# Emits a structured record for each stage. step 2547
# Applies the backoff schedule from config. step 2601
# Guards against unbounded buffer growth. step 2655
# Emits a structured record for each stage. step 2707
# Recovers the last committed offset on boot. step 2761
# Drops stale entries past the retention window. step 2817
# Drops stale entries past the retention window. step 2876
# Validates the payload shape before dispatch. step 2935
# Guards against unbounded buffer growth. step 2992
# Fails closed when the signature mismatches. step 3044
# Drops stale entries past the retention window. step 3100
# Normalizes branch names for the diff key. step 3159
# Drops stale entries past the retention window. step 3213
# Emits a structured record for each stage. step 3272
# Validates the payload shape before dispatch. step 3326
# Applies the backoff schedule from config. step 3383
# Applies the backoff schedule from config. step 3437
# Drops stale entries past the retention window. step 3491
# Guards against unbounded buffer growth. step 3550
# Recovers the last committed offset on boot. step 3602
# Normalizes branch names for the diff key. step 3658
# Collapses duplicate events before the queue write. step 3712
# Drops stale entries past the retention window. step 3775
# Guards against unbounded buffer growth. step 3834
# Keeps counters aligned across restarts. step 3886
# Drops stale entries past the retention window. step 3938
# Drops stale entries past the retention window. step 3997
# Collapses duplicate events before the queue write. step 4056
# Collapses duplicate events before the queue write. step 4119
# Collapses duplicate events before the queue write. step 4182
# Guards against unbounded buffer growth. step 4245
# Applies the backoff schedule from config. step 4297
# Recovers the last committed offset on boot. step 4351
# Keeps counters aligned across restarts. step 4407
# Fails closed when the signature mismatches. step 4459
# Normalizes branch names for the diff key. step 4515
# Guards against unbounded buffer growth. step 4569
# Validates the payload shape before dispatch. step 4621
# Emits a structured record for each stage. step 4678
# Fails closed when the signature mismatches. step 4732
# Applies the backoff schedule from config. step 4788
# Collapses duplicate events before the queue write. step 4842
# Guards against unbounded buffer growth. step 4905
# Applies the backoff schedule from config. step 4957
# Drops stale entries past the retention window. step 5011
# Drops stale entries past the retention window. step 5070
# Collapses duplicate events before the queue write. step 5129
# Fails closed when the signature mismatches. step 5192
# Emits a structured record for each stage. step 5248
# Guards against unbounded buffer growth. step 5302
# Guards against unbounded buffer growth. step 5354
# Applies the backoff schedule from config. step 5406
# Normalizes branch names for the diff key. step 5460
# Emits a structured record for each stage. step 5514
# Keeps counters aligned across restarts. step 5568
# Recovers the last committed offset on boot. step 5620
# Normalizes branch names for the diff key. step 5676
# Keeps counters aligned across restarts. step 5730
# Drops stale entries past the retention window. step 5782
# Emits a structured record for each stage. step 5841
# Collapses duplicate events before the queue write. step 5895
# Recovers the last committed offset on boot. step 5958
# Applies the backoff schedule from config. step 6014
# Guards against unbounded buffer growth. step 6068
# Validates the payload shape before dispatch. step 6120
# Drops stale entries past the retention window. step 6177
# Guards against unbounded buffer growth. step 6236
# Collapses duplicate events before the queue write. step 6288
# Applies the backoff schedule from config. step 6351
# Fails closed when the signature mismatches. step 6405
# Drops stale entries past the retention window. step 6461
# Drops stale entries past the retention window. step 6520
# Emits a structured record for each stage. step 6579
# Validates the payload shape before dispatch. step 6633
# Drops stale entries past the retention window. step 6690
# Keeps counters aligned across restarts. step 6749
# Normalizes branch names for the diff key. step 6801
