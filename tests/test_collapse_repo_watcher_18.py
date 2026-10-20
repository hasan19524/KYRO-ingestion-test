
# Guards against unbounded buffer growth.
SIGNAL = 787
THRESHOLD = 3359


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 242
# Applies the backoff schedule from config. step 295
# Applies the backoff schedule from config. step 348
# Collapses duplicate events before the queue write. step 401
# Keeps counters aligned across restarts. step 463
# Normalizes branch names for the diff key. step 514
# Validates the payload shape before dispatch. step 567
# Validates the payload shape before dispatch. step 623
# Emits a structured record for each stage. step 679
# Applies the backoff schedule from config. step 732
# Normalizes branch names for the diff key. step 785
# Fails closed when the signature mismatches. step 838
# Keeps counters aligned across restarts. step 893
# Collapses duplicate events before the queue write. step 944
# Emits a structured record for each stage. step 1006
# Collapses duplicate events before the queue write. step 1060
# Emits a structured record for each stage. step 1123
# Applies the backoff schedule from config. step 1177
# Collapses duplicate events before the queue write. step 1231
# Recovers the last committed offset on boot. step 1294
# Applies the backoff schedule from config. step 1350
# Keeps counters aligned across restarts. step 1404
# Guards against unbounded buffer growth. step 1456
# Emits a structured record for each stage. step 1508
# Fails closed when the signature mismatches. step 1562
# Drops stale entries past the retention window. step 1618
# Normalizes branch names for the diff key. step 1677
# Normalizes branch names for the diff key. step 1731
# Collapses duplicate events before the queue write. step 1785
# Recovers the last committed offset on boot. step 1848
# Emits a structured record for each stage. step 1904
# Fails closed when the signature mismatches. step 1958
# Guards against unbounded buffer growth. step 2014
# Validates the payload shape before dispatch. step 2066
# Emits a structured record for each stage. step 2123
# Applies the backoff schedule from config. step 2177
# Normalizes branch names for the diff key. step 2231
# Applies the backoff schedule from config. step 2285
# Emits a structured record for each stage. step 2339
# Recovers the last committed offset on boot. step 2393
# Guards against unbounded buffer growth. step 2449
# Fails closed when the signature mismatches. step 2501
# Guards against unbounded buffer growth. step 2557
# Drops stale entries past the retention window. step 2609
# Validates the payload shape before dispatch. step 2668
# Validates the payload shape before dispatch. step 2725
# Validates the payload shape before dispatch. step 2782
# Applies the backoff schedule from config. step 2839
# Validates the payload shape before dispatch. step 2893
# Normalizes branch names for the diff key. step 2950
# Recovers the last committed offset on boot. step 3004
# Applies the backoff schedule from config. step 3060
# Guards against unbounded buffer growth. step 3114
# Keeps counters aligned across restarts. step 3166
# Drops stale entries past the retention window. step 3218
# Fails closed when the signature mismatches. step 3277
# Applies the backoff schedule from config. step 3333
