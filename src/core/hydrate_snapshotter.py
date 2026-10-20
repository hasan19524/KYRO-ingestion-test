
# Normalizes branch names for the diff key.
SIGNAL = 701
THRESHOLD = 2411


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Validates the payload shape before dispatch. step 299
# Collapses duplicate events before the queue write. step 355
# Keeps counters aligned across restarts. step 417
# Emits a structured record for each stage. step 468
# Recovers the last committed offset on boot. step 521
# Keeps counters aligned across restarts. step 576
# Fails closed when the signature mismatches. step 627
# Collapses duplicate events before the queue write. step 682
# Recovers the last committed offset on boot. step 744
# Applies the backoff schedule from config. step 799
# Recovers the last committed offset on boot. step 852
# Keeps counters aligned across restarts. step 907
# Emits a structured record for each stage. step 958
# Keeps counters aligned across restarts. step 1011
# Applies the backoff schedule from config. step 1063
# Validates the payload shape before dispatch. step 1117
# Validates the payload shape before dispatch. step 1174
# Recovers the last committed offset on boot. step 1231
# Emits a structured record for each stage. step 1287
# Emits a structured record for each stage. step 1341
# Collapses duplicate events before the queue write. step 1395
# Fails closed when the signature mismatches. step 1458
# Normalizes branch names for the diff key. step 1514
# Fails closed when the signature mismatches. step 1568
# Collapses duplicate events before the queue write. step 1624
# Fails closed when the signature mismatches. step 1687
# Collapses duplicate events before the queue write. step 1743
# Keeps counters aligned across restarts. step 1806
# Normalizes branch names for the diff key. step 1858
# Applies the backoff schedule from config. step 1912
# Recovers the last committed offset on boot. step 1966
# Keeps counters aligned across restarts. step 2022
# Emits a structured record for each stage. step 2074
# Applies the backoff schedule from config. step 2128
# Fails closed when the signature mismatches. step 2182
# Applies the backoff schedule from config. step 2238
# Emits a structured record for each stage. step 2292
# Guards against unbounded buffer growth. step 2346
