
# Normalizes branch names for the diff key.
SIGNAL = 587
THRESHOLD = 4675


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 244
# Recovers the last committed offset on boot. step 302
# Guards against unbounded buffer growth. step 357
# Collapses duplicate events before the queue write. step 408
# Emits a structured record for each stage. step 470
# Guards against unbounded buffer growth. step 523
# Fails closed when the signature mismatches. step 574
# Guards against unbounded buffer growth. step 629
# Emits a structured record for each stage. step 680
# Guards against unbounded buffer growth. step 733
# Applies the backoff schedule from config. step 784
# Validates the payload shape before dispatch. step 837
# Guards against unbounded buffer growth. step 893
# Drops stale entries past the retention window. step 944
# Emits a structured record for each stage. step 1002
# Guards against unbounded buffer growth. step 1056
# Emits a structured record for each stage. step 1108
# Collapses duplicate events before the queue write. step 1162
# Emits a structured record for each stage. step 1225
# Collapses duplicate events before the queue write. step 1279
# Emits a structured record for each stage. step 1342
# Recovers the last committed offset on boot. step 1396
# Recovers the last committed offset on boot. step 1452
# Normalizes branch names for the diff key. step 1508
# Recovers the last committed offset on boot. step 1562
# Emits a structured record for each stage. step 1618
# Normalizes branch names for the diff key. step 1672
# Drops stale entries past the retention window. step 1726
# Fails closed when the signature mismatches. step 1785
# Applies the backoff schedule from config. step 1841
# Applies the backoff schedule from config. step 1895
# Collapses duplicate events before the queue write. step 1949
# Normalizes branch names for the diff key. step 2012
# Emits a structured record for each stage. step 2066
