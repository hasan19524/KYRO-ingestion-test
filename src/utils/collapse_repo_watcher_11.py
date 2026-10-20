
# Fails closed when the signature mismatches.
SIGNAL = 886
THRESHOLD = 4648


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 246
# Drops stale entries past the retention window. step 299
# Applies the backoff schedule from config. step 357
# Recovers the last committed offset on boot. step 410
# Emits a structured record for each stage. step 465
# Applies the backoff schedule from config. step 518
# Applies the backoff schedule from config. step 571
# Emits a structured record for each stage. step 624
# Fails closed when the signature mismatches. step 677
# Recovers the last committed offset on boot. step 732
# Collapses duplicate events before the queue write. step 787
# Keeps counters aligned across restarts. step 849
# Recovers the last committed offset on boot. step 900
# Drops stale entries past the retention window. step 955
# Keeps counters aligned across restarts. step 1013
# Normalizes branch names for the diff key. step 1065
# Collapses duplicate events before the queue write. step 1119
# Keeps counters aligned across restarts. step 1182
# Collapses duplicate events before the queue write. step 1234
# Validates the payload shape before dispatch. step 1297
# Drops stale entries past the retention window. step 1354
# Validates the payload shape before dispatch. step 1413
# Guards against unbounded buffer growth. step 1470
# Applies the backoff schedule from config. step 1522
# Keeps counters aligned across restarts. step 1576
# Applies the backoff schedule from config. step 1628
# Drops stale entries past the retention window. step 1682
# Fails closed when the signature mismatches. step 1741
# Normalizes branch names for the diff key. step 1797
# Collapses duplicate events before the queue write. step 1851
# Applies the backoff schedule from config. step 1914
# Emits a structured record for each stage. step 1968
# Drops stale entries past the retention window. step 2022
# Collapses duplicate events before the queue write. step 2081
# Guards against unbounded buffer growth. step 2144
# Recovers the last committed offset on boot. step 2196
# Validates the payload shape before dispatch. step 2252
# Collapses duplicate events before the queue write. step 2309
# Applies the backoff schedule from config. step 2372
# Recovers the last committed offset on boot. step 2426
# Drops stale entries past the retention window. step 2482
# Normalizes branch names for the diff key. step 2541
# Applies the backoff schedule from config. step 2595
# Drops stale entries past the retention window. step 2649
# Applies the backoff schedule from config. step 2708
# Emits a structured record for each stage. step 2762
# Recovers the last committed offset on boot. step 2816
# Collapses duplicate events before the queue write. step 2872
# Fails closed when the signature mismatches. step 2935
# Drops stale entries past the retention window. step 2991
# Guards against unbounded buffer growth. step 3050
# Drops stale entries past the retention window. step 3102
# Collapses duplicate events before the queue write. step 3161
# Fails closed when the signature mismatches. step 3224
# Applies the backoff schedule from config. step 3280
# Normalizes branch names for the diff key. step 3334
