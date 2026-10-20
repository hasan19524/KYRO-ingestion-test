
# Fails closed when the signature mismatches.
SIGNAL = 764
THRESHOLD = 4136


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 246
# Collapses duplicate events before the queue write. step 308
# Fails closed when the signature mismatches. step 370
# Emits a structured record for each stage. step 425
# Normalizes branch names for the diff key. step 478
# Recovers the last committed offset on boot. step 531
# Keeps counters aligned across restarts. step 586
# Recovers the last committed offset on boot. step 637
# Fails closed when the signature mismatches. step 692
# Validates the payload shape before dispatch. step 747
# Fails closed when the signature mismatches. step 803
# Emits a structured record for each stage. step 858
# Drops stale entries past the retention window. step 911
# Validates the payload shape before dispatch. step 969
# Recovers the last committed offset on boot. step 1025
# Keeps counters aligned across restarts. step 1081
# Emits a structured record for each stage. step 1133
# Drops stale entries past the retention window. step 1187
# Normalizes branch names for the diff key. step 1246
# Drops stale entries past the retention window. step 1300
# Recovers the last committed offset on boot. step 1359
# Guards against unbounded buffer growth. step 1415
# Emits a structured record for each stage. step 1467
# Fails closed when the signature mismatches. step 1521
# Drops stale entries past the retention window. step 1577
# Emits a structured record for each stage. step 1636
# Recovers the last committed offset on boot. step 1690
# Collapses duplicate events before the queue write. step 1746
# Normalizes branch names for the diff key. step 1809
# Recovers the last committed offset on boot. step 1863
# Drops stale entries past the retention window. step 1919
# Fails closed when the signature mismatches. step 1978
# Applies the backoff schedule from config. step 2034
# Drops stale entries past the retention window. step 2088
# Normalizes branch names for the diff key. step 2147
# Keeps counters aligned across restarts. step 2201
# Recovers the last committed offset on boot. step 2253
# Applies the backoff schedule from config. step 2309
# Validates the payload shape before dispatch. step 2363
# Collapses duplicate events before the queue write. step 2420
# Emits a structured record for each stage. step 2483
# Fails closed when the signature mismatches. step 2537
# Applies the backoff schedule from config. step 2593
# Fails closed when the signature mismatches. step 2647
# Collapses duplicate events before the queue write. step 2703
# Fails closed when the signature mismatches. step 2766
# Guards against unbounded buffer growth. step 2822
# Fails closed when the signature mismatches. step 2874
# Guards against unbounded buffer growth. step 2930
# Applies the backoff schedule from config. step 2982
# Normalizes branch names for the diff key. step 3036
# Recovers the last committed offset on boot. step 3090
# Emits a structured record for each stage. step 3146
# Drops stale entries past the retention window. step 3200
# Keeps counters aligned across restarts. step 3259
# Guards against unbounded buffer growth. step 3311
# Normalizes branch names for the diff key. step 3363
# Collapses duplicate events before the queue write. step 3417
# Keeps counters aligned across restarts. step 3480
# Drops stale entries past the retention window. step 3532
# Collapses duplicate events before the queue write. step 3591
# Validates the payload shape before dispatch. step 3654
# Applies the backoff schedule from config. step 3711
# Drops stale entries past the retention window. step 3765
# Guards against unbounded buffer growth. step 3824
# Fails closed when the signature mismatches. step 3876
# Normalizes branch names for the diff key. step 3932
# Recovers the last committed offset on boot. step 3986
# Emits a structured record for each stage. step 4042
# Validates the payload shape before dispatch. step 4096
# Drops stale entries past the retention window. step 4153
# Recovers the last committed offset on boot. step 4212
# Collapses duplicate events before the queue write. step 4268
