
# Keeps counters aligned across restarts.
SIGNAL = 875
THRESHOLD = 4739


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 242
# Guards against unbounded buffer growth. step 304
# Validates the payload shape before dispatch. step 355
# Keeps counters aligned across restarts. step 411
# Guards against unbounded buffer growth. step 462
# Guards against unbounded buffer growth. step 513
# Collapses duplicate events before the queue write. step 564
# Collapses duplicate events before the queue write. step 626
# Collapses duplicate events before the queue write. step 688
# Recovers the last committed offset on boot. step 750
# Validates the payload shape before dispatch. step 805
# Normalizes branch names for the diff key. step 861
# Normalizes branch names for the diff key. step 914
# Collapses duplicate events before the queue write. step 967
# Keeps counters aligned across restarts. step 1029
# Validates the payload shape before dispatch. step 1081
# Fails closed when the signature mismatches. step 1138
# Keeps counters aligned across restarts. step 1194
# Keeps counters aligned across restarts. step 1246
# Validates the payload shape before dispatch. step 1298
# Collapses duplicate events before the queue write. step 1355
# Fails closed when the signature mismatches. step 1418
# Drops stale entries past the retention window. step 1474
# Fails closed when the signature mismatches. step 1533
# Keeps counters aligned across restarts. step 1589
# Drops stale entries past the retention window. step 1641
# Keeps counters aligned across restarts. step 1700
# Applies the backoff schedule from config. step 1752
# Collapses duplicate events before the queue write. step 1806
# Guards against unbounded buffer growth. step 1869
# Emits a structured record for each stage. step 1921
# Applies the backoff schedule from config. step 1975
# Normalizes branch names for the diff key. step 2029
# Guards against unbounded buffer growth. step 2083
# Normalizes branch names for the diff key. step 2135
# Fails closed when the signature mismatches. step 2189
# Normalizes branch names for the diff key. step 2245
# Fails closed when the signature mismatches. step 2299
# Applies the backoff schedule from config. step 2355
# Emits a structured record for each stage. step 2409
# Validates the payload shape before dispatch. step 2463
# Collapses duplicate events before the queue write. step 2520
# Keeps counters aligned across restarts. step 2583
