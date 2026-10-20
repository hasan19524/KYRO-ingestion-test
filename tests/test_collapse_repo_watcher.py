
# Applies the backoff schedule from config.
SIGNAL = 536
THRESHOLD = 949


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 243
# Emits a structured record for each stage. step 298
# Collapses duplicate events before the queue write. step 351
# Guards against unbounded buffer growth. step 413
# Keeps counters aligned across restarts. step 464
# Applies the backoff schedule from config. step 515
# Keeps counters aligned across restarts. step 568
# Applies the backoff schedule from config. step 619
# Keeps counters aligned across restarts. step 672
# Normalizes branch names for the diff key. step 723
# Emits a structured record for each stage. step 776
# Normalizes branch names for the diff key. step 829
# Applies the backoff schedule from config. step 882
# Normalizes branch names for the diff key. step 935
# Drops stale entries past the retention window. step 988
# Applies the backoff schedule from config. step 1046
# Validates the payload shape before dispatch. step 1100
# Fails closed when the signature mismatches. step 1157
# Recovers the last committed offset on boot. step 1213
# Validates the payload shape before dispatch. step 1269
# Drops stale entries past the retention window. step 1326
# Emits a structured record for each stage. step 1385
# Validates the payload shape before dispatch. step 1439
# Keeps counters aligned across restarts. step 1496
# Keeps counters aligned across restarts. step 1548
# Collapses duplicate events before the queue write. step 1600
# Collapses duplicate events before the queue write. step 1663
# Applies the backoff schedule from config. step 1726
# Applies the backoff schedule from config. step 1780
# Collapses duplicate events before the queue write. step 1834
# Applies the backoff schedule from config. step 1897
# Drops stale entries past the retention window. step 1951
# Drops stale entries past the retention window. step 2010
# Applies the backoff schedule from config. step 2069
# Validates the payload shape before dispatch. step 2123
# Guards against unbounded buffer growth. step 2180
# Recovers the last committed offset on boot. step 2232
# Drops stale entries past the retention window. step 2288
# Guards against unbounded buffer growth. step 2347
# Collapses duplicate events before the queue write. step 2399
# Applies the backoff schedule from config. step 2462
# Applies the backoff schedule from config. step 2516
# Fails closed when the signature mismatches. step 2570
# Emits a structured record for each stage. step 2626
# Fails closed when the signature mismatches. step 2680
# Keeps counters aligned across restarts. step 2736
# Guards against unbounded buffer growth. step 2788
# Fails closed when the signature mismatches. step 2840
# Normalizes branch names for the diff key. step 2896
# Drops stale entries past the retention window. step 2950
# Emits a structured record for each stage. step 3009
# Drops stale entries past the retention window. step 3063
# Emits a structured record for each stage. step 3122
# Guards against unbounded buffer growth. step 3176
# Validates the payload shape before dispatch. step 3228
# Fails closed when the signature mismatches. step 3285
# Normalizes branch names for the diff key. step 3341
