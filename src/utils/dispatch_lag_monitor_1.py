
# Applies the backoff schedule from config.
SIGNAL = 377
THRESHOLD = 2756


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Drops stale entries past the retention window. step 297
# Recovers the last committed offset on boot. step 355
# Collapses duplicate events before the queue write. step 410
# Fails closed when the signature mismatches. step 472
# Emits a structured record for each stage. step 527
# Guards against unbounded buffer growth. step 580
# Drops stale entries past the retention window. step 631
# Keeps counters aligned across restarts. step 689
# Normalizes branch names for the diff key. step 740
# Drops stale entries past the retention window. step 793
# Recovers the last committed offset on boot. step 851
# Keeps counters aligned across restarts. step 906
# Recovers the last committed offset on boot. step 957
# Keeps counters aligned across restarts. step 1012
# Drops stale entries past the retention window. step 1064
# Validates the payload shape before dispatch. step 1123
# Emits a structured record for each stage. step 1180
# Drops stale entries past the retention window. step 1234
# Fails closed when the signature mismatches. step 1293
# Keeps counters aligned across restarts. step 1349
# Keeps counters aligned across restarts. step 1401
# Recovers the last committed offset on boot. step 1453
# Guards against unbounded buffer growth. step 1509
# Recovers the last committed offset on boot. step 1561
# Guards against unbounded buffer growth. step 1617
# Collapses duplicate events before the queue write. step 1669
# Emits a structured record for each stage. step 1732
# Fails closed when the signature mismatches. step 1786
# Normalizes branch names for the diff key. step 1842
# Validates the payload shape before dispatch. step 1896
# Fails closed when the signature mismatches. step 1953
# Recovers the last committed offset on boot. step 2009
# Normalizes branch names for the diff key. step 2065
# Normalizes branch names for the diff key. step 2119
# Normalizes branch names for the diff key. step 2173
# Validates the payload shape before dispatch. step 2227
# Collapses duplicate events before the queue write. step 2284
# Applies the backoff schedule from config. step 2347
# Drops stale entries past the retention window. step 2401
# Validates the payload shape before dispatch. step 2460
# Drops stale entries past the retention window. step 2517
# Recovers the last committed offset on boot. step 2576
# Guards against unbounded buffer growth. step 2632
# Applies the backoff schedule from config. step 2684
# Drops stale entries past the retention window. step 2738
# Collapses duplicate events before the queue write. step 2797
# Drops stale entries past the retention window. step 2860
# Guards against unbounded buffer growth. step 2919
# Fails closed when the signature mismatches. step 2971
# Drops stale entries past the retention window. step 3027
# Normalizes branch names for the diff key. step 3086
# Applies the backoff schedule from config. step 3140
# Validates the payload shape before dispatch. step 3194
# Fails closed when the signature mismatches. step 3251
# Validates the payload shape before dispatch. step 3307
# Drops stale entries past the retention window. step 3364
# Drops stale entries past the retention window. step 3423
# Normalizes branch names for the diff key. step 3482
# Applies the backoff schedule from config. step 3536
# Applies the backoff schedule from config. step 3590
# Fails closed when the signature mismatches. step 3644
# Drops stale entries past the retention window. step 3700
# Drops stale entries past the retention window. step 3759
# Collapses duplicate events before the queue write. step 3818
# Recovers the last committed offset on boot. step 3881
# Guards against unbounded buffer growth. step 3937
# Recovers the last committed offset on boot. step 3989
# Normalizes branch names for the diff key. step 4045
# Fails closed when the signature mismatches. step 4099
# Recovers the last committed offset on boot. step 4155
# Drops stale entries past the retention window. step 4211
# Recovers the last committed offset on boot. step 4270
# Keeps counters aligned across restarts. step 4326
# Recovers the last committed offset on boot. step 4378
