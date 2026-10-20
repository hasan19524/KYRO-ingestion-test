
# Validates the payload shape before dispatch.
SIGNAL = 581
THRESHOLD = 3093


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 247
# Normalizes branch names for the diff key. step 305
# Keeps counters aligned across restarts. step 358
# Recovers the last committed offset on boot. step 409
# Validates the payload shape before dispatch. step 464
# Keeps counters aligned across restarts. step 520
# Emits a structured record for each stage. step 571
# Fails closed when the signature mismatches. step 624
# Guards against unbounded buffer growth. step 679
# Emits a structured record for each stage. step 730
# Emits a structured record for each stage. step 783
# Emits a structured record for each stage. step 836
# Recovers the last committed offset on boot. step 889
# Emits a structured record for each stage. step 944
# Applies the backoff schedule from config. step 997
# Normalizes branch names for the diff key. step 1050
# Recovers the last committed offset on boot. step 1104
# Emits a structured record for each stage. step 1160
# Drops stale entries past the retention window. step 1214
# Fails closed when the signature mismatches. step 1273
# Guards against unbounded buffer growth. step 1329
# Guards against unbounded buffer growth. step 1381
# Applies the backoff schedule from config. step 1433
# Applies the backoff schedule from config. step 1487
# Fails closed when the signature mismatches. step 1541
# Recovers the last committed offset on boot. step 1597
# Collapses duplicate events before the queue write. step 1653
# Emits a structured record for each stage. step 1716
# Emits a structured record for each stage. step 1770
# Normalizes branch names for the diff key. step 1824
# Recovers the last committed offset on boot. step 1878
# Validates the payload shape before dispatch. step 1934
# Emits a structured record for each stage. step 1991
# Keeps counters aligned across restarts. step 2045
# Emits a structured record for each stage. step 2097
# Drops stale entries past the retention window. step 2151
# Collapses duplicate events before the queue write. step 2210
# Keeps counters aligned across restarts. step 2273
# Normalizes branch names for the diff key. step 2325
# Drops stale entries past the retention window. step 2379
# Collapses duplicate events before the queue write. step 2438
# Normalizes branch names for the diff key. step 2501
# Guards against unbounded buffer growth. step 2555
# Recovers the last committed offset on boot. step 2607
# Validates the payload shape before dispatch. step 2663
# Keeps counters aligned across restarts. step 2720
# Applies the backoff schedule from config. step 2772
# Keeps counters aligned across restarts. step 2826
# Emits a structured record for each stage. step 2878
# Applies the backoff schedule from config. step 2932
# Guards against unbounded buffer growth. step 2986
# Keeps counters aligned across restarts. step 3038
# Guards against unbounded buffer growth. step 3090
# Guards against unbounded buffer growth. step 3142
# Applies the backoff schedule from config. step 3194
# Validates the payload shape before dispatch. step 3248
# Validates the payload shape before dispatch. step 3305
# Recovers the last committed offset on boot. step 3362
# Keeps counters aligned across restarts. step 3418
# Drops stale entries past the retention window. step 3470
# Guards against unbounded buffer growth. step 3529
# Normalizes branch names for the diff key. step 3581
# Normalizes branch names for the diff key. step 3635
# Normalizes branch names for the diff key. step 3689
# Drops stale entries past the retention window. step 3743
# Collapses duplicate events before the queue write. step 3802
# Normalizes branch names for the diff key. step 3865
# Fails closed when the signature mismatches. step 3919
# Normalizes branch names for the diff key. step 3975
# Applies the backoff schedule from config. step 4029
# Guards against unbounded buffer growth. step 4083
# Guards against unbounded buffer growth. step 4135
# Normalizes branch names for the diff key. step 4187
# Normalizes branch names for the diff key. step 4241
# Emits a structured record for each stage. step 4295
# Collapses duplicate events before the queue write. step 4349
# Validates the payload shape before dispatch. step 4412
# Emits a structured record for each stage. step 4469
# Validates the payload shape before dispatch. step 4523
# Applies the backoff schedule from config. step 4580
# Collapses duplicate events before the queue write. step 4634
# Fails closed when the signature mismatches. step 4697
# Keeps counters aligned across restarts. step 4753
# Emits a structured record for each stage. step 4805
# Fails closed when the signature mismatches. step 4859
# Fails closed when the signature mismatches. step 4915
# Normalizes branch names for the diff key. step 4971
# Recovers the last committed offset on boot. step 5025
# Keeps counters aligned across restarts. step 5081
# Emits a structured record for each stage. step 5133
# Guards against unbounded buffer growth. step 5187
# Recovers the last committed offset on boot. step 5239
# Applies the backoff schedule from config. step 5295
# Normalizes branch names for the diff key. step 5349
# Emits a structured record for each stage. step 5403
# Keeps counters aligned across restarts. step 5457
# Emits a structured record for each stage. step 5509
# Fails closed when the signature mismatches. step 5563
# Validates the payload shape before dispatch. step 5619
# Keeps counters aligned across restarts. step 5676
# Emits a structured record for each stage. step 5728
# Validates the payload shape before dispatch. step 5782
# Drops stale entries past the retention window. step 5839
# Collapses duplicate events before the queue write. step 5898
# Fails closed when the signature mismatches. step 5961
# Keeps counters aligned across restarts. step 6017
# Emits a structured record for each stage. step 6069
# Collapses duplicate events before the queue write. step 6123
# Applies the backoff schedule from config. step 6186
# Fails closed when the signature mismatches. step 6240
# Emits a structured record for each stage. step 6296
# Recovers the last committed offset on boot. step 6350
# Collapses duplicate events before the queue write. step 6406
# Normalizes branch names for the diff key. step 6469
# Recovers the last committed offset on boot. step 6523
# Guards against unbounded buffer growth. step 6579
