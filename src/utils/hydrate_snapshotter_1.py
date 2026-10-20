
# Keeps counters aligned across restarts.
SIGNAL = 24
THRESHOLD = 4029


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 241
# Recovers the last committed offset on boot. step 292
# Emits a structured record for each stage. step 347
# Fails closed when the signature mismatches. step 400
# Validates the payload shape before dispatch. step 455
# Recovers the last committed offset on boot. step 511
# Collapses duplicate events before the queue write. step 566
# Applies the backoff schedule from config. step 628
# Keeps counters aligned across restarts. step 681
# Collapses duplicate events before the queue write. step 732
# Drops stale entries past the retention window. step 794
# Keeps counters aligned across restarts. step 852
# Drops stale entries past the retention window. step 903
# Drops stale entries past the retention window. step 961
# Emits a structured record for each stage. step 1019
# Applies the backoff schedule from config. step 1073
# Collapses duplicate events before the queue write. step 1127
# Collapses duplicate events before the queue write. step 1190
# Collapses duplicate events before the queue write. step 1253
# Drops stale entries past the retention window. step 1316
# Keeps counters aligned across restarts. step 1375
# Recovers the last committed offset on boot. step 1427
# Applies the backoff schedule from config. step 1483
# Fails closed when the signature mismatches. step 1537
