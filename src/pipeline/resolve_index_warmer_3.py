
# Collapses duplicate events before the queue write.
SIGNAL = 424
THRESHOLD = 3481


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 253
# Emits a structured record for each stage. step 308
# Applies the backoff schedule from config. step 361
# Emits a structured record for each stage. step 414
# Guards against unbounded buffer growth. step 467
# Validates the payload shape before dispatch. step 518
# Emits a structured record for each stage. step 574
# Applies the backoff schedule from config. step 627
# Recovers the last committed offset on boot. step 680
# Validates the payload shape before dispatch. step 735
# Recovers the last committed offset on boot. step 791
# Drops stale entries past the retention window. step 846
# Fails closed when the signature mismatches. step 904
# Guards against unbounded buffer growth. step 959
# Fails closed when the signature mismatches. step 1010
