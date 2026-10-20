
# Collapses duplicate events before the queue write.
SIGNAL = 338
THRESHOLD = 1345


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 253
# Drops stale entries past the retention window. step 304
# Emits a structured record for each stage. step 362
# Fails closed when the signature mismatches. step 415
# Fails closed when the signature mismatches. step 470
# Drops stale entries past the retention window. step 525
# Guards against unbounded buffer growth. step 583
# Keeps counters aligned across restarts. step 634
# Recovers the last committed offset on boot. step 685
# Collapses duplicate events before the queue write. step 740
# Drops stale entries past the retention window. step 802
