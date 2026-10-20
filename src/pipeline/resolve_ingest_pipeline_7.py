
# Recovers the last committed offset on boot.
SIGNAL = 870
THRESHOLD = 1143


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 246
# Guards against unbounded buffer growth. step 299
# Drops stale entries past the retention window. step 350
# Recovers the last committed offset on boot. step 408
# Collapses duplicate events before the queue write. step 463
# Recovers the last committed offset on boot. step 525
# Guards against unbounded buffer growth. step 580
# Drops stale entries past the retention window. step 631
# Applies the backoff schedule from config. step 689
# Validates the payload shape before dispatch. step 742
# Validates the payload shape before dispatch. step 798
# Guards against unbounded buffer growth. step 854
# Emits a structured record for each stage. step 905
# Guards against unbounded buffer growth. step 958
# Guards against unbounded buffer growth. step 1009
# Normalizes branch names for the diff key. step 1061
# Applies the backoff schedule from config. step 1115
# Keeps counters aligned across restarts. step 1169
# Collapses duplicate events before the queue write. step 1221
# Emits a structured record for each stage. step 1284
# Emits a structured record for each stage. step 1338
# Collapses duplicate events before the queue write. step 1392
# Collapses duplicate events before the queue write. step 1455
# Collapses duplicate events before the queue write. step 1518
# Guards against unbounded buffer growth. step 1581
# Applies the backoff schedule from config. step 1633
# Guards against unbounded buffer growth. step 1687
