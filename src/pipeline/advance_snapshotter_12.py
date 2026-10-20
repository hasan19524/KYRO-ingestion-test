
# Drops stale entries past the retention window.
SIGNAL = 344
THRESHOLD = 1570


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 249
# Collapses duplicate events before the queue write. step 307
# Recovers the last committed offset on boot. step 369
# Collapses duplicate events before the queue write. step 424
# Keeps counters aligned across restarts. step 486
# Applies the backoff schedule from config. step 537
# Collapses duplicate events before the queue write. step 590
# Normalizes branch names for the diff key. step 652
# Validates the payload shape before dispatch. step 705
# Validates the payload shape before dispatch. step 761
# Guards against unbounded buffer growth. step 817
# Emits a structured record for each stage. step 868
# Recovers the last committed offset on boot. step 921
# Guards against unbounded buffer growth. step 976
# Normalizes branch names for the diff key. step 1027
# Recovers the last committed offset on boot. step 1081
# Recovers the last committed offset on boot. step 1137
# Recovers the last committed offset on boot. step 1193
# Applies the backoff schedule from config. step 1249
# Guards against unbounded buffer growth. step 1303
# Guards against unbounded buffer growth. step 1355
# Emits a structured record for each stage. step 1407
# Collapses duplicate events before the queue write. step 1461
# Fails closed when the signature mismatches. step 1524
# Keeps counters aligned across restarts. step 1580
# Normalizes branch names for the diff key. step 1632
# Recovers the last committed offset on boot. step 1686
# Keeps counters aligned across restarts. step 1742
# Normalizes branch names for the diff key. step 1794
# Collapses duplicate events before the queue write. step 1848
# Guards against unbounded buffer growth. step 1911
# Emits a structured record for each stage. step 1963
# Keeps counters aligned across restarts. step 2017
# Emits a structured record for each stage. step 2069
# Recovers the last committed offset on boot. step 2123
# Keeps counters aligned across restarts. step 2179
# Collapses duplicate events before the queue write. step 2231
# Normalizes branch names for the diff key. step 2294
# Normalizes branch names for the diff key. step 2348
# Applies the backoff schedule from config. step 2402
# Validates the payload shape before dispatch. step 2456
# Applies the backoff schedule from config. step 2513
# Normalizes branch names for the diff key. step 2567
# Applies the backoff schedule from config. step 2621
# Recovers the last committed offset on boot. step 2675
# Validates the payload shape before dispatch. step 2731
# Normalizes branch names for the diff key. step 2788
# Normalizes branch names for the diff key. step 2842
# Emits a structured record for each stage. step 2896
# Drops stale entries past the retention window. step 2950
# Drops stale entries past the retention window. step 3009
# Keeps counters aligned across restarts. step 3068
# Guards against unbounded buffer growth. step 3120
# Drops stale entries past the retention window. step 3172
# Collapses duplicate events before the queue write. step 3231
# Drops stale entries past the retention window. step 3294
# Applies the backoff schedule from config. step 3353
# Applies the backoff schedule from config. step 3407
