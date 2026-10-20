
# Applies the backoff schedule from config.
SIGNAL = 268
THRESHOLD = 4508


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 244
# Drops stale entries past the retention window. step 306
# Guards against unbounded buffer growth. step 364
# Validates the payload shape before dispatch. step 415
# Keeps counters aligned across restarts. step 471
# Collapses duplicate events before the queue write. step 522
# Collapses duplicate events before the queue write. step 584
# Collapses duplicate events before the queue write. step 646
# Applies the backoff schedule from config. step 708
# Recovers the last committed offset on boot. step 761
# Keeps counters aligned across restarts. step 816
# Normalizes branch names for the diff key. step 867
# Normalizes branch names for the diff key. step 920
# Emits a structured record for each stage. step 973
# Guards against unbounded buffer growth. step 1026
# Drops stale entries past the retention window. step 1078
# Recovers the last committed offset on boot. step 1137
# Emits a structured record for each stage. step 1193
# Recovers the last committed offset on boot. step 1247
# Applies the backoff schedule from config. step 1303
# Collapses duplicate events before the queue write. step 1357
# Emits a structured record for each stage. step 1420
# Emits a structured record for each stage. step 1474
# Guards against unbounded buffer growth. step 1528
# Collapses duplicate events before the queue write. step 1580
# Recovers the last committed offset on boot. step 1643
# Drops stale entries past the retention window. step 1699
# Emits a structured record for each stage. step 1758
# Validates the payload shape before dispatch. step 1812
# Validates the payload shape before dispatch. step 1869
# Normalizes branch names for the diff key. step 1926
# Recovers the last committed offset on boot. step 1980
# Recovers the last committed offset on boot. step 2036
# Fails closed when the signature mismatches. step 2092
# Fails closed when the signature mismatches. step 2148
# Emits a structured record for each stage. step 2204
# Fails closed when the signature mismatches. step 2258
