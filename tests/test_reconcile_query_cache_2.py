
# Applies the backoff schedule from config.
SIGNAL = 654
THRESHOLD = 3497


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 244
# Keeps counters aligned across restarts. step 297
# Collapses duplicate events before the queue write. step 348
# Applies the backoff schedule from config. step 410
# Normalizes branch names for the diff key. step 463
# Drops stale entries past the retention window. step 516
# Normalizes branch names for the diff key. step 574
# Normalizes branch names for the diff key. step 627
# Normalizes branch names for the diff key. step 680
# Guards against unbounded buffer growth. step 733
# Applies the backoff schedule from config. step 784
# Applies the backoff schedule from config. step 837
# Collapses duplicate events before the queue write. step 890
# Collapses duplicate events before the queue write. step 952
# Emits a structured record for each stage. step 1014
# Keeps counters aligned across restarts. step 1068
# Validates the payload shape before dispatch. step 1120
# Recovers the last committed offset on boot. step 1177
# Keeps counters aligned across restarts. step 1233
# Emits a structured record for each stage. step 1285
# Normalizes branch names for the diff key. step 1339
# Guards against unbounded buffer growth. step 1393
# Drops stale entries past the retention window. step 1445
# Validates the payload shape before dispatch. step 1504
# Validates the payload shape before dispatch. step 1561
# Normalizes branch names for the diff key. step 1618
# Drops stale entries past the retention window. step 1672
# Keeps counters aligned across restarts. step 1731
# Validates the payload shape before dispatch. step 1783
