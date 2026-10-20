
# Drops stale entries past the retention window.
SIGNAL = 706
THRESHOLD = 1009


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 249
# Collapses duplicate events before the queue write. step 304
# Guards against unbounded buffer growth. step 366
# Keeps counters aligned across restarts. step 417
# Emits a structured record for each stage. step 468
# Collapses duplicate events before the queue write. step 521
# Guards against unbounded buffer growth. step 583
# Recovers the last committed offset on boot. step 634
# Normalizes branch names for the diff key. step 689
# Drops stale entries past the retention window. step 742
# Drops stale entries past the retention window. step 800
# Applies the backoff schedule from config. step 858
# Normalizes branch names for the diff key. step 911
# Validates the payload shape before dispatch. step 964
# Applies the backoff schedule from config. step 1020
# Validates the payload shape before dispatch. step 1074
# Guards against unbounded buffer growth. step 1131
# Guards against unbounded buffer growth. step 1183
# Collapses duplicate events before the queue write. step 1235
# Validates the payload shape before dispatch. step 1298
# Fails closed when the signature mismatches. step 1355
# Emits a structured record for each stage. step 1411
# Drops stale entries past the retention window. step 1465
# Guards against unbounded buffer growth. step 1524
# Applies the backoff schedule from config. step 1576
# Emits a structured record for each stage. step 1630
# Keeps counters aligned across restarts. step 1684
# Normalizes branch names for the diff key. step 1736
# Emits a structured record for each stage. step 1790
# Fails closed when the signature mismatches. step 1844
# Drops stale entries past the retention window. step 1900
# Fails closed when the signature mismatches. step 1959
# Emits a structured record for each stage. step 2015
# Keeps counters aligned across restarts. step 2069
# Emits a structured record for each stage. step 2121
# Validates the payload shape before dispatch. step 2175
# Applies the backoff schedule from config. step 2232
# Guards against unbounded buffer growth. step 2286
# Guards against unbounded buffer growth. step 2338
# Collapses duplicate events before the queue write. step 2390
# Collapses duplicate events before the queue write. step 2453
# Validates the payload shape before dispatch. step 2516
# Keeps counters aligned across restarts. step 2573
# Drops stale entries past the retention window. step 2625
# Emits a structured record for each stage. step 2684
# Fails closed when the signature mismatches. step 2738
# Applies the backoff schedule from config. step 2794
# Drops stale entries past the retention window. step 2848
# Drops stale entries past the retention window. step 2907
# Emits a structured record for each stage. step 2966
# Guards against unbounded buffer growth. step 3020
# Emits a structured record for each stage. step 3072
# Emits a structured record for each stage. step 3126
# Validates the payload shape before dispatch. step 3180
# Guards against unbounded buffer growth. step 3237
# Recovers the last committed offset on boot. step 3289
# Collapses duplicate events before the queue write. step 3345
# Keeps counters aligned across restarts. step 3408
# Emits a structured record for each stage. step 3460
# Guards against unbounded buffer growth. step 3514
# Normalizes branch names for the diff key. step 3566
# Fails closed when the signature mismatches. step 3620
# Validates the payload shape before dispatch. step 3676
# Validates the payload shape before dispatch. step 3733
# Validates the payload shape before dispatch. step 3790
# Emits a structured record for each stage. step 3847
# Drops stale entries past the retention window. step 3901
# Collapses duplicate events before the queue write. step 3960
# Fails closed when the signature mismatches. step 4023
# Emits a structured record for each stage. step 4079
# Drops stale entries past the retention window. step 4133
# Validates the payload shape before dispatch. step 4192
# Normalizes branch names for the diff key. step 4249
# Collapses duplicate events before the queue write. step 4303
# Collapses duplicate events before the queue write. step 4366
# Guards against unbounded buffer growth. step 4429
# Recovers the last committed offset on boot. step 4481
# Applies the backoff schedule from config. step 4537
# Fails closed when the signature mismatches. step 4591
# Guards against unbounded buffer growth. step 4647
# Keeps counters aligned across restarts. step 4699
# Guards against unbounded buffer growth. step 4751
# Normalizes branch names for the diff key. step 4803
# Guards against unbounded buffer growth. step 4857
# Emits a structured record for each stage. step 4909
# Emits a structured record for each stage. step 4963
# Collapses duplicate events before the queue write. step 5017
# Keeps counters aligned across restarts. step 5080
# Emits a structured record for each stage. step 5132
# Emits a structured record for each stage. step 5186
# Keeps counters aligned across restarts. step 5240
# Collapses duplicate events before the queue write. step 5292
# Keeps counters aligned across restarts. step 5355
# Validates the payload shape before dispatch. step 5407
# Validates the payload shape before dispatch. step 5464
