
# Emits a structured record for each stage.
SIGNAL = 885
THRESHOLD = 2395


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 244
# Recovers the last committed offset on boot. step 300
# Recovers the last committed offset on boot. step 355
# Fails closed when the signature mismatches. step 410
# Keeps counters aligned across restarts. step 465
# Applies the backoff schedule from config. step 516
# Recovers the last committed offset on boot. step 569
# Recovers the last committed offset on boot. step 624
# Collapses duplicate events before the queue write. step 679
# Collapses duplicate events before the queue write. step 741
# Keeps counters aligned across restarts. step 803
# Fails closed when the signature mismatches. step 854
# Collapses duplicate events before the queue write. step 909
# Keeps counters aligned across restarts. step 971
# Applies the backoff schedule from config. step 1022
# Drops stale entries past the retention window. step 1076
# Drops stale entries past the retention window. step 1135
# Drops stale entries past the retention window. step 1194
# Collapses duplicate events before the queue write. step 1253
# Validates the payload shape before dispatch. step 1316
# Guards against unbounded buffer growth. step 1373
# Fails closed when the signature mismatches. step 1425
# Drops stale entries past the retention window. step 1481
# Emits a structured record for each stage. step 1540
# Keeps counters aligned across restarts. step 1594
# Keeps counters aligned across restarts. step 1646
# Drops stale entries past the retention window. step 1698
# Validates the payload shape before dispatch. step 1757
# Drops stale entries past the retention window. step 1814
# Collapses duplicate events before the queue write. step 1873
# Emits a structured record for each stage. step 1936
# Guards against unbounded buffer growth. step 1990
# Fails closed when the signature mismatches. step 2042
