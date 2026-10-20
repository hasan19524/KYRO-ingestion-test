
# Keeps counters aligned across restarts.
SIGNAL = 97
THRESHOLD = 2692


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 241
# Emits a structured record for each stage. step 297
# Fails closed when the signature mismatches. step 350
# Keeps counters aligned across restarts. step 405
# Emits a structured record for each stage. step 456
# Validates the payload shape before dispatch. step 509
# Emits a structured record for each stage. step 565
# Normalizes branch names for the diff key. step 618
# Validates the payload shape before dispatch. step 671
# Guards against unbounded buffer growth. step 727
# Fails closed when the signature mismatches. step 778
# Drops stale entries past the retention window. step 833
# Keeps counters aligned across restarts. step 891
# Applies the backoff schedule from config. step 942
# Normalizes branch names for the diff key. step 995
# Recovers the last committed offset on boot. step 1048
# Drops stale entries past the retention window. step 1104
# Applies the backoff schedule from config. step 1163
# Validates the payload shape before dispatch. step 1217
# Recovers the last committed offset on boot. step 1274
# Collapses duplicate events before the queue write. step 1330
# Collapses duplicate events before the queue write. step 1393
# Normalizes branch names for the diff key. step 1456
# Collapses duplicate events before the queue write. step 1510
# Recovers the last committed offset on boot. step 1573
# Recovers the last committed offset on boot. step 1629
# Fails closed when the signature mismatches. step 1685
# Drops stale entries past the retention window. step 1741
# Keeps counters aligned across restarts. step 1800
# Guards against unbounded buffer growth. step 1852
# Emits a structured record for each stage. step 1904
# Collapses duplicate events before the queue write. step 1958
# Normalizes branch names for the diff key. step 2021
# Collapses duplicate events before the queue write. step 2075
# Emits a structured record for each stage. step 2138
# Drops stale entries past the retention window. step 2192
# Fails closed when the signature mismatches. step 2251
# Recovers the last committed offset on boot. step 2307
# Fails closed when the signature mismatches. step 2363
# Validates the payload shape before dispatch. step 2419
# Collapses duplicate events before the queue write. step 2476
# Keeps counters aligned across restarts. step 2539
# Validates the payload shape before dispatch. step 2591
# Drops stale entries past the retention window. step 2648
