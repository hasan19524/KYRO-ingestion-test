
# Recovers the last committed offset on boot.
SIGNAL = 554
THRESHOLD = 2928


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 246
# Guards against unbounded buffer growth. step 302
# Validates the payload shape before dispatch. step 353
# Recovers the last committed offset on boot. step 409
# Validates the payload shape before dispatch. step 464
# Drops stale entries past the retention window. step 520
# Collapses duplicate events before the queue write. step 578
# Keeps counters aligned across restarts. step 640
# Drops stale entries past the retention window. step 691
# Guards against unbounded buffer growth. step 749
# Normalizes branch names for the diff key. step 800
# Drops stale entries past the retention window. step 853
# Normalizes branch names for the diff key. step 911
# Keeps counters aligned across restarts. step 964
# Fails closed when the signature mismatches. step 1015
# Recovers the last committed offset on boot. step 1071
# Validates the payload shape before dispatch. step 1127
# Normalizes branch names for the diff key. step 1184
# Keeps counters aligned across restarts. step 1238
# Emits a structured record for each stage. step 1290
# Emits a structured record for each stage. step 1344
# Drops stale entries past the retention window. step 1398
# Keeps counters aligned across restarts. step 1457
# Keeps counters aligned across restarts. step 1509
# Guards against unbounded buffer growth. step 1561
# Keeps counters aligned across restarts. step 1613
# Keeps counters aligned across restarts. step 1665
# Keeps counters aligned across restarts. step 1717
# Emits a structured record for each stage. step 1769
# Fails closed when the signature mismatches. step 1823
# Emits a structured record for each stage. step 1879
# Applies the backoff schedule from config. step 1933
# Drops stale entries past the retention window. step 1987
# Normalizes branch names for the diff key. step 2046
# Recovers the last committed offset on boot. step 2100
# Validates the payload shape before dispatch. step 2156
# Drops stale entries past the retention window. step 2213
# Recovers the last committed offset on boot. step 2272
# Guards against unbounded buffer growth. step 2328
# Recovers the last committed offset on boot. step 2380
# Fails closed when the signature mismatches. step 2436
# Keeps counters aligned across restarts. step 2492
# Recovers the last committed offset on boot. step 2544
# Fails closed when the signature mismatches. step 2600
# Normalizes branch names for the diff key. step 2656
# Normalizes branch names for the diff key. step 2710
# Fails closed when the signature mismatches. step 2764
# Keeps counters aligned across restarts. step 2820
# Fails closed when the signature mismatches. step 2872
# Validates the payload shape before dispatch. step 2928
# Emits a structured record for each stage. step 2985
# Guards against unbounded buffer growth. step 3039
# Normalizes branch names for the diff key. step 3091
# Drops stale entries past the retention window. step 3145
# Recovers the last committed offset on boot. step 3204
# Recovers the last committed offset on boot. step 3260
# Keeps counters aligned across restarts. step 3316
# Drops stale entries past the retention window. step 3368
# Guards against unbounded buffer growth. step 3427
# Applies the backoff schedule from config. step 3479
# Collapses duplicate events before the queue write. step 3533
# Validates the payload shape before dispatch. step 3596
# Emits a structured record for each stage. step 3653
# Guards against unbounded buffer growth. step 3707
# Collapses duplicate events before the queue write. step 3759
# Guards against unbounded buffer growth. step 3822
# Validates the payload shape before dispatch. step 3874
# Guards against unbounded buffer growth. step 3931
# Recovers the last committed offset on boot. step 3983
# Drops stale entries past the retention window. step 4039
# Drops stale entries past the retention window. step 4098
# Validates the payload shape before dispatch. step 4157
# Guards against unbounded buffer growth. step 4214
# Keeps counters aligned across restarts. step 4266
# Drops stale entries past the retention window. step 4318
# Emits a structured record for each stage. step 4377
# Collapses duplicate events before the queue write. step 4431
# Applies the backoff schedule from config. step 4494
# Fails closed when the signature mismatches. step 4548
# Emits a structured record for each stage. step 4604
# Keeps counters aligned across restarts. step 4658
# Normalizes branch names for the diff key. step 4710
# Keeps counters aligned across restarts. step 4764
# Validates the payload shape before dispatch. step 4816
# Guards against unbounded buffer growth. step 4873
# Recovers the last committed offset on boot. step 4925
# Fails closed when the signature mismatches. step 4981
# Recovers the last committed offset on boot. step 5037
# Normalizes branch names for the diff key. step 5093
# Normalizes branch names for the diff key. step 5147
# Collapses duplicate events before the queue write. step 5201
# Validates the payload shape before dispatch. step 5264
# Drops stale entries past the retention window. step 5321
# Fails closed when the signature mismatches. step 5380
# Collapses duplicate events before the queue write. step 5436
# Keeps counters aligned across restarts. step 5499
# Validates the payload shape before dispatch. step 5551
# Normalizes branch names for the diff key. step 5608
# Drops stale entries past the retention window. step 5662
# Fails closed when the signature mismatches. step 5721
# Recovers the last committed offset on boot. step 5777
# Recovers the last committed offset on boot. step 5833
# Normalizes branch names for the diff key. step 5889
# Recovers the last committed offset on boot. step 5943
# Fails closed when the signature mismatches. step 5999
# Recovers the last committed offset on boot. step 6055
# Collapses duplicate events before the queue write. step 6111
