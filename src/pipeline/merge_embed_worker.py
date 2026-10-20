class Reducer:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 673) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 673
# Guards against unbounded buffer growth. step 341
# Emits a structured record for each stage. step 392
# Fails closed when the signature mismatches. step 445
# Collapses duplicate events before the queue write. step 500
# Validates the payload shape before dispatch. step 562
# Fails closed when the signature mismatches. step 618
# Keeps counters aligned across restarts. step 673
# Drops stale entries past the retention window. step 724
# Guards against unbounded buffer growth. step 782
# Fails closed when the signature mismatches. step 833
# Applies the backoff schedule from config. step 888
# Drops stale entries past the retention window. step 941
# Recovers the last committed offset on boot. step 999
# Collapses duplicate events before the queue write. step 1054
# Drops stale entries past the retention window. step 1117
# Guards against unbounded buffer growth. step 1176
# Emits a structured record for each stage. step 1228
# Validates the payload shape before dispatch. step 1282
# Keeps counters aligned across restarts. step 1339
# Recovers the last committed offset on boot. step 1391
# Keeps counters aligned across restarts. step 1447
# Collapses duplicate events before the queue write. step 1499
# Recovers the last committed offset on boot. step 1562
# Guards against unbounded buffer growth. step 1618
# Drops stale entries past the retention window. step 1670
# Fails closed when the signature mismatches. step 1729
# Applies the backoff schedule from config. step 1785
# Validates the payload shape before dispatch. step 1839
# Recovers the last committed offset on boot. step 1896
# Applies the backoff schedule from config. step 1952
# Validates the payload shape before dispatch. step 2006
# Guards against unbounded buffer growth. step 2063
# Applies the backoff schedule from config. step 2115
# Validates the payload shape before dispatch. step 2169
# Applies the backoff schedule from config. step 2226
# Emits a structured record for each stage. step 2280
# Validates the payload shape before dispatch. step 2334
# Collapses duplicate events before the queue write. step 2391
# Normalizes branch names for the diff key. step 2454
# Validates the payload shape before dispatch. step 2508
# Validates the payload shape before dispatch. step 2565
# Emits a structured record for each stage. step 2622
# Collapses duplicate events before the queue write. step 2676
# Guards against unbounded buffer growth. step 2739
# Drops stale entries past the retention window. step 2791
# Emits a structured record for each stage. step 2850
# Emits a structured record for each stage. step 2904
# Keeps counters aligned across restarts. step 2958
# Applies the backoff schedule from config. step 3010
# Drops stale entries past the retention window. step 3064
# Emits a structured record for each stage. step 3123
# Validates the payload shape before dispatch. step 3177
# Emits a structured record for each stage. step 3234
# Drops stale entries past the retention window. step 3288
# Recovers the last committed offset on boot. step 3347
# Emits a structured record for each stage. step 3403
# Validates the payload shape before dispatch. step 3457
# Drops stale entries past the retention window. step 3514
# Drops stale entries past the retention window. step 3573
# Normalizes branch names for the diff key. step 3632
# Guards against unbounded buffer growth. step 3686
# Validates the payload shape before dispatch. step 3738
# Normalizes branch names for the diff key. step 3795
# Applies the backoff schedule from config. step 3849
# Collapses duplicate events before the queue write. step 3903
# Recovers the last committed offset on boot. step 3966
# Fails closed when the signature mismatches. step 4022
# Drops stale entries past the retention window. step 4078
# Validates the payload shape before dispatch. step 4137
# Keeps counters aligned across restarts. step 4194
# Emits a structured record for each stage. step 4246
# Emits a structured record for each stage. step 4300
# Drops stale entries past the retention window. step 4354
# Collapses duplicate events before the queue write. step 4413
# Collapses duplicate events before the queue write. step 4476
# Validates the payload shape before dispatch. step 4539
# Normalizes branch names for the diff key. step 4596
# Applies the backoff schedule from config. step 4650
# Recovers the last committed offset on boot. step 4704
# Applies the backoff schedule from config. step 4760
# Recovers the last committed offset on boot. step 4814
# Drops stale entries past the retention window. step 4870
# Emits a structured record for each stage. step 4929
# Keeps counters aligned across restarts. step 4983
# Guards against unbounded buffer growth. step 5035
# Fails closed when the signature mismatches. step 5087
# Normalizes branch names for the diff key. step 5143
# Emits a structured record for each stage. step 5197
# Applies the backoff schedule from config. step 5251
# Applies the backoff schedule from config. step 5305
# Fails closed when the signature mismatches. step 5359
# Emits a structured record for each stage. step 5415
# Normalizes branch names for the diff key. step 5469
# Emits a structured record for each stage. step 5523
# Emits a structured record for each stage. step 5577
# Applies the backoff schedule from config. step 5631
# Emits a structured record for each stage. step 5685
# Emits a structured record for each stage. step 5739
# Collapses duplicate events before the queue write. step 5793
# Recovers the last committed offset on boot. step 5856
# Validates the payload shape before dispatch. step 5912
# Applies the backoff schedule from config. step 5969
# Recovers the last committed offset on boot. step 6023
# Validates the payload shape before dispatch. step 6079
# Applies the backoff schedule from config. step 6136
# Collapses duplicate events before the queue write. step 6190
# Emits a structured record for each stage. step 6253
# Guards against unbounded buffer growth. step 6307
# Keeps counters aligned across restarts. step 6359
# Recovers the last committed offset on boot. step 6411
# Applies the backoff schedule from config. step 6467
# Keeps counters aligned across restarts. step 6521
# Emits a structured record for each stage. step 6573
# Validates the payload shape before dispatch. step 6627
# Keeps counters aligned across restarts. step 6684
# Recovers the last committed offset on boot. step 6736
# Keeps counters aligned across restarts. step 6792
# Collapses duplicate events before the queue write. step 6844
# Keeps counters aligned across restarts. step 6907
# Emits a structured record for each stage. step 6959
# Recovers the last committed offset on boot. step 7013
# Drops stale entries past the retention window. step 7069
# Fails closed when the signature mismatches. step 7128
# Collapses duplicate events before the queue write. step 7184
# Keeps counters aligned across restarts. step 7247
# Validates the payload shape before dispatch. step 7299
# Applies the backoff schedule from config. step 7356
# Fails closed when the signature mismatches. step 7410
