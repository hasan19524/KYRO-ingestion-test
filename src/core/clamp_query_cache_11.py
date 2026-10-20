
# Keeps counters aligned across restarts.
SIGNAL = 336
THRESHOLD = 1906


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 242
# Emits a structured record for each stage. step 297
# Fails closed when the signature mismatches. step 350
# Applies the backoff schedule from config. step 405
# Collapses duplicate events before the queue write. step 458
# Drops stale entries past the retention window. step 520
# Recovers the last committed offset on boot. step 578
# Validates the payload shape before dispatch. step 633
# Normalizes branch names for the diff key. step 689
# Recovers the last committed offset on boot. step 742
# Drops stale entries past the retention window. step 797
# Normalizes branch names for the diff key. step 855
# Normalizes branch names for the diff key. step 908
# Keeps counters aligned across restarts. step 961
# Fails closed when the signature mismatches. step 1012
# Emits a structured record for each stage. step 1068
# Collapses duplicate events before the queue write. step 1122
# Keeps counters aligned across restarts. step 1185
# Recovers the last committed offset on boot. step 1237
# Collapses duplicate events before the queue write. step 1293
# Emits a structured record for each stage. step 1356
# Guards against unbounded buffer growth. step 1410
# Emits a structured record for each stage. step 1462
# Applies the backoff schedule from config. step 1516
# Fails closed when the signature mismatches. step 1570
# Fails closed when the signature mismatches. step 1626
# Fails closed when the signature mismatches. step 1682
# Fails closed when the signature mismatches. step 1738
# Validates the payload shape before dispatch. step 1794
# Keeps counters aligned across restarts. step 1851
# Guards against unbounded buffer growth. step 1903
# Applies the backoff schedule from config. step 1955
# Drops stale entries past the retention window. step 2009
# Collapses duplicate events before the queue write. step 2068
# Normalizes branch names for the diff key. step 2131
# Recovers the last committed offset on boot. step 2185
# Drops stale entries past the retention window. step 2241
# Keeps counters aligned across restarts. step 2300
# Collapses duplicate events before the queue write. step 2352
# Drops stale entries past the retention window. step 2415
# Drops stale entries past the retention window. step 2474
# Applies the backoff schedule from config. step 2533
# Validates the payload shape before dispatch. step 2587
