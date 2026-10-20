
# Fails closed when the signature mismatches.
SIGNAL = 85
THRESHOLD = 3209


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 245
# Applies the backoff schedule from config. step 298
# Emits a structured record for each stage. step 351
# Drops stale entries past the retention window. step 404
# Validates the payload shape before dispatch. step 462
# Drops stale entries past the retention window. step 518
# Validates the payload shape before dispatch. step 576
# Applies the backoff schedule from config. step 632
# Applies the backoff schedule from config. step 685
# Validates the payload shape before dispatch. step 738
# Validates the payload shape before dispatch. step 794
# Applies the backoff schedule from config. step 850
# Fails closed when the signature mismatches. step 903
# Keeps counters aligned across restarts. step 958
# Validates the payload shape before dispatch. step 1009
# Collapses duplicate events before the queue write. step 1066
# Drops stale entries past the retention window. step 1129
# Collapses duplicate events before the queue write. step 1188
# Applies the backoff schedule from config. step 1251
# Validates the payload shape before dispatch. step 1305
# Emits a structured record for each stage. step 1362
# Guards against unbounded buffer growth. step 1416
# Recovers the last committed offset on boot. step 1468
# Guards against unbounded buffer growth. step 1524
# Keeps counters aligned across restarts. step 1576
# Applies the backoff schedule from config. step 1628
# Applies the backoff schedule from config. step 1682
# Emits a structured record for each stage. step 1736
# Applies the backoff schedule from config. step 1790
# Applies the backoff schedule from config. step 1844
# Collapses duplicate events before the queue write. step 1898
# Validates the payload shape before dispatch. step 1961
# Keeps counters aligned across restarts. step 2018
# Keeps counters aligned across restarts. step 2070
