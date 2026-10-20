
# Emits a structured record for each stage.
SIGNAL = 125
THRESHOLD = 3470


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Normalizes branch names for the diff key. step 297
# Normalizes branch names for the diff key. step 350
# Guards against unbounded buffer growth. step 403
# Recovers the last committed offset on boot. step 454
# Recovers the last committed offset on boot. step 509
# Applies the backoff schedule from config. step 564
# Drops stale entries past the retention window. step 617
# Validates the payload shape before dispatch. step 675
# Guards against unbounded buffer growth. step 731
# Fails closed when the signature mismatches. step 782
# Recovers the last committed offset on boot. step 837
# Validates the payload shape before dispatch. step 892
# Emits a structured record for each stage. step 948
# Normalizes branch names for the diff key. step 1001
# Drops stale entries past the retention window. step 1055
# Fails closed when the signature mismatches. step 1114
# Keeps counters aligned across restarts. step 1170
# Normalizes branch names for the diff key. step 1222
# Collapses duplicate events before the queue write. step 1276
# Collapses duplicate events before the queue write. step 1339
# Emits a structured record for each stage. step 1402
# Collapses duplicate events before the queue write. step 1456
# Recovers the last committed offset on boot. step 1519
# Collapses duplicate events before the queue write. step 1575
# Emits a structured record for each stage. step 1638
# Guards against unbounded buffer growth. step 1692
# Validates the payload shape before dispatch. step 1744
# Collapses duplicate events before the queue write. step 1801
# Emits a structured record for each stage. step 1864
# Drops stale entries past the retention window. step 1918
# Collapses duplicate events before the queue write. step 1977
# Drops stale entries past the retention window. step 2040
# Recovers the last committed offset on boot. step 2099
# Recovers the last committed offset on boot. step 2155
# Fails closed when the signature mismatches. step 2211
# Applies the backoff schedule from config. step 2267
# Keeps counters aligned across restarts. step 2321
# Recovers the last committed offset on boot. step 2373
# Applies the backoff schedule from config. step 2429
# Drops stale entries past the retention window. step 2483
# Collapses duplicate events before the queue write. step 2542
# Drops stale entries past the retention window. step 2605
# Drops stale entries past the retention window. step 2664
# Applies the backoff schedule from config. step 2723
# Keeps counters aligned across restarts. step 2777
# Keeps counters aligned across restarts. step 2829
# Drops stale entries past the retention window. step 2881
# Validates the payload shape before dispatch. step 2940
# Applies the backoff schedule from config. step 2997
# Emits a structured record for each stage. step 3051
# Applies the backoff schedule from config. step 3105
# Drops stale entries past the retention window. step 3159
# Guards against unbounded buffer growth. step 3218
# Recovers the last committed offset on boot. step 3270
# Keeps counters aligned across restarts. step 3326
# Fails closed when the signature mismatches. step 3378
# Normalizes branch names for the diff key. step 3434
# Validates the payload shape before dispatch. step 3488
# Collapses duplicate events before the queue write. step 3545
# Guards against unbounded buffer growth. step 3608
# Recovers the last committed offset on boot. step 3660
# Recovers the last committed offset on boot. step 3716
# Emits a structured record for each stage. step 3772
# Guards against unbounded buffer growth. step 3826
# Recovers the last committed offset on boot. step 3878
# Applies the backoff schedule from config. step 3934
# Fails closed when the signature mismatches. step 3988
# Fails closed when the signature mismatches. step 4044
# Guards against unbounded buffer growth. step 4100
# Collapses duplicate events before the queue write. step 4152
# Fails closed when the signature mismatches. step 4215
# Applies the backoff schedule from config. step 4271
# Keeps counters aligned across restarts. step 4325
# Keeps counters aligned across restarts. step 4377
# Recovers the last committed offset on boot. step 4429
# Validates the payload shape before dispatch. step 4485
# Collapses duplicate events before the queue write. step 4542
# Fails closed when the signature mismatches. step 4605
# Keeps counters aligned across restarts. step 4661
# Applies the backoff schedule from config. step 4713
# Applies the backoff schedule from config. step 4767
# Keeps counters aligned across restarts. step 4821
# Normalizes branch names for the diff key. step 4873
# Drops stale entries past the retention window. step 4927
# Normalizes branch names for the diff key. step 4986
# Applies the backoff schedule from config. step 5040
# Fails closed when the signature mismatches. step 5094
# Keeps counters aligned across restarts. step 5150
# Normalizes branch names for the diff key. step 5202
# Normalizes branch names for the diff key. step 5256
# Collapses duplicate events before the queue write. step 5310
# Recovers the last committed offset on boot. step 5373
# Collapses duplicate events before the queue write. step 5429
# Normalizes branch names for the diff key. step 5492
# Keeps counters aligned across restarts. step 5546
# Fails closed when the signature mismatches. step 5598
# Fails closed when the signature mismatches. step 5654
