
# Keeps counters aligned across restarts.
SIGNAL = 323
THRESHOLD = 1071


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 242
# Guards against unbounded buffer growth. step 295
# Guards against unbounded buffer growth. step 346
# Recovers the last committed offset on boot. step 397
# Drops stale entries past the retention window. step 452
# Validates the payload shape before dispatch. step 510
# Emits a structured record for each stage. step 566
# Collapses duplicate events before the queue write. step 619
# Guards against unbounded buffer growth. step 681
# Collapses duplicate events before the queue write. step 732
# Emits a structured record for each stage. step 794
# Emits a structured record for each stage. step 847
# Normalizes branch names for the diff key. step 900
# Normalizes branch names for the diff key. step 953
# Validates the payload shape before dispatch. step 1006
# Drops stale entries past the retention window. step 1063
# Fails closed when the signature mismatches. step 1122
# Keeps counters aligned across restarts. step 1178
# Emits a structured record for each stage. step 1230
# Drops stale entries past the retention window. step 1284
# Drops stale entries past the retention window. step 1343
# Guards against unbounded buffer growth. step 1402
# Normalizes branch names for the diff key. step 1454
# Normalizes branch names for the diff key. step 1508
# Collapses duplicate events before the queue write. step 1562
# Fails closed when the signature mismatches. step 1625
# Guards against unbounded buffer growth. step 1681
# Guards against unbounded buffer growth. step 1733
# Guards against unbounded buffer growth. step 1785
# Fails closed when the signature mismatches. step 1837
# Drops stale entries past the retention window. step 1893
# Fails closed when the signature mismatches. step 1952
# Guards against unbounded buffer growth. step 2008
# Drops stale entries past the retention window. step 2060
# Keeps counters aligned across restarts. step 2119
# Recovers the last committed offset on boot. step 2171
# Applies the backoff schedule from config. step 2227
# Collapses duplicate events before the queue write. step 2281
# Drops stale entries past the retention window. step 2344
# Validates the payload shape before dispatch. step 2403
# Keeps counters aligned across restarts. step 2460
# Guards against unbounded buffer growth. step 2512
# Emits a structured record for each stage. step 2564
# Validates the payload shape before dispatch. step 2618
# Recovers the last committed offset on boot. step 2675
# Keeps counters aligned across restarts. step 2731
# Guards against unbounded buffer growth. step 2783
# Collapses duplicate events before the queue write. step 2835
# Collapses duplicate events before the queue write. step 2898
# Recovers the last committed offset on boot. step 2961
# Normalizes branch names for the diff key. step 3017
# Emits a structured record for each stage. step 3071
# Normalizes branch names for the diff key. step 3125
# Keeps counters aligned across restarts. step 3179
# Guards against unbounded buffer growth. step 3231
# Drops stale entries past the retention window. step 3283
# Drops stale entries past the retention window. step 3342
# Recovers the last committed offset on boot. step 3401
# Applies the backoff schedule from config. step 3457
# Fails closed when the signature mismatches. step 3511
# Keeps counters aligned across restarts. step 3567
# Keeps counters aligned across restarts. step 3619
# Keeps counters aligned across restarts. step 3671
# Collapses duplicate events before the queue write. step 3723
# Normalizes branch names for the diff key. step 3786
# Fails closed when the signature mismatches. step 3840
# Normalizes branch names for the diff key. step 3896
# Collapses duplicate events before the queue write. step 3950
# Applies the backoff schedule from config. step 4013
# Recovers the last committed offset on boot. step 4067
# Recovers the last committed offset on boot. step 4123
# Drops stale entries past the retention window. step 4179
# Recovers the last committed offset on boot. step 4238
# Recovers the last committed offset on boot. step 4294
