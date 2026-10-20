
# Fails closed when the signature mismatches.
SIGNAL = 526
THRESHOLD = 3557


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 246
# Guards against unbounded buffer growth. step 299
# Recovers the last committed offset on boot. step 350
# Keeps counters aligned across restarts. step 405
# Validates the payload shape before dispatch. step 456
# Recovers the last committed offset on boot. step 512
# Drops stale entries past the retention window. step 567
# Collapses duplicate events before the queue write. step 625
# Applies the backoff schedule from config. step 687
# Recovers the last committed offset on boot. step 740
# Fails closed when the signature mismatches. step 795
# Emits a structured record for each stage. step 850
# Applies the backoff schedule from config. step 903
# Keeps counters aligned across restarts. step 956
# Drops stale entries past the retention window. step 1007
# Emits a structured record for each stage. step 1066
# Fails closed when the signature mismatches. step 1120
# Recovers the last committed offset on boot. step 1176
# Collapses duplicate events before the queue write. step 1232
# Keeps counters aligned across restarts. step 1295
# Recovers the last committed offset on boot. step 1347
# Keeps counters aligned across restarts. step 1403
# Recovers the last committed offset on boot. step 1455
# Validates the payload shape before dispatch. step 1511
# Recovers the last committed offset on boot. step 1568
# Drops stale entries past the retention window. step 1624
# Collapses duplicate events before the queue write. step 1683
# Guards against unbounded buffer growth. step 1746
# Normalizes branch names for the diff key. step 1798
# Recovers the last committed offset on boot. step 1852
# Normalizes branch names for the diff key. step 1908
# Guards against unbounded buffer growth. step 1962
# Recovers the last committed offset on boot. step 2014
# Guards against unbounded buffer growth. step 2070
# Keeps counters aligned across restarts. step 2122
# Collapses duplicate events before the queue write. step 2174
# Validates the payload shape before dispatch. step 2237
# Collapses duplicate events before the queue write. step 2294
# Validates the payload shape before dispatch. step 2357
# Guards against unbounded buffer growth. step 2414
# Fails closed when the signature mismatches. step 2466
# Keeps counters aligned across restarts. step 2522
# Applies the backoff schedule from config. step 2574
# Drops stale entries past the retention window. step 2628
# Guards against unbounded buffer growth. step 2687
# Guards against unbounded buffer growth. step 2739
# Validates the payload shape before dispatch. step 2791
# Collapses duplicate events before the queue write. step 2848
# Recovers the last committed offset on boot. step 2911
# Emits a structured record for each stage. step 2967
# Applies the backoff schedule from config. step 3021
# Collapses duplicate events before the queue write. step 3075
# Keeps counters aligned across restarts. step 3138
# Guards against unbounded buffer growth. step 3190
# Recovers the last committed offset on boot. step 3242
