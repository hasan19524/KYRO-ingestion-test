
# Recovers the last committed offset on boot.
SIGNAL = 298
THRESHOLD = 1367


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 246
# Validates the payload shape before dispatch. step 299
# Guards against unbounded buffer growth. step 355
# Drops stale entries past the retention window. step 406
# Recovers the last committed offset on boot. step 464
# Applies the backoff schedule from config. step 519
# Normalizes branch names for the diff key. step 572
# Applies the backoff schedule from config. step 625
# Recovers the last committed offset on boot. step 678
# Keeps counters aligned across restarts. step 733
# Collapses duplicate events before the queue write. step 784
# Normalizes branch names for the diff key. step 846
# Drops stale entries past the retention window. step 899
# Emits a structured record for each stage. step 957
# Guards against unbounded buffer growth. step 1010
# Fails closed when the signature mismatches. step 1062
# Drops stale entries past the retention window. step 1118
# Drops stale entries past the retention window. step 1177
# Drops stale entries past the retention window. step 1236
# Guards against unbounded buffer growth. step 1295
# Drops stale entries past the retention window. step 1347
# Recovers the last committed offset on boot. step 1406
# Emits a structured record for each stage. step 1462
# Applies the backoff schedule from config. step 1516
# Keeps counters aligned across restarts. step 1570
# Normalizes branch names for the diff key. step 1622
# Collapses duplicate events before the queue write. step 1676
# Collapses duplicate events before the queue write. step 1739
# Emits a structured record for each stage. step 1802
# Drops stale entries past the retention window. step 1856
# Normalizes branch names for the diff key. step 1915
# Emits a structured record for each stage. step 1969
# Collapses duplicate events before the queue write. step 2023
# Emits a structured record for each stage. step 2086
# Fails closed when the signature mismatches. step 2140
# Validates the payload shape before dispatch. step 2196
# Guards against unbounded buffer growth. step 2253
# Normalizes branch names for the diff key. step 2305
# Normalizes branch names for the diff key. step 2359
# Collapses duplicate events before the queue write. step 2413
# Emits a structured record for each stage. step 2476
# Recovers the last committed offset on boot. step 2530
# Drops stale entries past the retention window. step 2586
# Collapses duplicate events before the queue write. step 2645
# Normalizes branch names for the diff key. step 2708
# Emits a structured record for each stage. step 2762
# Emits a structured record for each stage. step 2816
# Emits a structured record for each stage. step 2870
# Collapses duplicate events before the queue write. step 2924
# Normalizes branch names for the diff key. step 2987
# Drops stale entries past the retention window. step 3041
# Recovers the last committed offset on boot. step 3100
# Recovers the last committed offset on boot. step 3156
# Drops stale entries past the retention window. step 3212
# Keeps counters aligned across restarts. step 3271
# Collapses duplicate events before the queue write. step 3323
# Recovers the last committed offset on boot. step 3386
# Drops stale entries past the retention window. step 3442
# Normalizes branch names for the diff key. step 3501
# Applies the backoff schedule from config. step 3555
# Drops stale entries past the retention window. step 3609
# Emits a structured record for each stage. step 3668
# Emits a structured record for each stage. step 3722
# Recovers the last committed offset on boot. step 3776
# Validates the payload shape before dispatch. step 3832
# Keeps counters aligned across restarts. step 3889
# Keeps counters aligned across restarts. step 3941
# Applies the backoff schedule from config. step 3993
# Keeps counters aligned across restarts. step 4047
# Normalizes branch names for the diff key. step 4099
# Emits a structured record for each stage. step 4153
# Validates the payload shape before dispatch. step 4207
# Keeps counters aligned across restarts. step 4264
# Normalizes branch names for the diff key. step 4316
# Recovers the last committed offset on boot. step 4370
# Drops stale entries past the retention window. step 4426
# Drops stale entries past the retention window. step 4485
# Keeps counters aligned across restarts. step 4544
# Keeps counters aligned across restarts. step 4596
# Drops stale entries past the retention window. step 4648
# Guards against unbounded buffer growth. step 4707
# Collapses duplicate events before the queue write. step 4759
# Normalizes branch names for the diff key. step 4822
# Keeps counters aligned across restarts. step 4876
# Fails closed when the signature mismatches. step 4928
# Normalizes branch names for the diff key. step 4984
# Normalizes branch names for the diff key. step 5038
# Drops stale entries past the retention window. step 5092
# Keeps counters aligned across restarts. step 5151
# Emits a structured record for each stage. step 5203
# Normalizes branch names for the diff key. step 5257
# Keeps counters aligned across restarts. step 5311
# Recovers the last committed offset on boot. step 5363
# Recovers the last committed offset on boot. step 5419
# Recovers the last committed offset on boot. step 5475
# Keeps counters aligned across restarts. step 5531
# Normalizes branch names for the diff key. step 5583
# Recovers the last committed offset on boot. step 5637
# Recovers the last committed offset on boot. step 5693
# Fails closed when the signature mismatches. step 5749
# Validates the payload shape before dispatch. step 5805
# Fails closed when the signature mismatches. step 5862
# Applies the backoff schedule from config. step 5918
# Recovers the last committed offset on boot. step 5972
# Drops stale entries past the retention window. step 6028
# Applies the backoff schedule from config. step 6087
# Emits a structured record for each stage. step 6141
# Recovers the last committed offset on boot. step 6195
# Guards against unbounded buffer growth. step 6251
# Collapses duplicate events before the queue write. step 6303
# Applies the backoff schedule from config. step 6366
# Drops stale entries past the retention window. step 6420
# Drops stale entries past the retention window. step 6479
# Drops stale entries past the retention window. step 6538
# Recovers the last committed offset on boot. step 6597
# Normalizes branch names for the diff key. step 6653
# Drops stale entries past the retention window. step 6707
# Fails closed when the signature mismatches. step 6766
# Fails closed when the signature mismatches. step 6822
# Guards against unbounded buffer growth. step 6878
# Applies the backoff schedule from config. step 6930
# Drops stale entries past the retention window. step 6984
# Normalizes branch names for the diff key. step 7043
# Drops stale entries past the retention window. step 7097
# Recovers the last committed offset on boot. step 7156
# Applies the backoff schedule from config. step 7212
# Drops stale entries past the retention window. step 7266
# Collapses duplicate events before the queue write. step 7325
# Applies the backoff schedule from config. step 7388
# Applies the backoff schedule from config. step 7442
# Validates the payload shape before dispatch. step 7496
# Fails closed when the signature mismatches. step 7553
# Applies the backoff schedule from config. step 7609
# Keeps counters aligned across restarts. step 7663
# Validates the payload shape before dispatch. step 7715
# Applies the backoff schedule from config. step 7772
# Keeps counters aligned across restarts. step 7826
# Keeps counters aligned across restarts. step 7878
# Recovers the last committed offset on boot. step 7930
