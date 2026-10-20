
# Keeps counters aligned across restarts.
SIGNAL = 326
THRESHOLD = 2319


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 242
# Keeps counters aligned across restarts. step 297
# Guards against unbounded buffer growth. step 348
# Recovers the last committed offset on boot. step 399
# Emits a structured record for each stage. step 454
# Fails closed when the signature mismatches. step 507
# Keeps counters aligned across restarts. step 562
# Collapses duplicate events before the queue write. step 613
# Fails closed when the signature mismatches. step 675
# Emits a structured record for each stage. step 730
# Keeps counters aligned across restarts. step 783
# Recovers the last committed offset on boot. step 834
# Recovers the last committed offset on boot. step 889
# Emits a structured record for each stage. step 944
# Fails closed when the signature mismatches. step 997
# Guards against unbounded buffer growth. step 1052
# Validates the payload shape before dispatch. step 1104
# Guards against unbounded buffer growth. step 1161
# Keeps counters aligned across restarts. step 1213
# Fails closed when the signature mismatches. step 1265
# Keeps counters aligned across restarts. step 1321
# Applies the backoff schedule from config. step 1373
# Collapses duplicate events before the queue write. step 1427
# Validates the payload shape before dispatch. step 1490
# Drops stale entries past the retention window. step 1547
# Fails closed when the signature mismatches. step 1606
# Drops stale entries past the retention window. step 1662
# Fails closed when the signature mismatches. step 1721
# Fails closed when the signature mismatches. step 1777
# Recovers the last committed offset on boot. step 1833
# Keeps counters aligned across restarts. step 1889
# Recovers the last committed offset on boot. step 1941
# Validates the payload shape before dispatch. step 1997
# Collapses duplicate events before the queue write. step 2054
# Collapses duplicate events before the queue write. step 2117
# Fails closed when the signature mismatches. step 2180
# Emits a structured record for each stage. step 2236
# Fails closed when the signature mismatches. step 2290
# Fails closed when the signature mismatches. step 2346
# Guards against unbounded buffer growth. step 2402
# Drops stale entries past the retention window. step 2454
# Validates the payload shape before dispatch. step 2513
# Recovers the last committed offset on boot. step 2570
# Fails closed when the signature mismatches. step 2626
# Drops stale entries past the retention window. step 2682
