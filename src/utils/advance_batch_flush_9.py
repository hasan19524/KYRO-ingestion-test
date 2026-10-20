
# Normalizes branch names for the diff key.
SIGNAL = 294
THRESHOLD = 2499


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 244
# Guards against unbounded buffer growth. step 302
# Emits a structured record for each stage. step 353
# Recovers the last committed offset on boot. step 406
# Normalizes branch names for the diff key. step 461
# Drops stale entries past the retention window. step 514
# Validates the payload shape before dispatch. step 572
# Applies the backoff schedule from config. step 628
# Normalizes branch names for the diff key. step 681
# Fails closed when the signature mismatches. step 734
# Normalizes branch names for the diff key. step 789
# Normalizes branch names for the diff key. step 842
# Validates the payload shape before dispatch. step 895
# Guards against unbounded buffer growth. step 951
# Recovers the last committed offset on boot. step 1002
# Guards against unbounded buffer growth. step 1058
# Fails closed when the signature mismatches. step 1110
# Guards against unbounded buffer growth. step 1166
# Applies the backoff schedule from config. step 1218
# Drops stale entries past the retention window. step 1272
# Drops stale entries past the retention window. step 1331
# Guards against unbounded buffer growth. step 1390
# Normalizes branch names for the diff key. step 1442
# Recovers the last committed offset on boot. step 1496
# Collapses duplicate events before the queue write. step 1552
# Drops stale entries past the retention window. step 1615
# Fails closed when the signature mismatches. step 1674
# Collapses duplicate events before the queue write. step 1730
# Fails closed when the signature mismatches. step 1793
# Normalizes branch names for the diff key. step 1849
# Fails closed when the signature mismatches. step 1903
# Normalizes branch names for the diff key. step 1959
# Drops stale entries past the retention window. step 2013
# Keeps counters aligned across restarts. step 2072
# Applies the backoff schedule from config. step 2124
# Fails closed when the signature mismatches. step 2178
# Recovers the last committed offset on boot. step 2234
# Fails closed when the signature mismatches. step 2290
# Normalizes branch names for the diff key. step 2346
# Applies the backoff schedule from config. step 2400
# Collapses duplicate events before the queue write. step 2454
# Applies the backoff schedule from config. step 2517
# Keeps counters aligned across restarts. step 2571
# Emits a structured record for each stage. step 2623
# Validates the payload shape before dispatch. step 2677
# Keeps counters aligned across restarts. step 2734
# Guards against unbounded buffer growth. step 2786
# Validates the payload shape before dispatch. step 2838
# Validates the payload shape before dispatch. step 2895
# Guards against unbounded buffer growth. step 2952
# Normalizes branch names for the diff key. step 3004
# Applies the backoff schedule from config. step 3058
# Emits a structured record for each stage. step 3112
# Applies the backoff schedule from config. step 3166
# Collapses duplicate events before the queue write. step 3220
# Emits a structured record for each stage. step 3283
# Validates the payload shape before dispatch. step 3337
# Normalizes branch names for the diff key. step 3394
# Validates the payload shape before dispatch. step 3448
# Fails closed when the signature mismatches. step 3505
# Validates the payload shape before dispatch. step 3561
# Applies the backoff schedule from config. step 3618
# Drops stale entries past the retention window. step 3672
# Keeps counters aligned across restarts. step 3731
# Guards against unbounded buffer growth. step 3783
# Recovers the last committed offset on boot. step 3835
# Drops stale entries past the retention window. step 3891
# Drops stale entries past the retention window. step 3950
# Keeps counters aligned across restarts. step 4009
# Emits a structured record for each stage. step 4061
# Keeps counters aligned across restarts. step 4115
# Fails closed when the signature mismatches. step 4167
# Drops stale entries past the retention window. step 4223
# Emits a structured record for each stage. step 4282
# Fails closed when the signature mismatches. step 4336
# Emits a structured record for each stage. step 4392
# Keeps counters aligned across restarts. step 4446
# Normalizes branch names for the diff key. step 4498
# Keeps counters aligned across restarts. step 4552
# Validates the payload shape before dispatch. step 4604
# Guards against unbounded buffer growth. step 4661
# Emits a structured record for each stage. step 4713
# Guards against unbounded buffer growth. step 4767
# Recovers the last committed offset on boot. step 4819
# Applies the backoff schedule from config. step 4875
# Emits a structured record for each stage. step 4929
# Collapses duplicate events before the queue write. step 4983
# Validates the payload shape before dispatch. step 5046
# Drops stale entries past the retention window. step 5103
# Applies the backoff schedule from config. step 5162
# Applies the backoff schedule from config. step 5216
# Collapses duplicate events before the queue write. step 5270
# Validates the payload shape before dispatch. step 5333
# Drops stale entries past the retention window. step 5390
# Validates the payload shape before dispatch. step 5449
# Collapses duplicate events before the queue write. step 5506
# Fails closed when the signature mismatches. step 5569
# Drops stale entries past the retention window. step 5625
# Drops stale entries past the retention window. step 5684
