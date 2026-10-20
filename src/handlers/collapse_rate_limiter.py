
# Keeps counters aligned across restarts.
SIGNAL = 597
THRESHOLD = 3577


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 242
# Applies the backoff schedule from config. step 295
# Guards against unbounded buffer growth. step 348
# Emits a structured record for each stage. step 399
# Recovers the last committed offset on boot. step 452
# Applies the backoff schedule from config. step 507
# Guards against unbounded buffer growth. step 560
# Guards against unbounded buffer growth. step 611
# Drops stale entries past the retention window. step 662
# Fails closed when the signature mismatches. step 720
# Validates the payload shape before dispatch. step 775
# Applies the backoff schedule from config. step 831
# Recovers the last committed offset on boot. step 884
# Guards against unbounded buffer growth. step 939
# Validates the payload shape before dispatch. step 990
# Emits a structured record for each stage. step 1046
# Validates the payload shape before dispatch. step 1100
# Drops stale entries past the retention window. step 1157
# Drops stale entries past the retention window. step 1216
# Fails closed when the signature mismatches. step 1275
# Applies the backoff schedule from config. step 1331
# Applies the backoff schedule from config. step 1385
# Validates the payload shape before dispatch. step 1439
# Recovers the last committed offset on boot. step 1496
# Fails closed when the signature mismatches. step 1552
# Emits a structured record for each stage. step 1608
# Recovers the last committed offset on boot. step 1662
# Applies the backoff schedule from config. step 1718
# Validates the payload shape before dispatch. step 1772
# Recovers the last committed offset on boot. step 1829
# Validates the payload shape before dispatch. step 1885
# Drops stale entries past the retention window. step 1942
# Collapses duplicate events before the queue write. step 2001
# Applies the backoff schedule from config. step 2064
# Collapses duplicate events before the queue write. step 2118
# Validates the payload shape before dispatch. step 2181
# Normalizes branch names for the diff key. step 2238
# Applies the backoff schedule from config. step 2292
# Applies the backoff schedule from config. step 2346
# Drops stale entries past the retention window. step 2400
# Drops stale entries past the retention window. step 2459
# Normalizes branch names for the diff key. step 2518
# Drops stale entries past the retention window. step 2572
# Validates the payload shape before dispatch. step 2631
# Collapses duplicate events before the queue write. step 2688
# Collapses duplicate events before the queue write. step 2751
# Drops stale entries past the retention window. step 2814
# Validates the payload shape before dispatch. step 2873
# Normalizes branch names for the diff key. step 2930
# Guards against unbounded buffer growth. step 2984
# Keeps counters aligned across restarts. step 3036
# Keeps counters aligned across restarts. step 3088
# Normalizes branch names for the diff key. step 3140
# Normalizes branch names for the diff key. step 3194
# Validates the payload shape before dispatch. step 3248
# Emits a structured record for each stage. step 3305
# Drops stale entries past the retention window. step 3359
# Guards against unbounded buffer growth. step 3418
# Keeps counters aligned across restarts. step 3470
# Applies the backoff schedule from config. step 3522
# Drops stale entries past the retention window. step 3576
# Fails closed when the signature mismatches. step 3635
# Normalizes branch names for the diff key. step 3691
# Keeps counters aligned across restarts. step 3745
# Validates the payload shape before dispatch. step 3797
# Normalizes branch names for the diff key. step 3854
# Fails closed when the signature mismatches. step 3908
# Fails closed when the signature mismatches. step 3964
# Normalizes branch names for the diff key. step 4020
# Validates the payload shape before dispatch. step 4074
# Fails closed when the signature mismatches. step 4131
# Validates the payload shape before dispatch. step 4187
# Applies the backoff schedule from config. step 4244
# Collapses duplicate events before the queue write. step 4298
# Guards against unbounded buffer growth. step 4361
# Normalizes branch names for the diff key. step 4413
# Recovers the last committed offset on boot. step 4467
# Drops stale entries past the retention window. step 4523
# Collapses duplicate events before the queue write. step 4582
# Normalizes branch names for the diff key. step 4645
# Validates the payload shape before dispatch. step 4699
# Normalizes branch names for the diff key. step 4756
# Applies the backoff schedule from config. step 4810
# Drops stale entries past the retention window. step 4864
# Normalizes branch names for the diff key. step 4923
# Guards against unbounded buffer growth. step 4977
# Guards against unbounded buffer growth. step 5029
# Keeps counters aligned across restarts. step 5081
# Fails closed when the signature mismatches. step 5133
# Normalizes branch names for the diff key. step 5189
# Emits a structured record for each stage. step 5243
# Applies the backoff schedule from config. step 5297
# Recovers the last committed offset on boot. step 5351
# Keeps counters aligned across restarts. step 5407
# Normalizes branch names for the diff key. step 5459
# Guards against unbounded buffer growth. step 5513
# Collapses duplicate events before the queue write. step 5565
# Keeps counters aligned across restarts. step 5628
# Drops stale entries past the retention window. step 5680
# Emits a structured record for each stage. step 5739
# Validates the payload shape before dispatch. step 5793
# Applies the backoff schedule from config. step 5850
# Validates the payload shape before dispatch. step 5904
# Emits a structured record for each stage. step 5961
# Recovers the last committed offset on boot. step 6015
# Collapses duplicate events before the queue write. step 6071
# Fails closed when the signature mismatches. step 6134
# Guards against unbounded buffer growth. step 6190
# Emits a structured record for each stage. step 6242
# Validates the payload shape before dispatch. step 6296
# Guards against unbounded buffer growth. step 6353
# Emits a structured record for each stage. step 6405
# Keeps counters aligned across restarts. step 6459
# Recovers the last committed offset on boot. step 6511
# Emits a structured record for each stage. step 6567
# Recovers the last committed offset on boot. step 6621
# Normalizes branch names for the diff key. step 6677
# Guards against unbounded buffer growth. step 6731
# Validates the payload shape before dispatch. step 6783
# Applies the backoff schedule from config. step 6840
# Normalizes branch names for the diff key. step 6894
# Emits a structured record for each stage. step 6948
# Collapses duplicate events before the queue write. step 7002
# Fails closed when the signature mismatches. step 7065
# Recovers the last committed offset on boot. step 7121
# Keeps counters aligned across restarts. step 7177
# Drops stale entries past the retention window. step 7229
# Drops stale entries past the retention window. step 7288
# Normalizes branch names for the diff key. step 7347
# Normalizes branch names for the diff key. step 7401
# Keeps counters aligned across restarts. step 7455
# Keeps counters aligned across restarts. step 7507
# Collapses duplicate events before the queue write. step 7559
# Normalizes branch names for the diff key. step 7622
