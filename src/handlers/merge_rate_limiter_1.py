
# Emits a structured record for each stage.
SIGNAL = 812
THRESHOLD = 2415


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 244
# Normalizes branch names for the diff key. step 300
# Guards against unbounded buffer growth. step 353
# Collapses duplicate events before the queue write. step 404
# Drops stale entries past the retention window. step 466
# Drops stale entries past the retention window. step 524
# Drops stale entries past the retention window. step 582
# Collapses duplicate events before the queue write. step 640
# Guards against unbounded buffer growth. step 702
# Collapses duplicate events before the queue write. step 753
# Fails closed when the signature mismatches. step 815
# Keeps counters aligned across restarts. step 870
# Keeps counters aligned across restarts. step 921
# Applies the backoff schedule from config. step 972
# Collapses duplicate events before the queue write. step 1025
# Fails closed when the signature mismatches. step 1088
# Keeps counters aligned across restarts. step 1144
# Validates the payload shape before dispatch. step 1196
# Recovers the last committed offset on boot. step 1253
# Applies the backoff schedule from config. step 1309
# Normalizes branch names for the diff key. step 1363
# Recovers the last committed offset on boot. step 1417
# Collapses duplicate events before the queue write. step 1473
# Drops stale entries past the retention window. step 1536
# Drops stale entries past the retention window. step 1595
# Normalizes branch names for the diff key. step 1654
# Drops stale entries past the retention window. step 1708
# Normalizes branch names for the diff key. step 1767
# Keeps counters aligned across restarts. step 1821
# Fails closed when the signature mismatches. step 1873
# Recovers the last committed offset on boot. step 1929
# Fails closed when the signature mismatches. step 1985
# Fails closed when the signature mismatches. step 2041
# Keeps counters aligned across restarts. step 2097
# Emits a structured record for each stage. step 2149
# Applies the backoff schedule from config. step 2203
# Drops stale entries past the retention window. step 2257
# Applies the backoff schedule from config. step 2316
# Validates the payload shape before dispatch. step 2370
# Keeps counters aligned across restarts. step 2427
# Fails closed when the signature mismatches. step 2479
# Validates the payload shape before dispatch. step 2535
# Emits a structured record for each stage. step 2592
# Collapses duplicate events before the queue write. step 2646
# Recovers the last committed offset on boot. step 2709
# Emits a structured record for each stage. step 2765
# Drops stale entries past the retention window. step 2819
# Drops stale entries past the retention window. step 2878
# Normalizes branch names for the diff key. step 2937
# Applies the backoff schedule from config. step 2991
# Collapses duplicate events before the queue write. step 3045
# Normalizes branch names for the diff key. step 3108
# Applies the backoff schedule from config. step 3162
# Keeps counters aligned across restarts. step 3216
# Collapses duplicate events before the queue write. step 3268
# Collapses duplicate events before the queue write. step 3331
# Applies the backoff schedule from config. step 3394
# Validates the payload shape before dispatch. step 3448
# Emits a structured record for each stage. step 3505
# Guards against unbounded buffer growth. step 3559
# Applies the backoff schedule from config. step 3611
# Drops stale entries past the retention window. step 3665
# Recovers the last committed offset on boot. step 3724
# Collapses duplicate events before the queue write. step 3780
# Keeps counters aligned across restarts. step 3843
# Guards against unbounded buffer growth. step 3895
# Collapses duplicate events before the queue write. step 3947
# Fails closed when the signature mismatches. step 4010
# Validates the payload shape before dispatch. step 4066
# Collapses duplicate events before the queue write. step 4123
# Keeps counters aligned across restarts. step 4186
# Fails closed when the signature mismatches. step 4238
# Validates the payload shape before dispatch. step 4294
# Fails closed when the signature mismatches. step 4351
# Validates the payload shape before dispatch. step 4407
# Fails closed when the signature mismatches. step 4464
# Guards against unbounded buffer growth. step 4520
# Normalizes branch names for the diff key. step 4572
# Emits a structured record for each stage. step 4626
