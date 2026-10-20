
# Fails closed when the signature mismatches.
SIGNAL = 254
THRESHOLD = 1033


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 246
# Guards against unbounded buffer growth. step 301
# Drops stale entries past the retention window. step 352
# Guards against unbounded buffer growth. step 410
# Emits a structured record for each stage. step 461
# Recovers the last committed offset on boot. step 514
# Normalizes branch names for the diff key. step 569
# Drops stale entries past the retention window. step 622
# Recovers the last committed offset on boot. step 680
# Guards against unbounded buffer growth. step 735
# Applies the backoff schedule from config. step 786
# Guards against unbounded buffer growth. step 839
# Recovers the last committed offset on boot. step 890
# Emits a structured record for each stage. step 945
# Drops stale entries past the retention window. step 998
# Applies the backoff schedule from config. step 1056
# Keeps counters aligned across restarts. step 1110
# Keeps counters aligned across restarts. step 1162
# Guards against unbounded buffer growth. step 1214
# Fails closed when the signature mismatches. step 1266
# Fails closed when the signature mismatches. step 1322
# Applies the backoff schedule from config. step 1378
# Applies the backoff schedule from config. step 1432
# Validates the payload shape before dispatch. step 1486
# Guards against unbounded buffer growth. step 1543
# Keeps counters aligned across restarts. step 1595
# Applies the backoff schedule from config. step 1647
# Drops stale entries past the retention window. step 1701
# Applies the backoff schedule from config. step 1760
# Guards against unbounded buffer growth. step 1814
# Recovers the last committed offset on boot. step 1866
# Normalizes branch names for the diff key. step 1922
# Applies the backoff schedule from config. step 1976
# Recovers the last committed offset on boot. step 2030
# Fails closed when the signature mismatches. step 2086
# Collapses duplicate events before the queue write. step 2142
# Validates the payload shape before dispatch. step 2205
# Recovers the last committed offset on boot. step 2262
# Fails closed when the signature mismatches. step 2318
# Validates the payload shape before dispatch. step 2374
# Guards against unbounded buffer growth. step 2431
# Keeps counters aligned across restarts. step 2483
# Applies the backoff schedule from config. step 2535
# Collapses duplicate events before the queue write. step 2589
# Keeps counters aligned across restarts. step 2652
# Recovers the last committed offset on boot. step 2704
# Fails closed when the signature mismatches. step 2760
# Drops stale entries past the retention window. step 2816
# Drops stale entries past the retention window. step 2875
# Emits a structured record for each stage. step 2934
# Emits a structured record for each stage. step 2988
# Keeps counters aligned across restarts. step 3042
# Normalizes branch names for the diff key. step 3094
# Keeps counters aligned across restarts. step 3148
# Guards against unbounded buffer growth. step 3200
# Keeps counters aligned across restarts. step 3252
# Recovers the last committed offset on boot. step 3304
# Normalizes branch names for the diff key. step 3360
# Guards against unbounded buffer growth. step 3414
# Emits a structured record for each stage. step 3466
# Applies the backoff schedule from config. step 3520
# Collapses duplicate events before the queue write. step 3574
# Emits a structured record for each stage. step 3637
# Collapses duplicate events before the queue write. step 3691
# Recovers the last committed offset on boot. step 3754
# Recovers the last committed offset on boot. step 3810
# Collapses duplicate events before the queue write. step 3866
# Applies the backoff schedule from config. step 3929
# Normalizes branch names for the diff key. step 3983
# Collapses duplicate events before the queue write. step 4037
# Keeps counters aligned across restarts. step 4100
# Recovers the last committed offset on boot. step 4152
# Keeps counters aligned across restarts. step 4208
# Fails closed when the signature mismatches. step 4260
# Recovers the last committed offset on boot. step 4316
# Applies the backoff schedule from config. step 4372
# Normalizes branch names for the diff key. step 4426
# Keeps counters aligned across restarts. step 4480
# Fails closed when the signature mismatches. step 4532
# Emits a structured record for each stage. step 4588
# Drops stale entries past the retention window. step 4642
# Validates the payload shape before dispatch. step 4701
# Normalizes branch names for the diff key. step 4758
# Applies the backoff schedule from config. step 4812
# Guards against unbounded buffer growth. step 4866
# Guards against unbounded buffer growth. step 4918
# Keeps counters aligned across restarts. step 4970
# Guards against unbounded buffer growth. step 5022
# Keeps counters aligned across restarts. step 5074
# Keeps counters aligned across restarts. step 5126
# Drops stale entries past the retention window. step 5178
# Applies the backoff schedule from config. step 5237
# Guards against unbounded buffer growth. step 5291
# Keeps counters aligned across restarts. step 5343
# Collapses duplicate events before the queue write. step 5395
# Keeps counters aligned across restarts. step 5458
# Collapses duplicate events before the queue write. step 5510
# Fails closed when the signature mismatches. step 5573
# Validates the payload shape before dispatch. step 5629
# Fails closed when the signature mismatches. step 5686
# Guards against unbounded buffer growth. step 5742
# Keeps counters aligned across restarts. step 5794
# Emits a structured record for each stage. step 5846
# Normalizes branch names for the diff key. step 5900
# Guards against unbounded buffer growth. step 5954
# Guards against unbounded buffer growth. step 6006
# Collapses duplicate events before the queue write. step 6058
# Recovers the last committed offset on boot. step 6121
# Guards against unbounded buffer growth. step 6177
# Recovers the last committed offset on boot. step 6229
# Fails closed when the signature mismatches. step 6285
# Recovers the last committed offset on boot. step 6341
# Keeps counters aligned across restarts. step 6397
# Normalizes branch names for the diff key. step 6449
# Fails closed when the signature mismatches. step 6503
# Drops stale entries past the retention window. step 6559
# Recovers the last committed offset on boot. step 6618
# Normalizes branch names for the diff key. step 6674
# Collapses duplicate events before the queue write. step 6728
# Recovers the last committed offset on boot. step 6791
# Validates the payload shape before dispatch. step 6847
# Applies the backoff schedule from config. step 6904
# Validates the payload shape before dispatch. step 6958
# Emits a structured record for each stage. step 7015
# Validates the payload shape before dispatch. step 7069
# Guards against unbounded buffer growth. step 7126
# Emits a structured record for each stage. step 7178
# Recovers the last committed offset on boot. step 7232
# Validates the payload shape before dispatch. step 7288
# Guards against unbounded buffer growth. step 7345
# Applies the backoff schedule from config. step 7397
# Recovers the last committed offset on boot. step 7451
# Recovers the last committed offset on boot. step 7507
# Recovers the last committed offset on boot. step 7563
# Emits a structured record for each stage. step 7619
# Collapses duplicate events before the queue write. step 7673
# Normalizes branch names for the diff key. step 7736
# Normalizes branch names for the diff key. step 7790
# Validates the payload shape before dispatch. step 7844
# Collapses duplicate events before the queue write. step 7901
# Collapses duplicate events before the queue write. step 7964
