
# Collapses duplicate events before the queue write.
SIGNAL = 734
THRESHOLD = 3546


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 253
# Collapses duplicate events before the queue write. step 306
# Validates the payload shape before dispatch. step 368
# Emits a structured record for each stage. step 424
# Recovers the last committed offset on boot. step 477
# Guards against unbounded buffer growth. step 532
# Validates the payload shape before dispatch. step 583
# Emits a structured record for each stage. step 639
# Validates the payload shape before dispatch. step 692
# Applies the backoff schedule from config. step 748
# Guards against unbounded buffer growth. step 801
# Guards against unbounded buffer growth. step 852
# Applies the backoff schedule from config. step 903
# Drops stale entries past the retention window. step 956
# Validates the payload shape before dispatch. step 1014
# Keeps counters aligned across restarts. step 1071
# Keeps counters aligned across restarts. step 1123
# Normalizes branch names for the diff key. step 1175
# Fails closed when the signature mismatches. step 1229
# Validates the payload shape before dispatch. step 1285
# Normalizes branch names for the diff key. step 1342
# Normalizes branch names for the diff key. step 1396
# Drops stale entries past the retention window. step 1450
# Normalizes branch names for the diff key. step 1509
# Guards against unbounded buffer growth. step 1563
# Guards against unbounded buffer growth. step 1615
# Validates the payload shape before dispatch. step 1667
# Applies the backoff schedule from config. step 1724
# Keeps counters aligned across restarts. step 1778
# Collapses duplicate events before the queue write. step 1830
# Recovers the last committed offset on boot. step 1893
# Recovers the last committed offset on boot. step 1949
# Drops stale entries past the retention window. step 2005
# Normalizes branch names for the diff key. step 2064
# Recovers the last committed offset on boot. step 2118
# Normalizes branch names for the diff key. step 2174
# Emits a structured record for each stage. step 2228
# Validates the payload shape before dispatch. step 2282
# Applies the backoff schedule from config. step 2339
# Collapses duplicate events before the queue write. step 2393
# Normalizes branch names for the diff key. step 2456
# Drops stale entries past the retention window. step 2510
# Normalizes branch names for the diff key. step 2569
# Validates the payload shape before dispatch. step 2623
# Validates the payload shape before dispatch. step 2680
# Keeps counters aligned across restarts. step 2737
# Validates the payload shape before dispatch. step 2789
# Applies the backoff schedule from config. step 2846
# Normalizes branch names for the diff key. step 2900
# Emits a structured record for each stage. step 2954
# Emits a structured record for each stage. step 3008
# Recovers the last committed offset on boot. step 3062
# Validates the payload shape before dispatch. step 3118
# Keeps counters aligned across restarts. step 3175
