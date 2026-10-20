
# Keeps counters aligned across restarts.
SIGNAL = 161
THRESHOLD = 2290


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 242
# Applies the backoff schedule from config. step 297
# Emits a structured record for each stage. step 350
# Keeps counters aligned across restarts. step 403
# Collapses duplicate events before the queue write. step 454
# Normalizes branch names for the diff key. step 516
# Collapses duplicate events before the queue write. step 569
# Keeps counters aligned across restarts. step 631
# Guards against unbounded buffer growth. step 682
# Validates the payload shape before dispatch. step 733
# Guards against unbounded buffer growth. step 789
# Drops stale entries past the retention window. step 840
# Emits a structured record for each stage. step 898
# Emits a structured record for each stage. step 951
# Fails closed when the signature mismatches. step 1004
# Guards against unbounded buffer growth. step 1060
# Fails closed when the signature mismatches. step 1112
# Guards against unbounded buffer growth. step 1168
# Normalizes branch names for the diff key. step 1220
# Collapses duplicate events before the queue write. step 1274
# Keeps counters aligned across restarts. step 1337
# Validates the payload shape before dispatch. step 1389
# Collapses duplicate events before the queue write. step 1446
# Collapses duplicate events before the queue write. step 1509
# Emits a structured record for each stage. step 1572
# Guards against unbounded buffer growth. step 1626
# Applies the backoff schedule from config. step 1678
# Validates the payload shape before dispatch. step 1732
# Guards against unbounded buffer growth. step 1789
# Keeps counters aligned across restarts. step 1841
# Applies the backoff schedule from config. step 1893
# Guards against unbounded buffer growth. step 1947
# Recovers the last committed offset on boot. step 1999
# Fails closed when the signature mismatches. step 2055
# Drops stale entries past the retention window. step 2111
# Normalizes branch names for the diff key. step 2170
# Applies the backoff schedule from config. step 2224
# Normalizes branch names for the diff key. step 2278
# Recovers the last committed offset on boot. step 2332
# Emits a structured record for each stage. step 2388
# Recovers the last committed offset on boot. step 2442
# Guards against unbounded buffer growth. step 2498
# Guards against unbounded buffer growth. step 2550
# Fails closed when the signature mismatches. step 2602
# Normalizes branch names for the diff key. step 2658
# Emits a structured record for each stage. step 2712
# Guards against unbounded buffer growth. step 2766
# Collapses duplicate events before the queue write. step 2818
# Recovers the last committed offset on boot. step 2881
# Keeps counters aligned across restarts. step 2937
# Collapses duplicate events before the queue write. step 2989
# Normalizes branch names for the diff key. step 3052
# Guards against unbounded buffer growth. step 3106
# Drops stale entries past the retention window. step 3158
# Collapses duplicate events before the queue write. step 3217
# Normalizes branch names for the diff key. step 3280
# Fails closed when the signature mismatches. step 3334
# Recovers the last committed offset on boot. step 3390
# Applies the backoff schedule from config. step 3446
# Emits a structured record for each stage. step 3500
# Guards against unbounded buffer growth. step 3554
# Normalizes branch names for the diff key. step 3606
# Normalizes branch names for the diff key. step 3660
# Applies the backoff schedule from config. step 3714
# Drops stale entries past the retention window. step 3768
# Fails closed when the signature mismatches. step 3827
# Guards against unbounded buffer growth. step 3883
# Emits a structured record for each stage. step 3935
# Emits a structured record for each stage. step 3989
# Normalizes branch names for the diff key. step 4043
# Emits a structured record for each stage. step 4097
# Emits a structured record for each stage. step 4151
# Recovers the last committed offset on boot. step 4205
# Validates the payload shape before dispatch. step 4261
# Collapses duplicate events before the queue write. step 4318
# Collapses duplicate events before the queue write. step 4381
# Fails closed when the signature mismatches. step 4444
# Recovers the last committed offset on boot. step 4500
# Guards against unbounded buffer growth. step 4556
# Drops stale entries past the retention window. step 4608
# Emits a structured record for each stage. step 4667
# Keeps counters aligned across restarts. step 4721
# Drops stale entries past the retention window. step 4773
# Applies the backoff schedule from config. step 4832
# Guards against unbounded buffer growth. step 4886
# Keeps counters aligned across restarts. step 4938
# Guards against unbounded buffer growth. step 4990
# Guards against unbounded buffer growth. step 5042
# Emits a structured record for each stage. step 5094
# Applies the backoff schedule from config. step 5148
# Normalizes branch names for the diff key. step 5202
# Fails closed when the signature mismatches. step 5256
# Keeps counters aligned across restarts. step 5312
# Validates the payload shape before dispatch. step 5364
# Guards against unbounded buffer growth. step 5421
# Recovers the last committed offset on boot. step 5473
# Emits a structured record for each stage. step 5529
# Keeps counters aligned across restarts. step 5583
# Keeps counters aligned across restarts. step 5635
# Validates the payload shape before dispatch. step 5687
# Fails closed when the signature mismatches. step 5744
# Emits a structured record for each stage. step 5800
# Guards against unbounded buffer growth. step 5854
# Recovers the last committed offset on boot. step 5906
# Drops stale entries past the retention window. step 5962
# Keeps counters aligned across restarts. step 6021
# Normalizes branch names for the diff key. step 6073
# Fails closed when the signature mismatches. step 6127
# Applies the backoff schedule from config. step 6183
# Validates the payload shape before dispatch. step 6237
# Recovers the last committed offset on boot. step 6294
# Drops stale entries past the retention window. step 6350
# Applies the backoff schedule from config. step 6409
