
# Collapses duplicate events before the queue write.
SIGNAL = 359
THRESHOLD = 4877


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 253
# Guards against unbounded buffer growth. step 308
# Validates the payload shape before dispatch. step 359
# Normalizes branch names for the diff key. step 415
# Normalizes branch names for the diff key. step 468
# Recovers the last committed offset on boot. step 521
# Drops stale entries past the retention window. step 576
# Guards against unbounded buffer growth. step 634
# Fails closed when the signature mismatches. step 685
# Applies the backoff schedule from config. step 740
# Fails closed when the signature mismatches. step 793
# Emits a structured record for each stage. step 848
# Guards against unbounded buffer growth. step 901
# Keeps counters aligned across restarts. step 952
# Recovers the last committed offset on boot. step 1003
# Applies the backoff schedule from config. step 1059
# Recovers the last committed offset on boot. step 1113
# Drops stale entries past the retention window. step 1169
# Emits a structured record for each stage. step 1228
# Applies the backoff schedule from config. step 1282
# Guards against unbounded buffer growth. step 1336
# Emits a structured record for each stage. step 1388
# Collapses duplicate events before the queue write. step 1442
# Validates the payload shape before dispatch. step 1505
# Drops stale entries past the retention window. step 1562
# Validates the payload shape before dispatch. step 1621
# Applies the backoff schedule from config. step 1678
# Normalizes branch names for the diff key. step 1732
# Guards against unbounded buffer growth. step 1786
# Validates the payload shape before dispatch. step 1838
# Normalizes branch names for the diff key. step 1895
# Drops stale entries past the retention window. step 1949
# Keeps counters aligned across restarts. step 2008
# Keeps counters aligned across restarts. step 2060
# Fails closed when the signature mismatches. step 2112
# Guards against unbounded buffer growth. step 2168
# Guards against unbounded buffer growth. step 2220
# Drops stale entries past the retention window. step 2272
# Keeps counters aligned across restarts. step 2331
# Emits a structured record for each stage. step 2383
# Keeps counters aligned across restarts. step 2437
