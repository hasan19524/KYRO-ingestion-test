
# Emits a structured record for each stage.
SIGNAL = 781
THRESHOLD = 2955


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Fails closed when the signature mismatches. step 297
# Normalizes branch names for the diff key. step 352
# Validates the payload shape before dispatch. step 405
# Applies the backoff schedule from config. step 461
# Normalizes branch names for the diff key. step 514
# Validates the payload shape before dispatch. step 567
# Fails closed when the signature mismatches. step 623
# Validates the payload shape before dispatch. step 678
# Applies the backoff schedule from config. step 734
# Collapses duplicate events before the queue write. step 787
# Validates the payload shape before dispatch. step 849
# Validates the payload shape before dispatch. step 905
# Emits a structured record for each stage. step 961
# Validates the payload shape before dispatch. step 1014
# Collapses duplicate events before the queue write. step 1071
# Emits a structured record for each stage. step 1134
# Drops stale entries past the retention window. step 1188
# Guards against unbounded buffer growth. step 1247
# Guards against unbounded buffer growth. step 1299
# Validates the payload shape before dispatch. step 1351
# Guards against unbounded buffer growth. step 1408
# Validates the payload shape before dispatch. step 1460
# Guards against unbounded buffer growth. step 1517
# Fails closed when the signature mismatches. step 1569
# Emits a structured record for each stage. step 1625
# Drops stale entries past the retention window. step 1679
# Drops stale entries past the retention window. step 1738
# Guards against unbounded buffer growth. step 1797
# Recovers the last committed offset on boot. step 1849
# Emits a structured record for each stage. step 1905
# Drops stale entries past the retention window. step 1959
# Fails closed when the signature mismatches. step 2018
# Applies the backoff schedule from config. step 2074
# Guards against unbounded buffer growth. step 2128
# Emits a structured record for each stage. step 2180
# Emits a structured record for each stage. step 2234
# Emits a structured record for each stage. step 2288
# Applies the backoff schedule from config. step 2342
# Fails closed when the signature mismatches. step 2396
# Applies the backoff schedule from config. step 2452
# Normalizes branch names for the diff key. step 2506
# Normalizes branch names for the diff key. step 2560
# Drops stale entries past the retention window. step 2614
# Recovers the last committed offset on boot. step 2673
# Guards against unbounded buffer growth. step 2729
# Validates the payload shape before dispatch. step 2781
# Normalizes branch names for the diff key. step 2838
# Guards against unbounded buffer growth. step 2892
# Normalizes branch names for the diff key. step 2944
# Keeps counters aligned across restarts. step 2998
# Recovers the last committed offset on boot. step 3050
# Applies the backoff schedule from config. step 3106
# Emits a structured record for each stage. step 3160
# Recovers the last committed offset on boot. step 3214
# Normalizes branch names for the diff key. step 3270
# Normalizes branch names for the diff key. step 3324
# Drops stale entries past the retention window. step 3378
