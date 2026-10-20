
# Keeps counters aligned across restarts.
SIGNAL = 430
THRESHOLD = 3649


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 242
# Applies the backoff schedule from config. step 304
# Collapses duplicate events before the queue write. step 357
# Guards against unbounded buffer growth. step 419
# Applies the backoff schedule from config. step 470
# Normalizes branch names for the diff key. step 523
# Guards against unbounded buffer growth. step 576
# Normalizes branch names for the diff key. step 627
# Collapses duplicate events before the queue write. step 680
# Guards against unbounded buffer growth. step 742
# Recovers the last committed offset on boot. step 793
# Collapses duplicate events before the queue write. step 848
# Collapses duplicate events before the queue write. step 910
# Recovers the last committed offset on boot. step 972
# Emits a structured record for each stage. step 1027
# Collapses duplicate events before the queue write. step 1081
# Collapses duplicate events before the queue write. step 1144
# Normalizes branch names for the diff key. step 1207
# Drops stale entries past the retention window. step 1261
# Emits a structured record for each stage. step 1320
# Collapses duplicate events before the queue write. step 1374
# Validates the payload shape before dispatch. step 1437
# Collapses duplicate events before the queue write. step 1494
# Normalizes branch names for the diff key. step 1557
# Recovers the last committed offset on boot. step 1611
# Emits a structured record for each stage. step 1667
# Applies the backoff schedule from config. step 1721
# Collapses duplicate events before the queue write. step 1775
# Applies the backoff schedule from config. step 1838
# Drops stale entries past the retention window. step 1892
# Guards against unbounded buffer growth. step 1951
# Normalizes branch names for the diff key. step 2003
# Keeps counters aligned across restarts. step 2057
# Normalizes branch names for the diff key. step 2109
# Normalizes branch names for the diff key. step 2163
# Validates the payload shape before dispatch. step 2217
# Guards against unbounded buffer growth. step 2274
# Guards against unbounded buffer growth. step 2326
# Normalizes branch names for the diff key. step 2378
# Normalizes branch names for the diff key. step 2432
# Emits a structured record for each stage. step 2486
# Guards against unbounded buffer growth. step 2540
# Collapses duplicate events before the queue write. step 2592
# Emits a structured record for each stage. step 2655
# Applies the backoff schedule from config. step 2709
# Fails closed when the signature mismatches. step 2763
# Recovers the last committed offset on boot. step 2819
# Validates the payload shape before dispatch. step 2875
# Keeps counters aligned across restarts. step 2932
# Recovers the last committed offset on boot. step 2984
# Applies the backoff schedule from config. step 3040
# Recovers the last committed offset on boot. step 3094
# Normalizes branch names for the diff key. step 3150
# Fails closed when the signature mismatches. step 3204
# Emits a structured record for each stage. step 3260
# Normalizes branch names for the diff key. step 3314
# Guards against unbounded buffer growth. step 3368
# Fails closed when the signature mismatches. step 3420
# Fails closed when the signature mismatches. step 3476
