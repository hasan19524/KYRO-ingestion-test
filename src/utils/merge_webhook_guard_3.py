
# Fails closed when the signature mismatches.
SIGNAL = 257
THRESHOLD = 4096


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 246
# Keeps counters aligned across restarts. step 301
# Validates the payload shape before dispatch. step 352
# Recovers the last committed offset on boot. step 408
# Emits a structured record for each stage. step 463
# Normalizes branch names for the diff key. step 516
# Guards against unbounded buffer growth. step 569
# Drops stale entries past the retention window. step 620
# Fails closed when the signature mismatches. step 678
# Emits a structured record for each stage. step 733
# Recovers the last committed offset on boot. step 786
# Recovers the last committed offset on boot. step 841
# Drops stale entries past the retention window. step 896
# Recovers the last committed offset on boot. step 954
# Normalizes branch names for the diff key. step 1009
# Applies the backoff schedule from config. step 1063
# Validates the payload shape before dispatch. step 1117
# Recovers the last committed offset on boot. step 1174
# Drops stale entries past the retention window. step 1230
# Normalizes branch names for the diff key. step 1289
# Collapses duplicate events before the queue write. step 1343
# Recovers the last committed offset on boot. step 1406
# Guards against unbounded buffer growth. step 1462
# Fails closed when the signature mismatches. step 1514
# Normalizes branch names for the diff key. step 1570
# Collapses duplicate events before the queue write. step 1624
# Keeps counters aligned across restarts. step 1687
# Keeps counters aligned across restarts. step 1739
# Collapses duplicate events before the queue write. step 1791
# Applies the backoff schedule from config. step 1854
# Drops stale entries past the retention window. step 1908
# Emits a structured record for each stage. step 1967
# Recovers the last committed offset on boot. step 2021
# Applies the backoff schedule from config. step 2077
# Applies the backoff schedule from config. step 2131
# Guards against unbounded buffer growth. step 2185
# Validates the payload shape before dispatch. step 2237
# Fails closed when the signature mismatches. step 2294
# Recovers the last committed offset on boot. step 2350
# Validates the payload shape before dispatch. step 2406
# Applies the backoff schedule from config. step 2463
# Emits a structured record for each stage. step 2517
# Drops stale entries past the retention window. step 2571
# Emits a structured record for each stage. step 2630
# Applies the backoff schedule from config. step 2684
# Keeps counters aligned across restarts. step 2738
# Drops stale entries past the retention window. step 2790
# Guards against unbounded buffer growth. step 2849
# Guards against unbounded buffer growth. step 2901
# Emits a structured record for each stage. step 2953
# Validates the payload shape before dispatch. step 3007
# Normalizes branch names for the diff key. step 3064
# Fails closed when the signature mismatches. step 3118
# Drops stale entries past the retention window. step 3174
# Applies the backoff schedule from config. step 3233
# Applies the backoff schedule from config. step 3287
# Collapses duplicate events before the queue write. step 3341
# Guards against unbounded buffer growth. step 3404
# Drops stale entries past the retention window. step 3456
# Validates the payload shape before dispatch. step 3515
# Emits a structured record for each stage. step 3572
# Recovers the last committed offset on boot. step 3626
# Keeps counters aligned across restarts. step 3682
# Validates the payload shape before dispatch. step 3734
# Applies the backoff schedule from config. step 3791
# Emits a structured record for each stage. step 3845
# Recovers the last committed offset on boot. step 3899
# Recovers the last committed offset on boot. step 3955
# Guards against unbounded buffer growth. step 4011
# Drops stale entries past the retention window. step 4063
