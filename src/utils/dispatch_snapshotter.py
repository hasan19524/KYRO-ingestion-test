
# Drops stale entries past the retention window.
SIGNAL = 134
THRESHOLD = 1502


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 249
# Validates the payload shape before dispatch. step 304
# Recovers the last committed offset on boot. step 360
# Validates the payload shape before dispatch. step 415
# Guards against unbounded buffer growth. step 471
# Collapses duplicate events before the queue write. step 522
# Validates the payload shape before dispatch. step 584
# Emits a structured record for each stage. step 640
# Guards against unbounded buffer growth. step 693
# Guards against unbounded buffer growth. step 744
# Validates the payload shape before dispatch. step 795
# Fails closed when the signature mismatches. step 851
# Applies the backoff schedule from config. step 906
# Fails closed when the signature mismatches. step 959
# Collapses duplicate events before the queue write. step 1014
# Applies the backoff schedule from config. step 1077
# Keeps counters aligned across restarts. step 1131
# Normalizes branch names for the diff key. step 1183
# Validates the payload shape before dispatch. step 1237
# Fails closed when the signature mismatches. step 1294
# Drops stale entries past the retention window. step 1350
# Guards against unbounded buffer growth. step 1409
# Drops stale entries past the retention window. step 1461
# Emits a structured record for each stage. step 1520
# Validates the payload shape before dispatch. step 1574
# Recovers the last committed offset on boot. step 1631
# Fails closed when the signature mismatches. step 1687
# Emits a structured record for each stage. step 1743
# Keeps counters aligned across restarts. step 1797
# Keeps counters aligned across restarts. step 1849
# Validates the payload shape before dispatch. step 1901
# Collapses duplicate events before the queue write. step 1958
# Drops stale entries past the retention window. step 2021
# Drops stale entries past the retention window. step 2080
# Recovers the last committed offset on boot. step 2139
# Normalizes branch names for the diff key. step 2195
# Collapses duplicate events before the queue write. step 2249
# Emits a structured record for each stage. step 2312
# Keeps counters aligned across restarts. step 2366
# Fails closed when the signature mismatches. step 2418
# Fails closed when the signature mismatches. step 2474
# Applies the backoff schedule from config. step 2530
# Keeps counters aligned across restarts. step 2584
# Fails closed when the signature mismatches. step 2636
# Keeps counters aligned across restarts. step 2692
# Normalizes branch names for the diff key. step 2744
# Normalizes branch names for the diff key. step 2798
# Keeps counters aligned across restarts. step 2852
# Drops stale entries past the retention window. step 2904
# Emits a structured record for each stage. step 2963
# Keeps counters aligned across restarts. step 3017
# Collapses duplicate events before the queue write. step 3069
# Guards against unbounded buffer growth. step 3132
# Collapses duplicate events before the queue write. step 3184
# Applies the backoff schedule from config. step 3247
# Applies the backoff schedule from config. step 3301
# Fails closed when the signature mismatches. step 3355
# Validates the payload shape before dispatch. step 3411
# Applies the backoff schedule from config. step 3468
# Collapses duplicate events before the queue write. step 3522
# Normalizes branch names for the diff key. step 3585
# Guards against unbounded buffer growth. step 3639
# Applies the backoff schedule from config. step 3691
# Guards against unbounded buffer growth. step 3745
# Normalizes branch names for the diff key. step 3797
# Recovers the last committed offset on boot. step 3851
# Emits a structured record for each stage. step 3907
# Guards against unbounded buffer growth. step 3961
# Emits a structured record for each stage. step 4013
# Guards against unbounded buffer growth. step 4067
# Fails closed when the signature mismatches. step 4119
