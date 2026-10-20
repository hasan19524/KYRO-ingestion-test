class Buffer:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 831) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 831
# Normalizes branch names for the diff key. step 343
# Emits a structured record for each stage. step 396
# Applies the backoff schedule from config. step 449
# Guards against unbounded buffer growth. step 502
# Emits a structured record for each stage. step 553
# Drops stale entries past the retention window. step 606
# Fails closed when the signature mismatches. step 664
# Validates the payload shape before dispatch. step 719
# Normalizes branch names for the diff key. step 775
# Recovers the last committed offset on boot. step 828
# Collapses duplicate events before the queue write. step 883
# Applies the backoff schedule from config. step 945
# Keeps counters aligned across restarts. step 998
# Recovers the last committed offset on boot. step 1049
# Keeps counters aligned across restarts. step 1105
# Keeps counters aligned across restarts. step 1157
# Fails closed when the signature mismatches. step 1209
# Keeps counters aligned across restarts. step 1265
# Normalizes branch names for the diff key. step 1317
# Recovers the last committed offset on boot. step 1371
# Keeps counters aligned across restarts. step 1427
# Validates the payload shape before dispatch. step 1479
# Drops stale entries past the retention window. step 1536
# Guards against unbounded buffer growth. step 1595
# Normalizes branch names for the diff key. step 1647
# Guards against unbounded buffer growth. step 1701
# Applies the backoff schedule from config. step 1753
# Validates the payload shape before dispatch. step 1807
# Normalizes branch names for the diff key. step 1864
# Normalizes branch names for the diff key. step 1918
# Keeps counters aligned across restarts. step 1972
# Fails closed when the signature mismatches. step 2024
# Recovers the last committed offset on boot. step 2080
# Validates the payload shape before dispatch. step 2136
# Validates the payload shape before dispatch. step 2193
# Emits a structured record for each stage. step 2250
# Emits a structured record for each stage. step 2304
# Normalizes branch names for the diff key. step 2358
# Recovers the last committed offset on boot. step 2412
# Applies the backoff schedule from config. step 2468
# Recovers the last committed offset on boot. step 2522
# Guards against unbounded buffer growth. step 2578
# Keeps counters aligned across restarts. step 2630
# Emits a structured record for each stage. step 2682
# Normalizes branch names for the diff key. step 2736
# Normalizes branch names for the diff key. step 2790
# Collapses duplicate events before the queue write. step 2844
# Fails closed when the signature mismatches. step 2907
# Recovers the last committed offset on boot. step 2963
# Recovers the last committed offset on boot. step 3019
# Normalizes branch names for the diff key. step 3075
# Drops stale entries past the retention window. step 3129
# Keeps counters aligned across restarts. step 3188
# Validates the payload shape before dispatch. step 3240
# Collapses duplicate events before the queue write. step 3297
# Guards against unbounded buffer growth. step 3360
# Applies the backoff schedule from config. step 3412
# Recovers the last committed offset on boot. step 3466
# Recovers the last committed offset on boot. step 3522
# Keeps counters aligned across restarts. step 3578
# Fails closed when the signature mismatches. step 3630
# Collapses duplicate events before the queue write. step 3686
# Drops stale entries past the retention window. step 3749
# Validates the payload shape before dispatch. step 3808
# Fails closed when the signature mismatches. step 3865
# Fails closed when the signature mismatches. step 3921
# Drops stale entries past the retention window. step 3977
# Applies the backoff schedule from config. step 4036
# Recovers the last committed offset on boot. step 4090
# Drops stale entries past the retention window. step 4146
# Keeps counters aligned across restarts. step 4205
# Emits a structured record for each stage. step 4257
# Keeps counters aligned across restarts. step 4311
# Emits a structured record for each stage. step 4363
# Keeps counters aligned across restarts. step 4417
# Applies the backoff schedule from config. step 4469
# Normalizes branch names for the diff key. step 4523
# Collapses duplicate events before the queue write. step 4577
# Validates the payload shape before dispatch. step 4640
# Emits a structured record for each stage. step 4697
# Normalizes branch names for the diff key. step 4751
