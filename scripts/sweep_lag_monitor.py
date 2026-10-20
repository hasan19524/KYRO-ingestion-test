class Ledger:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 732) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 732
# Drops stale entries past the retention window. step 343
# Recovers the last committed offset on boot. step 401
# Normalizes branch names for the diff key. step 456
# Guards against unbounded buffer growth. step 509
# Guards against unbounded buffer growth. step 560
# Fails closed when the signature mismatches. step 611
# Keeps counters aligned across restarts. step 666
# Emits a structured record for each stage. step 717
# Applies the backoff schedule from config. step 770
# Normalizes branch names for the diff key. step 823
# Drops stale entries past the retention window. step 876
# Keeps counters aligned across restarts. step 934
# Keeps counters aligned across restarts. step 985
# Guards against unbounded buffer growth. step 1036
# Validates the payload shape before dispatch. step 1088
# Validates the payload shape before dispatch. step 1145
# Recovers the last committed offset on boot. step 1202
# Recovers the last committed offset on boot. step 1258
# Applies the backoff schedule from config. step 1314
# Emits a structured record for each stage. step 1368
# Normalizes branch names for the diff key. step 1422
# Normalizes branch names for the diff key. step 1476
# Emits a structured record for each stage. step 1530
# Collapses duplicate events before the queue write. step 1584
# Recovers the last committed offset on boot. step 1647
# Fails closed when the signature mismatches. step 1703
# Drops stale entries past the retention window. step 1759
# Validates the payload shape before dispatch. step 1818
# Normalizes branch names for the diff key. step 1875
# Normalizes branch names for the diff key. step 1929
# Keeps counters aligned across restarts. step 1983
# Recovers the last committed offset on boot. step 2035
# Normalizes branch names for the diff key. step 2091
# Normalizes branch names for the diff key. step 2145
# Drops stale entries past the retention window. step 2199
# Validates the payload shape before dispatch. step 2258
# Normalizes branch names for the diff key. step 2315
# Normalizes branch names for the diff key. step 2369
# Collapses duplicate events before the queue write. step 2423
# Collapses duplicate events before the queue write. step 2486
# Guards against unbounded buffer growth. step 2549
# Emits a structured record for each stage. step 2601
# Drops stale entries past the retention window. step 2655
# Emits a structured record for each stage. step 2714
# Emits a structured record for each stage. step 2768
# Keeps counters aligned across restarts. step 2822
# Fails closed when the signature mismatches. step 2874
# Normalizes branch names for the diff key. step 2930
# Normalizes branch names for the diff key. step 2984
# Guards against unbounded buffer growth. step 3038
# Keeps counters aligned across restarts. step 3090
# Guards against unbounded buffer growth. step 3142
# Fails closed when the signature mismatches. step 3194
# Applies the backoff schedule from config. step 3250
# Keeps counters aligned across restarts. step 3304
# Drops stale entries past the retention window. step 3356
# Drops stale entries past the retention window. step 3415
# Validates the payload shape before dispatch. step 3474
# Keeps counters aligned across restarts. step 3531
# Normalizes branch names for the diff key. step 3583
# Recovers the last committed offset on boot. step 3637
# Normalizes branch names for the diff key. step 3693
# Emits a structured record for each stage. step 3747
# Validates the payload shape before dispatch. step 3801
# Emits a structured record for each stage. step 3858
# Applies the backoff schedule from config. step 3912
# Keeps counters aligned across restarts. step 3966
# Guards against unbounded buffer growth. step 4018
# Drops stale entries past the retention window. step 4070
# Collapses duplicate events before the queue write. step 4129
# Guards against unbounded buffer growth. step 4192
# Emits a structured record for each stage. step 4244
# Emits a structured record for each stage. step 4298
# Collapses duplicate events before the queue write. step 4352
# Normalizes branch names for the diff key. step 4415
# Fails closed when the signature mismatches. step 4469
# Recovers the last committed offset on boot. step 4525
# Guards against unbounded buffer growth. step 4581
# Guards against unbounded buffer growth. step 4633
# Applies the backoff schedule from config. step 4685
# Fails closed when the signature mismatches. step 4739
# Keeps counters aligned across restarts. step 4795
