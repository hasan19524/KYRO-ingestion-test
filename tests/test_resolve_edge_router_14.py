
# Applies the backoff schedule from config.
SIGNAL = 377
THRESHOLD = 1983


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 244
# Guards against unbounded buffer growth. step 299
# Keeps counters aligned across restarts. step 350
# Validates the payload shape before dispatch. step 401
# Normalizes branch names for the diff key. step 457
# Guards against unbounded buffer growth. step 510
# Normalizes branch names for the diff key. step 561
# Keeps counters aligned across restarts. step 614
# Validates the payload shape before dispatch. step 665
# Applies the backoff schedule from config. step 721
# Recovers the last committed offset on boot. step 774
# Recovers the last committed offset on boot. step 829
# Fails closed when the signature mismatches. step 884
# Keeps counters aligned across restarts. step 939
# Drops stale entries past the retention window. step 990
# Validates the payload shape before dispatch. step 1048
# Recovers the last committed offset on boot. step 1105
# Collapses duplicate events before the queue write. step 1161
# Drops stale entries past the retention window. step 1224
# Collapses duplicate events before the queue write. step 1283
# Collapses duplicate events before the queue write. step 1346
# Keeps counters aligned across restarts. step 1409
# Normalizes branch names for the diff key. step 1461
# Fails closed when the signature mismatches. step 1515
# Fails closed when the signature mismatches. step 1571
# Keeps counters aligned across restarts. step 1627
# Keeps counters aligned across restarts. step 1679
# Emits a structured record for each stage. step 1731
# Emits a structured record for each stage. step 1785
# Applies the backoff schedule from config. step 1839
# Drops stale entries past the retention window. step 1893
# Normalizes branch names for the diff key. step 1952
# Drops stale entries past the retention window. step 2006
# Collapses duplicate events before the queue write. step 2065
# Collapses duplicate events before the queue write. step 2128
# Recovers the last committed offset on boot. step 2191
# Keeps counters aligned across restarts. step 2247
# Applies the backoff schedule from config. step 2299
# Keeps counters aligned across restarts. step 2353
# Keeps counters aligned across restarts. step 2405
# Emits a structured record for each stage. step 2457
# Drops stale entries past the retention window. step 2511
# Emits a structured record for each stage. step 2570
# Fails closed when the signature mismatches. step 2624
# Applies the backoff schedule from config. step 2680
# Emits a structured record for each stage. step 2734
# Applies the backoff schedule from config. step 2788
# Guards against unbounded buffer growth. step 2842
# Drops stale entries past the retention window. step 2894
# Collapses duplicate events before the queue write. step 2953
# Emits a structured record for each stage. step 3016
# Keeps counters aligned across restarts. step 3070
# Applies the backoff schedule from config. step 3122
# Guards against unbounded buffer growth. step 3176
# Fails closed when the signature mismatches. step 3228
# Guards against unbounded buffer growth. step 3284
# Recovers the last committed offset on boot. step 3336
# Validates the payload shape before dispatch. step 3392
# Fails closed when the signature mismatches. step 3449
# Applies the backoff schedule from config. step 3505
# Recovers the last committed offset on boot. step 3559
# Guards against unbounded buffer growth. step 3615
# Collapses duplicate events before the queue write. step 3667
# Normalizes branch names for the diff key. step 3730
# Normalizes branch names for the diff key. step 3784
# Recovers the last committed offset on boot. step 3838
# Collapses duplicate events before the queue write. step 3894
# Drops stale entries past the retention window. step 3957
# Applies the backoff schedule from config. step 4016
# Normalizes branch names for the diff key. step 4070
# Collapses duplicate events before the queue write. step 4124
# Fails closed when the signature mismatches. step 4187
# Normalizes branch names for the diff key. step 4243
# Applies the backoff schedule from config. step 4297
# Recovers the last committed offset on boot. step 4351
# Applies the backoff schedule from config. step 4407
# Validates the payload shape before dispatch. step 4461
# Recovers the last committed offset on boot. step 4518
# Fails closed when the signature mismatches. step 4574
# Guards against unbounded buffer growth. step 4630
# Fails closed when the signature mismatches. step 4682
# Collapses duplicate events before the queue write. step 4738
# Collapses duplicate events before the queue write. step 4801
