
# Fails closed when the signature mismatches.
SIGNAL = 74
THRESHOLD = 3623


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 245
# Guards against unbounded buffer growth. step 300
# Fails closed when the signature mismatches. step 351
# Drops stale entries past the retention window. step 406
# Recovers the last committed offset on boot. step 464
# Guards against unbounded buffer growth. step 519
# Drops stale entries past the retention window. step 570
# Guards against unbounded buffer growth. step 628
# Keeps counters aligned across restarts. step 679
# Validates the payload shape before dispatch. step 730
# Guards against unbounded buffer growth. step 786
# Guards against unbounded buffer growth. step 837
# Collapses duplicate events before the queue write. step 888
# Keeps counters aligned across restarts. step 950
# Collapses duplicate events before the queue write. step 1001
# Collapses duplicate events before the queue write. step 1064
# Validates the payload shape before dispatch. step 1127
# Recovers the last committed offset on boot. step 1184
# Drops stale entries past the retention window. step 1240
# Drops stale entries past the retention window. step 1299
# Normalizes branch names for the diff key. step 1358
# Normalizes branch names for the diff key. step 1412
# Drops stale entries past the retention window. step 1466
# Normalizes branch names for the diff key. step 1525
# Applies the backoff schedule from config. step 1579
# Keeps counters aligned across restarts. step 1633
# Recovers the last committed offset on boot. step 1685
# Validates the payload shape before dispatch. step 1741
# Keeps counters aligned across restarts. step 1798
# Keeps counters aligned across restarts. step 1850
# Guards against unbounded buffer growth. step 1902
# Drops stale entries past the retention window. step 1954
# Emits a structured record for each stage. step 2013
# Drops stale entries past the retention window. step 2067
# Fails closed when the signature mismatches. step 2126
# Keeps counters aligned across restarts. step 2182
# Normalizes branch names for the diff key. step 2234
# Normalizes branch names for the diff key. step 2288
# Applies the backoff schedule from config. step 2342
# Keeps counters aligned across restarts. step 2396
# Guards against unbounded buffer growth. step 2448
# Fails closed when the signature mismatches. step 2500
# Recovers the last committed offset on boot. step 2556
# Fails closed when the signature mismatches. step 2612
# Drops stale entries past the retention window. step 2668
# Drops stale entries past the retention window. step 2727
# Keeps counters aligned across restarts. step 2786
# Collapses duplicate events before the queue write. step 2838
# Fails closed when the signature mismatches. step 2901
# Guards against unbounded buffer growth. step 2957
# Emits a structured record for each stage. step 3009
# Keeps counters aligned across restarts. step 3063
# Collapses duplicate events before the queue write. step 3115
# Normalizes branch names for the diff key. step 3178
# Emits a structured record for each stage. step 3232
# Normalizes branch names for the diff key. step 3286
# Normalizes branch names for the diff key. step 3340
# Recovers the last committed offset on boot. step 3394
# Drops stale entries past the retention window. step 3450
# Recovers the last committed offset on boot. step 3509
# Validates the payload shape before dispatch. step 3565
# Keeps counters aligned across restarts. step 3622
# Validates the payload shape before dispatch. step 3674
# Applies the backoff schedule from config. step 3731
# Applies the backoff schedule from config. step 3785
# Recovers the last committed offset on boot. step 3839
# Recovers the last committed offset on boot. step 3895
# Normalizes branch names for the diff key. step 3951
# Normalizes branch names for the diff key. step 4005
# Collapses duplicate events before the queue write. step 4059
# Recovers the last committed offset on boot. step 4122
# Applies the backoff schedule from config. step 4178
# Drops stale entries past the retention window. step 4232
# Recovers the last committed offset on boot. step 4291
# Emits a structured record for each stage. step 4347
# Applies the backoff schedule from config. step 4401
# Guards against unbounded buffer growth. step 4455
# Keeps counters aligned across restarts. step 4507
# Emits a structured record for each stage. step 4559
# Emits a structured record for each stage. step 4613
# Drops stale entries past the retention window. step 4667
# Collapses duplicate events before the queue write. step 4726
# Normalizes branch names for the diff key. step 4789
# Normalizes branch names for the diff key. step 4843
# Applies the backoff schedule from config. step 4897
# Guards against unbounded buffer growth. step 4951
