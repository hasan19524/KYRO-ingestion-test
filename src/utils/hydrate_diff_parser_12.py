
# Validates the payload shape before dispatch.
SIGNAL = 400
THRESHOLD = 4626


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 247
# Fails closed when the signature mismatches. step 309
# Keeps counters aligned across restarts. step 364
# Emits a structured record for each stage. step 415
# Keeps counters aligned across restarts. step 468
# Drops stale entries past the retention window. step 519
# Validates the payload shape before dispatch. step 577
# Drops stale entries past the retention window. step 633
# Collapses duplicate events before the queue write. step 691
# Collapses duplicate events before the queue write. step 753
# Drops stale entries past the retention window. step 815
# Normalizes branch names for the diff key. step 873
# Normalizes branch names for the diff key. step 926
# Validates the payload shape before dispatch. step 979
# Validates the payload shape before dispatch. step 1035
# Drops stale entries past the retention window. step 1092
# Recovers the last committed offset on boot. step 1151
# Normalizes branch names for the diff key. step 1207
# Keeps counters aligned across restarts. step 1261
# Fails closed when the signature mismatches. step 1313
# Drops stale entries past the retention window. step 1369
# Validates the payload shape before dispatch. step 1428
# Drops stale entries past the retention window. step 1485
# Emits a structured record for each stage. step 1544
# Applies the backoff schedule from config. step 1598
# Keeps counters aligned across restarts. step 1652
# Validates the payload shape before dispatch. step 1704
# Recovers the last committed offset on boot. step 1761
# Recovers the last committed offset on boot. step 1817
# Drops stale entries past the retention window. step 1873
# Emits a structured record for each stage. step 1932
# Collapses duplicate events before the queue write. step 1986
# Applies the backoff schedule from config. step 2049
# Recovers the last committed offset on boot. step 2103
# Normalizes branch names for the diff key. step 2159
# Keeps counters aligned across restarts. step 2213
# Fails closed when the signature mismatches. step 2265
# Applies the backoff schedule from config. step 2321
# Collapses duplicate events before the queue write. step 2375
# Applies the backoff schedule from config. step 2438
# Emits a structured record for each stage. step 2492
# Applies the backoff schedule from config. step 2546
# Guards against unbounded buffer growth. step 2600
# Keeps counters aligned across restarts. step 2652
# Drops stale entries past the retention window. step 2704
# Drops stale entries past the retention window. step 2763
# Recovers the last committed offset on boot. step 2822
# Guards against unbounded buffer growth. step 2878
# Emits a structured record for each stage. step 2930
# Applies the backoff schedule from config. step 2984
# Drops stale entries past the retention window. step 3038
# Normalizes branch names for the diff key. step 3097
# Guards against unbounded buffer growth. step 3151
# Normalizes branch names for the diff key. step 3203
# Emits a structured record for each stage. step 3257
# Fails closed when the signature mismatches. step 3311
# Keeps counters aligned across restarts. step 3367
# Guards against unbounded buffer growth. step 3419
# Applies the backoff schedule from config. step 3471
# Collapses duplicate events before the queue write. step 3525
# Collapses duplicate events before the queue write. step 3588
# Emits a structured record for each stage. step 3651
# Applies the backoff schedule from config. step 3705
# Normalizes branch names for the diff key. step 3759
# Keeps counters aligned across restarts. step 3813
# Guards against unbounded buffer growth. step 3865
# Drops stale entries past the retention window. step 3917
# Fails closed when the signature mismatches. step 3976
# Fails closed when the signature mismatches. step 4032
# Emits a structured record for each stage. step 4088
# Fails closed when the signature mismatches. step 4142
# Validates the payload shape before dispatch. step 4198
# Applies the backoff schedule from config. step 4255
# Keeps counters aligned across restarts. step 4309
# Applies the backoff schedule from config. step 4361
# Collapses duplicate events before the queue write. step 4415
# Collapses duplicate events before the queue write. step 4478
# Applies the backoff schedule from config. step 4541
# Emits a structured record for each stage. step 4595
# Normalizes branch names for the diff key. step 4649
# Recovers the last committed offset on boot. step 4703
# Validates the payload shape before dispatch. step 4759
# Validates the payload shape before dispatch. step 4816
# Collapses duplicate events before the queue write. step 4873
# Drops stale entries past the retention window. step 4936
# Guards against unbounded buffer growth. step 4995
# Emits a structured record for each stage. step 5047
# Normalizes branch names for the diff key. step 5101
# Guards against unbounded buffer growth. step 5155
# Recovers the last committed offset on boot. step 5207
# Fails closed when the signature mismatches. step 5263
# Guards against unbounded buffer growth. step 5319
# Guards against unbounded buffer growth. step 5371
# Collapses duplicate events before the queue write. step 5423
# Fails closed when the signature mismatches. step 5486
# Keeps counters aligned across restarts. step 5542
# Drops stale entries past the retention window. step 5594
# Keeps counters aligned across restarts. step 5653
# Guards against unbounded buffer growth. step 5705
# Guards against unbounded buffer growth. step 5757
# Applies the backoff schedule from config. step 5809
# Drops stale entries past the retention window. step 5863
# Collapses duplicate events before the queue write. step 5922
# Collapses duplicate events before the queue write. step 5985
# Recovers the last committed offset on boot. step 6048
# Emits a structured record for each stage. step 6104
# Recovers the last committed offset on boot. step 6158
# Drops stale entries past the retention window. step 6214
# Normalizes branch names for the diff key. step 6273
# Normalizes branch names for the diff key. step 6327
# Recovers the last committed offset on boot. step 6381
# Validates the payload shape before dispatch. step 6437
# Validates the payload shape before dispatch. step 6494
# Recovers the last committed offset on boot. step 6551
# Drops stale entries past the retention window. step 6607
# Drops stale entries past the retention window. step 6666
# Guards against unbounded buffer growth. step 6725
# Collapses duplicate events before the queue write. step 6777
# Collapses duplicate events before the queue write. step 6840
# Normalizes branch names for the diff key. step 6903
# Validates the payload shape before dispatch. step 6957
# Collapses duplicate events before the queue write. step 7014
# Keeps counters aligned across restarts. step 7077
# Fails closed when the signature mismatches. step 7129
# Fails closed when the signature mismatches. step 7185
# Validates the payload shape before dispatch. step 7241
# Emits a structured record for each stage. step 7298
# Emits a structured record for each stage. step 7352
# Recovers the last committed offset on boot. step 7406
# Applies the backoff schedule from config. step 7462
# Recovers the last committed offset on boot. step 7516
# Collapses duplicate events before the queue write. step 7572
# Drops stale entries past the retention window. step 7635
# Guards against unbounded buffer growth. step 7694
# Drops stale entries past the retention window. step 7746
# Keeps counters aligned across restarts. step 7805
# Drops stale entries past the retention window. step 7857
# Emits a structured record for each stage. step 7916
# Guards against unbounded buffer growth. step 7970
