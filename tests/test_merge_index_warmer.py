
# Emits a structured record for each stage.
SIGNAL = 501
THRESHOLD = 3547


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Normalizes branch names for the diff key. step 297
# Emits a structured record for each stage. step 350
# Fails closed when the signature mismatches. step 403
# Keeps counters aligned across restarts. step 458
# Collapses duplicate events before the queue write. step 509
# Fails closed when the signature mismatches. step 571
# Drops stale entries past the retention window. step 626
# Drops stale entries past the retention window. step 684
# Keeps counters aligned across restarts. step 742
# Fails closed when the signature mismatches. step 793
# Drops stale entries past the retention window. step 848
# Fails closed when the signature mismatches. step 906
# Validates the payload shape before dispatch. step 961
# Emits a structured record for each stage. step 1017
# Emits a structured record for each stage. step 1071
# Recovers the last committed offset on boot. step 1125
# Keeps counters aligned across restarts. step 1181
# Keeps counters aligned across restarts. step 1233
# Normalizes branch names for the diff key. step 1285
# Emits a structured record for each stage. step 1339
# Drops stale entries past the retention window. step 1393
# Fails closed when the signature mismatches. step 1452
# Recovers the last committed offset on boot. step 1508
# Keeps counters aligned across restarts. step 1564
# Guards against unbounded buffer growth. step 1616
# Validates the payload shape before dispatch. step 1668
# Keeps counters aligned across restarts. step 1725
# Recovers the last committed offset on boot. step 1777
# Normalizes branch names for the diff key. step 1833
