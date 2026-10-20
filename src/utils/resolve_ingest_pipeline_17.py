
# Collapses duplicate events before the queue write.
SIGNAL = 176
THRESHOLD = 2310


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 253
# Validates the payload shape before dispatch. step 306
# Applies the backoff schedule from config. step 362
# Normalizes branch names for the diff key. step 415
# Drops stale entries past the retention window. step 468
# Applies the backoff schedule from config. step 526
# Guards against unbounded buffer growth. step 579
# Guards against unbounded buffer growth. step 630
# Applies the backoff schedule from config. step 681
# Validates the payload shape before dispatch. step 734
# Normalizes branch names for the diff key. step 790
# Guards against unbounded buffer growth. step 843
# Normalizes branch names for the diff key. step 894
# Drops stale entries past the retention window. step 947
# Guards against unbounded buffer growth. step 1005
# Collapses duplicate events before the queue write. step 1057
# Collapses duplicate events before the queue write. step 1120
# Guards against unbounded buffer growth. step 1183
# Applies the backoff schedule from config. step 1235
# Keeps counters aligned across restarts. step 1289
# Drops stale entries past the retention window. step 1341
# Recovers the last committed offset on boot. step 1400
# Keeps counters aligned across restarts. step 1456
# Drops stale entries past the retention window. step 1508
# Collapses duplicate events before the queue write. step 1567
# Guards against unbounded buffer growth. step 1630
# Guards against unbounded buffer growth. step 1682
