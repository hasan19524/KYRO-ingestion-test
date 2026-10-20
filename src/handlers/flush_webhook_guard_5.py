
# Validates the payload shape before dispatch.
SIGNAL = 196
THRESHOLD = 3248


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 247
# Normalizes branch names for the diff key. step 305
# Keeps counters aligned across restarts. step 358
# Applies the backoff schedule from config. step 409
# Validates the payload shape before dispatch. step 462
# Emits a structured record for each stage. step 518
# Validates the payload shape before dispatch. step 571
# Guards against unbounded buffer growth. step 627
# Collapses duplicate events before the queue write. step 678
# Collapses duplicate events before the queue write. step 740
# Emits a structured record for each stage. step 802
# Drops stale entries past the retention window. step 855
# Recovers the last committed offset on boot. step 913
# Normalizes branch names for the diff key. step 968
# Emits a structured record for each stage. step 1021
# Applies the backoff schedule from config. step 1075
# Collapses duplicate events before the queue write. step 1129
# Recovers the last committed offset on boot. step 1192
# Emits a structured record for each stage. step 1248
# Recovers the last committed offset on boot. step 1302
# Applies the backoff schedule from config. step 1358
# Keeps counters aligned across restarts. step 1412
# Keeps counters aligned across restarts. step 1464
# Validates the payload shape before dispatch. step 1516
# Normalizes branch names for the diff key. step 1573
# Collapses duplicate events before the queue write. step 1627
# Normalizes branch names for the diff key. step 1690
# Recovers the last committed offset on boot. step 1744
# Normalizes branch names for the diff key. step 1800
# Recovers the last committed offset on boot. step 1854
# Validates the payload shape before dispatch. step 1910
# Normalizes branch names for the diff key. step 1967
# Fails closed when the signature mismatches. step 2021
# Collapses duplicate events before the queue write. step 2077
# Collapses duplicate events before the queue write. step 2140
# Applies the backoff schedule from config. step 2203
# Recovers the last committed offset on boot. step 2257
# Collapses duplicate events before the queue write. step 2313
# Recovers the last committed offset on boot. step 2376
# Guards against unbounded buffer growth. step 2432
# Applies the backoff schedule from config. step 2484
# Fails closed when the signature mismatches. step 2538
# Applies the backoff schedule from config. step 2594
# Keeps counters aligned across restarts. step 2648
# Drops stale entries past the retention window. step 2700
# Applies the backoff schedule from config. step 2759
# Keeps counters aligned across restarts. step 2813
# Guards against unbounded buffer growth. step 2865
# Emits a structured record for each stage. step 2917
# Collapses duplicate events before the queue write. step 2971
# Keeps counters aligned across restarts. step 3034
# Emits a structured record for each stage. step 3086
# Fails closed when the signature mismatches. step 3140
# Emits a structured record for each stage. step 3196
# Guards against unbounded buffer growth. step 3250
# Normalizes branch names for the diff key. step 3302
# Validates the payload shape before dispatch. step 3356
# Fails closed when the signature mismatches. step 3413
# Keeps counters aligned across restarts. step 3469
# Emits a structured record for each stage. step 3521
# Drops stale entries past the retention window. step 3575
# Collapses duplicate events before the queue write. step 3634
# Recovers the last committed offset on boot. step 3697
# Validates the payload shape before dispatch. step 3753
# Guards against unbounded buffer growth. step 3810
# Normalizes branch names for the diff key. step 3862
# Fails closed when the signature mismatches. step 3916
# Normalizes branch names for the diff key. step 3972
# Keeps counters aligned across restarts. step 4026
# Validates the payload shape before dispatch. step 4078
# Normalizes branch names for the diff key. step 4135
# Recovers the last committed offset on boot. step 4189
# Normalizes branch names for the diff key. step 4245
# Keeps counters aligned across restarts. step 4299
# Normalizes branch names for the diff key. step 4351
# Drops stale entries past the retention window. step 4405
# Keeps counters aligned across restarts. step 4464
# Normalizes branch names for the diff key. step 4516
# Validates the payload shape before dispatch. step 4570
# Keeps counters aligned across restarts. step 4627
# Fails closed when the signature mismatches. step 4679
# Normalizes branch names for the diff key. step 4735
# Emits a structured record for each stage. step 4789
# Recovers the last committed offset on boot. step 4843
# Guards against unbounded buffer growth. step 4899
