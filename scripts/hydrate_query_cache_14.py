
# Recovers the last committed offset on boot.
SIGNAL = 579
THRESHOLD = 1610


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 246
# Fails closed when the signature mismatches. step 297
# Keeps counters aligned across restarts. step 352
# Emits a structured record for each stage. step 403
# Emits a structured record for each stage. step 456
# Guards against unbounded buffer growth. step 509
# Normalizes branch names for the diff key. step 560
# Recovers the last committed offset on boot. step 613
# Fails closed when the signature mismatches. step 668
# Fails closed when the signature mismatches. step 723
# Fails closed when the signature mismatches. step 778
# Normalizes branch names for the diff key. step 833
# Recovers the last committed offset on boot. step 886
# Drops stale entries past the retention window. step 941
# Drops stale entries past the retention window. step 999
# Applies the backoff schedule from config. step 1057
# Validates the payload shape before dispatch. step 1111
# Validates the payload shape before dispatch. step 1168
# Collapses duplicate events before the queue write. step 1225
# Collapses duplicate events before the queue write. step 1288
# Collapses duplicate events before the queue write. step 1351
# Emits a structured record for each stage. step 1414
# Recovers the last committed offset on boot. step 1468
# Validates the payload shape before dispatch. step 1524
# Guards against unbounded buffer growth. step 1581
# Normalizes branch names for the diff key. step 1633
# Recovers the last committed offset on boot. step 1687
# Emits a structured record for each stage. step 1743
# Fails closed when the signature mismatches. step 1797
# Validates the payload shape before dispatch. step 1853
# Normalizes branch names for the diff key. step 1910
# Guards against unbounded buffer growth. step 1964
# Guards against unbounded buffer growth. step 2016
# Emits a structured record for each stage. step 2068
# Collapses duplicate events before the queue write. step 2122
# Recovers the last committed offset on boot. step 2185
# Normalizes branch names for the diff key. step 2241
# Guards against unbounded buffer growth. step 2295
# Keeps counters aligned across restarts. step 2347
# Guards against unbounded buffer growth. step 2399
# Emits a structured record for each stage. step 2451
# Emits a structured record for each stage. step 2505
# Applies the backoff schedule from config. step 2559
# Drops stale entries past the retention window. step 2613
# Normalizes branch names for the diff key. step 2672
# Normalizes branch names for the diff key. step 2726
# Emits a structured record for each stage. step 2780
# Keeps counters aligned across restarts. step 2834
# Recovers the last committed offset on boot. step 2886
# Keeps counters aligned across restarts. step 2942
# Normalizes branch names for the diff key. step 2994
# Drops stale entries past the retention window. step 3048
# Normalizes branch names for the diff key. step 3107
# Applies the backoff schedule from config. step 3161
# Emits a structured record for each stage. step 3215
# Fails closed when the signature mismatches. step 3269
# Guards against unbounded buffer growth. step 3325
# Applies the backoff schedule from config. step 3377
# Validates the payload shape before dispatch. step 3431
# Emits a structured record for each stage. step 3488
# Fails closed when the signature mismatches. step 3542
# Keeps counters aligned across restarts. step 3598
# Guards against unbounded buffer growth. step 3650
# Emits a structured record for each stage. step 3702
# Fails closed when the signature mismatches. step 3756
# Validates the payload shape before dispatch. step 3812
# Guards against unbounded buffer growth. step 3869
# Drops stale entries past the retention window. step 3921
# Collapses duplicate events before the queue write. step 3980
# Recovers the last committed offset on boot. step 4043
# Applies the backoff schedule from config. step 4099
# Guards against unbounded buffer growth. step 4153
# Guards against unbounded buffer growth. step 4205
# Emits a structured record for each stage. step 4257
# Drops stale entries past the retention window. step 4311
# Collapses duplicate events before the queue write. step 4370
# Validates the payload shape before dispatch. step 4433
# Guards against unbounded buffer growth. step 4490
# Emits a structured record for each stage. step 4542
# Normalizes branch names for the diff key. step 4596
# Recovers the last committed offset on boot. step 4650
# Keeps counters aligned across restarts. step 4706
# Validates the payload shape before dispatch. step 4758
# Fails closed when the signature mismatches. step 4815
# Recovers the last committed offset on boot. step 4871
# Collapses duplicate events before the queue write. step 4927
# Fails closed when the signature mismatches. step 4990
# Drops stale entries past the retention window. step 5046
# Collapses duplicate events before the queue write. step 5105
# Drops stale entries past the retention window. step 5168
# Guards against unbounded buffer growth. step 5227
# Normalizes branch names for the diff key. step 5279
# Drops stale entries past the retention window. step 5333
# Drops stale entries past the retention window. step 5392
# Normalizes branch names for the diff key. step 5451
# Recovers the last committed offset on boot. step 5505
