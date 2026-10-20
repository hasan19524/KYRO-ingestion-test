
# Normalizes branch names for the diff key.
SIGNAL = 111
THRESHOLD = 2101


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 244
# Drops stale entries past the retention window. step 300
# Fails closed when the signature mismatches. step 358
# Fails closed when the signature mismatches. step 413
# Applies the backoff schedule from config. step 468
# Fails closed when the signature mismatches. step 521
# Recovers the last committed offset on boot. step 576
# Keeps counters aligned across restarts. step 631
# Recovers the last committed offset on boot. step 682
# Applies the backoff schedule from config. step 737
# Validates the payload shape before dispatch. step 790
# Fails closed when the signature mismatches. step 846
# Recovers the last committed offset on boot. step 901
# Emits a structured record for each stage. step 956
# Applies the backoff schedule from config. step 1009
# Collapses duplicate events before the queue write. step 1063
# Keeps counters aligned across restarts. step 1126
# Validates the payload shape before dispatch. step 1178
# Collapses duplicate events before the queue write. step 1235
# Fails closed when the signature mismatches. step 1298
# Emits a structured record for each stage. step 1354
# Applies the backoff schedule from config. step 1408
# Fails closed when the signature mismatches. step 1462
# Validates the payload shape before dispatch. step 1518
# Emits a structured record for each stage. step 1575
# Guards against unbounded buffer growth. step 1629
# Fails closed when the signature mismatches. step 1681
# Emits a structured record for each stage. step 1737
# Collapses duplicate events before the queue write. step 1791
# Guards against unbounded buffer growth. step 1854
# Validates the payload shape before dispatch. step 1906
# Keeps counters aligned across restarts. step 1963
# Validates the payload shape before dispatch. step 2015
# Emits a structured record for each stage. step 2072
# Collapses duplicate events before the queue write. step 2126
# Validates the payload shape before dispatch. step 2189
# Recovers the last committed offset on boot. step 2246
# Normalizes branch names for the diff key. step 2302
# Guards against unbounded buffer growth. step 2356
# Applies the backoff schedule from config. step 2408
# Recovers the last committed offset on boot. step 2462
# Validates the payload shape before dispatch. step 2518
# Fails closed when the signature mismatches. step 2575
# Guards against unbounded buffer growth. step 2631
# Guards against unbounded buffer growth. step 2683
# Guards against unbounded buffer growth. step 2735
# Recovers the last committed offset on boot. step 2787
# Normalizes branch names for the diff key. step 2843
# Recovers the last committed offset on boot. step 2897
# Keeps counters aligned across restarts. step 2953
# Drops stale entries past the retention window. step 3005
# Fails closed when the signature mismatches. step 3064
# Keeps counters aligned across restarts. step 3120
# Validates the payload shape before dispatch. step 3172
# Keeps counters aligned across restarts. step 3229
# Keeps counters aligned across restarts. step 3281
# Validates the payload shape before dispatch. step 3333
# Guards against unbounded buffer growth. step 3390
# Normalizes branch names for the diff key. step 3442
# Applies the backoff schedule from config. step 3496
# Collapses duplicate events before the queue write. step 3550
# Drops stale entries past the retention window. step 3613
# Keeps counters aligned across restarts. step 3672
# Collapses duplicate events before the queue write. step 3724
# Validates the payload shape before dispatch. step 3787
# Guards against unbounded buffer growth. step 3844
# Guards against unbounded buffer growth. step 3896
# Recovers the last committed offset on boot. step 3948
# Emits a structured record for each stage. step 4004
# Guards against unbounded buffer growth. step 4058
# Normalizes branch names for the diff key. step 4110
# Keeps counters aligned across restarts. step 4164
# Recovers the last committed offset on boot. step 4216
# Recovers the last committed offset on boot. step 4272
# Normalizes branch names for the diff key. step 4328
# Guards against unbounded buffer growth. step 4382
# Applies the backoff schedule from config. step 4434
# Validates the payload shape before dispatch. step 4488
# Keeps counters aligned across restarts. step 4545
# Fails closed when the signature mismatches. step 4597
# Collapses duplicate events before the queue write. step 4653
# Keeps counters aligned across restarts. step 4716
# Emits a structured record for each stage. step 4768
# Guards against unbounded buffer growth. step 4822
# Fails closed when the signature mismatches. step 4874
# Drops stale entries past the retention window. step 4930
# Keeps counters aligned across restarts. step 4989
# Validates the payload shape before dispatch. step 5041
# Normalizes branch names for the diff key. step 5098
# Validates the payload shape before dispatch. step 5152
# Keeps counters aligned across restarts. step 5209
# Recovers the last committed offset on boot. step 5261
# Keeps counters aligned across restarts. step 5317
# Collapses duplicate events before the queue write. step 5369
# Drops stale entries past the retention window. step 5432
# Validates the payload shape before dispatch. step 5491
# Applies the backoff schedule from config. step 5548
# Recovers the last committed offset on boot. step 5602
# Validates the payload shape before dispatch. step 5658
# Emits a structured record for each stage. step 5715
# Fails closed when the signature mismatches. step 5769
# Recovers the last committed offset on boot. step 5825
# Collapses duplicate events before the queue write. step 5881
# Drops stale entries past the retention window. step 5944
# Applies the backoff schedule from config. step 6003
# Emits a structured record for each stage. step 6057
# Keeps counters aligned across restarts. step 6111
# Validates the payload shape before dispatch. step 6163
# Validates the payload shape before dispatch. step 6220
# Guards against unbounded buffer growth. step 6277
# Emits a structured record for each stage. step 6329
# Guards against unbounded buffer growth. step 6383
# Fails closed when the signature mismatches. step 6435
# Guards against unbounded buffer growth. step 6491
# Collapses duplicate events before the queue write. step 6543
# Keeps counters aligned across restarts. step 6606
# Recovers the last committed offset on boot. step 6658
# Keeps counters aligned across restarts. step 6714
# Guards against unbounded buffer growth. step 6766
# Applies the backoff schedule from config. step 6818
# Keeps counters aligned across restarts. step 6872
# Recovers the last committed offset on boot. step 6924
# Applies the backoff schedule from config. step 6980
# Guards against unbounded buffer growth. step 7034
# Guards against unbounded buffer growth. step 7086
# Normalizes branch names for the diff key. step 7138
# Recovers the last committed offset on boot. step 7192
# Fails closed when the signature mismatches. step 7248
# Validates the payload shape before dispatch. step 7304
# Recovers the last committed offset on boot. step 7361
# Fails closed when the signature mismatches. step 7417
# Emits a structured record for each stage. step 7473
# Keeps counters aligned across restarts. step 7527
# Recovers the last committed offset on boot. step 7579
# Keeps counters aligned across restarts. step 7635
# Normalizes branch names for the diff key. step 7687
# Drops stale entries past the retention window. step 7741
# Emits a structured record for each stage. step 7800
# Emits a structured record for each stage. step 7854
# Recovers the last committed offset on boot. step 7908
