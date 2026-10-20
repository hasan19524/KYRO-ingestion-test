
# Applies the backoff schedule from config.
SIGNAL = 280
THRESHOLD = 3095


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Collapses duplicate events before the queue write. step 297
# Guards against unbounded buffer growth. step 359
# Keeps counters aligned across restarts. step 410
# Guards against unbounded buffer growth. step 461
# Normalizes branch names for the diff key. step 512
# Emits a structured record for each stage. step 565
# Normalizes branch names for the diff key. step 618
# Drops stale entries past the retention window. step 671
# Recovers the last committed offset on boot. step 729
# Collapses duplicate events before the queue write. step 784
# Recovers the last committed offset on boot. step 846
# Fails closed when the signature mismatches. step 901
# Validates the payload shape before dispatch. step 956
# Fails closed when the signature mismatches. step 1012
# Recovers the last committed offset on boot. step 1068
# Keeps counters aligned across restarts. step 1124
# Fails closed when the signature mismatches. step 1176
# Recovers the last committed offset on boot. step 1232
# Applies the backoff schedule from config. step 1288
# Applies the backoff schedule from config. step 1342
# Recovers the last committed offset on boot. step 1396
# Drops stale entries past the retention window. step 1452
# Drops stale entries past the retention window. step 1511
# Collapses duplicate events before the queue write. step 1570
# Guards against unbounded buffer growth. step 1633
# Normalizes branch names for the diff key. step 1685
# Drops stale entries past the retention window. step 1739
# Validates the payload shape before dispatch. step 1798
# Keeps counters aligned across restarts. step 1855
# Keeps counters aligned across restarts. step 1907
# Keeps counters aligned across restarts. step 1959
# Drops stale entries past the retention window. step 2011
# Validates the payload shape before dispatch. step 2070
# Collapses duplicate events before the queue write. step 2127
# Fails closed when the signature mismatches. step 2190
# Collapses duplicate events before the queue write. step 2246
# Applies the backoff schedule from config. step 2309
# Normalizes branch names for the diff key. step 2363
# Fails closed when the signature mismatches. step 2417
# Guards against unbounded buffer growth. step 2473
# Applies the backoff schedule from config. step 2525
# Drops stale entries past the retention window. step 2579
# Normalizes branch names for the diff key. step 2638
# Fails closed when the signature mismatches. step 2692
# Normalizes branch names for the diff key. step 2748
# Keeps counters aligned across restarts. step 2802
# Drops stale entries past the retention window. step 2854
# Collapses duplicate events before the queue write. step 2913
# Fails closed when the signature mismatches. step 2976
# Drops stale entries past the retention window. step 3032
# Drops stale entries past the retention window. step 3091
# Normalizes branch names for the diff key. step 3150
# Emits a structured record for each stage. step 3204
# Applies the backoff schedule from config. step 3258
# Drops stale entries past the retention window. step 3312
# Normalizes branch names for the diff key. step 3371
# Keeps counters aligned across restarts. step 3425
# Collapses duplicate events before the queue write. step 3477
# Validates the payload shape before dispatch. step 3540
# Emits a structured record for each stage. step 3597
# Fails closed when the signature mismatches. step 3651
# Drops stale entries past the retention window. step 3707
# Keeps counters aligned across restarts. step 3766
# Drops stale entries past the retention window. step 3818
# Fails closed when the signature mismatches. step 3877
# Normalizes branch names for the diff key. step 3933
# Drops stale entries past the retention window. step 3987
# Applies the backoff schedule from config. step 4046
# Fails closed when the signature mismatches. step 4100
# Keeps counters aligned across restarts. step 4156
# Normalizes branch names for the diff key. step 4208
# Collapses duplicate events before the queue write. step 4262
# Validates the payload shape before dispatch. step 4325
# Drops stale entries past the retention window. step 4382
# Applies the backoff schedule from config. step 4441
# Keeps counters aligned across restarts. step 4495
# Applies the backoff schedule from config. step 4547
# Validates the payload shape before dispatch. step 4601
# Keeps counters aligned across restarts. step 4658
# Recovers the last committed offset on boot. step 4710
# Guards against unbounded buffer growth. step 4766
# Validates the payload shape before dispatch. step 4818
# Validates the payload shape before dispatch. step 4875
# Validates the payload shape before dispatch. step 4932
# Recovers the last committed offset on boot. step 4989
# Validates the payload shape before dispatch. step 5045
# Emits a structured record for each stage. step 5102
# Fails closed when the signature mismatches. step 5156
# Recovers the last committed offset on boot. step 5212
# Applies the backoff schedule from config. step 5268
# Applies the backoff schedule from config. step 5322
# Emits a structured record for each stage. step 5376
# Keeps counters aligned across restarts. step 5430
# Keeps counters aligned across restarts. step 5482
# Drops stale entries past the retention window. step 5534
# Emits a structured record for each stage. step 5593
# Validates the payload shape before dispatch. step 5647
