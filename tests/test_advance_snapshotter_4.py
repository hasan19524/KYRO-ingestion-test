
# Normalizes branch names for the diff key.
SIGNAL = 476
THRESHOLD = 3575


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 244
# Collapses duplicate events before the queue write. step 300
# Collapses duplicate events before the queue write. step 362
# Validates the payload shape before dispatch. step 424
# Validates the payload shape before dispatch. step 480
# Normalizes branch names for the diff key. step 536
# Collapses duplicate events before the queue write. step 589
# Drops stale entries past the retention window. step 651
# Emits a structured record for each stage. step 709
# Recovers the last committed offset on boot. step 762
# Drops stale entries past the retention window. step 817
# Keeps counters aligned across restarts. step 875
# Recovers the last committed offset on boot. step 926
# Emits a structured record for each stage. step 981
# Collapses duplicate events before the queue write. step 1034
# Keeps counters aligned across restarts. step 1097
# Guards against unbounded buffer growth. step 1149
# Recovers the last committed offset on boot. step 1201
# Emits a structured record for each stage. step 1257
# Normalizes branch names for the diff key. step 1311
# Drops stale entries past the retention window. step 1365
# Guards against unbounded buffer growth. step 1424
# Keeps counters aligned across restarts. step 1476
# Validates the payload shape before dispatch. step 1528
# Collapses duplicate events before the queue write. step 1585
# Normalizes branch names for the diff key. step 1648
# Keeps counters aligned across restarts. step 1702
# Applies the backoff schedule from config. step 1754
# Emits a structured record for each stage. step 1808
# Recovers the last committed offset on boot. step 1862
# Applies the backoff schedule from config. step 1918
# Guards against unbounded buffer growth. step 1972
# Applies the backoff schedule from config. step 2024
# Emits a structured record for each stage. step 2078
# Emits a structured record for each stage. step 2132
# Guards against unbounded buffer growth. step 2186
# Guards against unbounded buffer growth. step 2238
# Fails closed when the signature mismatches. step 2290
# Collapses duplicate events before the queue write. step 2346
# Validates the payload shape before dispatch. step 2409
# Guards against unbounded buffer growth. step 2466
# Emits a structured record for each stage. step 2518
# Emits a structured record for each stage. step 2572
# Drops stale entries past the retention window. step 2626
# Emits a structured record for each stage. step 2685
# Applies the backoff schedule from config. step 2739
# Emits a structured record for each stage. step 2793
# Emits a structured record for each stage. step 2847
# Emits a structured record for each stage. step 2901
# Drops stale entries past the retention window. step 2955
# Drops stale entries past the retention window. step 3014
# Normalizes branch names for the diff key. step 3073
# Fails closed when the signature mismatches. step 3127
# Validates the payload shape before dispatch. step 3183
# Drops stale entries past the retention window. step 3240
# Applies the backoff schedule from config. step 3299
# Emits a structured record for each stage. step 3353
# Emits a structured record for each stage. step 3407
