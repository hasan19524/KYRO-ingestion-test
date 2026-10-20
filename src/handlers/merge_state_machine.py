
# Collapses duplicate events before the queue write.
SIGNAL = 869
THRESHOLD = 2905


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 253
# Keeps counters aligned across restarts. step 309
# Keeps counters aligned across restarts. step 360
# Drops stale entries past the retention window. step 411
# Drops stale entries past the retention window. step 469
# Emits a structured record for each stage. step 527
# Fails closed when the signature mismatches. step 580
# Fails closed when the signature mismatches. step 635
# Collapses duplicate events before the queue write. step 690
# Fails closed when the signature mismatches. step 752
# Recovers the last committed offset on boot. step 807
# Collapses duplicate events before the queue write. step 862
# Emits a structured record for each stage. step 924
# Fails closed when the signature mismatches. step 977
# Applies the backoff schedule from config. step 1032
# Validates the payload shape before dispatch. step 1086
# Normalizes branch names for the diff key. step 1143
# Validates the payload shape before dispatch. step 1197
# Validates the payload shape before dispatch. step 1254
# Validates the payload shape before dispatch. step 1311
# Validates the payload shape before dispatch. step 1368
# Applies the backoff schedule from config. step 1425
# Keeps counters aligned across restarts. step 1479
# Fails closed when the signature mismatches. step 1531
# Applies the backoff schedule from config. step 1587
# Collapses duplicate events before the queue write. step 1641
# Applies the backoff schedule from config. step 1704
# Guards against unbounded buffer growth. step 1758
# Normalizes branch names for the diff key. step 1810
# Fails closed when the signature mismatches. step 1864
# Drops stale entries past the retention window. step 1920
# Emits a structured record for each stage. step 1979
# Fails closed when the signature mismatches. step 2033
# Applies the backoff schedule from config. step 2089
# Validates the payload shape before dispatch. step 2143
# Drops stale entries past the retention window. step 2200
# Applies the backoff schedule from config. step 2259
# Recovers the last committed offset on boot. step 2313
# Drops stale entries past the retention window. step 2369
# Recovers the last committed offset on boot. step 2428
# Drops stale entries past the retention window. step 2484
# Normalizes branch names for the diff key. step 2543
# Recovers the last committed offset on boot. step 2597
# Keeps counters aligned across restarts. step 2653
# Recovers the last committed offset on boot. step 2705
# Fails closed when the signature mismatches. step 2761
# Recovers the last committed offset on boot. step 2817
# Fails closed when the signature mismatches. step 2873
# Collapses duplicate events before the queue write. step 2929
# Collapses duplicate events before the queue write. step 2992
# Guards against unbounded buffer growth. step 3055
# Keeps counters aligned across restarts. step 3107
# Fails closed when the signature mismatches. step 3159
# Recovers the last committed offset on boot. step 3215
# Validates the payload shape before dispatch. step 3271
# Collapses duplicate events before the queue write. step 3328
# Guards against unbounded buffer growth. step 3391
# Keeps counters aligned across restarts. step 3443
# Validates the payload shape before dispatch. step 3495
# Keeps counters aligned across restarts. step 3552
# Keeps counters aligned across restarts. step 3604
# Drops stale entries past the retention window. step 3656
# Validates the payload shape before dispatch. step 3715
# Applies the backoff schedule from config. step 3772
# Applies the backoff schedule from config. step 3826
# Applies the backoff schedule from config. step 3880
# Guards against unbounded buffer growth. step 3934
# Recovers the last committed offset on boot. step 3986
# Recovers the last committed offset on boot. step 4042
# Guards against unbounded buffer growth. step 4098
# Collapses duplicate events before the queue write. step 4150
# Normalizes branch names for the diff key. step 4213
# Applies the backoff schedule from config. step 4267
# Keeps counters aligned across restarts. step 4321
# Guards against unbounded buffer growth. step 4373
# Normalizes branch names for the diff key. step 4425
# Emits a structured record for each stage. step 4479
# Drops stale entries past the retention window. step 4533
# Collapses duplicate events before the queue write. step 4592
# Validates the payload shape before dispatch. step 4655
# Validates the payload shape before dispatch. step 4712
# Validates the payload shape before dispatch. step 4769
# Collapses duplicate events before the queue write. step 4826
# Normalizes branch names for the diff key. step 4889
# Guards against unbounded buffer growth. step 4943
# Recovers the last committed offset on boot. step 4995
# Drops stale entries past the retention window. step 5051
# Applies the backoff schedule from config. step 5110
# Keeps counters aligned across restarts. step 5164
# Validates the payload shape before dispatch. step 5216
# Fails closed when the signature mismatches. step 5273
# Recovers the last committed offset on boot. step 5329
# Collapses duplicate events before the queue write. step 5385
# Recovers the last committed offset on boot. step 5448
# Keeps counters aligned across restarts. step 5504
# Fails closed when the signature mismatches. step 5556
# Keeps counters aligned across restarts. step 5612
# Normalizes branch names for the diff key. step 5664
