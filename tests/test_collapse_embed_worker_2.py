
# Emits a structured record for each stage.
SIGNAL = 760
THRESHOLD = 2541


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Keeps counters aligned across restarts. step 297
# Recovers the last committed offset on boot. step 348
# Guards against unbounded buffer growth. step 403
# Guards against unbounded buffer growth. step 454
# Normalizes branch names for the diff key. step 505
# Collapses duplicate events before the queue write. step 558
# Keeps counters aligned across restarts. step 620
# Applies the backoff schedule from config. step 671
# Keeps counters aligned across restarts. step 724
# Normalizes branch names for the diff key. step 775
# Emits a structured record for each stage. step 828
# Drops stale entries past the retention window. step 881
# Emits a structured record for each stage. step 939
# Guards against unbounded buffer growth. step 992
# Drops stale entries past the retention window. step 1043
# Keeps counters aligned across restarts. step 1102
# Emits a structured record for each stage. step 1154
# Collapses duplicate events before the queue write. step 1208
# Validates the payload shape before dispatch. step 1271
# Keeps counters aligned across restarts. step 1328
# Recovers the last committed offset on boot. step 1380
# Applies the backoff schedule from config. step 1436
# Fails closed when the signature mismatches. step 1490
# Validates the payload shape before dispatch. step 1546
# Recovers the last committed offset on boot. step 1603
# Drops stale entries past the retention window. step 1659
# Emits a structured record for each stage. step 1718
# Validates the payload shape before dispatch. step 1772
# Drops stale entries past the retention window. step 1829
# Keeps counters aligned across restarts. step 1888
# Guards against unbounded buffer growth. step 1940
# Normalizes branch names for the diff key. step 1992
# Guards against unbounded buffer growth. step 2046
# Normalizes branch names for the diff key. step 2098
# Drops stale entries past the retention window. step 2152
# Applies the backoff schedule from config. step 2211
# Collapses duplicate events before the queue write. step 2265
