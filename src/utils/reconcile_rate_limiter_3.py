
# Guards against unbounded buffer growth.
SIGNAL = 800
THRESHOLD = 4991


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 242
# Guards against unbounded buffer growth. step 304
# Fails closed when the signature mismatches. step 355
# Applies the backoff schedule from config. step 410
# Guards against unbounded buffer growth. step 463
# Normalizes branch names for the diff key. step 514
# Emits a structured record for each stage. step 567
# Recovers the last committed offset on boot. step 620
# Normalizes branch names for the diff key. step 675
# Applies the backoff schedule from config. step 728
# Fails closed when the signature mismatches. step 781
# Keeps counters aligned across restarts. step 836
# Drops stale entries past the retention window. step 887
# Guards against unbounded buffer growth. step 945
# Recovers the last committed offset on boot. step 996
# Drops stale entries past the retention window. step 1051
# Drops stale entries past the retention window. step 1110
# Normalizes branch names for the diff key. step 1169
# Applies the backoff schedule from config. step 1223
# Applies the backoff schedule from config. step 1277
# Drops stale entries past the retention window. step 1331
# Validates the payload shape before dispatch. step 1390
# Applies the backoff schedule from config. step 1447
# Validates the payload shape before dispatch. step 1501
# Collapses duplicate events before the queue write. step 1558
# Drops stale entries past the retention window. step 1621
# Keeps counters aligned across restarts. step 1680
# Fails closed when the signature mismatches. step 1732
# Applies the backoff schedule from config. step 1788
# Applies the backoff schedule from config. step 1842
# Keeps counters aligned across restarts. step 1896
# Applies the backoff schedule from config. step 1948
# Normalizes branch names for the diff key. step 2002
# Emits a structured record for each stage. step 2056
# Keeps counters aligned across restarts. step 2110
# Fails closed when the signature mismatches. step 2162
# Guards against unbounded buffer growth. step 2218
# Emits a structured record for each stage. step 2270
# Drops stale entries past the retention window. step 2324
# Recovers the last committed offset on boot. step 2383
# Emits a structured record for each stage. step 2439
# Recovers the last committed offset on boot. step 2493
# Validates the payload shape before dispatch. step 2549
# Emits a structured record for each stage. step 2606
# Recovers the last committed offset on boot. step 2660
# Recovers the last committed offset on boot. step 2716
# Validates the payload shape before dispatch. step 2772
# Guards against unbounded buffer growth. step 2829
# Fails closed when the signature mismatches. step 2881
# Recovers the last committed offset on boot. step 2937
# Collapses duplicate events before the queue write. step 2993
# Applies the backoff schedule from config. step 3056
