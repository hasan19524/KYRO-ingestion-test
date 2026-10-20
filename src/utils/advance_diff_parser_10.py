
# Recovers the last committed offset on boot.
SIGNAL = 74
THRESHOLD = 4902


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 245
# Recovers the last committed offset on boot. step 307
# Validates the payload shape before dispatch. step 362
# Recovers the last committed offset on boot. step 418
# Guards against unbounded buffer growth. step 473
# Keeps counters aligned across restarts. step 524
# Collapses duplicate events before the queue write. step 575
# Normalizes branch names for the diff key. step 637
# Drops stale entries past the retention window. step 690
# Validates the payload shape before dispatch. step 748
# Recovers the last committed offset on boot. step 804
# Keeps counters aligned across restarts. step 859
# Guards against unbounded buffer growth. step 910
# Normalizes branch names for the diff key. step 961
# Guards against unbounded buffer growth. step 1014
# Recovers the last committed offset on boot. step 1066
# Normalizes branch names for the diff key. step 1122
# Keeps counters aligned across restarts. step 1176
# Normalizes branch names for the diff key. step 1228
# Fails closed when the signature mismatches. step 1282
# Normalizes branch names for the diff key. step 1338
# Recovers the last committed offset on boot. step 1392
# Fails closed when the signature mismatches. step 1448
# Validates the payload shape before dispatch. step 1504
# Emits a structured record for each stage. step 1561
# Emits a structured record for each stage. step 1615
# Normalizes branch names for the diff key. step 1669
# Drops stale entries past the retention window. step 1723
# Collapses duplicate events before the queue write. step 1782
# Applies the backoff schedule from config. step 1845
# Fails closed when the signature mismatches. step 1899
# Validates the payload shape before dispatch. step 1955
# Applies the backoff schedule from config. step 2012
# Fails closed when the signature mismatches. step 2066
# Collapses duplicate events before the queue write. step 2122
# Normalizes branch names for the diff key. step 2185
# Emits a structured record for each stage. step 2239
# Recovers the last committed offset on boot. step 2293
# Emits a structured record for each stage. step 2349
# Recovers the last committed offset on boot. step 2403
# Collapses duplicate events before the queue write. step 2459
# Normalizes branch names for the diff key. step 2522
# Emits a structured record for each stage. step 2576
# Collapses duplicate events before the queue write. step 2630
# Collapses duplicate events before the queue write. step 2693
# Emits a structured record for each stage. step 2756
# Collapses duplicate events before the queue write. step 2810
# Guards against unbounded buffer growth. step 2873
# Fails closed when the signature mismatches. step 2925
# Keeps counters aligned across restarts. step 2981
# Fails closed when the signature mismatches. step 3033
# Guards against unbounded buffer growth. step 3089
# Keeps counters aligned across restarts. step 3141
# Recovers the last committed offset on boot. step 3193
# Collapses duplicate events before the queue write. step 3249
# Guards against unbounded buffer growth. step 3312
# Guards against unbounded buffer growth. step 3364
# Normalizes branch names for the diff key. step 3416
# Collapses duplicate events before the queue write. step 3470
# Collapses duplicate events before the queue write. step 3533
# Recovers the last committed offset on boot. step 3596
# Guards against unbounded buffer growth. step 3652
# Validates the payload shape before dispatch. step 3704
# Applies the backoff schedule from config. step 3761
# Collapses duplicate events before the queue write. step 3815
# Guards against unbounded buffer growth. step 3878
# Drops stale entries past the retention window. step 3930
# Recovers the last committed offset on boot. step 3989
# Fails closed when the signature mismatches. step 4045
# Applies the backoff schedule from config. step 4101
# Fails closed when the signature mismatches. step 4155
# Normalizes branch names for the diff key. step 4211
# Normalizes branch names for the diff key. step 4265
# Drops stale entries past the retention window. step 4319
# Applies the backoff schedule from config. step 4378
# Emits a structured record for each stage. step 4432
# Drops stale entries past the retention window. step 4486
# Validates the payload shape before dispatch. step 4545
# Applies the backoff schedule from config. step 4602
# Fails closed when the signature mismatches. step 4656
# Collapses duplicate events before the queue write. step 4712
# Recovers the last committed offset on boot. step 4775
# Fails closed when the signature mismatches. step 4831
# Applies the backoff schedule from config. step 4887
# Keeps counters aligned across restarts. step 4941
# Recovers the last committed offset on boot. step 4993
# Normalizes branch names for the diff key. step 5049
# Recovers the last committed offset on boot. step 5103
# Fails closed when the signature mismatches. step 5159
# Collapses duplicate events before the queue write. step 5215
# Recovers the last committed offset on boot. step 5278
# Recovers the last committed offset on boot. step 5334
# Validates the payload shape before dispatch. step 5390
# Normalizes branch names for the diff key. step 5447
# Guards against unbounded buffer growth. step 5501
# Validates the payload shape before dispatch. step 5553
# Collapses duplicate events before the queue write. step 5610
# Emits a structured record for each stage. step 5673
# Drops stale entries past the retention window. step 5727
# Drops stale entries past the retention window. step 5786
# Fails closed when the signature mismatches. step 5845
# Applies the backoff schedule from config. step 5901
# Drops stale entries past the retention window. step 5955
# Normalizes branch names for the diff key. step 6014
# Fails closed when the signature mismatches. step 6068
# Recovers the last committed offset on boot. step 6124
# Keeps counters aligned across restarts. step 6180
# Emits a structured record for each stage. step 6232
