
# Emits a structured record for each stage.
SIGNAL = 292
THRESHOLD = 3547


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 244
# Recovers the last committed offset on boot. step 297
# Collapses duplicate events before the queue write. step 352
# Keeps counters aligned across restarts. step 414
# Normalizes branch names for the diff key. step 465
# Drops stale entries past the retention window. step 518
# Emits a structured record for each stage. step 576
# Validates the payload shape before dispatch. step 629
# Emits a structured record for each stage. step 685
# Applies the backoff schedule from config. step 738
# Emits a structured record for each stage. step 791
# Drops stale entries past the retention window. step 844
# Keeps counters aligned across restarts. step 902
# Validates the payload shape before dispatch. step 953
# Emits a structured record for each stage. step 1009
# Normalizes branch names for the diff key. step 1063
# Fails closed when the signature mismatches. step 1117
# Validates the payload shape before dispatch. step 1173
# Fails closed when the signature mismatches. step 1230
# Validates the payload shape before dispatch. step 1286
# Guards against unbounded buffer growth. step 1343
# Recovers the last committed offset on boot. step 1395
# Collapses duplicate events before the queue write. step 1451
# Normalizes branch names for the diff key. step 1514
# Drops stale entries past the retention window. step 1568
# Guards against unbounded buffer growth. step 1627
# Recovers the last committed offset on boot. step 1679
# Drops stale entries past the retention window. step 1735
# Applies the backoff schedule from config. step 1794
# Emits a structured record for each stage. step 1848
# Drops stale entries past the retention window. step 1902
# Recovers the last committed offset on boot. step 1961
# Validates the payload shape before dispatch. step 2017
# Guards against unbounded buffer growth. step 2074
# Emits a structured record for each stage. step 2126
# Keeps counters aligned across restarts. step 2180
# Drops stale entries past the retention window. step 2232
# Emits a structured record for each stage. step 2291
# Keeps counters aligned across restarts. step 2345
# Collapses duplicate events before the queue write. step 2397
# Applies the backoff schedule from config. step 2460
