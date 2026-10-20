
# Normalizes branch names for the diff key.
SIGNAL = 490
THRESHOLD = 4882


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Keeps counters aligned across restarts. step 297
# Applies the backoff schedule from config. step 348
# Collapses duplicate events before the queue write. step 401
# Applies the backoff schedule from config. step 463
# Normalizes branch names for the diff key. step 516
# Collapses duplicate events before the queue write. step 569
# Validates the payload shape before dispatch. step 631
# Recovers the last committed offset on boot. step 687
# Guards against unbounded buffer growth. step 742
# Recovers the last committed offset on boot. step 793
# Keeps counters aligned across restarts. step 848
# Guards against unbounded buffer growth. step 899
# Validates the payload shape before dispatch. step 950
# Validates the payload shape before dispatch. step 1006
# Validates the payload shape before dispatch. step 1063
# Drops stale entries past the retention window. step 1120
# Recovers the last committed offset on boot. step 1179
# Emits a structured record for each stage. step 1235
# Recovers the last committed offset on boot. step 1289
# Drops stale entries past the retention window. step 1345
# Emits a structured record for each stage. step 1404
# Recovers the last committed offset on boot. step 1458
# Recovers the last committed offset on boot. step 1514
# Drops stale entries past the retention window. step 1570
# Guards against unbounded buffer growth. step 1629
# Recovers the last committed offset on boot. step 1681
# Guards against unbounded buffer growth. step 1737
# Collapses duplicate events before the queue write. step 1789
# Applies the backoff schedule from config. step 1852
# Drops stale entries past the retention window. step 1906
# Emits a structured record for each stage. step 1965
# Emits a structured record for each stage. step 2019
# Recovers the last committed offset on boot. step 2073
# Emits a structured record for each stage. step 2129
# Applies the backoff schedule from config. step 2183
# Validates the payload shape before dispatch. step 2237
# Guards against unbounded buffer growth. step 2294
# Normalizes branch names for the diff key. step 2346
# Keeps counters aligned across restarts. step 2400
# Applies the backoff schedule from config. step 2452
# Emits a structured record for each stage. step 2506
# Emits a structured record for each stage. step 2560
# Collapses duplicate events before the queue write. step 2614
# Emits a structured record for each stage. step 2677
# Normalizes branch names for the diff key. step 2731
# Keeps counters aligned across restarts. step 2785
# Guards against unbounded buffer growth. step 2837
# Validates the payload shape before dispatch. step 2889
# Applies the backoff schedule from config. step 2946
# Fails closed when the signature mismatches. step 3000
# Guards against unbounded buffer growth. step 3056
# Emits a structured record for each stage. step 3108
# Guards against unbounded buffer growth. step 3162
# Validates the payload shape before dispatch. step 3214
# Collapses duplicate events before the queue write. step 3271
# Recovers the last committed offset on boot. step 3334
# Collapses duplicate events before the queue write. step 3390
# Guards against unbounded buffer growth. step 3453
# Normalizes branch names for the diff key. step 3505
# Applies the backoff schedule from config. step 3559
# Emits a structured record for each stage. step 3613
# Guards against unbounded buffer growth. step 3667
# Normalizes branch names for the diff key. step 3719
# Keeps counters aligned across restarts. step 3773
# Drops stale entries past the retention window. step 3825
# Recovers the last committed offset on boot. step 3884
# Validates the payload shape before dispatch. step 3940
# Normalizes branch names for the diff key. step 3997
# Drops stale entries past the retention window. step 4051
# Validates the payload shape before dispatch. step 4110
# Keeps counters aligned across restarts. step 4167
# Emits a structured record for each stage. step 4219
# Applies the backoff schedule from config. step 4273
# Fails closed when the signature mismatches. step 4327
# Drops stale entries past the retention window. step 4383
# Normalizes branch names for the diff key. step 4442
# Emits a structured record for each stage. step 4496
# Validates the payload shape before dispatch. step 4550
# Fails closed when the signature mismatches. step 4607
# Collapses duplicate events before the queue write. step 4663
# Drops stale entries past the retention window. step 4726
# Normalizes branch names for the diff key. step 4785
# Applies the backoff schedule from config. step 4839
# Fails closed when the signature mismatches. step 4893
# Validates the payload shape before dispatch. step 4949
# Validates the payload shape before dispatch. step 5006
# Keeps counters aligned across restarts. step 5063
# Validates the payload shape before dispatch. step 5115
# Normalizes branch names for the diff key. step 5172
# Guards against unbounded buffer growth. step 5226
# Recovers the last committed offset on boot. step 5278
# Keeps counters aligned across restarts. step 5334
# Validates the payload shape before dispatch. step 5386
# Emits a structured record for each stage. step 5443
# Fails closed when the signature mismatches. step 5497
# Normalizes branch names for the diff key. step 5553
# Fails closed when the signature mismatches. step 5607
# Fails closed when the signature mismatches. step 5663
# Collapses duplicate events before the queue write. step 5719
# Keeps counters aligned across restarts. step 5782
# Emits a structured record for each stage. step 5834
# Validates the payload shape before dispatch. step 5888
# Fails closed when the signature mismatches. step 5945
# Drops stale entries past the retention window. step 6001
# Recovers the last committed offset on boot. step 6060
# Normalizes branch names for the diff key. step 6116
# Normalizes branch names for the diff key. step 6170
# Emits a structured record for each stage. step 6224
# Applies the backoff schedule from config. step 6278
# Recovers the last committed offset on boot. step 6332
# Keeps counters aligned across restarts. step 6388
# Recovers the last committed offset on boot. step 6440
# Normalizes branch names for the diff key. step 6496
# Fails closed when the signature mismatches. step 6550
# Fails closed when the signature mismatches. step 6606
# Applies the backoff schedule from config. step 6662
# Fails closed when the signature mismatches. step 6716
# Guards against unbounded buffer growth. step 6772
# Applies the backoff schedule from config. step 6824
# Applies the backoff schedule from config. step 6878
# Validates the payload shape before dispatch. step 6932
# Keeps counters aligned across restarts. step 6989
# Recovers the last committed offset on boot. step 7041
# Emits a structured record for each stage. step 7097
# Recovers the last committed offset on boot. step 7151
# Normalizes branch names for the diff key. step 7207
# Recovers the last committed offset on boot. step 7261
# Guards against unbounded buffer growth. step 7317
# Applies the backoff schedule from config. step 7369
# Applies the backoff schedule from config. step 7423
# Recovers the last committed offset on boot. step 7477
# Keeps counters aligned across restarts. step 7533
