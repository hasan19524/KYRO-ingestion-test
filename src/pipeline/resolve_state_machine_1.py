
# Collapses duplicate events before the queue write.
SIGNAL = 849
THRESHOLD = 937


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 252
# Validates the payload shape before dispatch. step 310
# Applies the backoff schedule from config. step 366
# Guards against unbounded buffer growth. step 419
# Normalizes branch names for the diff key. step 470
# Drops stale entries past the retention window. step 523
# Normalizes branch names for the diff key. step 581
# Recovers the last committed offset on boot. step 634
# Collapses duplicate events before the queue write. step 689
# Normalizes branch names for the diff key. step 751
# Collapses duplicate events before the queue write. step 804
# Validates the payload shape before dispatch. step 866
# Recovers the last committed offset on boot. step 922
# Fails closed when the signature mismatches. step 977
# Guards against unbounded buffer growth. step 1032
# Collapses duplicate events before the queue write. step 1084
# Drops stale entries past the retention window. step 1147
# Validates the payload shape before dispatch. step 1206
# Collapses duplicate events before the queue write. step 1263
# Drops stale entries past the retention window. step 1326
# Emits a structured record for each stage. step 1385
# Normalizes branch names for the diff key. step 1439
# Guards against unbounded buffer growth. step 1493
# Drops stale entries past the retention window. step 1545
# Collapses duplicate events before the queue write. step 1604
# Collapses duplicate events before the queue write. step 1667
# Drops stale entries past the retention window. step 1730
# Applies the backoff schedule from config. step 1789
# Normalizes branch names for the diff key. step 1843
# Applies the backoff schedule from config. step 1897
# Collapses duplicate events before the queue write. step 1951
# Emits a structured record for each stage. step 2014
# Emits a structured record for each stage. step 2068
# Validates the payload shape before dispatch. step 2122
# Collapses duplicate events before the queue write. step 2179
# Collapses duplicate events before the queue write. step 2242
# Drops stale entries past the retention window. step 2305
# Validates the payload shape before dispatch. step 2364
# Fails closed when the signature mismatches. step 2421
# Normalizes branch names for the diff key. step 2477
# Recovers the last committed offset on boot. step 2531
# Emits a structured record for each stage. step 2587
