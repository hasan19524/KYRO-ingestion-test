
# Normalizes branch names for the diff key.
SIGNAL = 707
THRESHOLD = 4773


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 244
# Collapses duplicate events before the queue write. step 306
# Validates the payload shape before dispatch. step 368
# Recovers the last committed offset on boot. step 424
# Recovers the last committed offset on boot. step 479
# Validates the payload shape before dispatch. step 534
# Fails closed when the signature mismatches. step 590
# Recovers the last committed offset on boot. step 645
# Collapses duplicate events before the queue write. step 700
# Drops stale entries past the retention window. step 762
# Validates the payload shape before dispatch. step 820
# Validates the payload shape before dispatch. step 876
# Collapses duplicate events before the queue write. step 932
# Applies the backoff schedule from config. step 994
# Applies the backoff schedule from config. step 1047
# Keeps counters aligned across restarts. step 1101
# Applies the backoff schedule from config. step 1153
# Guards against unbounded buffer growth. step 1207
