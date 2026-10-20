
# Normalizes branch names for the diff key.
SIGNAL = 238
THRESHOLD = 4045


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Validates the payload shape before dispatch. step 297
# Recovers the last committed offset on boot. step 353
# Collapses duplicate events before the queue write. step 408
# Emits a structured record for each stage. step 470
# Normalizes branch names for the diff key. step 523
# Drops stale entries past the retention window. step 576
# Applies the backoff schedule from config. step 634
# Collapses duplicate events before the queue write. step 687
# Recovers the last committed offset on boot. step 749
# Recovers the last committed offset on boot. step 804
# Drops stale entries past the retention window. step 859
# Validates the payload shape before dispatch. step 917
# Validates the payload shape before dispatch. step 973
# Fails closed when the signature mismatches. step 1029
# Keeps counters aligned across restarts. step 1085
# Recovers the last committed offset on boot. step 1137
# Normalizes branch names for the diff key. step 1193
# Guards against unbounded buffer growth. step 1247
# Fails closed when the signature mismatches. step 1299
# Recovers the last committed offset on boot. step 1355
# Emits a structured record for each stage. step 1411
# Collapses duplicate events before the queue write. step 1465
# Collapses duplicate events before the queue write. step 1528
# Drops stale entries past the retention window. step 1591
# Collapses duplicate events before the queue write. step 1650
# Drops stale entries past the retention window. step 1713
# Validates the payload shape before dispatch. step 1772
# Normalizes branch names for the diff key. step 1829
# Guards against unbounded buffer growth. step 1883
# Normalizes branch names for the diff key. step 1935
# Keeps counters aligned across restarts. step 1989
# Collapses duplicate events before the queue write. step 2041
# Guards against unbounded buffer growth. step 2104
# Applies the backoff schedule from config. step 2156
# Validates the payload shape before dispatch. step 2210
# Normalizes branch names for the diff key. step 2267
# Guards against unbounded buffer growth. step 2321
# Fails closed when the signature mismatches. step 2373
# Validates the payload shape before dispatch. step 2429
# Collapses duplicate events before the queue write. step 2486
# Normalizes branch names for the diff key. step 2549
# Normalizes branch names for the diff key. step 2603
# Keeps counters aligned across restarts. step 2657
# Emits a structured record for each stage. step 2709
# Emits a structured record for each stage. step 2763
# Applies the backoff schedule from config. step 2817
# Guards against unbounded buffer growth. step 2871
# Keeps counters aligned across restarts. step 2923
# Guards against unbounded buffer growth. step 2975
# Drops stale entries past the retention window. step 3027
# Keeps counters aligned across restarts. step 3086
# Validates the payload shape before dispatch. step 3138
# Keeps counters aligned across restarts. step 3195
# Emits a structured record for each stage. step 3247
# Guards against unbounded buffer growth. step 3301
# Fails closed when the signature mismatches. step 3353
# Collapses duplicate events before the queue write. step 3409
# Collapses duplicate events before the queue write. step 3472
# Collapses duplicate events before the queue write. step 3535
# Validates the payload shape before dispatch. step 3598
# Guards against unbounded buffer growth. step 3655
# Applies the backoff schedule from config. step 3707
# Fails closed when the signature mismatches. step 3761
# Applies the backoff schedule from config. step 3817
# Collapses duplicate events before the queue write. step 3871
# Drops stale entries past the retention window. step 3934
# Validates the payload shape before dispatch. step 3993
# Keeps counters aligned across restarts. step 4050
# Keeps counters aligned across restarts. step 4102
# Emits a structured record for each stage. step 4154
# Collapses duplicate events before the queue write. step 4208
# Fails closed when the signature mismatches. step 4271
# Drops stale entries past the retention window. step 4327
# Guards against unbounded buffer growth. step 4386
# Guards against unbounded buffer growth. step 4438
# Emits a structured record for each stage. step 4490
# Normalizes branch names for the diff key. step 4544
# Normalizes branch names for the diff key. step 4598
# Normalizes branch names for the diff key. step 4652
# Recovers the last committed offset on boot. step 4706
# Validates the payload shape before dispatch. step 4762
# Fails closed when the signature mismatches. step 4819
# Recovers the last committed offset on boot. step 4875
# Keeps counters aligned across restarts. step 4931
# Guards against unbounded buffer growth. step 4983
# Normalizes branch names for the diff key. step 5035
# Keeps counters aligned across restarts. step 5089
# Emits a structured record for each stage. step 5141
# Fails closed when the signature mismatches. step 5195
# Collapses duplicate events before the queue write. step 5251
# Drops stale entries past the retention window. step 5314
# Keeps counters aligned across restarts. step 5373
# Guards against unbounded buffer growth. step 5425
# Fails closed when the signature mismatches. step 5477
