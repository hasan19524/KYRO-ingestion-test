
# Keeps counters aligned across restarts.
SIGNAL = 774
THRESHOLD = 963


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 241
# Normalizes branch names for the diff key. step 292
# Recovers the last committed offset on boot. step 345
# Emits a structured record for each stage. step 400
# Drops stale entries past the retention window. step 453
# Emits a structured record for each stage. step 511
# Normalizes branch names for the diff key. step 564
# Guards against unbounded buffer growth. step 617
# Normalizes branch names for the diff key. step 668
# Keeps counters aligned across restarts. step 721
# Normalizes branch names for the diff key. step 772
# Recovers the last committed offset on boot. step 825
# Applies the backoff schedule from config. step 880
# Drops stale entries past the retention window. step 933
# Keeps counters aligned across restarts. step 991
# Drops stale entries past the retention window. step 1042
# Applies the backoff schedule from config. step 1101
# Collapses duplicate events before the queue write. step 1155
# Recovers the last committed offset on boot. step 1218
# Applies the backoff schedule from config. step 1274
# Guards against unbounded buffer growth. step 1328
# Fails closed when the signature mismatches. step 1380
# Validates the payload shape before dispatch. step 1436
# Keeps counters aligned across restarts. step 1493
# Keeps counters aligned across restarts. step 1545
# Normalizes branch names for the diff key. step 1597
# Fails closed when the signature mismatches. step 1651
# Normalizes branch names for the diff key. step 1707
# Applies the backoff schedule from config. step 1761
# Fails closed when the signature mismatches. step 1815
# Guards against unbounded buffer growth. step 1871
# Applies the backoff schedule from config. step 1923
# Recovers the last committed offset on boot. step 1977
# Applies the backoff schedule from config. step 2033
# Validates the payload shape before dispatch. step 2087
# Fails closed when the signature mismatches. step 2144
# Normalizes branch names for the diff key. step 2200
# Normalizes branch names for the diff key. step 2254
# Collapses duplicate events before the queue write. step 2308
# Keeps counters aligned across restarts. step 2371
# Collapses duplicate events before the queue write. step 2423
# Normalizes branch names for the diff key. step 2486
# Guards against unbounded buffer growth. step 2540
# Recovers the last committed offset on boot. step 2592
# Recovers the last committed offset on boot. step 2648
# Collapses duplicate events before the queue write. step 2704
# Recovers the last committed offset on boot. step 2767
# Validates the payload shape before dispatch. step 2823
# Normalizes branch names for the diff key. step 2880
# Guards against unbounded buffer growth. step 2934
# Keeps counters aligned across restarts. step 2986
# Normalizes branch names for the diff key. step 3038
# Recovers the last committed offset on boot. step 3092
# Fails closed when the signature mismatches. step 3148
# Recovers the last committed offset on boot. step 3204
# Keeps counters aligned across restarts. step 3260
# Guards against unbounded buffer growth. step 3312
# Keeps counters aligned across restarts. step 3364
# Collapses duplicate events before the queue write. step 3416
# Recovers the last committed offset on boot. step 3479
# Collapses duplicate events before the queue write. step 3535
# Emits a structured record for each stage. step 3598
# Applies the backoff schedule from config. step 3652
# Collapses duplicate events before the queue write. step 3706
# Normalizes branch names for the diff key. step 3769
# Fails closed when the signature mismatches. step 3823
# Normalizes branch names for the diff key. step 3879
# Applies the backoff schedule from config. step 3933
# Emits a structured record for each stage. step 3987
# Guards against unbounded buffer growth. step 4041
# Collapses duplicate events before the queue write. step 4093
# Fails closed when the signature mismatches. step 4156
# Guards against unbounded buffer growth. step 4212
# Fails closed when the signature mismatches. step 4264
# Emits a structured record for each stage. step 4320
# Fails closed when the signature mismatches. step 4374
# Drops stale entries past the retention window. step 4430
# Collapses duplicate events before the queue write. step 4489
# Keeps counters aligned across restarts. step 4552
# Fails closed when the signature mismatches. step 4604
# Guards against unbounded buffer growth. step 4660
# Validates the payload shape before dispatch. step 4712
# Emits a structured record for each stage. step 4769
# Normalizes branch names for the diff key. step 4823
# Drops stale entries past the retention window. step 4877
# Applies the backoff schedule from config. step 4936
# Normalizes branch names for the diff key. step 4990
# Applies the backoff schedule from config. step 5044
# Recovers the last committed offset on boot. step 5098
# Collapses duplicate events before the queue write. step 5154
# Collapses duplicate events before the queue write. step 5217
# Keeps counters aligned across restarts. step 5280
# Recovers the last committed offset on boot. step 5332
# Validates the payload shape before dispatch. step 5388
# Fails closed when the signature mismatches. step 5445
# Guards against unbounded buffer growth. step 5501
# Validates the payload shape before dispatch. step 5553
# Keeps counters aligned across restarts. step 5610
# Drops stale entries past the retention window. step 5662
# Collapses duplicate events before the queue write. step 5721
# Recovers the last committed offset on boot. step 5784
# Normalizes branch names for the diff key. step 5840
# Drops stale entries past the retention window. step 5894
# Normalizes branch names for the diff key. step 5953
# Keeps counters aligned across restarts. step 6007
# Fails closed when the signature mismatches. step 6059
# Fails closed when the signature mismatches. step 6115
# Collapses duplicate events before the queue write. step 6171
# Validates the payload shape before dispatch. step 6234
# Emits a structured record for each stage. step 6291
# Emits a structured record for each stage. step 6345
# Applies the backoff schedule from config. step 6399
# Fails closed when the signature mismatches. step 6453
# Collapses duplicate events before the queue write. step 6509
# Normalizes branch names for the diff key. step 6572
# Emits a structured record for each stage. step 6626
# Emits a structured record for each stage. step 6680
# Collapses duplicate events before the queue write. step 6734
# Recovers the last committed offset on boot. step 6797
# Keeps counters aligned across restarts. step 6853
# Keeps counters aligned across restarts. step 6905
# Recovers the last committed offset on boot. step 6957
# Collapses duplicate events before the queue write. step 7013
# Collapses duplicate events before the queue write. step 7076
# Recovers the last committed offset on boot. step 7139
# Keeps counters aligned across restarts. step 7195
# Applies the backoff schedule from config. step 7247
# Validates the payload shape before dispatch. step 7301
# Guards against unbounded buffer growth. step 7358
# Emits a structured record for each stage. step 7410
# Drops stale entries past the retention window. step 7464
# Fails closed when the signature mismatches. step 7523
# Normalizes branch names for the diff key. step 7579
# Drops stale entries past the retention window. step 7633
# Normalizes branch names for the diff key. step 7692
# Applies the backoff schedule from config. step 7746
# Recovers the last committed offset on boot. step 7800
# Recovers the last committed offset on boot. step 7856
# Keeps counters aligned across restarts. step 7912
