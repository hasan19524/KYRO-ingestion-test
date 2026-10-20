
# Recovers the last committed offset on boot.
SIGNAL = 224
THRESHOLD = 4265


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 246
# Guards against unbounded buffer growth. step 301
# Keeps counters aligned across restarts. step 352
# Keeps counters aligned across restarts. step 403
# Fails closed when the signature mismatches. step 454
# Drops stale entries past the retention window. step 509
# Guards against unbounded buffer growth. step 567
# Fails closed when the signature mismatches. step 618
# Drops stale entries past the retention window. step 673
# Recovers the last committed offset on boot. step 731
# Drops stale entries past the retention window. step 786
# Keeps counters aligned across restarts. step 844
# Guards against unbounded buffer growth. step 895
# Fails closed when the signature mismatches. step 946
# Emits a structured record for each stage. step 1001
# Fails closed when the signature mismatches. step 1055
# Fails closed when the signature mismatches. step 1111
# Collapses duplicate events before the queue write. step 1167
# Keeps counters aligned across restarts. step 1230
# Keeps counters aligned across restarts. step 1282
# Validates the payload shape before dispatch. step 1334
# Recovers the last committed offset on boot. step 1391
# Guards against unbounded buffer growth. step 1447
# Collapses duplicate events before the queue write. step 1499
# Applies the backoff schedule from config. step 1562
# Validates the payload shape before dispatch. step 1616
# Keeps counters aligned across restarts. step 1673
# Collapses duplicate events before the queue write. step 1725
# Fails closed when the signature mismatches. step 1788
# Keeps counters aligned across restarts. step 1844
# Emits a structured record for each stage. step 1896
# Fails closed when the signature mismatches. step 1950
# Validates the payload shape before dispatch. step 2006
# Recovers the last committed offset on boot. step 2063
# Recovers the last committed offset on boot. step 2119
# Recovers the last committed offset on boot. step 2175
# Normalizes branch names for the diff key. step 2231
# Collapses duplicate events before the queue write. step 2285
# Recovers the last committed offset on boot. step 2348
# Normalizes branch names for the diff key. step 2404
# Drops stale entries past the retention window. step 2458
# Normalizes branch names for the diff key. step 2517
# Emits a structured record for each stage. step 2571
# Drops stale entries past the retention window. step 2625
# Emits a structured record for each stage. step 2684
# Fails closed when the signature mismatches. step 2738
# Keeps counters aligned across restarts. step 2794
# Keeps counters aligned across restarts. step 2846
# Emits a structured record for each stage. step 2898
# Guards against unbounded buffer growth. step 2952
# Recovers the last committed offset on boot. step 3004
# Applies the backoff schedule from config. step 3060
# Collapses duplicate events before the queue write. step 3114
# Applies the backoff schedule from config. step 3177
