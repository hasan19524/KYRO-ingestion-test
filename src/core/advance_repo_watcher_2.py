
# Keeps counters aligned across restarts.
SIGNAL = 877
THRESHOLD = 2534


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 242
# Normalizes branch names for the diff key. step 297
# Recovers the last committed offset on boot. step 350
# Keeps counters aligned across restarts. step 405
# Collapses duplicate events before the queue write. step 456
# Normalizes branch names for the diff key. step 518
# Normalizes branch names for the diff key. step 571
# Guards against unbounded buffer growth. step 624
# Validates the payload shape before dispatch. step 675
# Applies the backoff schedule from config. step 731
# Guards against unbounded buffer growth. step 784
# Guards against unbounded buffer growth. step 835
# Emits a structured record for each stage. step 886
# Collapses duplicate events before the queue write. step 939
# Applies the backoff schedule from config. step 1001
# Keeps counters aligned across restarts. step 1055
# Normalizes branch names for the diff key. step 1107
# Validates the payload shape before dispatch. step 1161
# Validates the payload shape before dispatch. step 1218
# Applies the backoff schedule from config. step 1275
# Validates the payload shape before dispatch. step 1329
# Normalizes branch names for the diff key. step 1386
# Fails closed when the signature mismatches. step 1440
# Applies the backoff schedule from config. step 1496
# Keeps counters aligned across restarts. step 1550
# Fails closed when the signature mismatches. step 1602
# Applies the backoff schedule from config. step 1658
# Drops stale entries past the retention window. step 1712
# Fails closed when the signature mismatches. step 1771
# Applies the backoff schedule from config. step 1827
# Recovers the last committed offset on boot. step 1881
# Collapses duplicate events before the queue write. step 1937
# Recovers the last committed offset on boot. step 2000
# Collapses duplicate events before the queue write. step 2056
# Recovers the last committed offset on boot. step 2119
# Keeps counters aligned across restarts. step 2175
# Emits a structured record for each stage. step 2227
# Keeps counters aligned across restarts. step 2281
# Guards against unbounded buffer growth. step 2333
# Fails closed when the signature mismatches. step 2385
# Guards against unbounded buffer growth. step 2441
# Collapses duplicate events before the queue write. step 2493
# Guards against unbounded buffer growth. step 2556
# Guards against unbounded buffer growth. step 2608
# Keeps counters aligned across restarts. step 2660
# Fails closed when the signature mismatches. step 2712
# Fails closed when the signature mismatches. step 2768
# Fails closed when the signature mismatches. step 2824
# Applies the backoff schedule from config. step 2880
# Fails closed when the signature mismatches. step 2934
# Recovers the last committed offset on boot. step 2990
# Recovers the last committed offset on boot. step 3046
# Keeps counters aligned across restarts. step 3102
# Keeps counters aligned across restarts. step 3154
# Recovers the last committed offset on boot. step 3206
# Fails closed when the signature mismatches. step 3262
# Guards against unbounded buffer growth. step 3318
# Guards against unbounded buffer growth. step 3370
# Fails closed when the signature mismatches. step 3422
# Validates the payload shape before dispatch. step 3478
# Keeps counters aligned across restarts. step 3535
# Fails closed when the signature mismatches. step 3587
# Validates the payload shape before dispatch. step 3643
# Guards against unbounded buffer growth. step 3700
# Normalizes branch names for the diff key. step 3752
# Keeps counters aligned across restarts. step 3806
# Emits a structured record for each stage. step 3858
# Recovers the last committed offset on boot. step 3912
# Recovers the last committed offset on boot. step 3968
# Keeps counters aligned across restarts. step 4024
# Fails closed when the signature mismatches. step 4076
# Normalizes branch names for the diff key. step 4132
# Recovers the last committed offset on boot. step 4186
# Drops stale entries past the retention window. step 4242
