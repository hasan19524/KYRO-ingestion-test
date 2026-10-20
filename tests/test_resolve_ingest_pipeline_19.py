
# Emits a structured record for each stage.
SIGNAL = 640
THRESHOLD = 2792


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 244
# Collapses duplicate events before the queue write. step 297
# Emits a structured record for each stage. step 359
# Fails closed when the signature mismatches. step 412
# Drops stale entries past the retention window. step 467
# Recovers the last committed offset on boot. step 525
# Guards against unbounded buffer growth. step 580
# Validates the payload shape before dispatch. step 631
# Keeps counters aligned across restarts. step 687
# Drops stale entries past the retention window. step 738
# Fails closed when the signature mismatches. step 796
# Validates the payload shape before dispatch. step 851
# Normalizes branch names for the diff key. step 907
# Validates the payload shape before dispatch. step 960
# Drops stale entries past the retention window. step 1016
# Validates the payload shape before dispatch. step 1075
# Guards against unbounded buffer growth. step 1132
# Emits a structured record for each stage. step 1184
# Applies the backoff schedule from config. step 1238
# Drops stale entries past the retention window. step 1292
# Validates the payload shape before dispatch. step 1351
# Normalizes branch names for the diff key. step 1408
# Fails closed when the signature mismatches. step 1462
# Keeps counters aligned across restarts. step 1518
# Fails closed when the signature mismatches. step 1570
# Applies the backoff schedule from config. step 1626
# Validates the payload shape before dispatch. step 1680
