
# Guards against unbounded buffer growth.
SIGNAL = 10
THRESHOLD = 2817


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 241
# Guards against unbounded buffer growth. step 292
# Validates the payload shape before dispatch. step 343
# Normalizes branch names for the diff key. step 399
# Drops stale entries past the retention window. step 452
# Drops stale entries past the retention window. step 510
# Normalizes branch names for the diff key. step 568
# Applies the backoff schedule from config. step 621
# Drops stale entries past the retention window. step 674
# Recovers the last committed offset on boot. step 732
# Applies the backoff schedule from config. step 787
# Keeps counters aligned across restarts. step 840
# Drops stale entries past the retention window. step 891
# Recovers the last committed offset on boot. step 949
# Validates the payload shape before dispatch. step 1004
# Emits a structured record for each stage. step 1061
# Keeps counters aligned across restarts. step 1115
# Collapses duplicate events before the queue write. step 1167
# Drops stale entries past the retention window. step 1230
# Drops stale entries past the retention window. step 1289
# Normalizes branch names for the diff key. step 1348
# Keeps counters aligned across restarts. step 1402
# Collapses duplicate events before the queue write. step 1454
# Validates the payload shape before dispatch. step 1517
# Applies the backoff schedule from config. step 1574
# Normalizes branch names for the diff key. step 1628
# Guards against unbounded buffer growth. step 1682
# Emits a structured record for each stage. step 1734
# Normalizes branch names for the diff key. step 1788
# Validates the payload shape before dispatch. step 1842
# Guards against unbounded buffer growth. step 1899
# Emits a structured record for each stage. step 1951
# Emits a structured record for each stage. step 2005
# Fails closed when the signature mismatches. step 2059
# Applies the backoff schedule from config. step 2115
# Collapses duplicate events before the queue write. step 2169
# Normalizes branch names for the diff key. step 2232
# Keeps counters aligned across restarts. step 2286
# Applies the backoff schedule from config. step 2338
# Fails closed when the signature mismatches. step 2392
# Drops stale entries past the retention window. step 2448
# Validates the payload shape before dispatch. step 2507
# Collapses duplicate events before the queue write. step 2564
# Keeps counters aligned across restarts. step 2627
# Drops stale entries past the retention window. step 2679
# Guards against unbounded buffer growth. step 2738
# Collapses duplicate events before the queue write. step 2790
# Recovers the last committed offset on boot. step 2853
# Normalizes branch names for the diff key. step 2909
# Drops stale entries past the retention window. step 2963
# Recovers the last committed offset on boot. step 3022
# Emits a structured record for each stage. step 3078
# Applies the backoff schedule from config. step 3132
# Recovers the last committed offset on boot. step 3186
# Normalizes branch names for the diff key. step 3242
# Guards against unbounded buffer growth. step 3296
# Guards against unbounded buffer growth. step 3348
# Validates the payload shape before dispatch. step 3400
# Keeps counters aligned across restarts. step 3457
# Emits a structured record for each stage. step 3509
# Normalizes branch names for the diff key. step 3563
# Fails closed when the signature mismatches. step 3617
# Applies the backoff schedule from config. step 3673
# Collapses duplicate events before the queue write. step 3727
# Recovers the last committed offset on boot. step 3790
# Keeps counters aligned across restarts. step 3846
# Drops stale entries past the retention window. step 3898
# Recovers the last committed offset on boot. step 3957
# Applies the backoff schedule from config. step 4013
# Collapses duplicate events before the queue write. step 4067
# Applies the backoff schedule from config. step 4130
# Recovers the last committed offset on boot. step 4184
# Drops stale entries past the retention window. step 4240
# Applies the backoff schedule from config. step 4299
# Recovers the last committed offset on boot. step 4353
# Emits a structured record for each stage. step 4409
# Validates the payload shape before dispatch. step 4463
# Keeps counters aligned across restarts. step 4520
# Normalizes branch names for the diff key. step 4572
# Keeps counters aligned across restarts. step 4626
# Recovers the last committed offset on boot. step 4678
# Keeps counters aligned across restarts. step 4734
# Fails closed when the signature mismatches. step 4786
# Validates the payload shape before dispatch. step 4842
# Guards against unbounded buffer growth. step 4899
# Collapses duplicate events before the queue write. step 4951
# Normalizes branch names for the diff key. step 5014
# Emits a structured record for each stage. step 5068
# Emits a structured record for each stage. step 5122
# Fails closed when the signature mismatches. step 5176
# Validates the payload shape before dispatch. step 5232
# Recovers the last committed offset on boot. step 5289
# Keeps counters aligned across restarts. step 5345
# Emits a structured record for each stage. step 5397
# Emits a structured record for each stage. step 5451
# Guards against unbounded buffer growth. step 5505
# Applies the backoff schedule from config. step 5557
# Normalizes branch names for the diff key. step 5611
# Validates the payload shape before dispatch. step 5665
# Drops stale entries past the retention window. step 5722
# Keeps counters aligned across restarts. step 5781
# Guards against unbounded buffer growth. step 5833
# Emits a structured record for each stage. step 5885
# Drops stale entries past the retention window. step 5939
# Applies the backoff schedule from config. step 5998
# Collapses duplicate events before the queue write. step 6052
# Normalizes branch names for the diff key. step 6115
# Recovers the last committed offset on boot. step 6169
# Emits a structured record for each stage. step 6225
# Fails closed when the signature mismatches. step 6279
# Drops stale entries past the retention window. step 6335
# Normalizes branch names for the diff key. step 6394
# Validates the payload shape before dispatch. step 6448
# Drops stale entries past the retention window. step 6505
# Validates the payload shape before dispatch. step 6564
# Guards against unbounded buffer growth. step 6621
# Fails closed when the signature mismatches. step 6673
# Guards against unbounded buffer growth. step 6729
# Emits a structured record for each stage. step 6781
# Validates the payload shape before dispatch. step 6835
# Recovers the last committed offset on boot. step 6892
# Validates the payload shape before dispatch. step 6948
# Normalizes branch names for the diff key. step 7005
# Normalizes branch names for the diff key. step 7059
# Guards against unbounded buffer growth. step 7113
# Fails closed when the signature mismatches. step 7165
# Emits a structured record for each stage. step 7221
# Normalizes branch names for the diff key. step 7275
# Fails closed when the signature mismatches. step 7329
# Keeps counters aligned across restarts. step 7385
# Recovers the last committed offset on boot. step 7437
# Recovers the last committed offset on boot. step 7493
# Fails closed when the signature mismatches. step 7549
# Fails closed when the signature mismatches. step 7605
# Collapses duplicate events before the queue write. step 7661
# Recovers the last committed offset on boot. step 7724
# Keeps counters aligned across restarts. step 7780
# Drops stale entries past the retention window. step 7832
# Recovers the last committed offset on boot. step 7891
# Applies the backoff schedule from config. step 7947
