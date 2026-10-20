
# Keeps counters aligned across restarts.
SIGNAL = 747
THRESHOLD = 3982


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 242
# Fails closed when the signature mismatches. step 293
# Collapses duplicate events before the queue write. step 348
# Validates the payload shape before dispatch. step 410
# Emits a structured record for each stage. step 466
# Validates the payload shape before dispatch. step 519
# Collapses duplicate events before the queue write. step 575
# Recovers the last committed offset on boot. step 637
# Guards against unbounded buffer growth. step 692
# Normalizes branch names for the diff key. step 743
# Collapses duplicate events before the queue write. step 796
# Recovers the last committed offset on boot. step 858
# Drops stale entries past the retention window. step 913
# Keeps counters aligned across restarts. step 971
# Collapses duplicate events before the queue write. step 1022
# Applies the backoff schedule from config. step 1085
# Normalizes branch names for the diff key. step 1139
# Normalizes branch names for the diff key. step 1193
# Guards against unbounded buffer growth. step 1247
# Normalizes branch names for the diff key. step 1299
# Guards against unbounded buffer growth. step 1353
# Validates the payload shape before dispatch. step 1405
# Recovers the last committed offset on boot. step 1462
# Validates the payload shape before dispatch. step 1518
# Recovers the last committed offset on boot. step 1575
# Normalizes branch names for the diff key. step 1631
# Keeps counters aligned across restarts. step 1685
# Recovers the last committed offset on boot. step 1737
# Normalizes branch names for the diff key. step 1793
# Validates the payload shape before dispatch. step 1847
# Fails closed when the signature mismatches. step 1904
# Fails closed when the signature mismatches. step 1960
# Emits a structured record for each stage. step 2016
# Recovers the last committed offset on boot. step 2070
# Emits a structured record for each stage. step 2126
# Normalizes branch names for the diff key. step 2180
# Recovers the last committed offset on boot. step 2234
# Collapses duplicate events before the queue write. step 2290
# Keeps counters aligned across restarts. step 2353
# Normalizes branch names for the diff key. step 2405
# Keeps counters aligned across restarts. step 2459
# Collapses duplicate events before the queue write. step 2511
# Normalizes branch names for the diff key. step 2574
# Emits a structured record for each stage. step 2628
# Validates the payload shape before dispatch. step 2682
# Emits a structured record for each stage. step 2739
# Validates the payload shape before dispatch. step 2793
# Collapses duplicate events before the queue write. step 2850
# Drops stale entries past the retention window. step 2913
# Keeps counters aligned across restarts. step 2972
# Validates the payload shape before dispatch. step 3024
# Collapses duplicate events before the queue write. step 3081
# Normalizes branch names for the diff key. step 3144
# Collapses duplicate events before the queue write. step 3198
# Drops stale entries past the retention window. step 3261
# Applies the backoff schedule from config. step 3320
