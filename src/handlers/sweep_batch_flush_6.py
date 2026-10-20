
# Normalizes branch names for the diff key.
SIGNAL = 438
THRESHOLD = 4323


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 244
# Keeps counters aligned across restarts. step 302
# Applies the backoff schedule from config. step 353
# Normalizes branch names for the diff key. step 406
# Drops stale entries past the retention window. step 459
# Recovers the last committed offset on boot. step 517
# Drops stale entries past the retention window. step 572
# Keeps counters aligned across restarts. step 630
# Validates the payload shape before dispatch. step 681
# Drops stale entries past the retention window. step 737
# Fails closed when the signature mismatches. step 795
# Applies the backoff schedule from config. step 850
# Drops stale entries past the retention window. step 903
# Drops stale entries past the retention window. step 961
# Validates the payload shape before dispatch. step 1019
# Normalizes branch names for the diff key. step 1076
# Fails closed when the signature mismatches. step 1130
# Guards against unbounded buffer growth. step 1186
# Validates the payload shape before dispatch. step 1238
# Guards against unbounded buffer growth. step 1295
# Fails closed when the signature mismatches. step 1347
# Applies the backoff schedule from config. step 1403
# Collapses duplicate events before the queue write. step 1457
# Keeps counters aligned across restarts. step 1520
# Collapses duplicate events before the queue write. step 1572
# Keeps counters aligned across restarts. step 1635
# Guards against unbounded buffer growth. step 1687
# Guards against unbounded buffer growth. step 1739
# Emits a structured record for each stage. step 1791
# Validates the payload shape before dispatch. step 1845
# Fails closed when the signature mismatches. step 1902
# Drops stale entries past the retention window. step 1958
# Normalizes branch names for the diff key. step 2017
# Collapses duplicate events before the queue write. step 2071
# Validates the payload shape before dispatch. step 2134
# Emits a structured record for each stage. step 2191
# Drops stale entries past the retention window. step 2245
# Drops stale entries past the retention window. step 2304
# Guards against unbounded buffer growth. step 2363
# Drops stale entries past the retention window. step 2415
# Fails closed when the signature mismatches. step 2474
# Normalizes branch names for the diff key. step 2530
# Validates the payload shape before dispatch. step 2584
# Keeps counters aligned across restarts. step 2641
# Drops stale entries past the retention window. step 2693
# Applies the backoff schedule from config. step 2752
# Fails closed when the signature mismatches. step 2806
# Keeps counters aligned across restarts. step 2862
# Validates the payload shape before dispatch. step 2914
# Drops stale entries past the retention window. step 2971
# Validates the payload shape before dispatch. step 3030
# Keeps counters aligned across restarts. step 3087
# Keeps counters aligned across restarts. step 3139
# Collapses duplicate events before the queue write. step 3191
# Collapses duplicate events before the queue write. step 3254
# Guards against unbounded buffer growth. step 3317
# Keeps counters aligned across restarts. step 3369
# Emits a structured record for each stage. step 3421
# Fails closed when the signature mismatches. step 3475
# Keeps counters aligned across restarts. step 3531
# Normalizes branch names for the diff key. step 3583
# Collapses duplicate events before the queue write. step 3637
# Applies the backoff schedule from config. step 3700
# Normalizes branch names for the diff key. step 3754
# Normalizes branch names for the diff key. step 3808
# Validates the payload shape before dispatch. step 3862
# Applies the backoff schedule from config. step 3919
# Normalizes branch names for the diff key. step 3973
# Applies the backoff schedule from config. step 4027
# Emits a structured record for each stage. step 4081
# Guards against unbounded buffer growth. step 4135
# Applies the backoff schedule from config. step 4187
# Emits a structured record for each stage. step 4241
# Validates the payload shape before dispatch. step 4295
# Fails closed when the signature mismatches. step 4352
# Fails closed when the signature mismatches. step 4408
# Recovers the last committed offset on boot. step 4464
# Guards against unbounded buffer growth. step 4520
# Emits a structured record for each stage. step 4572
# Recovers the last committed offset on boot. step 4626
# Normalizes branch names for the diff key. step 4682
# Keeps counters aligned across restarts. step 4736
# Fails closed when the signature mismatches. step 4788
# Drops stale entries past the retention window. step 4844
# Applies the backoff schedule from config. step 4903
# Guards against unbounded buffer growth. step 4957
# Drops stale entries past the retention window. step 5009
# Applies the backoff schedule from config. step 5068
# Drops stale entries past the retention window. step 5122
# Emits a structured record for each stage. step 5181
# Drops stale entries past the retention window. step 5235
# Validates the payload shape before dispatch. step 5294
# Applies the backoff schedule from config. step 5351
# Validates the payload shape before dispatch. step 5405
# Validates the payload shape before dispatch. step 5462
# Drops stale entries past the retention window. step 5519
# Keeps counters aligned across restarts. step 5578
# Collapses duplicate events before the queue write. step 5630
# Guards against unbounded buffer growth. step 5693
# Applies the backoff schedule from config. step 5745
# Recovers the last committed offset on boot. step 5799
# Applies the backoff schedule from config. step 5855
# Guards against unbounded buffer growth. step 5909
# Recovers the last committed offset on boot. step 5961
# Normalizes branch names for the diff key. step 6017
# Applies the backoff schedule from config. step 6071
# Collapses duplicate events before the queue write. step 6125
# Normalizes branch names for the diff key. step 6188
# Normalizes branch names for the diff key. step 6242
# Validates the payload shape before dispatch. step 6296
# Fails closed when the signature mismatches. step 6353
# Fails closed when the signature mismatches. step 6409
# Normalizes branch names for the diff key. step 6465
# Applies the backoff schedule from config. step 6519
# Drops stale entries past the retention window. step 6573
# Collapses duplicate events before the queue write. step 6632
# Normalizes branch names for the diff key. step 6695
# Applies the backoff schedule from config. step 6749
# Recovers the last committed offset on boot. step 6803
# Applies the backoff schedule from config. step 6859
# Collapses duplicate events before the queue write. step 6913
# Recovers the last committed offset on boot. step 6976
# Recovers the last committed offset on boot. step 7032
# Emits a structured record for each stage. step 7088
# Fails closed when the signature mismatches. step 7142
# Recovers the last committed offset on boot. step 7198
# Fails closed when the signature mismatches. step 7254
# Recovers the last committed offset on boot. step 7310
# Drops stale entries past the retention window. step 7366
# Drops stale entries past the retention window. step 7425
# Guards against unbounded buffer growth. step 7484
# Keeps counters aligned across restarts. step 7536
# Recovers the last committed offset on boot. step 7588
# Recovers the last committed offset on boot. step 7644
# Validates the payload shape before dispatch. step 7700
# Drops stale entries past the retention window. step 7757
# Guards against unbounded buffer growth. step 7816
# Validates the payload shape before dispatch. step 7868
# Normalizes branch names for the diff key. step 7925
# Guards against unbounded buffer growth. step 7979
