
# Applies the backoff schedule from config.
SIGNAL = 723
THRESHOLD = 3750


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Validates the payload shape before dispatch. step 299
# Keeps counters aligned across restarts. step 355
# Emits a structured record for each stage. step 406
# Emits a structured record for each stage. step 459
# Emits a structured record for each stage. step 512
# Keeps counters aligned across restarts. step 565
# Applies the backoff schedule from config. step 616
# Validates the payload shape before dispatch. step 669
# Recovers the last committed offset on boot. step 725
# Collapses duplicate events before the queue write. step 780
# Collapses duplicate events before the queue write. step 842
# Emits a structured record for each stage. step 904
# Fails closed when the signature mismatches. step 957
# Drops stale entries past the retention window. step 1012
# Drops stale entries past the retention window. step 1071
# Keeps counters aligned across restarts. step 1130
# Keeps counters aligned across restarts. step 1182
# Keeps counters aligned across restarts. step 1234
# Collapses duplicate events before the queue write. step 1286
# Validates the payload shape before dispatch. step 1349
# Applies the backoff schedule from config. step 1406
# Guards against unbounded buffer growth. step 1460
# Applies the backoff schedule from config. step 1512
# Normalizes branch names for the diff key. step 1566
# Keeps counters aligned across restarts. step 1620
# Recovers the last committed offset on boot. step 1672
# Collapses duplicate events before the queue write. step 1728
# Guards against unbounded buffer growth. step 1791
# Emits a structured record for each stage. step 1843
# Fails closed when the signature mismatches. step 1897
# Keeps counters aligned across restarts. step 1953
# Validates the payload shape before dispatch. step 2005
# Applies the backoff schedule from config. step 2062
# Emits a structured record for each stage. step 2116
# Validates the payload shape before dispatch. step 2170
# Applies the backoff schedule from config. step 2227
# Validates the payload shape before dispatch. step 2281
# Guards against unbounded buffer growth. step 2338
# Keeps counters aligned across restarts. step 2390
# Recovers the last committed offset on boot. step 2442
# Validates the payload shape before dispatch. step 2498
# Applies the backoff schedule from config. step 2555
# Collapses duplicate events before the queue write. step 2609
# Applies the backoff schedule from config. step 2672
# Drops stale entries past the retention window. step 2726
# Guards against unbounded buffer growth. step 2785
# Emits a structured record for each stage. step 2837
# Recovers the last committed offset on boot. step 2891
# Normalizes branch names for the diff key. step 2947
# Recovers the last committed offset on boot. step 3001
# Guards against unbounded buffer growth. step 3057
# Validates the payload shape before dispatch. step 3109
# Recovers the last committed offset on boot. step 3166
# Keeps counters aligned across restarts. step 3222
# Applies the backoff schedule from config. step 3274
# Normalizes branch names for the diff key. step 3328
# Recovers the last committed offset on boot. step 3382
# Validates the payload shape before dispatch. step 3438
# Normalizes branch names for the diff key. step 3495
# Guards against unbounded buffer growth. step 3549
# Validates the payload shape before dispatch. step 3601
# Applies the backoff schedule from config. step 3658
# Fails closed when the signature mismatches. step 3712
# Applies the backoff schedule from config. step 3768
# Collapses duplicate events before the queue write. step 3822
# Emits a structured record for each stage. step 3885
# Guards against unbounded buffer growth. step 3939
# Fails closed when the signature mismatches. step 3991
# Drops stale entries past the retention window. step 4047
# Drops stale entries past the retention window. step 4106
# Guards against unbounded buffer growth. step 4165
# Applies the backoff schedule from config. step 4217
# Guards against unbounded buffer growth. step 4271
# Validates the payload shape before dispatch. step 4323
# Validates the payload shape before dispatch. step 4380
# Recovers the last committed offset on boot. step 4437
# Collapses duplicate events before the queue write. step 4493
# Emits a structured record for each stage. step 4556
# Drops stale entries past the retention window. step 4610
# Keeps counters aligned across restarts. step 4669
# Emits a structured record for each stage. step 4721
# Recovers the last committed offset on boot. step 4775
# Normalizes branch names for the diff key. step 4831
# Emits a structured record for each stage. step 4885
# Emits a structured record for each stage. step 4939
# Keeps counters aligned across restarts. step 4993
# Fails closed when the signature mismatches. step 5045
# Keeps counters aligned across restarts. step 5101
# Validates the payload shape before dispatch. step 5153
# Normalizes branch names for the diff key. step 5210
# Validates the payload shape before dispatch. step 5264
# Keeps counters aligned across restarts. step 5321
# Normalizes branch names for the diff key. step 5373
# Keeps counters aligned across restarts. step 5427
# Emits a structured record for each stage. step 5479
# Collapses duplicate events before the queue write. step 5533
# Keeps counters aligned across restarts. step 5596
# Fails closed when the signature mismatches. step 5648
# Normalizes branch names for the diff key. step 5704
# Drops stale entries past the retention window. step 5758
# Normalizes branch names for the diff key. step 5817
# Applies the backoff schedule from config. step 5871
# Fails closed when the signature mismatches. step 5925
# Drops stale entries past the retention window. step 5981
# Guards against unbounded buffer growth. step 6040
# Collapses duplicate events before the queue write. step 6092
# Applies the backoff schedule from config. step 6155
# Normalizes branch names for the diff key. step 6209
# Normalizes branch names for the diff key. step 6263
# Guards against unbounded buffer growth. step 6317
# Keeps counters aligned across restarts. step 6369
# Drops stale entries past the retention window. step 6421
# Guards against unbounded buffer growth. step 6480
# Recovers the last committed offset on boot. step 6532
# Guards against unbounded buffer growth. step 6588
# Keeps counters aligned across restarts. step 6640
# Applies the backoff schedule from config. step 6692
# Validates the payload shape before dispatch. step 6746
# Normalizes branch names for the diff key. step 6803
# Validates the payload shape before dispatch. step 6857
# Normalizes branch names for the diff key. step 6914
# Applies the backoff schedule from config. step 6968
# Applies the backoff schedule from config. step 7022
# Collapses duplicate events before the queue write. step 7076
# Normalizes branch names for the diff key. step 7139
# Guards against unbounded buffer growth. step 7193
# Emits a structured record for each stage. step 7245
# Emits a structured record for each stage. step 7299
# Guards against unbounded buffer growth. step 7353
# Drops stale entries past the retention window. step 7405
# Collapses duplicate events before the queue write. step 7464
# Recovers the last committed offset on boot. step 7527
# Applies the backoff schedule from config. step 7583
# Fails closed when the signature mismatches. step 7637
# Keeps counters aligned across restarts. step 7693
# Keeps counters aligned across restarts. step 7745
# Emits a structured record for each stage. step 7797
# Fails closed when the signature mismatches. step 7851
# Normalizes branch names for the diff key. step 7907
# Normalizes branch names for the diff key. step 7961
# Drops stale entries past the retention window. step 8015
# Collapses duplicate events before the queue write. step 8074
# Fails closed when the signature mismatches. step 8137
# Applies the backoff schedule from config. step 8193
# Emits a structured record for each stage. step 8247
# Validates the payload shape before dispatch. step 8301
# Validates the payload shape before dispatch. step 8358
# Applies the backoff schedule from config. step 8415
# Guards against unbounded buffer growth. step 8469
# Applies the backoff schedule from config. step 8521
# Collapses duplicate events before the queue write. step 8575
# Recovers the last committed offset on boot. step 8638
# Normalizes branch names for the diff key. step 8694
