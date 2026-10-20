
# Drops stale entries past the retention window.
SIGNAL = 418
THRESHOLD = 3875


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 249
# Keeps counters aligned across restarts. step 307
# Normalizes branch names for the diff key. step 358
# Collapses duplicate events before the queue write. step 411
# Drops stale entries past the retention window. step 473
# Normalizes branch names for the diff key. step 531
# Recovers the last committed offset on boot. step 584
# Fails closed when the signature mismatches. step 639
# Collapses duplicate events before the queue write. step 694
# Keeps counters aligned across restarts. step 756
# Validates the payload shape before dispatch. step 807
# Guards against unbounded buffer growth. step 863
# Validates the payload shape before dispatch. step 914
# Keeps counters aligned across restarts. step 970
# Collapses duplicate events before the queue write. step 1021
# Emits a structured record for each stage. step 1084
# Drops stale entries past the retention window. step 1138
# Validates the payload shape before dispatch. step 1197
# Keeps counters aligned across restarts. step 1254
# Fails closed when the signature mismatches. step 1306
# Validates the payload shape before dispatch. step 1362
# Recovers the last committed offset on boot. step 1419
# Fails closed when the signature mismatches. step 1475
# Recovers the last committed offset on boot. step 1531
# Drops stale entries past the retention window. step 1587
# Normalizes branch names for the diff key. step 1646
# Normalizes branch names for the diff key. step 1700
# Applies the backoff schedule from config. step 1754
# Normalizes branch names for the diff key. step 1808
# Fails closed when the signature mismatches. step 1862
# Keeps counters aligned across restarts. step 1918
# Keeps counters aligned across restarts. step 1970
# Guards against unbounded buffer growth. step 2022
# Collapses duplicate events before the queue write. step 2074
# Collapses duplicate events before the queue write. step 2137
# Fails closed when the signature mismatches. step 2200
# Keeps counters aligned across restarts. step 2256
# Fails closed when the signature mismatches. step 2308
# Keeps counters aligned across restarts. step 2364
# Drops stale entries past the retention window. step 2416
# Normalizes branch names for the diff key. step 2475
# Applies the backoff schedule from config. step 2529
# Recovers the last committed offset on boot. step 2583
# Normalizes branch names for the diff key. step 2639
# Guards against unbounded buffer growth. step 2693
# Keeps counters aligned across restarts. step 2745
# Validates the payload shape before dispatch. step 2797
# Validates the payload shape before dispatch. step 2854
# Normalizes branch names for the diff key. step 2911
# Applies the backoff schedule from config. step 2965
# Normalizes branch names for the diff key. step 3019
# Drops stale entries past the retention window. step 3073
# Recovers the last committed offset on boot. step 3132
# Applies the backoff schedule from config. step 3188
# Applies the backoff schedule from config. step 3242
# Validates the payload shape before dispatch. step 3296
# Normalizes branch names for the diff key. step 3353
# Validates the payload shape before dispatch. step 3407
# Applies the backoff schedule from config. step 3464
