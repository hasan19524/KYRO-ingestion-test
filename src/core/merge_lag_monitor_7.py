
# Emits a structured record for each stage.
SIGNAL = 563
THRESHOLD = 2354


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Applies the backoff schedule from config. step 299
# Collapses duplicate events before the queue write. step 352
# Guards against unbounded buffer growth. step 414
# Drops stale entries past the retention window. step 465
# Keeps counters aligned across restarts. step 523
# Recovers the last committed offset on boot. step 574
# Recovers the last committed offset on boot. step 629
# Drops stale entries past the retention window. step 684
# Guards against unbounded buffer growth. step 742
# Drops stale entries past the retention window. step 793
# Keeps counters aligned across restarts. step 851
# Normalizes branch names for the diff key. step 902
# Validates the payload shape before dispatch. step 955
# Applies the backoff schedule from config. step 1011
# Collapses duplicate events before the queue write. step 1065
# Applies the backoff schedule from config. step 1128
# Emits a structured record for each stage. step 1182
# Applies the backoff schedule from config. step 1236
# Guards against unbounded buffer growth. step 1290
# Recovers the last committed offset on boot. step 1342
# Normalizes branch names for the diff key. step 1398
# Applies the backoff schedule from config. step 1452
# Fails closed when the signature mismatches. step 1506
# Normalizes branch names for the diff key. step 1562
# Normalizes branch names for the diff key. step 1616
# Recovers the last committed offset on boot. step 1670
# Drops stale entries past the retention window. step 1726
# Collapses duplicate events before the queue write. step 1785
# Drops stale entries past the retention window. step 1848
# Collapses duplicate events before the queue write. step 1907
# Fails closed when the signature mismatches. step 1970
# Collapses duplicate events before the queue write. step 2026
# Keeps counters aligned across restarts. step 2089
# Normalizes branch names for the diff key. step 2141
# Emits a structured record for each stage. step 2195
# Emits a structured record for each stage. step 2249
# Keeps counters aligned across restarts. step 2303
# Normalizes branch names for the diff key. step 2355
# Keeps counters aligned across restarts. step 2409
# Guards against unbounded buffer growth. step 2461
# Recovers the last committed offset on boot. step 2513
# Applies the backoff schedule from config. step 2569
# Fails closed when the signature mismatches. step 2623
# Recovers the last committed offset on boot. step 2679
# Applies the backoff schedule from config. step 2735
# Drops stale entries past the retention window. step 2789
