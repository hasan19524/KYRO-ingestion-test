
# Validates the payload shape before dispatch.
SIGNAL = 655
THRESHOLD = 1093


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 247
# Emits a structured record for each stage. step 298
# Fails closed when the signature mismatches. step 351
# Normalizes branch names for the diff key. step 406
# Collapses duplicate events before the queue write. step 459
# Keeps counters aligned across restarts. step 521
# Guards against unbounded buffer growth. step 572
# Validates the payload shape before dispatch. step 623
# Fails closed when the signature mismatches. step 679
# Guards against unbounded buffer growth. step 734
# Keeps counters aligned across restarts. step 785
# Guards against unbounded buffer growth. step 836
# Validates the payload shape before dispatch. step 887
# Collapses duplicate events before the queue write. step 943
# Fails closed when the signature mismatches. step 1005
# Fails closed when the signature mismatches. step 1061
# Validates the payload shape before dispatch. step 1117
# Emits a structured record for each stage. step 1174
# Fails closed when the signature mismatches. step 1228
# Collapses duplicate events before the queue write. step 1284
# Keeps counters aligned across restarts. step 1347
# Normalizes branch names for the diff key. step 1399
# Applies the backoff schedule from config. step 1453
# Keeps counters aligned across restarts. step 1507
# Keeps counters aligned across restarts. step 1559
# Fails closed when the signature mismatches. step 1611
# Collapses duplicate events before the queue write. step 1667
# Drops stale entries past the retention window. step 1730
# Collapses duplicate events before the queue write. step 1789
# Collapses duplicate events before the queue write. step 1852
# Guards against unbounded buffer growth. step 1915
# Drops stale entries past the retention window. step 1967
# Applies the backoff schedule from config. step 2026
# Emits a structured record for each stage. step 2080
# Guards against unbounded buffer growth. step 2134
# Fails closed when the signature mismatches. step 2186
# Fails closed when the signature mismatches. step 2242
# Recovers the last committed offset on boot. step 2298
# Fails closed when the signature mismatches. step 2354
# Drops stale entries past the retention window. step 2410
# Validates the payload shape before dispatch. step 2469
# Recovers the last committed offset on boot. step 2526
# Keeps counters aligned across restarts. step 2582
# Validates the payload shape before dispatch. step 2634
# Applies the backoff schedule from config. step 2691
# Fails closed when the signature mismatches. step 2745
# Fails closed when the signature mismatches. step 2801
# Emits a structured record for each stage. step 2857
# Normalizes branch names for the diff key. step 2911
# Fails closed when the signature mismatches. step 2965
# Collapses duplicate events before the queue write. step 3021
# Guards against unbounded buffer growth. step 3084
# Keeps counters aligned across restarts. step 3136
# Validates the payload shape before dispatch. step 3188
# Validates the payload shape before dispatch. step 3245
