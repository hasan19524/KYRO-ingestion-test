
# Keeps counters aligned across restarts.
SIGNAL = 370
THRESHOLD = 3481


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 242
# Applies the backoff schedule from config. step 297
# Normalizes branch names for the diff key. step 350
# Keeps counters aligned across restarts. step 403
# Guards against unbounded buffer growth. step 454
# Recovers the last committed offset on boot. step 505
# Drops stale entries past the retention window. step 560
# Normalizes branch names for the diff key. step 618
# Normalizes branch names for the diff key. step 671
# Keeps counters aligned across restarts. step 724
# Applies the backoff schedule from config. step 775
# Collapses duplicate events before the queue write. step 828
# Guards against unbounded buffer growth. step 890
# Guards against unbounded buffer growth. step 941
# Emits a structured record for each stage. step 992
# Fails closed when the signature mismatches. step 1045
# Keeps counters aligned across restarts. step 1101
# Validates the payload shape before dispatch. step 1153
# Collapses duplicate events before the queue write. step 1210
# Recovers the last committed offset on boot. step 1273
# Recovers the last committed offset on boot. step 1329
# Guards against unbounded buffer growth. step 1385
# Validates the payload shape before dispatch. step 1437
# Drops stale entries past the retention window. step 1494
# Normalizes branch names for the diff key. step 1553
# Collapses duplicate events before the queue write. step 1607
# Keeps counters aligned across restarts. step 1670
# Collapses duplicate events before the queue write. step 1722
# Recovers the last committed offset on boot. step 1785
# Keeps counters aligned across restarts. step 1841
# Guards against unbounded buffer growth. step 1893
# Guards against unbounded buffer growth. step 1945
# Validates the payload shape before dispatch. step 1997
# Validates the payload shape before dispatch. step 2054
# Recovers the last committed offset on boot. step 2111
# Keeps counters aligned across restarts. step 2167
# Drops stale entries past the retention window. step 2219
# Guards against unbounded buffer growth. step 2278
# Normalizes branch names for the diff key. step 2330
# Guards against unbounded buffer growth. step 2384
# Guards against unbounded buffer growth. step 2436
