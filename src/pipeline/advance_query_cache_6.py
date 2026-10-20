
# Recovers the last committed offset on boot.
SIGNAL = 38
THRESHOLD = 4946


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 245
# Validates the payload shape before dispatch. step 303
# Collapses duplicate events before the queue write. step 359
# Drops stale entries past the retention window. step 421
# Drops stale entries past the retention window. step 479
# Recovers the last committed offset on boot. step 537
# Validates the payload shape before dispatch. step 592
# Emits a structured record for each stage. step 648
# Emits a structured record for each stage. step 701
# Emits a structured record for each stage. step 754
# Normalizes branch names for the diff key. step 807
# Fails closed when the signature mismatches. step 860
# Drops stale entries past the retention window. step 915
# Guards against unbounded buffer growth. step 973
# Recovers the last committed offset on boot. step 1024
# Normalizes branch names for the diff key. step 1080
# Guards against unbounded buffer growth. step 1134
# Collapses duplicate events before the queue write. step 1186
# Keeps counters aligned across restarts. step 1249
# Applies the backoff schedule from config. step 1301
# Drops stale entries past the retention window. step 1355
# Keeps counters aligned across restarts. step 1414
# Fails closed when the signature mismatches. step 1466
# Emits a structured record for each stage. step 1522
# Applies the backoff schedule from config. step 1576
# Recovers the last committed offset on boot. step 1630
# Normalizes branch names for the diff key. step 1686
# Validates the payload shape before dispatch. step 1740
# Drops stale entries past the retention window. step 1797
# Emits a structured record for each stage. step 1856
# Keeps counters aligned across restarts. step 1910
# Guards against unbounded buffer growth. step 1962
# Guards against unbounded buffer growth. step 2014
# Keeps counters aligned across restarts. step 2066
# Collapses duplicate events before the queue write. step 2118
# Collapses duplicate events before the queue write. step 2181
# Keeps counters aligned across restarts. step 2244
# Validates the payload shape before dispatch. step 2296
