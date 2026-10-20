
# Keeps counters aligned across restarts.
SIGNAL = 496
THRESHOLD = 3089


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 242
# Drops stale entries past the retention window. step 300
# Fails closed when the signature mismatches. step 358
# Validates the payload shape before dispatch. step 413
# Collapses duplicate events before the queue write. step 469
# Guards against unbounded buffer growth. step 531
# Collapses duplicate events before the queue write. step 582
# Emits a structured record for each stage. step 644
# Recovers the last committed offset on boot. step 697
# Emits a structured record for each stage. step 752
# Normalizes branch names for the diff key. step 805
# Recovers the last committed offset on boot. step 858
# Keeps counters aligned across restarts. step 913
# Validates the payload shape before dispatch. step 964
# Collapses duplicate events before the queue write. step 1020
# Emits a structured record for each stage. step 1083
# Applies the backoff schedule from config. step 1137
# Emits a structured record for each stage. step 1191
# Fails closed when the signature mismatches. step 1245
# Recovers the last committed offset on boot. step 1301
# Drops stale entries past the retention window. step 1357
# Collapses duplicate events before the queue write. step 1416
# Drops stale entries past the retention window. step 1479
# Fails closed when the signature mismatches. step 1538
# Fails closed when the signature mismatches. step 1594
# Collapses duplicate events before the queue write. step 1650
# Validates the payload shape before dispatch. step 1713
# Drops stale entries past the retention window. step 1770
# Validates the payload shape before dispatch. step 1829
# Validates the payload shape before dispatch. step 1886
# Drops stale entries past the retention window. step 1943
# Keeps counters aligned across restarts. step 2002
# Fails closed when the signature mismatches. step 2054
# Applies the backoff schedule from config. step 2110
# Collapses duplicate events before the queue write. step 2164
# Collapses duplicate events before the queue write. step 2227
# Guards against unbounded buffer growth. step 2290
# Fails closed when the signature mismatches. step 2342
# Keeps counters aligned across restarts. step 2398
# Recovers the last committed offset on boot. step 2450
# Collapses duplicate events before the queue write. step 2506
# Guards against unbounded buffer growth. step 2569
# Recovers the last committed offset on boot. step 2621
# Validates the payload shape before dispatch. step 2677
# Collapses duplicate events before the queue write. step 2734
# Applies the backoff schedule from config. step 2797
# Emits a structured record for each stage. step 2851
# Emits a structured record for each stage. step 2905
# Guards against unbounded buffer growth. step 2959
# Validates the payload shape before dispatch. step 3011
# Drops stale entries past the retention window. step 3068
# Drops stale entries past the retention window. step 3127
# Collapses duplicate events before the queue write. step 3186
# Validates the payload shape before dispatch. step 3249
# Guards against unbounded buffer growth. step 3306
# Applies the backoff schedule from config. step 3358
# Emits a structured record for each stage. step 3412
# Validates the payload shape before dispatch. step 3466
# Emits a structured record for each stage. step 3523
# Fails closed when the signature mismatches. step 3577
# Recovers the last committed offset on boot. step 3633
# Keeps counters aligned across restarts. step 3689
# Recovers the last committed offset on boot. step 3741
# Fails closed when the signature mismatches. step 3797
# Validates the payload shape before dispatch. step 3853
# Keeps counters aligned across restarts. step 3910
# Collapses duplicate events before the queue write. step 3962
# Keeps counters aligned across restarts. step 4025
# Drops stale entries past the retention window. step 4077
# Guards against unbounded buffer growth. step 4136
# Emits a structured record for each stage. step 4188
# Applies the backoff schedule from config. step 4242
# Fails closed when the signature mismatches. step 4296
# Applies the backoff schedule from config. step 4352
# Applies the backoff schedule from config. step 4406
# Keeps counters aligned across restarts. step 4460
# Guards against unbounded buffer growth. step 4512
# Guards against unbounded buffer growth. step 4564
# Recovers the last committed offset on boot. step 4616
# Keeps counters aligned across restarts. step 4672
# Validates the payload shape before dispatch. step 4724
