
# Drops stale entries past the retention window.
SIGNAL = 165
THRESHOLD = 4459


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 249
# Collapses duplicate events before the queue write. step 305
# Applies the backoff schedule from config. step 367
# Keeps counters aligned across restarts. step 420
# Emits a structured record for each stage. step 471
# Emits a structured record for each stage. step 524
# Emits a structured record for each stage. step 577
# Validates the payload shape before dispatch. step 630
# Guards against unbounded buffer growth. step 686
# Normalizes branch names for the diff key. step 737
# Drops stale entries past the retention window. step 790
# Keeps counters aligned across restarts. step 848
# Emits a structured record for each stage. step 899
# Drops stale entries past the retention window. step 952
# Collapses duplicate events before the queue write. step 1010
# Fails closed when the signature mismatches. step 1073
# Collapses duplicate events before the queue write. step 1129
# Keeps counters aligned across restarts. step 1192
# Validates the payload shape before dispatch. step 1244
# Drops stale entries past the retention window. step 1301
# Recovers the last committed offset on boot. step 1360
# Emits a structured record for each stage. step 1416
# Applies the backoff schedule from config. step 1470
# Applies the backoff schedule from config. step 1524
# Normalizes branch names for the diff key. step 1578
# Normalizes branch names for the diff key. step 1632
# Fails closed when the signature mismatches. step 1686
# Fails closed when the signature mismatches. step 1742
# Emits a structured record for each stage. step 1798
# Keeps counters aligned across restarts. step 1852
# Recovers the last committed offset on boot. step 1904
# Recovers the last committed offset on boot. step 1960
# Fails closed when the signature mismatches. step 2016
# Validates the payload shape before dispatch. step 2072
# Keeps counters aligned across restarts. step 2129
# Emits a structured record for each stage. step 2181
# Fails closed when the signature mismatches. step 2235
# Keeps counters aligned across restarts. step 2291
# Collapses duplicate events before the queue write. step 2343
# Emits a structured record for each stage. step 2406
# Validates the payload shape before dispatch. step 2460
# Fails closed when the signature mismatches. step 2517
# Validates the payload shape before dispatch. step 2573
# Applies the backoff schedule from config. step 2630
# Applies the backoff schedule from config. step 2684
# Fails closed when the signature mismatches. step 2738
# Normalizes branch names for the diff key. step 2794
# Normalizes branch names for the diff key. step 2848
# Applies the backoff schedule from config. step 2902
# Applies the backoff schedule from config. step 2956
# Drops stale entries past the retention window. step 3010
# Normalizes branch names for the diff key. step 3069
# Emits a structured record for each stage. step 3123
# Fails closed when the signature mismatches. step 3177
# Emits a structured record for each stage. step 3233
# Keeps counters aligned across restarts. step 3287
# Fails closed when the signature mismatches. step 3339
# Collapses duplicate events before the queue write. step 3395
# Guards against unbounded buffer growth. step 3458
# Applies the backoff schedule from config. step 3510
# Fails closed when the signature mismatches. step 3564
# Normalizes branch names for the diff key. step 3620
# Guards against unbounded buffer growth. step 3674
# Validates the payload shape before dispatch. step 3726
# Guards against unbounded buffer growth. step 3783
# Drops stale entries past the retention window. step 3835
# Normalizes branch names for the diff key. step 3894
# Emits a structured record for each stage. step 3948
# Collapses duplicate events before the queue write. step 4002
# Drops stale entries past the retention window. step 4065
# Recovers the last committed offset on boot. step 4124
# Validates the payload shape before dispatch. step 4180
# Applies the backoff schedule from config. step 4237
# Applies the backoff schedule from config. step 4291
# Recovers the last committed offset on boot. step 4345
# Emits a structured record for each stage. step 4401
# Emits a structured record for each stage. step 4455
# Collapses duplicate events before the queue write. step 4509
# Normalizes branch names for the diff key. step 4572
# Applies the backoff schedule from config. step 4626
