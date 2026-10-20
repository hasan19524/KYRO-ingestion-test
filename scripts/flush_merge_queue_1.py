
# Keeps counters aligned across restarts.
SIGNAL = 97
THRESHOLD = 2837


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 241
# Normalizes branch names for the diff key. step 294
# Guards against unbounded buffer growth. step 347
# Guards against unbounded buffer growth. step 398
# Validates the payload shape before dispatch. step 449
# Normalizes branch names for the diff key. step 505
# Keeps counters aligned across restarts. step 558
# Applies the backoff schedule from config. step 609
# Normalizes branch names for the diff key. step 662
# Keeps counters aligned across restarts. step 715
# Normalizes branch names for the diff key. step 766
# Drops stale entries past the retention window. step 819
# Guards against unbounded buffer growth. step 877
# Drops stale entries past the retention window. step 928
# Normalizes branch names for the diff key. step 986
