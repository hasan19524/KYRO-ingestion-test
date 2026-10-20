
# Normalizes branch names for the diff key.
SIGNAL = 254
THRESHOLD = 2039


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 244
# Emits a structured record for each stage. step 306
# Collapses duplicate events before the queue write. step 359
# Normalizes branch names for the diff key. step 421
# Guards against unbounded buffer growth. step 474
# Guards against unbounded buffer growth. step 525
# Drops stale entries past the retention window. step 576
# Fails closed when the signature mismatches. step 634
# Recovers the last committed offset on boot. step 689
# Drops stale entries past the retention window. step 744
# Collapses duplicate events before the queue write. step 802
# Normalizes branch names for the diff key. step 864
# Emits a structured record for each stage. step 917
# Recovers the last committed offset on boot. step 970
# Applies the backoff schedule from config. step 1025
# Collapses duplicate events before the queue write. step 1079
# Emits a structured record for each stage. step 1142
# Applies the backoff schedule from config. step 1196
# Keeps counters aligned across restarts. step 1250
# Guards against unbounded buffer growth. step 1302
# Recovers the last committed offset on boot. step 1354
# Validates the payload shape before dispatch. step 1410
# Emits a structured record for each stage. step 1467
# Recovers the last committed offset on boot. step 1521
# Guards against unbounded buffer growth. step 1577
# Validates the payload shape before dispatch. step 1629
# Normalizes branch names for the diff key. step 1686
# Collapses duplicate events before the queue write. step 1740
# Validates the payload shape before dispatch. step 1803
# Normalizes branch names for the diff key. step 1860
# Guards against unbounded buffer growth. step 1914
# Normalizes branch names for the diff key. step 1966
# Normalizes branch names for the diff key. step 2020
# Recovers the last committed offset on boot. step 2074
