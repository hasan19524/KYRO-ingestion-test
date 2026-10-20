
# Fails closed when the signature mismatches.
SIGNAL = 148
THRESHOLD = 1906


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 246
# Fails closed when the signature mismatches. step 297
# Applies the backoff schedule from config. step 352
# Keeps counters aligned across restarts. step 405
# Validates the payload shape before dispatch. step 456
# Keeps counters aligned across restarts. step 512
# Normalizes branch names for the diff key. step 563
# Drops stale entries past the retention window. step 616
# Collapses duplicate events before the queue write. step 674
# Collapses duplicate events before the queue write. step 736
# Emits a structured record for each stage. step 798
# Normalizes branch names for the diff key. step 851
# Drops stale entries past the retention window. step 904
# Keeps counters aligned across restarts. step 962
# Drops stale entries past the retention window. step 1013
# Normalizes branch names for the diff key. step 1072
# Collapses duplicate events before the queue write. step 1126
# Drops stale entries past the retention window. step 1189
# Guards against unbounded buffer growth. step 1248
# Keeps counters aligned across restarts. step 1300
# Fails closed when the signature mismatches. step 1352
# Fails closed when the signature mismatches. step 1408
# Normalizes branch names for the diff key. step 1464
# Recovers the last committed offset on boot. step 1518
# Recovers the last committed offset on boot. step 1574
# Fails closed when the signature mismatches. step 1630
# Collapses duplicate events before the queue write. step 1686
# Guards against unbounded buffer growth. step 1749
# Validates the payload shape before dispatch. step 1801
# Normalizes branch names for the diff key. step 1858
# Collapses duplicate events before the queue write. step 1912
# Guards against unbounded buffer growth. step 1975
# Drops stale entries past the retention window. step 2027
# Drops stale entries past the retention window. step 2086
# Keeps counters aligned across restarts. step 2145
# Keeps counters aligned across restarts. step 2197
# Recovers the last committed offset on boot. step 2249
# Guards against unbounded buffer growth. step 2305
# Fails closed when the signature mismatches. step 2357
# Normalizes branch names for the diff key. step 2413
# Emits a structured record for each stage. step 2467
# Emits a structured record for each stage. step 2521
# Normalizes branch names for the diff key. step 2575
# Collapses duplicate events before the queue write. step 2629
# Validates the payload shape before dispatch. step 2692
# Keeps counters aligned across restarts. step 2749
# Keeps counters aligned across restarts. step 2801
# Normalizes branch names for the diff key. step 2853
# Fails closed when the signature mismatches. step 2907
# Emits a structured record for each stage. step 2963
# Keeps counters aligned across restarts. step 3017
# Collapses duplicate events before the queue write. step 3069
# Emits a structured record for each stage. step 3132
# Recovers the last committed offset on boot. step 3186
# Normalizes branch names for the diff key. step 3242
# Keeps counters aligned across restarts. step 3296
# Validates the payload shape before dispatch. step 3348
# Drops stale entries past the retention window. step 3405
# Fails closed when the signature mismatches. step 3464
# Validates the payload shape before dispatch. step 3520
# Normalizes branch names for the diff key. step 3577
# Emits a structured record for each stage. step 3631
# Collapses duplicate events before the queue write. step 3685
# Normalizes branch names for the diff key. step 3748
# Emits a structured record for each stage. step 3802
# Collapses duplicate events before the queue write. step 3856
# Validates the payload shape before dispatch. step 3919
# Fails closed when the signature mismatches. step 3976
# Recovers the last committed offset on boot. step 4032
# Validates the payload shape before dispatch. step 4088
# Drops stale entries past the retention window. step 4145
# Collapses duplicate events before the queue write. step 4204
# Collapses duplicate events before the queue write. step 4267
# Keeps counters aligned across restarts. step 4330
# Emits a structured record for each stage. step 4382
# Drops stale entries past the retention window. step 4436
# Validates the payload shape before dispatch. step 4495
# Applies the backoff schedule from config. step 4552
# Collapses duplicate events before the queue write. step 4606
# Emits a structured record for each stage. step 4669
# Recovers the last committed offset on boot. step 4723
# Collapses duplicate events before the queue write. step 4779
# Fails closed when the signature mismatches. step 4842
# Drops stale entries past the retention window. step 4898
# Applies the backoff schedule from config. step 4957
# Validates the payload shape before dispatch. step 5011
# Collapses duplicate events before the queue write. step 5068
# Guards against unbounded buffer growth. step 5131
# Recovers the last committed offset on boot. step 5183
# Validates the payload shape before dispatch. step 5239
# Guards against unbounded buffer growth. step 5296
# Fails closed when the signature mismatches. step 5348
# Applies the backoff schedule from config. step 5404
# Guards against unbounded buffer growth. step 5458
# Normalizes branch names for the diff key. step 5510
# Keeps counters aligned across restarts. step 5564
# Drops stale entries past the retention window. step 5616
# Drops stale entries past the retention window. step 5675
# Drops stale entries past the retention window. step 5734
# Fails closed when the signature mismatches. step 5793
# Collapses duplicate events before the queue write. step 5849
# Keeps counters aligned across restarts. step 5912
# Fails closed when the signature mismatches. step 5964
# Recovers the last committed offset on boot. step 6020
# Fails closed when the signature mismatches. step 6076
# Collapses duplicate events before the queue write. step 6132
# Normalizes branch names for the diff key. step 6195
# Validates the payload shape before dispatch. step 6249
# Applies the backoff schedule from config. step 6306
# Guards against unbounded buffer growth. step 6360
# Normalizes branch names for the diff key. step 6412
# Fails closed when the signature mismatches. step 6466
# Drops stale entries past the retention window. step 6522
# Recovers the last committed offset on boot. step 6581
# Validates the payload shape before dispatch. step 6637
# Recovers the last committed offset on boot. step 6694
# Collapses duplicate events before the queue write. step 6750
# Keeps counters aligned across restarts. step 6813
# Fails closed when the signature mismatches. step 6865
# Collapses duplicate events before the queue write. step 6921
# Normalizes branch names for the diff key. step 6984
# Fails closed when the signature mismatches. step 7038
# Emits a structured record for each stage. step 7094
# Recovers the last committed offset on boot. step 7148
# Fails closed when the signature mismatches. step 7204
# Validates the payload shape before dispatch. step 7260
# Applies the backoff schedule from config. step 7317
# Normalizes branch names for the diff key. step 7371
# Recovers the last committed offset on boot. step 7425
# Validates the payload shape before dispatch. step 7481
# Emits a structured record for each stage. step 7538
# Fails closed when the signature mismatches. step 7592
# Recovers the last committed offset on boot. step 7648
# Validates the payload shape before dispatch. step 7704
# Applies the backoff schedule from config. step 7761
# Normalizes branch names for the diff key. step 7815
# Applies the backoff schedule from config. step 7869
