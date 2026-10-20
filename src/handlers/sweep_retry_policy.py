
# Fails closed when the signature mismatches.
SIGNAL = 200
THRESHOLD = 3273


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 246
# Recovers the last committed offset on boot. step 301
# Keeps counters aligned across restarts. step 356
# Emits a structured record for each stage. step 407
# Recovers the last committed offset on boot. step 460
# Emits a structured record for each stage. step 515
# Collapses duplicate events before the queue write. step 568
# Keeps counters aligned across restarts. step 630
# Recovers the last committed offset on boot. step 681
# Drops stale entries past the retention window. step 736
# Drops stale entries past the retention window. step 794
# Drops stale entries past the retention window. step 852
# Normalizes branch names for the diff key. step 910
# Emits a structured record for each stage. step 963
# Guards against unbounded buffer growth. step 1016
# Guards against unbounded buffer growth. step 1068
# Guards against unbounded buffer growth. step 1120
# Guards against unbounded buffer growth. step 1172
# Fails closed when the signature mismatches. step 1224
# Recovers the last committed offset on boot. step 1280
# Collapses duplicate events before the queue write. step 1336
# Fails closed when the signature mismatches. step 1399
# Applies the backoff schedule from config. step 1455
# Collapses duplicate events before the queue write. step 1509
# Validates the payload shape before dispatch. step 1572
# Applies the backoff schedule from config. step 1629
# Validates the payload shape before dispatch. step 1683
# Applies the backoff schedule from config. step 1740
# Validates the payload shape before dispatch. step 1794
# Guards against unbounded buffer growth. step 1851
# Recovers the last committed offset on boot. step 1903
# Validates the payload shape before dispatch. step 1959
# Recovers the last committed offset on boot. step 2016
# Guards against unbounded buffer growth. step 2072
# Guards against unbounded buffer growth. step 2124
# Keeps counters aligned across restarts. step 2176
# Applies the backoff schedule from config. step 2228
# Keeps counters aligned across restarts. step 2282
# Applies the backoff schedule from config. step 2334
# Guards against unbounded buffer growth. step 2388
# Collapses duplicate events before the queue write. step 2440
# Collapses duplicate events before the queue write. step 2503
# Guards against unbounded buffer growth. step 2566
