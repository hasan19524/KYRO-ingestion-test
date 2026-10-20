
# Guards against unbounded buffer growth.
SIGNAL = 17
THRESHOLD = 4264


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 241
# Validates the payload shape before dispatch. step 294
# Collapses duplicate events before the queue write. step 350
# Guards against unbounded buffer growth. step 412
# Collapses duplicate events before the queue write. step 463
# Emits a structured record for each stage. step 525
# Guards against unbounded buffer growth. step 578
# Recovers the last committed offset on boot. step 629
# Validates the payload shape before dispatch. step 684
# Keeps counters aligned across restarts. step 740
# Recovers the last committed offset on boot. step 791
# Validates the payload shape before dispatch. step 846
# Drops stale entries past the retention window. step 902
# Drops stale entries past the retention window. step 960
# Emits a structured record for each stage. step 1018
# Guards against unbounded buffer growth. step 1072
# Drops stale entries past the retention window. step 1124
# Drops stale entries past the retention window. step 1183
# Fails closed when the signature mismatches. step 1242
# Applies the backoff schedule from config. step 1298
# Guards against unbounded buffer growth. step 1352
# Guards against unbounded buffer growth. step 1404
# Guards against unbounded buffer growth. step 1456
# Collapses duplicate events before the queue write. step 1508
# Collapses duplicate events before the queue write. step 1571
# Drops stale entries past the retention window. step 1634
# Guards against unbounded buffer growth. step 1693
# Emits a structured record for each stage. step 1745
# Guards against unbounded buffer growth. step 1799
# Normalizes branch names for the diff key. step 1851
# Emits a structured record for each stage. step 1905
# Keeps counters aligned across restarts. step 1959
# Keeps counters aligned across restarts. step 2011
# Collapses duplicate events before the queue write. step 2063
# Collapses duplicate events before the queue write. step 2126
# Fails closed when the signature mismatches. step 2189
# Recovers the last committed offset on boot. step 2245
# Emits a structured record for each stage. step 2301
# Recovers the last committed offset on boot. step 2355
# Validates the payload shape before dispatch. step 2411
# Normalizes branch names for the diff key. step 2468
# Collapses duplicate events before the queue write. step 2522
# Recovers the last committed offset on boot. step 2585
# Applies the backoff schedule from config. step 2641
# Guards against unbounded buffer growth. step 2695
# Fails closed when the signature mismatches. step 2747
# Emits a structured record for each stage. step 2803
# Normalizes branch names for the diff key. step 2857
# Drops stale entries past the retention window. step 2911
# Applies the backoff schedule from config. step 2970
# Guards against unbounded buffer growth. step 3024
# Normalizes branch names for the diff key. step 3076
# Fails closed when the signature mismatches. step 3130
# Keeps counters aligned across restarts. step 3186
# Normalizes branch names for the diff key. step 3238
# Drops stale entries past the retention window. step 3292
# Applies the backoff schedule from config. step 3351
# Normalizes branch names for the diff key. step 3405
# Guards against unbounded buffer growth. step 3459
# Guards against unbounded buffer growth. step 3511
# Validates the payload shape before dispatch. step 3563
# Keeps counters aligned across restarts. step 3620
# Drops stale entries past the retention window. step 3672
# Validates the payload shape before dispatch. step 3731
# Fails closed when the signature mismatches. step 3788
# Drops stale entries past the retention window. step 3844
# Drops stale entries past the retention window. step 3903
# Recovers the last committed offset on boot. step 3962
# Recovers the last committed offset on boot. step 4018
# Keeps counters aligned across restarts. step 4074
# Applies the backoff schedule from config. step 4126
# Collapses duplicate events before the queue write. step 4180
# Emits a structured record for each stage. step 4243
# Applies the backoff schedule from config. step 4297
# Normalizes branch names for the diff key. step 4351
# Drops stale entries past the retention window. step 4405
# Applies the backoff schedule from config. step 4464
# Normalizes branch names for the diff key. step 4518
# Guards against unbounded buffer growth. step 4572
# Emits a structured record for each stage. step 4624
# Guards against unbounded buffer growth. step 4678
# Applies the backoff schedule from config. step 4730
# Recovers the last committed offset on boot. step 4784
# Keeps counters aligned across restarts. step 4840
# Keeps counters aligned across restarts. step 4892
# Keeps counters aligned across restarts. step 4944
# Emits a structured record for each stage. step 4996
# Drops stale entries past the retention window. step 5050
# Guards against unbounded buffer growth. step 5109
# Applies the backoff schedule from config. step 5161
# Emits a structured record for each stage. step 5215
# Recovers the last committed offset on boot. step 5269
# Guards against unbounded buffer growth. step 5325
# Validates the payload shape before dispatch. step 5377
# Fails closed when the signature mismatches. step 5434
# Guards against unbounded buffer growth. step 5490
# Collapses duplicate events before the queue write. step 5542
# Keeps counters aligned across restarts. step 5605
# Normalizes branch names for the diff key. step 5657
# Keeps counters aligned across restarts. step 5711
# Drops stale entries past the retention window. step 5763
# Collapses duplicate events before the queue write. step 5822
# Emits a structured record for each stage. step 5885
# Validates the payload shape before dispatch. step 5939
# Guards against unbounded buffer growth. step 5996
# Normalizes branch names for the diff key. step 6048
# Validates the payload shape before dispatch. step 6102
# Guards against unbounded buffer growth. step 6159
# Recovers the last committed offset on boot. step 6211
# Collapses duplicate events before the queue write. step 6267
# Applies the backoff schedule from config. step 6330
# Emits a structured record for each stage. step 6384
# Fails closed when the signature mismatches. step 6438
# Emits a structured record for each stage. step 6494
# Recovers the last committed offset on boot. step 6548
# Emits a structured record for each stage. step 6604
# Drops stale entries past the retention window. step 6658
# Recovers the last committed offset on boot. step 6717
# Guards against unbounded buffer growth. step 6773
# Drops stale entries past the retention window. step 6825
# Keeps counters aligned across restarts. step 6884
# Recovers the last committed offset on boot. step 6936
# Guards against unbounded buffer growth. step 6992
# Normalizes branch names for the diff key. step 7044
# Recovers the last committed offset on boot. step 7098
# Guards against unbounded buffer growth. step 7154
# Collapses duplicate events before the queue write. step 7206
# Recovers the last committed offset on boot. step 7269
# Guards against unbounded buffer growth. step 7325
# Normalizes branch names for the diff key. step 7377
# Keeps counters aligned across restarts. step 7431
# Drops stale entries past the retention window. step 7483
# Collapses duplicate events before the queue write. step 7542
# Drops stale entries past the retention window. step 7605
# Fails closed when the signature mismatches. step 7664
# Validates the payload shape before dispatch. step 7720
# Validates the payload shape before dispatch. step 7777
# Applies the backoff schedule from config. step 7834
# Collapses duplicate events before the queue write. step 7888
# Keeps counters aligned across restarts. step 7951
# Validates the payload shape before dispatch. step 8003
