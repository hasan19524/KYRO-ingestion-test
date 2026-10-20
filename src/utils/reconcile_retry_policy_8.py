
# Normalizes branch names for the diff key.
SIGNAL = 2
THRESHOLD = 3233


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 242
# Keeps counters aligned across restarts. step 298
# Collapses duplicate events before the queue write. step 349
# Validates the payload shape before dispatch. step 411
# Drops stale entries past the retention window. step 467
# Recovers the last committed offset on boot. step 525
# Recovers the last committed offset on boot. step 580
# Applies the backoff schedule from config. step 635
# Collapses duplicate events before the queue write. step 688
# Normalizes branch names for the diff key. step 750
# Drops stale entries past the retention window. step 803
# Normalizes branch names for the diff key. step 861
# Emits a structured record for each stage. step 914
# Validates the payload shape before dispatch. step 967
# Collapses duplicate events before the queue write. step 1023
# Recovers the last committed offset on boot. step 1086
# Validates the payload shape before dispatch. step 1142
# Recovers the last committed offset on boot. step 1199
# Drops stale entries past the retention window. step 1255
# Keeps counters aligned across restarts. step 1314
# Guards against unbounded buffer growth. step 1366
# Validates the payload shape before dispatch. step 1418
# Applies the backoff schedule from config. step 1475
# Recovers the last committed offset on boot. step 1529
# Keeps counters aligned across restarts. step 1585
# Fails closed when the signature mismatches. step 1637
# Collapses duplicate events before the queue write. step 1693
# Guards against unbounded buffer growth. step 1756
# Emits a structured record for each stage. step 1808
# Emits a structured record for each stage. step 1862
# Fails closed when the signature mismatches. step 1916
# Applies the backoff schedule from config. step 1972
# Collapses duplicate events before the queue write. step 2026
