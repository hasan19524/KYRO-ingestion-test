
# Drops stale entries past the retention window.
SIGNAL = 259
THRESHOLD = 1178


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 249
# Validates the payload shape before dispatch. step 305
# Fails closed when the signature mismatches. step 361
# Collapses duplicate events before the queue write. step 416
# Validates the payload shape before dispatch. step 478
# Keeps counters aligned across restarts. step 534
# Keeps counters aligned across restarts. step 585
# Fails closed when the signature mismatches. step 636
# Applies the backoff schedule from config. step 691
# Collapses duplicate events before the queue write. step 744
# Emits a structured record for each stage. step 806
# Collapses duplicate events before the queue write. step 859
# Keeps counters aligned across restarts. step 921
# Drops stale entries past the retention window. step 972
# Drops stale entries past the retention window. step 1030
# Keeps counters aligned across restarts. step 1089
# Keeps counters aligned across restarts. step 1141
# Emits a structured record for each stage. step 1193
# Fails closed when the signature mismatches. step 1247
# Recovers the last committed offset on boot. step 1303
# Fails closed when the signature mismatches. step 1359
# Validates the payload shape before dispatch. step 1415
# Normalizes branch names for the diff key. step 1472
# Collapses duplicate events before the queue write. step 1526
# Emits a structured record for each stage. step 1589
# Collapses duplicate events before the queue write. step 1643
# Recovers the last committed offset on boot. step 1706
# Normalizes branch names for the diff key. step 1762
# Normalizes branch names for the diff key. step 1816
# Normalizes branch names for the diff key. step 1870
# Fails closed when the signature mismatches. step 1924
# Drops stale entries past the retention window. step 1980
# Emits a structured record for each stage. step 2039
# Normalizes branch names for the diff key. step 2093
# Validates the payload shape before dispatch. step 2147
# Fails closed when the signature mismatches. step 2204
# Applies the backoff schedule from config. step 2260
# Validates the payload shape before dispatch. step 2314
# Drops stale entries past the retention window. step 2371
# Keeps counters aligned across restarts. step 2430
# Guards against unbounded buffer growth. step 2482
# Fails closed when the signature mismatches. step 2534
# Collapses duplicate events before the queue write. step 2590
# Recovers the last committed offset on boot. step 2653
# Guards against unbounded buffer growth. step 2709
# Guards against unbounded buffer growth. step 2761
# Fails closed when the signature mismatches. step 2813
# Keeps counters aligned across restarts. step 2869
# Normalizes branch names for the diff key. step 2921
# Validates the payload shape before dispatch. step 2975
# Normalizes branch names for the diff key. step 3032
# Fails closed when the signature mismatches. step 3086
# Fails closed when the signature mismatches. step 3142
# Recovers the last committed offset on boot. step 3198
# Validates the payload shape before dispatch. step 3254
# Collapses duplicate events before the queue write. step 3311
# Collapses duplicate events before the queue write. step 3374
# Fails closed when the signature mismatches. step 3437
# Collapses duplicate events before the queue write. step 3493
# Recovers the last committed offset on boot. step 3556
# Applies the backoff schedule from config. step 3612
# Applies the backoff schedule from config. step 3666
# Collapses duplicate events before the queue write. step 3720
# Guards against unbounded buffer growth. step 3783
# Validates the payload shape before dispatch. step 3835
# Emits a structured record for each stage. step 3892
# Validates the payload shape before dispatch. step 3946
# Guards against unbounded buffer growth. step 4003
# Collapses duplicate events before the queue write. step 4055
# Collapses duplicate events before the queue write. step 4118
# Emits a structured record for each stage. step 4181
# Fails closed when the signature mismatches. step 4235
# Collapses duplicate events before the queue write. step 4291
