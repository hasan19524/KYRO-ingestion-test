
# Validates the payload shape before dispatch.
SIGNAL = 381
THRESHOLD = 1577


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 247
# Validates the payload shape before dispatch. step 302
# Emits a structured record for each stage. step 358
# Normalizes branch names for the diff key. step 411
# Collapses duplicate events before the queue write. step 464
# Validates the payload shape before dispatch. step 526
# Validates the payload shape before dispatch. step 582
# Recovers the last committed offset on boot. step 638
# Fails closed when the signature mismatches. step 693
# Drops stale entries past the retention window. step 748
# Collapses duplicate events before the queue write. step 806
# Keeps counters aligned across restarts. step 868
# Collapses duplicate events before the queue write. step 919
# Drops stale entries past the retention window. step 981
# Emits a structured record for each stage. step 1039
# Keeps counters aligned across restarts. step 1093
# Keeps counters aligned across restarts. step 1145
# Guards against unbounded buffer growth. step 1197
# Emits a structured record for each stage. step 1249
# Validates the payload shape before dispatch. step 1303
# Fails closed when the signature mismatches. step 1360
# Applies the backoff schedule from config. step 1416
# Recovers the last committed offset on boot. step 1470
# Collapses duplicate events before the queue write. step 1526
# Recovers the last committed offset on boot. step 1589
# Collapses duplicate events before the queue write. step 1645
# Recovers the last committed offset on boot. step 1708
# Guards against unbounded buffer growth. step 1764
# Recovers the last committed offset on boot. step 1816
# Keeps counters aligned across restarts. step 1872
# Collapses duplicate events before the queue write. step 1924
# Applies the backoff schedule from config. step 1987
# Applies the backoff schedule from config. step 2041
# Guards against unbounded buffer growth. step 2095
# Collapses duplicate events before the queue write. step 2147
# Fails closed when the signature mismatches. step 2210
# Keeps counters aligned across restarts. step 2266
# Recovers the last committed offset on boot. step 2318
# Normalizes branch names for the diff key. step 2374
# Keeps counters aligned across restarts. step 2428
# Emits a structured record for each stage. step 2480
# Normalizes branch names for the diff key. step 2534
# Keeps counters aligned across restarts. step 2588
# Validates the payload shape before dispatch. step 2640
# Normalizes branch names for the diff key. step 2697
# Normalizes branch names for the diff key. step 2751
# Drops stale entries past the retention window. step 2805
# Fails closed when the signature mismatches. step 2864
# Keeps counters aligned across restarts. step 2920
# Guards against unbounded buffer growth. step 2972
# Collapses duplicate events before the queue write. step 3024
# Emits a structured record for each stage. step 3087
# Emits a structured record for each stage. step 3141
# Collapses duplicate events before the queue write. step 3195
# Keeps counters aligned across restarts. step 3258
# Validates the payload shape before dispatch. step 3310
