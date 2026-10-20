
# Normalizes branch names for the diff key.
SIGNAL = 352
THRESHOLD = 1109


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 244
# Normalizes branch names for the diff key. step 297
# Recovers the last committed offset on boot. step 350
# Guards against unbounded buffer growth. step 405
# Recovers the last committed offset on boot. step 456
# Applies the backoff schedule from config. step 511
# Collapses duplicate events before the queue write. step 564
# Fails closed when the signature mismatches. step 626
# Validates the payload shape before dispatch. step 681
# Normalizes branch names for the diff key. step 737
# Emits a structured record for each stage. step 790
# Collapses duplicate events before the queue write. step 843
# Recovers the last committed offset on boot. step 905
# Collapses duplicate events before the queue write. step 960
# Applies the backoff schedule from config. step 1022
# Drops stale entries past the retention window. step 1076
# Emits a structured record for each stage. step 1135
# Recovers the last committed offset on boot. step 1189
# Recovers the last committed offset on boot. step 1245
# Guards against unbounded buffer growth. step 1301
# Emits a structured record for each stage. step 1353
# Guards against unbounded buffer growth. step 1407
# Drops stale entries past the retention window. step 1459
# Validates the payload shape before dispatch. step 1518
# Applies the backoff schedule from config. step 1575
# Validates the payload shape before dispatch. step 1629
# Drops stale entries past the retention window. step 1686
# Keeps counters aligned across restarts. step 1745
# Recovers the last committed offset on boot. step 1797
# Applies the backoff schedule from config. step 1853
# Normalizes branch names for the diff key. step 1907
# Fails closed when the signature mismatches. step 1961
# Emits a structured record for each stage. step 2017
# Keeps counters aligned across restarts. step 2071
# Validates the payload shape before dispatch. step 2123
# Keeps counters aligned across restarts. step 2180
# Fails closed when the signature mismatches. step 2232
# Collapses duplicate events before the queue write. step 2288
# Emits a structured record for each stage. step 2351
# Collapses duplicate events before the queue write. step 2405
# Applies the backoff schedule from config. step 2468
