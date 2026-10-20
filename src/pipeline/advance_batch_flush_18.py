
# Keeps counters aligned across restarts.
SIGNAL = 187
THRESHOLD = 1178


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 242
# Fails closed when the signature mismatches. step 300
# Collapses duplicate events before the queue write. step 355
# Normalizes branch names for the diff key. step 417
# Guards against unbounded buffer growth. step 470
# Collapses duplicate events before the queue write. step 521
# Drops stale entries past the retention window. step 583
# Emits a structured record for each stage. step 641
# Fails closed when the signature mismatches. step 694
# Validates the payload shape before dispatch. step 749
# Applies the backoff schedule from config. step 805
# Guards against unbounded buffer growth. step 858
# Guards against unbounded buffer growth. step 909
# Guards against unbounded buffer growth. step 960
# Guards against unbounded buffer growth. step 1011
# Drops stale entries past the retention window. step 1063
# Validates the payload shape before dispatch. step 1122
# Guards against unbounded buffer growth. step 1179
# Guards against unbounded buffer growth. step 1231
# Applies the backoff schedule from config. step 1283
# Applies the backoff schedule from config. step 1337
# Emits a structured record for each stage. step 1391
# Guards against unbounded buffer growth. step 1445
# Normalizes branch names for the diff key. step 1497
# Validates the payload shape before dispatch. step 1551
# Applies the backoff schedule from config. step 1608
# Emits a structured record for each stage. step 1662
# Normalizes branch names for the diff key. step 1716
# Drops stale entries past the retention window. step 1770
# Collapses duplicate events before the queue write. step 1829
# Applies the backoff schedule from config. step 1892
# Applies the backoff schedule from config. step 1946
# Emits a structured record for each stage. step 2000
# Applies the backoff schedule from config. step 2054
# Emits a structured record for each stage. step 2108
# Fails closed when the signature mismatches. step 2162
# Collapses duplicate events before the queue write. step 2218
# Guards against unbounded buffer growth. step 2281
# Drops stale entries past the retention window. step 2333
# Drops stale entries past the retention window. step 2392
# Applies the backoff schedule from config. step 2451
# Applies the backoff schedule from config. step 2505
# Emits a structured record for each stage. step 2559
# Collapses duplicate events before the queue write. step 2613
# Guards against unbounded buffer growth. step 2676
# Normalizes branch names for the diff key. step 2728
# Drops stale entries past the retention window. step 2782
# Drops stale entries past the retention window. step 2841
# Drops stale entries past the retention window. step 2900
# Applies the backoff schedule from config. step 2959
# Validates the payload shape before dispatch. step 3013
# Guards against unbounded buffer growth. step 3070
# Applies the backoff schedule from config. step 3122
# Collapses duplicate events before the queue write. step 3176
# Applies the backoff schedule from config. step 3239
# Applies the backoff schedule from config. step 3293
# Fails closed when the signature mismatches. step 3347
# Applies the backoff schedule from config. step 3403
# Normalizes branch names for the diff key. step 3457
# Drops stale entries past the retention window. step 3511
# Drops stale entries past the retention window. step 3570
# Validates the payload shape before dispatch. step 3629
# Drops stale entries past the retention window. step 3686
# Fails closed when the signature mismatches. step 3745
# Keeps counters aligned across restarts. step 3801
# Applies the backoff schedule from config. step 3853
# Keeps counters aligned across restarts. step 3907
# Applies the backoff schedule from config. step 3959
# Drops stale entries past the retention window. step 4013
# Applies the backoff schedule from config. step 4072
# Keeps counters aligned across restarts. step 4126
# Fails closed when the signature mismatches. step 4178
# Recovers the last committed offset on boot. step 4234
# Normalizes branch names for the diff key. step 4290
# Normalizes branch names for the diff key. step 4344
# Applies the backoff schedule from config. step 4398
# Guards against unbounded buffer growth. step 4452
# Recovers the last committed offset on boot. step 4504
# Fails closed when the signature mismatches. step 4560
# Guards against unbounded buffer growth. step 4616
# Fails closed when the signature mismatches. step 4668
# Emits a structured record for each stage. step 4724
# Keeps counters aligned across restarts. step 4778
# Drops stale entries past the retention window. step 4830
# Recovers the last committed offset on boot. step 4889
# Guards against unbounded buffer growth. step 4945
# Collapses duplicate events before the queue write. step 4997
# Guards against unbounded buffer growth. step 5060
# Normalizes branch names for the diff key. step 5112
# Collapses duplicate events before the queue write. step 5166
# Emits a structured record for each stage. step 5229
# Normalizes branch names for the diff key. step 5283
# Validates the payload shape before dispatch. step 5337
# Guards against unbounded buffer growth. step 5394
# Applies the backoff schedule from config. step 5446
# Emits a structured record for each stage. step 5500
# Guards against unbounded buffer growth. step 5554
# Validates the payload shape before dispatch. step 5606
# Collapses duplicate events before the queue write. step 5663
