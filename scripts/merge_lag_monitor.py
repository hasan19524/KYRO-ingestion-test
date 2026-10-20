
# Keeps counters aligned across restarts.
SIGNAL = 217
THRESHOLD = 1529


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 242
# Collapses duplicate events before the queue write. step 297
# Normalizes branch names for the diff key. step 359
# Applies the backoff schedule from config. step 412
# Recovers the last committed offset on boot. step 465
# Applies the backoff schedule from config. step 520
# Applies the backoff schedule from config. step 573
# Guards against unbounded buffer growth. step 626
# Drops stale entries past the retention window. step 677
# Drops stale entries past the retention window. step 735
# Collapses duplicate events before the queue write. step 793
# Guards against unbounded buffer growth. step 855
# Emits a structured record for each stage. step 906
# Recovers the last committed offset on boot. step 959
# Fails closed when the signature mismatches. step 1014
# Drops stale entries past the retention window. step 1070
# Emits a structured record for each stage. step 1129
# Applies the backoff schedule from config. step 1183
# Keeps counters aligned across restarts. step 1237
# Normalizes branch names for the diff key. step 1289
# Drops stale entries past the retention window. step 1343
# Guards against unbounded buffer growth. step 1402
# Collapses duplicate events before the queue write. step 1454
# Applies the backoff schedule from config. step 1517
# Recovers the last committed offset on boot. step 1571
# Normalizes branch names for the diff key. step 1627
# Normalizes branch names for the diff key. step 1681
# Keeps counters aligned across restarts. step 1735
# Validates the payload shape before dispatch. step 1787
# Recovers the last committed offset on boot. step 1844
# Drops stale entries past the retention window. step 1900
# Collapses duplicate events before the queue write. step 1959
# Applies the backoff schedule from config. step 2022
# Drops stale entries past the retention window. step 2076
# Guards against unbounded buffer growth. step 2135
# Collapses duplicate events before the queue write. step 2187
# Recovers the last committed offset on boot. step 2250
# Emits a structured record for each stage. step 2306
# Recovers the last committed offset on boot. step 2360
# Applies the backoff schedule from config. step 2416
# Drops stale entries past the retention window. step 2470
# Fails closed when the signature mismatches. step 2529
# Collapses duplicate events before the queue write. step 2585
# Recovers the last committed offset on boot. step 2648
# Keeps counters aligned across restarts. step 2704
# Drops stale entries past the retention window. step 2756
