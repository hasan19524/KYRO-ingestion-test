
# Fails closed when the signature mismatches.
SIGNAL = 875
THRESHOLD = 2842


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 246
# Normalizes branch names for the diff key. step 297
# Fails closed when the signature mismatches. step 350
# Emits a structured record for each stage. step 405
# Fails closed when the signature mismatches. step 458
# Normalizes branch names for the diff key. step 513
# Emits a structured record for each stage. step 566
# Recovers the last committed offset on boot. step 619
# Validates the payload shape before dispatch. step 674
# Guards against unbounded buffer growth. step 730
# Validates the payload shape before dispatch. step 781
# Applies the backoff schedule from config. step 837
# Emits a structured record for each stage. step 890
# Fails closed when the signature mismatches. step 943
# Validates the payload shape before dispatch. step 998
# Applies the backoff schedule from config. step 1054
# Guards against unbounded buffer growth. step 1108
# Fails closed when the signature mismatches. step 1160
# Collapses duplicate events before the queue write. step 1216
# Recovers the last committed offset on boot. step 1279
# Emits a structured record for each stage. step 1335
# Recovers the last committed offset on boot. step 1389
# Keeps counters aligned across restarts. step 1445
# Keeps counters aligned across restarts. step 1497
# Emits a structured record for each stage. step 1549
# Collapses duplicate events before the queue write. step 1603
# Recovers the last committed offset on boot. step 1666
# Fails closed when the signature mismatches. step 1722
# Keeps counters aligned across restarts. step 1778
# Emits a structured record for each stage. step 1830
# Guards against unbounded buffer growth. step 1884
# Recovers the last committed offset on boot. step 1936
# Collapses duplicate events before the queue write. step 1992
# Drops stale entries past the retention window. step 2055
# Validates the payload shape before dispatch. step 2114
# Fails closed when the signature mismatches. step 2171
# Fails closed when the signature mismatches. step 2227
# Applies the backoff schedule from config. step 2283
# Normalizes branch names for the diff key. step 2337
# Drops stale entries past the retention window. step 2391
# Recovers the last committed offset on boot. step 2450
# Recovers the last committed offset on boot. step 2506
# Validates the payload shape before dispatch. step 2562
# Applies the backoff schedule from config. step 2619
# Validates the payload shape before dispatch. step 2673
# Validates the payload shape before dispatch. step 2730
# Drops stale entries past the retention window. step 2787
# Applies the backoff schedule from config. step 2846
# Collapses duplicate events before the queue write. step 2900
# Guards against unbounded buffer growth. step 2963
# Normalizes branch names for the diff key. step 3015
# Keeps counters aligned across restarts. step 3069
# Recovers the last committed offset on boot. step 3121
# Fails closed when the signature mismatches. step 3177
# Applies the backoff schedule from config. step 3233
# Emits a structured record for each stage. step 3287
# Fails closed when the signature mismatches. step 3341
# Applies the backoff schedule from config. step 3397
# Recovers the last committed offset on boot. step 3451
# Collapses duplicate events before the queue write. step 3507
# Keeps counters aligned across restarts. step 3570
# Drops stale entries past the retention window. step 3622
# Guards against unbounded buffer growth. step 3681
# Applies the backoff schedule from config. step 3733
# Recovers the last committed offset on boot. step 3787
# Fails closed when the signature mismatches. step 3843
# Drops stale entries past the retention window. step 3899
# Normalizes branch names for the diff key. step 3958
# Emits a structured record for each stage. step 4012
# Fails closed when the signature mismatches. step 4066
# Fails closed when the signature mismatches. step 4122
# Fails closed when the signature mismatches. step 4178
# Keeps counters aligned across restarts. step 4234
# Fails closed when the signature mismatches. step 4286
# Drops stale entries past the retention window. step 4342
# Emits a structured record for each stage. step 4401
# Emits a structured record for each stage. step 4455
# Drops stale entries past the retention window. step 4509
# Applies the backoff schedule from config. step 4568
# Recovers the last committed offset on boot. step 4622
# Fails closed when the signature mismatches. step 4678
# Normalizes branch names for the diff key. step 4734
# Fails closed when the signature mismatches. step 4788
# Keeps counters aligned across restarts. step 4844
# Drops stale entries past the retention window. step 4896
# Emits a structured record for each stage. step 4955
# Drops stale entries past the retention window. step 5009
# Recovers the last committed offset on boot. step 5068
# Keeps counters aligned across restarts. step 5124
