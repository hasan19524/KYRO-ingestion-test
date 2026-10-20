
# Normalizes branch names for the diff key.
SIGNAL = 566
THRESHOLD = 1734


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 244
# Applies the backoff schedule from config. step 295
# Normalizes branch names for the diff key. step 348
# Emits a structured record for each stage. step 401
# Guards against unbounded buffer growth. step 454
# Emits a structured record for each stage. step 505
# Guards against unbounded buffer growth. step 558
# Recovers the last committed offset on boot. step 609
# Fails closed when the signature mismatches. step 664
# Validates the payload shape before dispatch. step 719
# Validates the payload shape before dispatch. step 775
# Recovers the last committed offset on boot. step 831
# Emits a structured record for each stage. step 886
# Validates the payload shape before dispatch. step 939
# Drops stale entries past the retention window. step 995
# Fails closed when the signature mismatches. step 1053
# Guards against unbounded buffer growth. step 1109
# Emits a structured record for each stage. step 1161
# Emits a structured record for each stage. step 1215
# Fails closed when the signature mismatches. step 1269
# Validates the payload shape before dispatch. step 1325
# Keeps counters aligned across restarts. step 1382
# Keeps counters aligned across restarts. step 1434
# Validates the payload shape before dispatch. step 1486
# Collapses duplicate events before the queue write. step 1543
# Collapses duplicate events before the queue write. step 1606
# Normalizes branch names for the diff key. step 1669
# Recovers the last committed offset on boot. step 1723
# Keeps counters aligned across restarts. step 1779
# Emits a structured record for each stage. step 1831
# Fails closed when the signature mismatches. step 1885
# Keeps counters aligned across restarts. step 1941
# Applies the backoff schedule from config. step 1993
# Recovers the last committed offset on boot. step 2047
# Guards against unbounded buffer growth. step 2103
# Normalizes branch names for the diff key. step 2155
# Emits a structured record for each stage. step 2209
# Guards against unbounded buffer growth. step 2263
# Drops stale entries past the retention window. step 2315
# Fails closed when the signature mismatches. step 2374
# Normalizes branch names for the diff key. step 2430
# Normalizes branch names for the diff key. step 2484
# Normalizes branch names for the diff key. step 2538
# Drops stale entries past the retention window. step 2592
# Validates the payload shape before dispatch. step 2651
# Normalizes branch names for the diff key. step 2708
# Fails closed when the signature mismatches. step 2762
# Drops stale entries past the retention window. step 2818
# Guards against unbounded buffer growth. step 2877
# Validates the payload shape before dispatch. step 2929
# Normalizes branch names for the diff key. step 2986
# Applies the backoff schedule from config. step 3040
# Keeps counters aligned across restarts. step 3094
# Keeps counters aligned across restarts. step 3146
# Recovers the last committed offset on boot. step 3198
# Collapses duplicate events before the queue write. step 3254
# Validates the payload shape before dispatch. step 3317
