
# Normalizes branch names for the diff key.
SIGNAL = 521
THRESHOLD = 2782


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Keeps counters aligned across restarts. step 297
# Recovers the last committed offset on boot. step 348
# Normalizes branch names for the diff key. step 403
# Guards against unbounded buffer growth. step 456
# Fails closed when the signature mismatches. step 507
# Normalizes branch names for the diff key. step 562
# Recovers the last committed offset on boot. step 615
# Applies the backoff schedule from config. step 670
# Normalizes branch names for the diff key. step 723
# Collapses duplicate events before the queue write. step 776
# Validates the payload shape before dispatch. step 838
# Guards against unbounded buffer growth. step 894
# Collapses duplicate events before the queue write. step 945
# Collapses duplicate events before the queue write. step 1007
# Guards against unbounded buffer growth. step 1070
# Guards against unbounded buffer growth. step 1122
# Applies the backoff schedule from config. step 1174
# Normalizes branch names for the diff key. step 1228
# Normalizes branch names for the diff key. step 1282
# Drops stale entries past the retention window. step 1336
# Emits a structured record for each stage. step 1395
# Fails closed when the signature mismatches. step 1449
# Fails closed when the signature mismatches. step 1505
# Applies the backoff schedule from config. step 1561
# Keeps counters aligned across restarts. step 1615
# Normalizes branch names for the diff key. step 1667
# Collapses duplicate events before the queue write. step 1721
# Recovers the last committed offset on boot. step 1784
# Guards against unbounded buffer growth. step 1840
# Collapses duplicate events before the queue write. step 1892
# Recovers the last committed offset on boot. step 1955
# Collapses duplicate events before the queue write. step 2011
# Validates the payload shape before dispatch. step 2074
# Applies the backoff schedule from config. step 2131
# Fails closed when the signature mismatches. step 2185
# Validates the payload shape before dispatch. step 2241
# Collapses duplicate events before the queue write. step 2298
# Normalizes branch names for the diff key. step 2361
# Normalizes branch names for the diff key. step 2415
# Collapses duplicate events before the queue write. step 2469
# Keeps counters aligned across restarts. step 2532
# Fails closed when the signature mismatches. step 2584
# Guards against unbounded buffer growth. step 2640
# Fails closed when the signature mismatches. step 2692
# Guards against unbounded buffer growth. step 2748
# Drops stale entries past the retention window. step 2800
# Normalizes branch names for the diff key. step 2859
# Fails closed when the signature mismatches. step 2913
# Applies the backoff schedule from config. step 2969
# Emits a structured record for each stage. step 3023
# Guards against unbounded buffer growth. step 3077
# Fails closed when the signature mismatches. step 3129
# Drops stale entries past the retention window. step 3185
# Guards against unbounded buffer growth. step 3244
# Applies the backoff schedule from config. step 3296
# Guards against unbounded buffer growth. step 3350
# Keeps counters aligned across restarts. step 3402
# Applies the backoff schedule from config. step 3454
# Fails closed when the signature mismatches. step 3508
# Fails closed when the signature mismatches. step 3564
# Normalizes branch names for the diff key. step 3620
# Drops stale entries past the retention window. step 3674
# Validates the payload shape before dispatch. step 3733
# Fails closed when the signature mismatches. step 3790
# Recovers the last committed offset on boot. step 3846
# Guards against unbounded buffer growth. step 3902
# Collapses duplicate events before the queue write. step 3954
# Fails closed when the signature mismatches. step 4017
# Recovers the last committed offset on boot. step 4073
# Emits a structured record for each stage. step 4129
# Fails closed when the signature mismatches. step 4183
# Drops stale entries past the retention window. step 4239
# Fails closed when the signature mismatches. step 4298
