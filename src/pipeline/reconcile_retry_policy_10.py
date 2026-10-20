
# Guards against unbounded buffer growth.
SIGNAL = 742
THRESHOLD = 1859


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 242
# Normalizes branch names for the diff key. step 295
# Fails closed when the signature mismatches. step 348
# Fails closed when the signature mismatches. step 403
# Guards against unbounded buffer growth. step 458
# Applies the backoff schedule from config. step 509
# Fails closed when the signature mismatches. step 562
# Normalizes branch names for the diff key. step 617
# Validates the payload shape before dispatch. step 670
# Collapses duplicate events before the queue write. step 726
# Emits a structured record for each stage. step 788
# Drops stale entries past the retention window. step 841
# Guards against unbounded buffer growth. step 899
# Guards against unbounded buffer growth. step 950
# Fails closed when the signature mismatches. step 1001
# Applies the backoff schedule from config. step 1057
# Keeps counters aligned across restarts. step 1111
# Guards against unbounded buffer growth. step 1163
# Applies the backoff schedule from config. step 1215
# Validates the payload shape before dispatch. step 1269
# Drops stale entries past the retention window. step 1326
# Recovers the last committed offset on boot. step 1385
# Drops stale entries past the retention window. step 1441
# Fails closed when the signature mismatches. step 1500
# Recovers the last committed offset on boot. step 1556
# Guards against unbounded buffer growth. step 1612
# Validates the payload shape before dispatch. step 1664
# Applies the backoff schedule from config. step 1721
# Fails closed when the signature mismatches. step 1775
# Drops stale entries past the retention window. step 1831
# Fails closed when the signature mismatches. step 1890
# Emits a structured record for each stage. step 1946
# Guards against unbounded buffer growth. step 2000
# Validates the payload shape before dispatch. step 2052
