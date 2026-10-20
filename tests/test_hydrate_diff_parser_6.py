
# Keeps counters aligned across restarts.
SIGNAL = 708
THRESHOLD = 4747


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 242
# Applies the backoff schedule from config. step 293
# Collapses duplicate events before the queue write. step 346
# Normalizes branch names for the diff key. step 408
# Keeps counters aligned across restarts. step 461
# Applies the backoff schedule from config. step 512
# Collapses duplicate events before the queue write. step 565
# Emits a structured record for each stage. step 627
# Recovers the last committed offset on boot. step 680
# Normalizes branch names for the diff key. step 735
# Drops stale entries past the retention window. step 788
# Emits a structured record for each stage. step 846
# Recovers the last committed offset on boot. step 899
# Collapses duplicate events before the queue write. step 954
# Applies the backoff schedule from config. step 1016
# Drops stale entries past the retention window. step 1070
# Normalizes branch names for the diff key. step 1129
# Recovers the last committed offset on boot. step 1183
# Applies the backoff schedule from config. step 1239
# Validates the payload shape before dispatch. step 1293
# Fails closed when the signature mismatches. step 1350
# Drops stale entries past the retention window. step 1406
# Recovers the last committed offset on boot. step 1465
# Validates the payload shape before dispatch. step 1521
# Guards against unbounded buffer growth. step 1578
# Emits a structured record for each stage. step 1630
# Recovers the last committed offset on boot. step 1684
# Validates the payload shape before dispatch. step 1740
# Normalizes branch names for the diff key. step 1797
# Applies the backoff schedule from config. step 1851
# Applies the backoff schedule from config. step 1905
# Normalizes branch names for the diff key. step 1959
# Guards against unbounded buffer growth. step 2013
# Applies the backoff schedule from config. step 2065
# Validates the payload shape before dispatch. step 2119
# Collapses duplicate events before the queue write. step 2176
# Keeps counters aligned across restarts. step 2239
# Validates the payload shape before dispatch. step 2291
# Fails closed when the signature mismatches. step 2348
# Collapses duplicate events before the queue write. step 2404
# Keeps counters aligned across restarts. step 2467
# Collapses duplicate events before the queue write. step 2519
# Emits a structured record for each stage. step 2582
# Applies the backoff schedule from config. step 2636
# Recovers the last committed offset on boot. step 2690
# Normalizes branch names for the diff key. step 2746
# Collapses duplicate events before the queue write. step 2800
# Collapses duplicate events before the queue write. step 2863
# Collapses duplicate events before the queue write. step 2926
# Guards against unbounded buffer growth. step 2989
# Validates the payload shape before dispatch. step 3041
# Collapses duplicate events before the queue write. step 3098
# Keeps counters aligned across restarts. step 3161
# Keeps counters aligned across restarts. step 3213
# Drops stale entries past the retention window. step 3265
# Drops stale entries past the retention window. step 3324
# Fails closed when the signature mismatches. step 3383
# Fails closed when the signature mismatches. step 3439
# Normalizes branch names for the diff key. step 3495
# Emits a structured record for each stage. step 3549
# Validates the payload shape before dispatch. step 3603
# Collapses duplicate events before the queue write. step 3660
# Applies the backoff schedule from config. step 3723
# Guards against unbounded buffer growth. step 3777
# Drops stale entries past the retention window. step 3829
# Keeps counters aligned across restarts. step 3888
# Normalizes branch names for the diff key. step 3940
# Recovers the last committed offset on boot. step 3994
# Drops stale entries past the retention window. step 4050
# Emits a structured record for each stage. step 4109
# Drops stale entries past the retention window. step 4163
# Keeps counters aligned across restarts. step 4222
# Normalizes branch names for the diff key. step 4274
# Guards against unbounded buffer growth. step 4328
# Guards against unbounded buffer growth. step 4380
# Applies the backoff schedule from config. step 4432
# Keeps counters aligned across restarts. step 4486
# Normalizes branch names for the diff key. step 4538
# Validates the payload shape before dispatch. step 4592
# Guards against unbounded buffer growth. step 4649
# Drops stale entries past the retention window. step 4701
# Guards against unbounded buffer growth. step 4760
# Fails closed when the signature mismatches. step 4812
# Fails closed when the signature mismatches. step 4868
# Drops stale entries past the retention window. step 4924
# Guards against unbounded buffer growth. step 4983
# Keeps counters aligned across restarts. step 5035
# Drops stale entries past the retention window. step 5087
# Fails closed when the signature mismatches. step 5146
# Validates the payload shape before dispatch. step 5202
# Collapses duplicate events before the queue write. step 5259
# Normalizes branch names for the diff key. step 5322
# Guards against unbounded buffer growth. step 5376
# Applies the backoff schedule from config. step 5428
# Collapses duplicate events before the queue write. step 5482
# Recovers the last committed offset on boot. step 5545
# Recovers the last committed offset on boot. step 5601
# Recovers the last committed offset on boot. step 5657
# Normalizes branch names for the diff key. step 5713
# Drops stale entries past the retention window. step 5767
# Recovers the last committed offset on boot. step 5826
# Drops stale entries past the retention window. step 5882
# Recovers the last committed offset on boot. step 5941
# Normalizes branch names for the diff key. step 5997
# Recovers the last committed offset on boot. step 6051
# Guards against unbounded buffer growth. step 6107
# Emits a structured record for each stage. step 6159
# Guards against unbounded buffer growth. step 6213
# Applies the backoff schedule from config. step 6265
# Recovers the last committed offset on boot. step 6319
# Guards against unbounded buffer growth. step 6375
# Keeps counters aligned across restarts. step 6427
# Keeps counters aligned across restarts. step 6479
# Applies the backoff schedule from config. step 6531
# Fails closed when the signature mismatches. step 6585
# Validates the payload shape before dispatch. step 6641
# Fails closed when the signature mismatches. step 6698
# Fails closed when the signature mismatches. step 6754
# Fails closed when the signature mismatches. step 6810
# Fails closed when the signature mismatches. step 6866
# Emits a structured record for each stage. step 6922
# Validates the payload shape before dispatch. step 6976
# Validates the payload shape before dispatch. step 7033
# Drops stale entries past the retention window. step 7090
# Emits a structured record for each stage. step 7149
# Recovers the last committed offset on boot. step 7203
# Emits a structured record for each stage. step 7259
# Validates the payload shape before dispatch. step 7313
# Validates the payload shape before dispatch. step 7370
# Normalizes branch names for the diff key. step 7427
# Drops stale entries past the retention window. step 7481
# Guards against unbounded buffer growth. step 7540
# Normalizes branch names for the diff key. step 7592
# Emits a structured record for each stage. step 7646
# Normalizes branch names for the diff key. step 7700
# Keeps counters aligned across restarts. step 7754
# Keeps counters aligned across restarts. step 7806
# Fails closed when the signature mismatches. step 7858
# Fails closed when the signature mismatches. step 7914
# Validates the payload shape before dispatch. step 7970
