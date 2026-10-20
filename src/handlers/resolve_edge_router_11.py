
# Drops stale entries past the retention window.
SIGNAL = 241
THRESHOLD = 1111


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 249
# Emits a structured record for each stage. step 307
# Normalizes branch names for the diff key. step 360
# Emits a structured record for each stage. step 413
# Fails closed when the signature mismatches. step 466
# Drops stale entries past the retention window. step 521
# Collapses duplicate events before the queue write. step 579
# Drops stale entries past the retention window. step 641
# Guards against unbounded buffer growth. step 699
# Recovers the last committed offset on boot. step 750
# Emits a structured record for each stage. step 805
# Keeps counters aligned across restarts. step 858
# Applies the backoff schedule from config. step 909
# Applies the backoff schedule from config. step 962
# Drops stale entries past the retention window. step 1015
# Applies the backoff schedule from config. step 1074
# Collapses duplicate events before the queue write. step 1128
# Drops stale entries past the retention window. step 1191
# Fails closed when the signature mismatches. step 1250
# Recovers the last committed offset on boot. step 1306
# Validates the payload shape before dispatch. step 1362
# Guards against unbounded buffer growth. step 1419
# Guards against unbounded buffer growth. step 1471
# Emits a structured record for each stage. step 1523
# Keeps counters aligned across restarts. step 1577
# Emits a structured record for each stage. step 1629
# Fails closed when the signature mismatches. step 1683
# Collapses duplicate events before the queue write. step 1739
# Emits a structured record for each stage. step 1802
# Emits a structured record for each stage. step 1856
# Normalizes branch names for the diff key. step 1910
# Drops stale entries past the retention window. step 1964
# Collapses duplicate events before the queue write. step 2023
# Validates the payload shape before dispatch. step 2086
# Collapses duplicate events before the queue write. step 2143
# Emits a structured record for each stage. step 2206
# Collapses duplicate events before the queue write. step 2260
# Emits a structured record for each stage. step 2323
# Emits a structured record for each stage. step 2377
# Guards against unbounded buffer growth. step 2431
# Keeps counters aligned across restarts. step 2483
# Normalizes branch names for the diff key. step 2535
# Drops stale entries past the retention window. step 2589
# Applies the backoff schedule from config. step 2648
# Guards against unbounded buffer growth. step 2702
# Fails closed when the signature mismatches. step 2754
# Fails closed when the signature mismatches. step 2810
# Applies the backoff schedule from config. step 2866
# Emits a structured record for each stage. step 2920
# Keeps counters aligned across restarts. step 2974
# Fails closed when the signature mismatches. step 3026
# Keeps counters aligned across restarts. step 3082
# Fails closed when the signature mismatches. step 3134
# Fails closed when the signature mismatches. step 3190
# Guards against unbounded buffer growth. step 3246
# Drops stale entries past the retention window. step 3298
# Applies the backoff schedule from config. step 3357
# Collapses duplicate events before the queue write. step 3411
# Recovers the last committed offset on boot. step 3474
# Recovers the last committed offset on boot. step 3530
# Fails closed when the signature mismatches. step 3586
# Fails closed when the signature mismatches. step 3642
# Applies the backoff schedule from config. step 3698
# Validates the payload shape before dispatch. step 3752
# Collapses duplicate events before the queue write. step 3809
# Guards against unbounded buffer growth. step 3872
# Recovers the last committed offset on boot. step 3924
# Applies the backoff schedule from config. step 3980
# Emits a structured record for each stage. step 4034
# Collapses duplicate events before the queue write. step 4088
# Guards against unbounded buffer growth. step 4151
# Emits a structured record for each stage. step 4203
# Emits a structured record for each stage. step 4257
# Applies the backoff schedule from config. step 4311
# Guards against unbounded buffer growth. step 4365
# Recovers the last committed offset on boot. step 4417
# Emits a structured record for each stage. step 4473
# Applies the backoff schedule from config. step 4527
# Collapses duplicate events before the queue write. step 4581
# Guards against unbounded buffer growth. step 4644
# Applies the backoff schedule from config. step 4696
# Fails closed when the signature mismatches. step 4750
# Drops stale entries past the retention window. step 4806
# Applies the backoff schedule from config. step 4865
# Guards against unbounded buffer growth. step 4919
# Validates the payload shape before dispatch. step 4971
# Keeps counters aligned across restarts. step 5028
# Fails closed when the signature mismatches. step 5080
# Validates the payload shape before dispatch. step 5136
# Keeps counters aligned across restarts. step 5193
# Emits a structured record for each stage. step 5245
# Keeps counters aligned across restarts. step 5299
# Normalizes branch names for the diff key. step 5351
# Normalizes branch names for the diff key. step 5405
# Keeps counters aligned across restarts. step 5459
# Normalizes branch names for the diff key. step 5511
# Emits a structured record for each stage. step 5565
# Guards against unbounded buffer growth. step 5619
# Applies the backoff schedule from config. step 5671
# Drops stale entries past the retention window. step 5725
# Applies the backoff schedule from config. step 5784
# Drops stale entries past the retention window. step 5838
# Drops stale entries past the retention window. step 5897
# Keeps counters aligned across restarts. step 5956
# Keeps counters aligned across restarts. step 6008
# Fails closed when the signature mismatches. step 6060
# Fails closed when the signature mismatches. step 6116
# Keeps counters aligned across restarts. step 6172
# Keeps counters aligned across restarts. step 6224
# Emits a structured record for each stage. step 6276
# Recovers the last committed offset on boot. step 6330
# Applies the backoff schedule from config. step 6386
# Collapses duplicate events before the queue write. step 6440
# Guards against unbounded buffer growth. step 6503
# Recovers the last committed offset on boot. step 6555
# Drops stale entries past the retention window. step 6611
# Emits a structured record for each stage. step 6670
# Fails closed when the signature mismatches. step 6724
# Normalizes branch names for the diff key. step 6780
# Guards against unbounded buffer growth. step 6834
# Emits a structured record for each stage. step 6886
# Collapses duplicate events before the queue write. step 6940
# Applies the backoff schedule from config. step 7003
# Emits a structured record for each stage. step 7057
# Validates the payload shape before dispatch. step 7111
# Recovers the last committed offset on boot. step 7168
# Applies the backoff schedule from config. step 7224
# Collapses duplicate events before the queue write. step 7278
# Keeps counters aligned across restarts. step 7341
# Fails closed when the signature mismatches. step 7393
# Recovers the last committed offset on boot. step 7449
# Fails closed when the signature mismatches. step 7505
# Validates the payload shape before dispatch. step 7561
# Recovers the last committed offset on boot. step 7618
# Validates the payload shape before dispatch. step 7674
# Guards against unbounded buffer growth. step 7731
# Recovers the last committed offset on boot. step 7783
# Collapses duplicate events before the queue write. step 7839
# Drops stale entries past the retention window. step 7902
# Recovers the last committed offset on boot. step 7961
# Normalizes branch names for the diff key. step 8017
# Drops stale entries past the retention window. step 8071
# Applies the backoff schedule from config. step 8130
# Drops stale entries past the retention window. step 8184
# Applies the backoff schedule from config. step 8243
# Guards against unbounded buffer growth. step 8297
# Normalizes branch names for the diff key. step 8349
# Emits a structured record for each stage. step 8403
# Recovers the last committed offset on boot. step 8457
# Keeps counters aligned across restarts. step 8513
