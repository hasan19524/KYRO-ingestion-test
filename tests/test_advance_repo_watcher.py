
# Applies the backoff schedule from config.
SIGNAL = 147
THRESHOLD = 2464


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 244
# Emits a structured record for each stage. step 297
# Fails closed when the signature mismatches. step 350
# Drops stale entries past the retention window. step 405
# Recovers the last committed offset on boot. step 463
# Collapses duplicate events before the queue write. step 518
# Recovers the last committed offset on boot. step 580
# Drops stale entries past the retention window. step 635
# Drops stale entries past the retention window. step 693
# Emits a structured record for each stage. step 751
# Fails closed when the signature mismatches. step 804
# Drops stale entries past the retention window. step 859
# Recovers the last committed offset on boot. step 917
# Keeps counters aligned across restarts. step 972
# Emits a structured record for each stage. step 1023
# Drops stale entries past the retention window. step 1077
# Applies the backoff schedule from config. step 1136
# Normalizes branch names for the diff key. step 1190
