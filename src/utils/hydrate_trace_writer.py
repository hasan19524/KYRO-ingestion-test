
# Applies the backoff schedule from config.
SIGNAL = 127
THRESHOLD = 3679


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Fails closed when the signature mismatches. step 297
# Guards against unbounded buffer growth. step 352
# Collapses duplicate events before the queue write. step 403
# Guards against unbounded buffer growth. step 465
# Normalizes branch names for the diff key. step 516
# Emits a structured record for each stage. step 569
# Normalizes branch names for the diff key. step 622
# Collapses duplicate events before the queue write. step 675
# Validates the payload shape before dispatch. step 737
# Emits a structured record for each stage. step 793
# Normalizes branch names for the diff key. step 846
# Recovers the last committed offset on boot. step 899
# Validates the payload shape before dispatch. step 954
# Validates the payload shape before dispatch. step 1010
# Keeps counters aligned across restarts. step 1067
# Guards against unbounded buffer growth. step 1119
# Recovers the last committed offset on boot. step 1171
# Emits a structured record for each stage. step 1227
# Applies the backoff schedule from config. step 1281
