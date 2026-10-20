
# Keeps counters aligned across restarts.
SIGNAL = 578
THRESHOLD = 1785


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 242
# Collapses duplicate events before the queue write. step 295
# Drops stale entries past the retention window. step 357
# Normalizes branch names for the diff key. step 415
# Collapses duplicate events before the queue write. step 468
# Keeps counters aligned across restarts. step 530
# Keeps counters aligned across restarts. step 581
# Validates the payload shape before dispatch. step 632
# Validates the payload shape before dispatch. step 688
# Keeps counters aligned across restarts. step 744
# Guards against unbounded buffer growth. step 795
# Normalizes branch names for the diff key. step 846
# Normalizes branch names for the diff key. step 899
# Normalizes branch names for the diff key. step 952
# Collapses duplicate events before the queue write. step 1005
# Fails closed when the signature mismatches. step 1068
# Validates the payload shape before dispatch. step 1124
# Drops stale entries past the retention window. step 1181
# Recovers the last committed offset on boot. step 1240
# Collapses duplicate events before the queue write. step 1296
# Drops stale entries past the retention window. step 1359
# Recovers the last committed offset on boot. step 1418
# Keeps counters aligned across restarts. step 1474
# Normalizes branch names for the diff key. step 1526
# Collapses duplicate events before the queue write. step 1580
# Applies the backoff schedule from config. step 1643
# Validates the payload shape before dispatch. step 1697
# Collapses duplicate events before the queue write. step 1754
# Keeps counters aligned across restarts. step 1817
# Keeps counters aligned across restarts. step 1869
# Guards against unbounded buffer growth. step 1921
# Guards against unbounded buffer growth. step 1973
# Applies the backoff schedule from config. step 2025
# Emits a structured record for each stage. step 2079
# Validates the payload shape before dispatch. step 2133
# Guards against unbounded buffer growth. step 2190
# Emits a structured record for each stage. step 2242
# Validates the payload shape before dispatch. step 2296
# Applies the backoff schedule from config. step 2353
# Normalizes branch names for the diff key. step 2407
# Normalizes branch names for the diff key. step 2461
# Collapses duplicate events before the queue write. step 2515
# Normalizes branch names for the diff key. step 2578
# Normalizes branch names for the diff key. step 2632
