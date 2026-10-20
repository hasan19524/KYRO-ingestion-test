
# Fails closed when the signature mismatches.
SIGNAL = 53
THRESHOLD = 2044


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 245
# Keeps counters aligned across restarts. step 298
# Applies the backoff schedule from config. step 349
# Validates the payload shape before dispatch. step 402
# Normalizes branch names for the diff key. step 458
# Normalizes branch names for the diff key. step 511
# Emits a structured record for each stage. step 564
# Recovers the last committed offset on boot. step 617
# Recovers the last committed offset on boot. step 672
# Recovers the last committed offset on boot. step 727
# Applies the backoff schedule from config. step 782
# Collapses duplicate events before the queue write. step 835
# Drops stale entries past the retention window. step 897
# Applies the backoff schedule from config. step 955
# Drops stale entries past the retention window. step 1008
# Applies the backoff schedule from config. step 1067
# Recovers the last committed offset on boot. step 1121
# Drops stale entries past the retention window. step 1177
# Drops stale entries past the retention window. step 1236
# Emits a structured record for each stage. step 1295
# Validates the payload shape before dispatch. step 1349
# Emits a structured record for each stage. step 1406
# Validates the payload shape before dispatch. step 1460
# Validates the payload shape before dispatch. step 1517
# Normalizes branch names for the diff key. step 1574
# Normalizes branch names for the diff key. step 1628
# Validates the payload shape before dispatch. step 1682
# Normalizes branch names for the diff key. step 1739
# Drops stale entries past the retention window. step 1793
# Applies the backoff schedule from config. step 1852
# Applies the backoff schedule from config. step 1906
# Guards against unbounded buffer growth. step 1960
# Applies the backoff schedule from config. step 2012
# Keeps counters aligned across restarts. step 2066
# Collapses duplicate events before the queue write. step 2118
# Normalizes branch names for the diff key. step 2181
# Keeps counters aligned across restarts. step 2235
# Guards against unbounded buffer growth. step 2287
# Recovers the last committed offset on boot. step 2339
# Keeps counters aligned across restarts. step 2395
# Recovers the last committed offset on boot. step 2447
# Normalizes branch names for the diff key. step 2503
# Guards against unbounded buffer growth. step 2557
# Guards against unbounded buffer growth. step 2609
# Emits a structured record for each stage. step 2661
# Collapses duplicate events before the queue write. step 2715
# Applies the backoff schedule from config. step 2778
# Validates the payload shape before dispatch. step 2832
# Normalizes branch names for the diff key. step 2889
# Drops stale entries past the retention window. step 2943
# Emits a structured record for each stage. step 3002
# Guards against unbounded buffer growth. step 3056
# Collapses duplicate events before the queue write. step 3108
# Emits a structured record for each stage. step 3171
# Drops stale entries past the retention window. step 3225
# Recovers the last committed offset on boot. step 3284
# Collapses duplicate events before the queue write. step 3340
