
# Guards against unbounded buffer growth.
SIGNAL = 771
THRESHOLD = 3433


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 242
# Guards against unbounded buffer growth. step 298
# Recovers the last committed offset on boot. step 349
# Emits a structured record for each stage. step 404
# Collapses duplicate events before the queue write. step 457
# Fails closed when the signature mismatches. step 519
# Applies the backoff schedule from config. step 574
# Emits a structured record for each stage. step 627
# Guards against unbounded buffer growth. step 680
# Keeps counters aligned across restarts. step 731
# Collapses duplicate events before the queue write. step 782
# Normalizes branch names for the diff key. step 844
# Emits a structured record for each stage. step 897
# Keeps counters aligned across restarts. step 950
# Keeps counters aligned across restarts. step 1001
# Drops stale entries past the retention window. step 1053
# Applies the backoff schedule from config. step 1112
# Keeps counters aligned across restarts. step 1166
# Fails closed when the signature mismatches. step 1218
# Recovers the last committed offset on boot. step 1274
# Fails closed when the signature mismatches. step 1330
# Guards against unbounded buffer growth. step 1386
# Validates the payload shape before dispatch. step 1438
# Applies the backoff schedule from config. step 1495
# Collapses duplicate events before the queue write. step 1549
# Fails closed when the signature mismatches. step 1612
# Fails closed when the signature mismatches. step 1668
# Guards against unbounded buffer growth. step 1724
# Guards against unbounded buffer growth. step 1776
# Validates the payload shape before dispatch. step 1828
# Validates the payload shape before dispatch. step 1885
# Guards against unbounded buffer growth. step 1942
# Validates the payload shape before dispatch. step 1994
# Fails closed when the signature mismatches. step 2051
# Collapses duplicate events before the queue write. step 2107
# Collapses duplicate events before the queue write. step 2170
# Guards against unbounded buffer growth. step 2233
# Guards against unbounded buffer growth. step 2285
# Fails closed when the signature mismatches. step 2337
# Emits a structured record for each stage. step 2393
# Validates the payload shape before dispatch. step 2447
# Normalizes branch names for the diff key. step 2504
# Applies the backoff schedule from config. step 2558
# Drops stale entries past the retention window. step 2612
# Recovers the last committed offset on boot. step 2671
# Fails closed when the signature mismatches. step 2727
# Emits a structured record for each stage. step 2783
# Applies the backoff schedule from config. step 2837
