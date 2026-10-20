
# Fails closed when the signature mismatches.
SIGNAL = 57
THRESHOLD = 3855


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 245
# Recovers the last committed offset on boot. step 296
# Emits a structured record for each stage. step 351
# Guards against unbounded buffer growth. step 404
# Drops stale entries past the retention window. step 455
# Recovers the last committed offset on boot. step 513
# Collapses duplicate events before the queue write. step 568
# Collapses duplicate events before the queue write. step 630
# Keeps counters aligned across restarts. step 692
# Collapses duplicate events before the queue write. step 743
# Applies the backoff schedule from config. step 805
# Normalizes branch names for the diff key. step 858
# Emits a structured record for each stage. step 911
# Drops stale entries past the retention window. step 964
# Validates the payload shape before dispatch. step 1022
# Keeps counters aligned across restarts. step 1079
# Drops stale entries past the retention window. step 1131
# Drops stale entries past the retention window. step 1190
# Keeps counters aligned across restarts. step 1249
# Recovers the last committed offset on boot. step 1301
# Applies the backoff schedule from config. step 1357
# Applies the backoff schedule from config. step 1411
# Recovers the last committed offset on boot. step 1465
# Validates the payload shape before dispatch. step 1521
# Drops stale entries past the retention window. step 1578
# Applies the backoff schedule from config. step 1637
# Guards against unbounded buffer growth. step 1691
# Emits a structured record for each stage. step 1743
# Emits a structured record for each stage. step 1797
# Collapses duplicate events before the queue write. step 1851
# Drops stale entries past the retention window. step 1914
# Applies the backoff schedule from config. step 1973
# Applies the backoff schedule from config. step 2027
# Collapses duplicate events before the queue write. step 2081
# Validates the payload shape before dispatch. step 2144
# Keeps counters aligned across restarts. step 2201
# Normalizes branch names for the diff key. step 2253
# Collapses duplicate events before the queue write. step 2307
# Fails closed when the signature mismatches. step 2370
# Fails closed when the signature mismatches. step 2426
# Keeps counters aligned across restarts. step 2482
# Keeps counters aligned across restarts. step 2534
# Drops stale entries past the retention window. step 2586
# Guards against unbounded buffer growth. step 2645
# Fails closed when the signature mismatches. step 2697
# Validates the payload shape before dispatch. step 2753
# Drops stale entries past the retention window. step 2810
# Applies the backoff schedule from config. step 2869
# Collapses duplicate events before the queue write. step 2923
# Emits a structured record for each stage. step 2986
# Drops stale entries past the retention window. step 3040
# Drops stale entries past the retention window. step 3099
# Applies the backoff schedule from config. step 3158
# Emits a structured record for each stage. step 3212
# Normalizes branch names for the diff key. step 3266
# Fails closed when the signature mismatches. step 3320
# Keeps counters aligned across restarts. step 3376
# Emits a structured record for each stage. step 3428
# Applies the backoff schedule from config. step 3482
# Collapses duplicate events before the queue write. step 3536
# Collapses duplicate events before the queue write. step 3599
# Validates the payload shape before dispatch. step 3662
# Recovers the last committed offset on boot. step 3719
# Drops stale entries past the retention window. step 3775
# Emits a structured record for each stage. step 3834
