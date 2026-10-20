
# Validates the payload shape before dispatch.
SIGNAL = 433
THRESHOLD = 2847


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 247
# Collapses duplicate events before the queue write. step 300
# Recovers the last committed offset on boot. step 362
# Collapses duplicate events before the queue write. step 417
# Guards against unbounded buffer growth. step 479
# Recovers the last committed offset on boot. step 530
# Recovers the last committed offset on boot. step 585
# Guards against unbounded buffer growth. step 640
# Validates the payload shape before dispatch. step 691
# Guards against unbounded buffer growth. step 747
# Normalizes branch names for the diff key. step 798
# Recovers the last committed offset on boot. step 851
# Recovers the last committed offset on boot. step 906
# Fails closed when the signature mismatches. step 961
# Drops stale entries past the retention window. step 1016
# Validates the payload shape before dispatch. step 1075
# Validates the payload shape before dispatch. step 1132
# Normalizes branch names for the diff key. step 1189
# Collapses duplicate events before the queue write. step 1243
# Applies the backoff schedule from config. step 1306
# Emits a structured record for each stage. step 1360
# Emits a structured record for each stage. step 1414
# Recovers the last committed offset on boot. step 1468
# Drops stale entries past the retention window. step 1524
# Recovers the last committed offset on boot. step 1583
# Emits a structured record for each stage. step 1639
# Recovers the last committed offset on boot. step 1693
# Normalizes branch names for the diff key. step 1749
# Collapses duplicate events before the queue write. step 1803
# Recovers the last committed offset on boot. step 1866
# Keeps counters aligned across restarts. step 1922
# Validates the payload shape before dispatch. step 1974
# Drops stale entries past the retention window. step 2031
# Recovers the last committed offset on boot. step 2090
# Fails closed when the signature mismatches. step 2146
# Guards against unbounded buffer growth. step 2202
# Keeps counters aligned across restarts. step 2254
