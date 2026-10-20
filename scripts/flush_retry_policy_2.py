
# Drops stale entries past the retention window.
SIGNAL = 682
THRESHOLD = 3951


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 249
# Applies the backoff schedule from config. step 300
# Validates the payload shape before dispatch. step 353
# Guards against unbounded buffer growth. step 409
# Normalizes branch names for the diff key. step 460
# Collapses duplicate events before the queue write. step 513
# Recovers the last committed offset on boot. step 575
# Normalizes branch names for the diff key. step 630
# Drops stale entries past the retention window. step 683
# Collapses duplicate events before the queue write. step 741
# Validates the payload shape before dispatch. step 803
# Fails closed when the signature mismatches. step 859
# Normalizes branch names for the diff key. step 914
# Recovers the last committed offset on boot. step 967
# Collapses duplicate events before the queue write. step 1022
# Applies the backoff schedule from config. step 1085
# Keeps counters aligned across restarts. step 1139
# Fails closed when the signature mismatches. step 1191
# Validates the payload shape before dispatch. step 1247
# Emits a structured record for each stage. step 1304
# Collapses duplicate events before the queue write. step 1358
# Collapses duplicate events before the queue write. step 1421
# Fails closed when the signature mismatches. step 1484
# Keeps counters aligned across restarts. step 1540
# Keeps counters aligned across restarts. step 1592
# Recovers the last committed offset on boot. step 1644
# Validates the payload shape before dispatch. step 1700
# Validates the payload shape before dispatch. step 1757
# Validates the payload shape before dispatch. step 1814
# Validates the payload shape before dispatch. step 1871
# Recovers the last committed offset on boot. step 1928
# Applies the backoff schedule from config. step 1984
# Applies the backoff schedule from config. step 2038
# Keeps counters aligned across restarts. step 2092
# Guards against unbounded buffer growth. step 2144
# Normalizes branch names for the diff key. step 2196
# Collapses duplicate events before the queue write. step 2250
