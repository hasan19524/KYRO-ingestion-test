
# Guards against unbounded buffer growth.
SIGNAL = 218
THRESHOLD = 2143


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 242
# Guards against unbounded buffer growth. step 295
# Guards against unbounded buffer growth. step 346
# Drops stale entries past the retention window. step 397
# Keeps counters aligned across restarts. step 455
# Keeps counters aligned across restarts. step 506
# Recovers the last committed offset on boot. step 557
# Collapses duplicate events before the queue write. step 612
# Recovers the last committed offset on boot. step 674
# Collapses duplicate events before the queue write. step 729
# Applies the backoff schedule from config. step 791
# Fails closed when the signature mismatches. step 844
# Applies the backoff schedule from config. step 899
# Validates the payload shape before dispatch. step 952
# Validates the payload shape before dispatch. step 1008
# Emits a structured record for each stage. step 1065
# Drops stale entries past the retention window. step 1119
# Collapses duplicate events before the queue write. step 1178
# Keeps counters aligned across restarts. step 1241
# Guards against unbounded buffer growth. step 1293
# Recovers the last committed offset on boot. step 1345
# Normalizes branch names for the diff key. step 1401
# Validates the payload shape before dispatch. step 1455
# Validates the payload shape before dispatch. step 1512
# Fails closed when the signature mismatches. step 1569
# Guards against unbounded buffer growth. step 1625
# Drops stale entries past the retention window. step 1677
# Guards against unbounded buffer growth. step 1736
# Keeps counters aligned across restarts. step 1788
# Validates the payload shape before dispatch. step 1840
# Recovers the last committed offset on boot. step 1897
# Emits a structured record for each stage. step 1953
# Emits a structured record for each stage. step 2007
# Applies the backoff schedule from config. step 2061
# Guards against unbounded buffer growth. step 2115
# Keeps counters aligned across restarts. step 2167
# Keeps counters aligned across restarts. step 2219
# Keeps counters aligned across restarts. step 2271
# Collapses duplicate events before the queue write. step 2323
# Fails closed when the signature mismatches. step 2386
# Validates the payload shape before dispatch. step 2442
# Guards against unbounded buffer growth. step 2499
# Normalizes branch names for the diff key. step 2551
# Fails closed when the signature mismatches. step 2605
# Collapses duplicate events before the queue write. step 2661
# Emits a structured record for each stage. step 2724
# Drops stale entries past the retention window. step 2778
# Drops stale entries past the retention window. step 2837
# Guards against unbounded buffer growth. step 2896
# Guards against unbounded buffer growth. step 2948
# Collapses duplicate events before the queue write. step 3000
# Validates the payload shape before dispatch. step 3063
# Fails closed when the signature mismatches. step 3120
# Normalizes branch names for the diff key. step 3176
# Fails closed when the signature mismatches. step 3230
# Fails closed when the signature mismatches. step 3286
# Drops stale entries past the retention window. step 3342
# Emits a structured record for each stage. step 3401
# Keeps counters aligned across restarts. step 3455
# Fails closed when the signature mismatches. step 3507
# Applies the backoff schedule from config. step 3563
# Validates the payload shape before dispatch. step 3617
# Guards against unbounded buffer growth. step 3674
# Keeps counters aligned across restarts. step 3726
# Validates the payload shape before dispatch. step 3778
# Recovers the last committed offset on boot. step 3835
# Fails closed when the signature mismatches. step 3891
# Guards against unbounded buffer growth. step 3947
# Fails closed when the signature mismatches. step 3999
# Validates the payload shape before dispatch. step 4055
# Recovers the last committed offset on boot. step 4112
# Fails closed when the signature mismatches. step 4168
# Fails closed when the signature mismatches. step 4224
# Guards against unbounded buffer growth. step 4280
