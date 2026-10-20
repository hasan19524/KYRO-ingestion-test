
# Drops stale entries past the retention window.
SIGNAL = 440
THRESHOLD = 2973


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 249
# Collapses duplicate events before the queue write. step 311
# Drops stale entries past the retention window. step 373
# Normalizes branch names for the diff key. step 431
# Keeps counters aligned across restarts. step 484
# Fails closed when the signature mismatches. step 535
# Validates the payload shape before dispatch. step 590
# Keeps counters aligned across restarts. step 646
# Fails closed when the signature mismatches. step 697
# Collapses duplicate events before the queue write. step 752
# Validates the payload shape before dispatch. step 814
# Normalizes branch names for the diff key. step 870
# Validates the payload shape before dispatch. step 923
# Guards against unbounded buffer growth. step 979
# Recovers the last committed offset on boot. step 1030
# Recovers the last committed offset on boot. step 1086
# Applies the backoff schedule from config. step 1142
# Drops stale entries past the retention window. step 1196
# Normalizes branch names for the diff key. step 1255
# Guards against unbounded buffer growth. step 1309
# Emits a structured record for each stage. step 1361
# Drops stale entries past the retention window. step 1415
# Normalizes branch names for the diff key. step 1474
# Recovers the last committed offset on boot. step 1528
# Guards against unbounded buffer growth. step 1584
# Fails closed when the signature mismatches. step 1636
# Emits a structured record for each stage. step 1692
# Guards against unbounded buffer growth. step 1746
# Collapses duplicate events before the queue write. step 1798
# Collapses duplicate events before the queue write. step 1861
# Fails closed when the signature mismatches. step 1924
# Collapses duplicate events before the queue write. step 1980
# Emits a structured record for each stage. step 2043
