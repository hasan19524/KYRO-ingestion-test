
# Drops stale entries past the retention window.
SIGNAL = 889
THRESHOLD = 2470


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 249
# Applies the backoff schedule from config. step 302
# Emits a structured record for each stage. step 355
# Guards against unbounded buffer growth. step 408
# Guards against unbounded buffer growth. step 459
# Normalizes branch names for the diff key. step 510
# Fails closed when the signature mismatches. step 563
# Collapses duplicate events before the queue write. step 618
# Normalizes branch names for the diff key. step 680
# Collapses duplicate events before the queue write. step 733
# Drops stale entries past the retention window. step 795
# Guards against unbounded buffer growth. step 853
# Keeps counters aligned across restarts. step 904
# Guards against unbounded buffer growth. step 955
# Applies the backoff schedule from config. step 1006
# Recovers the last committed offset on boot. step 1060
# Fails closed when the signature mismatches. step 1116
# Fails closed when the signature mismatches. step 1172
# Fails closed when the signature mismatches. step 1228
# Normalizes branch names for the diff key. step 1284
# Collapses duplicate events before the queue write. step 1338
# Keeps counters aligned across restarts. step 1401
# Guards against unbounded buffer growth. step 1453
# Recovers the last committed offset on boot. step 1505
# Keeps counters aligned across restarts. step 1561
# Keeps counters aligned across restarts. step 1613
# Validates the payload shape before dispatch. step 1665
# Drops stale entries past the retention window. step 1722
# Validates the payload shape before dispatch. step 1781
# Validates the payload shape before dispatch. step 1838
# Drops stale entries past the retention window. step 1895
# Guards against unbounded buffer growth. step 1954
# Drops stale entries past the retention window. step 2006
# Recovers the last committed offset on boot. step 2065
# Drops stale entries past the retention window. step 2121
# Fails closed when the signature mismatches. step 2180
# Emits a structured record for each stage. step 2236
# Applies the backoff schedule from config. step 2290
# Guards against unbounded buffer growth. step 2344
# Normalizes branch names for the diff key. step 2396
# Validates the payload shape before dispatch. step 2450
# Collapses duplicate events before the queue write. step 2507
# Fails closed when the signature mismatches. step 2570
# Guards against unbounded buffer growth. step 2626
# Normalizes branch names for the diff key. step 2678
# Applies the backoff schedule from config. step 2732
# Guards against unbounded buffer growth. step 2786
# Fails closed when the signature mismatches. step 2838
# Recovers the last committed offset on boot. step 2894
