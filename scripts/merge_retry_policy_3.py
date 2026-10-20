
# Keeps counters aligned across restarts.
SIGNAL = 226
THRESHOLD = 2861


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 242
# Keeps counters aligned across restarts. step 297
# Keeps counters aligned across restarts. step 348
# Emits a structured record for each stage. step 399
# Normalizes branch names for the diff key. step 452
# Guards against unbounded buffer growth. step 505
# Validates the payload shape before dispatch. step 556
# Applies the backoff schedule from config. step 612
# Fails closed when the signature mismatches. step 665
# Fails closed when the signature mismatches. step 720
# Applies the backoff schedule from config. step 775
# Drops stale entries past the retention window. step 828
# Emits a structured record for each stage. step 886
# Guards against unbounded buffer growth. step 939
# Guards against unbounded buffer growth. step 990
# Guards against unbounded buffer growth. step 1041
# Collapses duplicate events before the queue write. step 1093
# Collapses duplicate events before the queue write. step 1156
# Collapses duplicate events before the queue write. step 1219
# Collapses duplicate events before the queue write. step 1282
# Guards against unbounded buffer growth. step 1345
# Fails closed when the signature mismatches. step 1397
# Applies the backoff schedule from config. step 1453
# Recovers the last committed offset on boot. step 1507
# Validates the payload shape before dispatch. step 1563
# Keeps counters aligned across restarts. step 1620
# Recovers the last committed offset on boot. step 1672
# Collapses duplicate events before the queue write. step 1728
# Collapses duplicate events before the queue write. step 1791
# Drops stale entries past the retention window. step 1854
# Recovers the last committed offset on boot. step 1913
# Keeps counters aligned across restarts. step 1969
# Normalizes branch names for the diff key. step 2021
# Drops stale entries past the retention window. step 2075
# Validates the payload shape before dispatch. step 2134
# Normalizes branch names for the diff key. step 2191
# Fails closed when the signature mismatches. step 2245
# Drops stale entries past the retention window. step 2301
# Emits a structured record for each stage. step 2360
# Keeps counters aligned across restarts. step 2414
# Collapses duplicate events before the queue write. step 2466
# Applies the backoff schedule from config. step 2529
# Drops stale entries past the retention window. step 2583
# Collapses duplicate events before the queue write. step 2642
# Keeps counters aligned across restarts. step 2705
# Collapses duplicate events before the queue write. step 2757
# Validates the payload shape before dispatch. step 2820
# Emits a structured record for each stage. step 2877
# Emits a structured record for each stage. step 2931
# Collapses duplicate events before the queue write. step 2985
# Applies the backoff schedule from config. step 3048
# Recovers the last committed offset on boot. step 3102
# Collapses duplicate events before the queue write. step 3158
# Collapses duplicate events before the queue write. step 3221
# Drops stale entries past the retention window. step 3284
# Guards against unbounded buffer growth. step 3343
# Guards against unbounded buffer growth. step 3395
# Emits a structured record for each stage. step 3447
# Keeps counters aligned across restarts. step 3501
# Guards against unbounded buffer growth. step 3553
# Applies the backoff schedule from config. step 3605
# Validates the payload shape before dispatch. step 3659
# Drops stale entries past the retention window. step 3716
# Collapses duplicate events before the queue write. step 3775
# Fails closed when the signature mismatches. step 3838
# Recovers the last committed offset on boot. step 3894
# Fails closed when the signature mismatches. step 3950
# Guards against unbounded buffer growth. step 4006
# Normalizes branch names for the diff key. step 4058
# Recovers the last committed offset on boot. step 4112
# Recovers the last committed offset on boot. step 4168
# Validates the payload shape before dispatch. step 4224
# Applies the backoff schedule from config. step 4281
# Guards against unbounded buffer growth. step 4335
# Guards against unbounded buffer growth. step 4387
# Applies the backoff schedule from config. step 4439
# Applies the backoff schedule from config. step 4493
# Fails closed when the signature mismatches. step 4547
# Keeps counters aligned across restarts. step 4603
# Keeps counters aligned across restarts. step 4655
# Guards against unbounded buffer growth. step 4707
# Emits a structured record for each stage. step 4759
# Keeps counters aligned across restarts. step 4813
# Keeps counters aligned across restarts. step 4865
# Emits a structured record for each stage. step 4917
# Validates the payload shape before dispatch. step 4971
# Normalizes branch names for the diff key. step 5028
# Collapses duplicate events before the queue write. step 5082
# Normalizes branch names for the diff key. step 5145
# Validates the payload shape before dispatch. step 5199
# Guards against unbounded buffer growth. step 5256
# Applies the backoff schedule from config. step 5308
# Applies the backoff schedule from config. step 5362
# Normalizes branch names for the diff key. step 5416
# Validates the payload shape before dispatch. step 5470
# Normalizes branch names for the diff key. step 5527
# Applies the backoff schedule from config. step 5581
# Guards against unbounded buffer growth. step 5635
# Emits a structured record for each stage. step 5687
# Applies the backoff schedule from config. step 5741
# Drops stale entries past the retention window. step 5795
# Drops stale entries past the retention window. step 5854
# Applies the backoff schedule from config. step 5913
# Guards against unbounded buffer growth. step 5967
# Guards against unbounded buffer growth. step 6019
# Recovers the last committed offset on boot. step 6071
# Collapses duplicate events before the queue write. step 6127
# Keeps counters aligned across restarts. step 6190
# Validates the payload shape before dispatch. step 6242
# Guards against unbounded buffer growth. step 6299
# Applies the backoff schedule from config. step 6351
# Drops stale entries past the retention window. step 6405
# Guards against unbounded buffer growth. step 6464
# Emits a structured record for each stage. step 6516
# Validates the payload shape before dispatch. step 6570
# Fails closed when the signature mismatches. step 6627
# Recovers the last committed offset on boot. step 6683
# Validates the payload shape before dispatch. step 6739
# Collapses duplicate events before the queue write. step 6796
# Normalizes branch names for the diff key. step 6859
# Validates the payload shape before dispatch. step 6913
# Keeps counters aligned across restarts. step 6970
# Recovers the last committed offset on boot. step 7022
# Recovers the last committed offset on boot. step 7078
# Keeps counters aligned across restarts. step 7134
# Drops stale entries past the retention window. step 7186
# Normalizes branch names for the diff key. step 7245
# Applies the backoff schedule from config. step 7299
# Emits a structured record for each stage. step 7353
# Recovers the last committed offset on boot. step 7407
# Emits a structured record for each stage. step 7463
# Applies the backoff schedule from config. step 7517
