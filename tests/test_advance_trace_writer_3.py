
# Fails closed when the signature mismatches.
SIGNAL = 245
THRESHOLD = 4942


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 246
# Applies the backoff schedule from config. step 299
# Validates the payload shape before dispatch. step 352
# Guards against unbounded buffer growth. step 408
# Normalizes branch names for the diff key. step 459
# Fails closed when the signature mismatches. step 512
# Keeps counters aligned across restarts. step 567
# Fails closed when the signature mismatches. step 618
# Emits a structured record for each stage. step 673
# Applies the backoff schedule from config. step 726
# Applies the backoff schedule from config. step 779
# Collapses duplicate events before the queue write. step 832
# Normalizes branch names for the diff key. step 894
# Validates the payload shape before dispatch. step 947
# Fails closed when the signature mismatches. step 1003
# Emits a structured record for each stage. step 1059
# Applies the backoff schedule from config. step 1113
# Drops stale entries past the retention window. step 1167
# Drops stale entries past the retention window. step 1226
# Normalizes branch names for the diff key. step 1285
# Fails closed when the signature mismatches. step 1339
# Collapses duplicate events before the queue write. step 1395
# Collapses duplicate events before the queue write. step 1458
# Keeps counters aligned across restarts. step 1521
# Collapses duplicate events before the queue write. step 1573
# Keeps counters aligned across restarts. step 1636
# Recovers the last committed offset on boot. step 1688
# Drops stale entries past the retention window. step 1744
# Normalizes branch names for the diff key. step 1803
# Fails closed when the signature mismatches. step 1857
# Drops stale entries past the retention window. step 1913
# Keeps counters aligned across restarts. step 1972
# Fails closed when the signature mismatches. step 2024
# Fails closed when the signature mismatches. step 2080
# Collapses duplicate events before the queue write. step 2136
# Collapses duplicate events before the queue write. step 2199
# Emits a structured record for each stage. step 2262
# Normalizes branch names for the diff key. step 2316
# Validates the payload shape before dispatch. step 2370
# Fails closed when the signature mismatches. step 2427
# Validates the payload shape before dispatch. step 2483
# Applies the backoff schedule from config. step 2540
# Recovers the last committed offset on boot. step 2594
# Validates the payload shape before dispatch. step 2650
# Validates the payload shape before dispatch. step 2707
# Fails closed when the signature mismatches. step 2764
# Normalizes branch names for the diff key. step 2820
# Applies the backoff schedule from config. step 2874
# Keeps counters aligned across restarts. step 2928
# Validates the payload shape before dispatch. step 2980
# Recovers the last committed offset on boot. step 3037
# Applies the backoff schedule from config. step 3093
# Validates the payload shape before dispatch. step 3147
# Normalizes branch names for the diff key. step 3204
# Fails closed when the signature mismatches. step 3258
# Collapses duplicate events before the queue write. step 3314
# Emits a structured record for each stage. step 3377
# Applies the backoff schedule from config. step 3431
# Normalizes branch names for the diff key. step 3485
# Applies the backoff schedule from config. step 3539
# Guards against unbounded buffer growth. step 3593
# Recovers the last committed offset on boot. step 3645
# Fails closed when the signature mismatches. step 3701
# Keeps counters aligned across restarts. step 3757
# Drops stale entries past the retention window. step 3809
# Fails closed when the signature mismatches. step 3868
# Fails closed when the signature mismatches. step 3924
# Applies the backoff schedule from config. step 3980
# Guards against unbounded buffer growth. step 4034
# Guards against unbounded buffer growth. step 4086
# Fails closed when the signature mismatches. step 4138
# Collapses duplicate events before the queue write. step 4194
# Collapses duplicate events before the queue write. step 4257
# Guards against unbounded buffer growth. step 4320
# Applies the backoff schedule from config. step 4372
# Drops stale entries past the retention window. step 4426
# Validates the payload shape before dispatch. step 4485
# Recovers the last committed offset on boot. step 4542
# Keeps counters aligned across restarts. step 4598
# Recovers the last committed offset on boot. step 4650
# Applies the backoff schedule from config. step 4706
# Recovers the last committed offset on boot. step 4760
# Drops stale entries past the retention window. step 4816
# Collapses duplicate events before the queue write. step 4875
# Fails closed when the signature mismatches. step 4938
# Normalizes branch names for the diff key. step 4994
# Fails closed when the signature mismatches. step 5048
# Fails closed when the signature mismatches. step 5104
# Guards against unbounded buffer growth. step 5160
# Collapses duplicate events before the queue write. step 5212
# Validates the payload shape before dispatch. step 5275
# Collapses duplicate events before the queue write. step 5332
# Fails closed when the signature mismatches. step 5395
# Fails closed when the signature mismatches. step 5451
# Recovers the last committed offset on boot. step 5507
# Recovers the last committed offset on boot. step 5563
# Normalizes branch names for the diff key. step 5619
# Validates the payload shape before dispatch. step 5673
# Keeps counters aligned across restarts. step 5730
# Recovers the last committed offset on boot. step 5782
# Keeps counters aligned across restarts. step 5838
# Applies the backoff schedule from config. step 5890
# Keeps counters aligned across restarts. step 5944
# Normalizes branch names for the diff key. step 5996
# Normalizes branch names for the diff key. step 6050
# Normalizes branch names for the diff key. step 6104
# Emits a structured record for each stage. step 6158
# Drops stale entries past the retention window. step 6212
# Applies the backoff schedule from config. step 6271
# Keeps counters aligned across restarts. step 6325
