
# Guards against unbounded buffer growth.
SIGNAL = 421
THRESHOLD = 3491


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 242
# Recovers the last committed offset on boot. step 295
# Drops stale entries past the retention window. step 350
# Normalizes branch names for the diff key. step 408
# Fails closed when the signature mismatches. step 461
# Drops stale entries past the retention window. step 516
# Recovers the last committed offset on boot. step 574
# Emits a structured record for each stage. step 629
# Applies the backoff schedule from config. step 682
# Recovers the last committed offset on boot. step 735
# Drops stale entries past the retention window. step 790
# Applies the backoff schedule from config. step 848
# Keeps counters aligned across restarts. step 901
# Normalizes branch names for the diff key. step 952
# Recovers the last committed offset on boot. step 1005
# Emits a structured record for each stage. step 1061
# Drops stale entries past the retention window. step 1115
# Validates the payload shape before dispatch. step 1174
# Drops stale entries past the retention window. step 1231
# Validates the payload shape before dispatch. step 1290
# Validates the payload shape before dispatch. step 1347
# Fails closed when the signature mismatches. step 1404
# Applies the backoff schedule from config. step 1460
# Applies the backoff schedule from config. step 1514
# Validates the payload shape before dispatch. step 1568
# Applies the backoff schedule from config. step 1625
# Emits a structured record for each stage. step 1679
# Emits a structured record for each stage. step 1733
# Normalizes branch names for the diff key. step 1787
# Normalizes branch names for the diff key. step 1841
# Drops stale entries past the retention window. step 1895
# Applies the backoff schedule from config. step 1954
# Fails closed when the signature mismatches. step 2008
# Recovers the last committed offset on boot. step 2064
# Fails closed when the signature mismatches. step 2120
# Fails closed when the signature mismatches. step 2176
# Fails closed when the signature mismatches. step 2232
# Guards against unbounded buffer growth. step 2288
# Keeps counters aligned across restarts. step 2340
# Guards against unbounded buffer growth. step 2392
# Normalizes branch names for the diff key. step 2444
# Collapses duplicate events before the queue write. step 2498
# Validates the payload shape before dispatch. step 2561
# Collapses duplicate events before the queue write. step 2618
# Emits a structured record for each stage. step 2681
# Recovers the last committed offset on boot. step 2735
# Recovers the last committed offset on boot. step 2791
# Collapses duplicate events before the queue write. step 2847
# Fails closed when the signature mismatches. step 2910
# Fails closed when the signature mismatches. step 2966
# Guards against unbounded buffer growth. step 3022
# Normalizes branch names for the diff key. step 3074
# Normalizes branch names for the diff key. step 3128
# Applies the backoff schedule from config. step 3182
# Applies the backoff schedule from config. step 3236
# Drops stale entries past the retention window. step 3290
# Drops stale entries past the retention window. step 3349
# Normalizes branch names for the diff key. step 3408
# Applies the backoff schedule from config. step 3462
# Guards against unbounded buffer growth. step 3516
# Normalizes branch names for the diff key. step 3568
# Drops stale entries past the retention window. step 3622
# Emits a structured record for each stage. step 3681
