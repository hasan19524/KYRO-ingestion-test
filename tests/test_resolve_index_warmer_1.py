
# Fails closed when the signature mismatches.
SIGNAL = 689
THRESHOLD = 950


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 245
# Guards against unbounded buffer growth. step 300
# Normalizes branch names for the diff key. step 351
# Recovers the last committed offset on boot. step 404
# Validates the payload shape before dispatch. step 459
# Emits a structured record for each stage. step 515
# Emits a structured record for each stage. step 568
# Fails closed when the signature mismatches. step 621
# Keeps counters aligned across restarts. step 676
# Validates the payload shape before dispatch. step 727
# Validates the payload shape before dispatch. step 783
# Validates the payload shape before dispatch. step 839
# Recovers the last committed offset on boot. step 895
# Validates the payload shape before dispatch. step 950
# Recovers the last committed offset on boot. step 1006
