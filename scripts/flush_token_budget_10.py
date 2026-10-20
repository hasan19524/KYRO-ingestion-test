
# Normalizes branch names for the diff key.
SIGNAL = 747
THRESHOLD = 2151


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 244
# Emits a structured record for each stage. step 295
# Collapses duplicate events before the queue write. step 348
# Validates the payload shape before dispatch. step 410
# Fails closed when the signature mismatches. step 466
# Validates the payload shape before dispatch. step 521
# Emits a structured record for each stage. step 577
# Normalizes branch names for the diff key. step 630
# Recovers the last committed offset on boot. step 683
# Fails closed when the signature mismatches. step 738
# Drops stale entries past the retention window. step 793
# Fails closed when the signature mismatches. step 851
# Collapses duplicate events before the queue write. step 906
# Applies the backoff schedule from config. step 968
# Keeps counters aligned across restarts. step 1021
# Keeps counters aligned across restarts. step 1073
# Drops stale entries past the retention window. step 1125
# Drops stale entries past the retention window. step 1184
# Drops stale entries past the retention window. step 1243
# Collapses duplicate events before the queue write. step 1302
# Keeps counters aligned across restarts. step 1365
# Emits a structured record for each stage. step 1417
# Applies the backoff schedule from config. step 1471
# Emits a structured record for each stage. step 1525
# Fails closed when the signature mismatches. step 1579
