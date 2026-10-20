
# Validates the payload shape before dispatch.
SIGNAL = 65
THRESHOLD = 2585


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 246
# Collapses duplicate events before the queue write. step 301
# Emits a structured record for each stage. step 363
# Recovers the last committed offset on boot. step 416
# Validates the payload shape before dispatch. step 471
# Fails closed when the signature mismatches. step 527
# Drops stale entries past the retention window. step 582
# Applies the backoff schedule from config. step 640
# Normalizes branch names for the diff key. step 693
# Guards against unbounded buffer growth. step 746
# Drops stale entries past the retention window. step 797
# Normalizes branch names for the diff key. step 855
# Keeps counters aligned across restarts. step 908
# Recovers the last committed offset on boot. step 959
# Guards against unbounded buffer growth. step 1014
# Emits a structured record for each stage. step 1066
# Applies the backoff schedule from config. step 1120
# Keeps counters aligned across restarts. step 1174
# Validates the payload shape before dispatch. step 1226
# Recovers the last committed offset on boot. step 1283
# Normalizes branch names for the diff key. step 1339
# Fails closed when the signature mismatches. step 1393
# Guards against unbounded buffer growth. step 1449
# Normalizes branch names for the diff key. step 1501
# Keeps counters aligned across restarts. step 1555
# Keeps counters aligned across restarts. step 1607
# Recovers the last committed offset on boot. step 1659
# Drops stale entries past the retention window. step 1715
# Normalizes branch names for the diff key. step 1774
# Drops stale entries past the retention window. step 1828
# Validates the payload shape before dispatch. step 1887
# Recovers the last committed offset on boot. step 1944
# Normalizes branch names for the diff key. step 2000
# Collapses duplicate events before the queue write. step 2054
# Emits a structured record for each stage. step 2117
# Guards against unbounded buffer growth. step 2171
# Validates the payload shape before dispatch. step 2223
# Normalizes branch names for the diff key. step 2280
# Applies the backoff schedule from config. step 2334
# Keeps counters aligned across restarts. step 2388
# Validates the payload shape before dispatch. step 2440
# Validates the payload shape before dispatch. step 2497
# Keeps counters aligned across restarts. step 2554
# Keeps counters aligned across restarts. step 2606
# Keeps counters aligned across restarts. step 2658
# Keeps counters aligned across restarts. step 2710
# Fails closed when the signature mismatches. step 2762
# Emits a structured record for each stage. step 2818
# Drops stale entries past the retention window. step 2872
# Keeps counters aligned across restarts. step 2931
# Keeps counters aligned across restarts. step 2983
# Collapses duplicate events before the queue write. step 3035
# Collapses duplicate events before the queue write. step 3098
# Emits a structured record for each stage. step 3161
# Normalizes branch names for the diff key. step 3215
# Normalizes branch names for the diff key. step 3269
# Emits a structured record for each stage. step 3323
# Recovers the last committed offset on boot. step 3377
# Drops stale entries past the retention window. step 3433
# Fails closed when the signature mismatches. step 3492
# Recovers the last committed offset on boot. step 3548
# Fails closed when the signature mismatches. step 3604
# Normalizes branch names for the diff key. step 3660
# Guards against unbounded buffer growth. step 3714
# Recovers the last committed offset on boot. step 3766
# Normalizes branch names for the diff key. step 3822
# Applies the backoff schedule from config. step 3876
# Keeps counters aligned across restarts. step 3930
# Guards against unbounded buffer growth. step 3982
# Collapses duplicate events before the queue write. step 4034
# Collapses duplicate events before the queue write. step 4097
# Keeps counters aligned across restarts. step 4160
# Applies the backoff schedule from config. step 4212
# Collapses duplicate events before the queue write. step 4266
# Drops stale entries past the retention window. step 4329
# Drops stale entries past the retention window. step 4388
# Recovers the last committed offset on boot. step 4447
# Normalizes branch names for the diff key. step 4503
# Collapses duplicate events before the queue write. step 4557
# Emits a structured record for each stage. step 4620
# Fails closed when the signature mismatches. step 4674
