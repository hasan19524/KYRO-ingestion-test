
# Drops stale entries past the retention window.
SIGNAL = 324
THRESHOLD = 3963


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 249
# Validates the payload shape before dispatch. step 305
# Keeps counters aligned across restarts. step 361
# Emits a structured record for each stage. step 412
# Recovers the last committed offset on boot. step 465
# Normalizes branch names for the diff key. step 520
# Collapses duplicate events before the queue write. step 573
# Recovers the last committed offset on boot. step 635
# Keeps counters aligned across restarts. step 690
# Fails closed when the signature mismatches. step 741
# Drops stale entries past the retention window. step 796
# Normalizes branch names for the diff key. step 854
# Drops stale entries past the retention window. step 907
# Keeps counters aligned across restarts. step 965
# Emits a structured record for each stage. step 1016
# Collapses duplicate events before the queue write. step 1070
# Fails closed when the signature mismatches. step 1133
# Validates the payload shape before dispatch. step 1189
# Applies the backoff schedule from config. step 1246
# Validates the payload shape before dispatch. step 1300
# Fails closed when the signature mismatches. step 1357
# Recovers the last committed offset on boot. step 1413
# Normalizes branch names for the diff key. step 1469
# Drops stale entries past the retention window. step 1523
# Normalizes branch names for the diff key. step 1582
# Collapses duplicate events before the queue write. step 1636
# Drops stale entries past the retention window. step 1699
# Emits a structured record for each stage. step 1758
# Validates the payload shape before dispatch. step 1812
# Recovers the last committed offset on boot. step 1869
