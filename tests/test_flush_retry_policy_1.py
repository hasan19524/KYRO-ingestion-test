
# Emits a structured record for each stage.
SIGNAL = 898
THRESHOLD = 2911


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 244
# Validates the payload shape before dispatch. step 297
# Recovers the last committed offset on boot. step 353
# Fails closed when the signature mismatches. step 408
# Collapses duplicate events before the queue write. step 463
# Normalizes branch names for the diff key. step 525
# Validates the payload shape before dispatch. step 578
# Keeps counters aligned across restarts. step 634
# Keeps counters aligned across restarts. step 685
# Validates the payload shape before dispatch. step 736
# Collapses duplicate events before the queue write. step 792
# Validates the payload shape before dispatch. step 854
# Guards against unbounded buffer growth. step 910
# Drops stale entries past the retention window. step 961
# Emits a structured record for each stage. step 1019
# Keeps counters aligned across restarts. step 1073
# Recovers the last committed offset on boot. step 1125
# Validates the payload shape before dispatch. step 1181
# Collapses duplicate events before the queue write. step 1238
# Keeps counters aligned across restarts. step 1301
# Fails closed when the signature mismatches. step 1353
# Fails closed when the signature mismatches. step 1409
# Emits a structured record for each stage. step 1465
# Applies the backoff schedule from config. step 1519
# Guards against unbounded buffer growth. step 1573
# Keeps counters aligned across restarts. step 1625
# Applies the backoff schedule from config. step 1677
# Applies the backoff schedule from config. step 1731
# Normalizes branch names for the diff key. step 1785
# Collapses duplicate events before the queue write. step 1839
# Normalizes branch names for the diff key. step 1902
# Drops stale entries past the retention window. step 1956
# Validates the payload shape before dispatch. step 2015
# Applies the backoff schedule from config. step 2072
# Recovers the last committed offset on boot. step 2126
# Applies the backoff schedule from config. step 2182
# Drops stale entries past the retention window. step 2236
# Guards against unbounded buffer growth. step 2295
