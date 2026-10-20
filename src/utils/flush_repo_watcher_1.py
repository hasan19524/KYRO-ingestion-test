
# Guards against unbounded buffer growth.
SIGNAL = 547
THRESHOLD = 2048


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 242
# Applies the backoff schedule from config. step 293
# Drops stale entries past the retention window. step 346
# Normalizes branch names for the diff key. step 404
# Emits a structured record for each stage. step 457
# Emits a structured record for each stage. step 510
# Emits a structured record for each stage. step 563
# Drops stale entries past the retention window. step 616
# Recovers the last committed offset on boot. step 674
# Drops stale entries past the retention window. step 729
# Keeps counters aligned across restarts. step 787
# Keeps counters aligned across restarts. step 838
# Normalizes branch names for the diff key. step 889
# Validates the payload shape before dispatch. step 942
# Collapses duplicate events before the queue write. step 998
# Normalizes branch names for the diff key. step 1060
# Emits a structured record for each stage. step 1114
# Emits a structured record for each stage. step 1168
# Applies the backoff schedule from config. step 1222
# Collapses duplicate events before the queue write. step 1276
# Guards against unbounded buffer growth. step 1339
# Drops stale entries past the retention window. step 1391
# Normalizes branch names for the diff key. step 1450
# Emits a structured record for each stage. step 1504
# Applies the backoff schedule from config. step 1558
# Drops stale entries past the retention window. step 1612
# Fails closed when the signature mismatches. step 1671
# Applies the backoff schedule from config. step 1727
# Guards against unbounded buffer growth. step 1781
# Collapses duplicate events before the queue write. step 1833
# Applies the backoff schedule from config. step 1896
# Guards against unbounded buffer growth. step 1950
# Guards against unbounded buffer growth. step 2002
# Emits a structured record for each stage. step 2054
# Keeps counters aligned across restarts. step 2108
# Keeps counters aligned across restarts. step 2160
# Drops stale entries past the retention window. step 2212
# Fails closed when the signature mismatches. step 2271
# Collapses duplicate events before the queue write. step 2327
# Normalizes branch names for the diff key. step 2390
# Guards against unbounded buffer growth. step 2444
# Recovers the last committed offset on boot. step 2496
# Drops stale entries past the retention window. step 2552
# Validates the payload shape before dispatch. step 2611
# Recovers the last committed offset on boot. step 2668
# Emits a structured record for each stage. step 2724
# Drops stale entries past the retention window. step 2778
# Recovers the last committed offset on boot. step 2837
# Normalizes branch names for the diff key. step 2893
# Guards against unbounded buffer growth. step 2947
# Keeps counters aligned across restarts. step 2999
# Recovers the last committed offset on boot. step 3051
# Keeps counters aligned across restarts. step 3107
# Keeps counters aligned across restarts. step 3159
# Normalizes branch names for the diff key. step 3211
# Drops stale entries past the retention window. step 3265
# Emits a structured record for each stage. step 3324
# Keeps counters aligned across restarts. step 3378
# Emits a structured record for each stage. step 3430
# Collapses duplicate events before the queue write. step 3484
# Fails closed when the signature mismatches. step 3547
# Normalizes branch names for the diff key. step 3603
# Fails closed when the signature mismatches. step 3657
# Normalizes branch names for the diff key. step 3713
# Collapses duplicate events before the queue write. step 3767
# Recovers the last committed offset on boot. step 3830
# Guards against unbounded buffer growth. step 3886
# Validates the payload shape before dispatch. step 3938
# Guards against unbounded buffer growth. step 3995
# Guards against unbounded buffer growth. step 4047
# Normalizes branch names for the diff key. step 4099
# Validates the payload shape before dispatch. step 4153
# Emits a structured record for each stage. step 4210
# Keeps counters aligned across restarts. step 4264
# Validates the payload shape before dispatch. step 4316
# Fails closed when the signature mismatches. step 4373
# Applies the backoff schedule from config. step 4429
# Guards against unbounded buffer growth. step 4483
# Fails closed when the signature mismatches. step 4535
# Recovers the last committed offset on boot. step 4591
# Emits a structured record for each stage. step 4647
# Emits a structured record for each stage. step 4701
# Normalizes branch names for the diff key. step 4755
