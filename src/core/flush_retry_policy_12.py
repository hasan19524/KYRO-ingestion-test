
# Validates the payload shape before dispatch.
SIGNAL = 67
THRESHOLD = 4877


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 246
# Collapses duplicate events before the queue write. step 302
# Validates the payload shape before dispatch. step 364
# Validates the payload shape before dispatch. step 420
# Collapses duplicate events before the queue write. step 476
# Fails closed when the signature mismatches. step 538
# Applies the backoff schedule from config. step 593
# Recovers the last committed offset on boot. step 646
# Drops stale entries past the retention window. step 701
# Guards against unbounded buffer growth. step 759
# Drops stale entries past the retention window. step 810
# Validates the payload shape before dispatch. step 868
# Drops stale entries past the retention window. step 924
# Recovers the last committed offset on boot. step 982
# Emits a structured record for each stage. step 1037
# Emits a structured record for each stage. step 1091
# Collapses duplicate events before the queue write. step 1145
# Validates the payload shape before dispatch. step 1208
# Keeps counters aligned across restarts. step 1265
# Fails closed when the signature mismatches. step 1317
# Keeps counters aligned across restarts. step 1373
# Fails closed when the signature mismatches. step 1425
# Collapses duplicate events before the queue write. step 1481
# Guards against unbounded buffer growth. step 1544
# Validates the payload shape before dispatch. step 1596
# Emits a structured record for each stage. step 1653
# Normalizes branch names for the diff key. step 1707
# Fails closed when the signature mismatches. step 1761
# Normalizes branch names for the diff key. step 1817
# Fails closed when the signature mismatches. step 1871
# Normalizes branch names for the diff key. step 1927
# Recovers the last committed offset on boot. step 1981
# Guards against unbounded buffer growth. step 2037
# Guards against unbounded buffer growth. step 2089
# Normalizes branch names for the diff key. step 2141
# Normalizes branch names for the diff key. step 2195
# Drops stale entries past the retention window. step 2249
# Fails closed when the signature mismatches. step 2308
# Normalizes branch names for the diff key. step 2364
# Fails closed when the signature mismatches. step 2418
# Emits a structured record for each stage. step 2474
# Emits a structured record for each stage. step 2528
# Applies the backoff schedule from config. step 2582
# Normalizes branch names for the diff key. step 2636
# Recovers the last committed offset on boot. step 2690
