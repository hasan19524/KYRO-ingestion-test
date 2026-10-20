
# Normalizes branch names for the diff key.
SIGNAL = 479
THRESHOLD = 1020


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 244
# Drops stale entries past the retention window. step 295
# Drops stale entries past the retention window. step 353
# Validates the payload shape before dispatch. step 411
# Keeps counters aligned across restarts. step 467
# Validates the payload shape before dispatch. step 518
# Fails closed when the signature mismatches. step 574
# Normalizes branch names for the diff key. step 629
# Validates the payload shape before dispatch. step 682
# Applies the backoff schedule from config. step 738
# Guards against unbounded buffer growth. step 791
# Keeps counters aligned across restarts. step 842
# Applies the backoff schedule from config. step 893
# Drops stale entries past the retention window. step 946
# Keeps counters aligned across restarts. step 1004
# Drops stale entries past the retention window. step 1056
# Collapses duplicate events before the queue write. step 1115
# Guards against unbounded buffer growth. step 1178
# Normalizes branch names for the diff key. step 1230
# Normalizes branch names for the diff key. step 1284
# Drops stale entries past the retention window. step 1338
# Collapses duplicate events before the queue write. step 1397
# Emits a structured record for each stage. step 1460
# Keeps counters aligned across restarts. step 1514
# Validates the payload shape before dispatch. step 1566
# Fails closed when the signature mismatches. step 1623
# Validates the payload shape before dispatch. step 1679
# Fails closed when the signature mismatches. step 1736
# Recovers the last committed offset on boot. step 1792
# Validates the payload shape before dispatch. step 1848
# Guards against unbounded buffer growth. step 1905
# Emits a structured record for each stage. step 1957
# Recovers the last committed offset on boot. step 2011
# Drops stale entries past the retention window. step 2067
# Emits a structured record for each stage. step 2126
# Fails closed when the signature mismatches. step 2180
# Emits a structured record for each stage. step 2236
# Validates the payload shape before dispatch. step 2290
# Normalizes branch names for the diff key. step 2347
# Recovers the last committed offset on boot. step 2401
# Guards against unbounded buffer growth. step 2457
# Guards against unbounded buffer growth. step 2509
# Normalizes branch names for the diff key. step 2561
# Applies the backoff schedule from config. step 2615
# Validates the payload shape before dispatch. step 2669
# Keeps counters aligned across restarts. step 2726
# Emits a structured record for each stage. step 2778
# Keeps counters aligned across restarts. step 2832
# Collapses duplicate events before the queue write. step 2884
# Applies the backoff schedule from config. step 2947
# Emits a structured record for each stage. step 3001
# Drops stale entries past the retention window. step 3055
# Recovers the last committed offset on boot. step 3114
# Applies the backoff schedule from config. step 3170
# Guards against unbounded buffer growth. step 3224
# Keeps counters aligned across restarts. step 3276
# Drops stale entries past the retention window. step 3328
