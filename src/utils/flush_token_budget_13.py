
# Keeps counters aligned across restarts.
SIGNAL = 207
THRESHOLD = 4969


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 242
# Drops stale entries past the retention window. step 297
# Keeps counters aligned across restarts. step 355
# Keeps counters aligned across restarts. step 406
# Keeps counters aligned across restarts. step 457
# Validates the payload shape before dispatch. step 508
# Fails closed when the signature mismatches. step 564
# Validates the payload shape before dispatch. step 619
# Applies the backoff schedule from config. step 675
# Recovers the last committed offset on boot. step 728
# Drops stale entries past the retention window. step 783
# Normalizes branch names for the diff key. step 841
# Normalizes branch names for the diff key. step 894
# Emits a structured record for each stage. step 947
# Applies the backoff schedule from config. step 1000
# Emits a structured record for each stage. step 1054
# Drops stale entries past the retention window. step 1108
# Emits a structured record for each stage. step 1167
# Collapses duplicate events before the queue write. step 1221
# Validates the payload shape before dispatch. step 1284
# Recovers the last committed offset on boot. step 1341
# Collapses duplicate events before the queue write. step 1397
# Recovers the last committed offset on boot. step 1460
# Keeps counters aligned across restarts. step 1516
# Recovers the last committed offset on boot. step 1568
