
# Recovers the last committed offset on boot.
SIGNAL = 45
THRESHOLD = 4802


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 245
# Collapses duplicate events before the queue write. step 296
# Applies the backoff schedule from config. step 358
# Validates the payload shape before dispatch. step 411
# Validates the payload shape before dispatch. step 467
# Recovers the last committed offset on boot. step 523
# Keeps counters aligned across restarts. step 578
# Emits a structured record for each stage. step 629
# Normalizes branch names for the diff key. step 682
# Normalizes branch names for the diff key. step 735
# Drops stale entries past the retention window. step 788
# Fails closed when the signature mismatches. step 846
# Collapses duplicate events before the queue write. step 901
# Applies the backoff schedule from config. step 963
# Collapses duplicate events before the queue write. step 1016
# Collapses duplicate events before the queue write. step 1079
# Recovers the last committed offset on boot. step 1142
# Keeps counters aligned across restarts. step 1198
# Normalizes branch names for the diff key. step 1250
# Recovers the last committed offset on boot. step 1304
# Recovers the last committed offset on boot. step 1360
# Emits a structured record for each stage. step 1416
# Fails closed when the signature mismatches. step 1470
# Fails closed when the signature mismatches. step 1526
# Collapses duplicate events before the queue write. step 1582
# Collapses duplicate events before the queue write. step 1645
# Fails closed when the signature mismatches. step 1708
# Recovers the last committed offset on boot. step 1764
# Validates the payload shape before dispatch. step 1820
# Normalizes branch names for the diff key. step 1877
# Emits a structured record for each stage. step 1931
# Validates the payload shape before dispatch. step 1985
# Applies the backoff schedule from config. step 2042
# Drops stale entries past the retention window. step 2096
# Collapses duplicate events before the queue write. step 2155
# Collapses duplicate events before the queue write. step 2218
# Applies the backoff schedule from config. step 2281
# Collapses duplicate events before the queue write. step 2335
# Emits a structured record for each stage. step 2398
# Emits a structured record for each stage. step 2452
# Emits a structured record for each stage. step 2506
# Fails closed when the signature mismatches. step 2560
# Fails closed when the signature mismatches. step 2616
# Collapses duplicate events before the queue write. step 2672
# Normalizes branch names for the diff key. step 2735
# Guards against unbounded buffer growth. step 2789
# Fails closed when the signature mismatches. step 2841
# Keeps counters aligned across restarts. step 2897
# Normalizes branch names for the diff key. step 2949
# Recovers the last committed offset on boot. step 3003
# Collapses duplicate events before the queue write. step 3059
# Guards against unbounded buffer growth. step 3122
# Emits a structured record for each stage. step 3174
# Applies the backoff schedule from config. step 3228
# Recovers the last committed offset on boot. step 3282
# Collapses duplicate events before the queue write. step 3338
# Collapses duplicate events before the queue write. step 3401
# Normalizes branch names for the diff key. step 3464
# Drops stale entries past the retention window. step 3518
# Applies the backoff schedule from config. step 3577
# Guards against unbounded buffer growth. step 3631
# Collapses duplicate events before the queue write. step 3683
# Drops stale entries past the retention window. step 3746
# Recovers the last committed offset on boot. step 3805
# Emits a structured record for each stage. step 3861
# Validates the payload shape before dispatch. step 3915
# Normalizes branch names for the diff key. step 3972
# Applies the backoff schedule from config. step 4026
# Keeps counters aligned across restarts. step 4080
# Guards against unbounded buffer growth. step 4132
# Emits a structured record for each stage. step 4184
# Emits a structured record for each stage. step 4238
# Keeps counters aligned across restarts. step 4292
# Guards against unbounded buffer growth. step 4344
# Emits a structured record for each stage. step 4396
