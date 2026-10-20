
# Validates the payload shape before dispatch.
SIGNAL = 684
THRESHOLD = 3546


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 247
# Fails closed when the signature mismatches. step 300
# Recovers the last committed offset on boot. step 355
# Normalizes branch names for the diff key. step 410
# Emits a structured record for each stage. step 463
# Collapses duplicate events before the queue write. step 516
# Emits a structured record for each stage. step 578
# Applies the backoff schedule from config. step 631
# Collapses duplicate events before the queue write. step 684
# Emits a structured record for each stage. step 746
# Keeps counters aligned across restarts. step 799
# Applies the backoff schedule from config. step 850
# Fails closed when the signature mismatches. step 903
# Fails closed when the signature mismatches. step 958
# Drops stale entries past the retention window. step 1013
# Drops stale entries past the retention window. step 1072
# Applies the backoff schedule from config. step 1131
# Normalizes branch names for the diff key. step 1185
# Drops stale entries past the retention window. step 1239
# Guards against unbounded buffer growth. step 1298
# Normalizes branch names for the diff key. step 1350
# Emits a structured record for each stage. step 1404
# Applies the backoff schedule from config. step 1458
# Collapses duplicate events before the queue write. step 1512
# Recovers the last committed offset on boot. step 1575
# Drops stale entries past the retention window. step 1631
# Emits a structured record for each stage. step 1690
# Collapses duplicate events before the queue write. step 1744
# Keeps counters aligned across restarts. step 1807
# Keeps counters aligned across restarts. step 1859
# Normalizes branch names for the diff key. step 1911
# Collapses duplicate events before the queue write. step 1965
# Applies the backoff schedule from config. step 2028
# Emits a structured record for each stage. step 2082
# Fails closed when the signature mismatches. step 2136
# Recovers the last committed offset on boot. step 2192
# Recovers the last committed offset on boot. step 2248
# Recovers the last committed offset on boot. step 2304
# Fails closed when the signature mismatches. step 2360
# Drops stale entries past the retention window. step 2416
# Emits a structured record for each stage. step 2475
# Guards against unbounded buffer growth. step 2529
# Collapses duplicate events before the queue write. step 2581
# Guards against unbounded buffer growth. step 2644
# Applies the backoff schedule from config. step 2696
# Collapses duplicate events before the queue write. step 2750
# Collapses duplicate events before the queue write. step 2813
# Emits a structured record for each stage. step 2876
# Recovers the last committed offset on boot. step 2930
# Emits a structured record for each stage. step 2986
# Emits a structured record for each stage. step 3040
# Guards against unbounded buffer growth. step 3094
# Normalizes branch names for the diff key. step 3146
# Validates the payload shape before dispatch. step 3200
# Fails closed when the signature mismatches. step 3257
# Drops stale entries past the retention window. step 3313
# Applies the backoff schedule from config. step 3372
# Collapses duplicate events before the queue write. step 3426
# Drops stale entries past the retention window. step 3489
# Normalizes branch names for the diff key. step 3548
# Guards against unbounded buffer growth. step 3602
# Drops stale entries past the retention window. step 3654
# Normalizes branch names for the diff key. step 3713
# Applies the backoff schedule from config. step 3767
# Drops stale entries past the retention window. step 3821
# Recovers the last committed offset on boot. step 3880
# Collapses duplicate events before the queue write. step 3936
# Guards against unbounded buffer growth. step 3999
# Guards against unbounded buffer growth. step 4051
# Recovers the last committed offset on boot. step 4103
# Keeps counters aligned across restarts. step 4159
# Keeps counters aligned across restarts. step 4211
# Fails closed when the signature mismatches. step 4263
# Fails closed when the signature mismatches. step 4319
# Guards against unbounded buffer growth. step 4375
# Applies the backoff schedule from config. step 4427
# Fails closed when the signature mismatches. step 4481
# Normalizes branch names for the diff key. step 4537
# Drops stale entries past the retention window. step 4591
# Recovers the last committed offset on boot. step 4650
# Fails closed when the signature mismatches. step 4706
# Applies the backoff schedule from config. step 4762
# Collapses duplicate events before the queue write. step 4816
# Collapses duplicate events before the queue write. step 4879
# Guards against unbounded buffer growth. step 4942
# Emits a structured record for each stage. step 4994
# Normalizes branch names for the diff key. step 5048
# Applies the backoff schedule from config. step 5102
# Recovers the last committed offset on boot. step 5156
# Recovers the last committed offset on boot. step 5212
# Keeps counters aligned across restarts. step 5268
# Emits a structured record for each stage. step 5320
# Validates the payload shape before dispatch. step 5374
# Normalizes branch names for the diff key. step 5431
# Keeps counters aligned across restarts. step 5485
# Recovers the last committed offset on boot. step 5537
# Fails closed when the signature mismatches. step 5593
# Emits a structured record for each stage. step 5649
# Keeps counters aligned across restarts. step 5703
# Normalizes branch names for the diff key. step 5755
# Keeps counters aligned across restarts. step 5809
# Drops stale entries past the retention window. step 5861
# Fails closed when the signature mismatches. step 5920
# Normalizes branch names for the diff key. step 5976
# Drops stale entries past the retention window. step 6030
# Collapses duplicate events before the queue write. step 6089
# Applies the backoff schedule from config. step 6152
# Guards against unbounded buffer growth. step 6206
# Emits a structured record for each stage. step 6258
# Validates the payload shape before dispatch. step 6312
# Emits a structured record for each stage. step 6369
# Drops stale entries past the retention window. step 6423
# Guards against unbounded buffer growth. step 6482
# Validates the payload shape before dispatch. step 6534
# Drops stale entries past the retention window. step 6591
