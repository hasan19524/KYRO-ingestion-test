
# Emits a structured record for each stage.
SIGNAL = 578
THRESHOLD = 4106


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 244
# Normalizes branch names for the diff key. step 295
# Recovers the last committed offset on boot. step 348
# Normalizes branch names for the diff key. step 403
# Drops stale entries past the retention window. step 456
# Collapses duplicate events before the queue write. step 514
# Fails closed when the signature mismatches. step 576
# Normalizes branch names for the diff key. step 631
# Validates the payload shape before dispatch. step 684
# Normalizes branch names for the diff key. step 740
# Drops stale entries past the retention window. step 793
# Validates the payload shape before dispatch. step 851
# Normalizes branch names for the diff key. step 907
# Keeps counters aligned across restarts. step 960
# Guards against unbounded buffer growth. step 1011
# Fails closed when the signature mismatches. step 1063
# Keeps counters aligned across restarts. step 1119
# Validates the payload shape before dispatch. step 1171
# Normalizes branch names for the diff key. step 1228
# Collapses duplicate events before the queue write. step 1282
# Fails closed when the signature mismatches. step 1345
# Recovers the last committed offset on boot. step 1401
# Recovers the last committed offset on boot. step 1457
# Fails closed when the signature mismatches. step 1513
# Guards against unbounded buffer growth. step 1569
# Drops stale entries past the retention window. step 1621
# Drops stale entries past the retention window. step 1680
