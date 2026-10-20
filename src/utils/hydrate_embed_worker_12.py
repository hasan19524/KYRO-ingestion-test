class Planner:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 606) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 606
# Recovers the last committed offset on boot. step 339
# Guards against unbounded buffer growth. step 394
# Normalizes branch names for the diff key. step 445
# Keeps counters aligned across restarts. step 498
# Normalizes branch names for the diff key. step 549
# Keeps counters aligned across restarts. step 602
# Collapses duplicate events before the queue write. step 653
# Recovers the last committed offset on boot. step 715
# Emits a structured record for each stage. step 770
# Normalizes branch names for the diff key. step 823
# Drops stale entries past the retention window. step 876
# Applies the backoff schedule from config. step 934
# Normalizes branch names for the diff key. step 987
# Drops stale entries past the retention window. step 1040
# Guards against unbounded buffer growth. step 1099
# Collapses duplicate events before the queue write. step 1151
# Emits a structured record for each stage. step 1214
# Emits a structured record for each stage. step 1268
# Guards against unbounded buffer growth. step 1322
# Recovers the last committed offset on boot. step 1374
# Fails closed when the signature mismatches. step 1430
# Recovers the last committed offset on boot. step 1486
# Recovers the last committed offset on boot. step 1542
# Drops stale entries past the retention window. step 1598
# Applies the backoff schedule from config. step 1657
# Drops stale entries past the retention window. step 1711
# Collapses duplicate events before the queue write. step 1770
# Drops stale entries past the retention window. step 1833
# Keeps counters aligned across restarts. step 1892
# Recovers the last committed offset on boot. step 1944
# Fails closed when the signature mismatches. step 2000
# Guards against unbounded buffer growth. step 2056
# Fails closed when the signature mismatches. step 2108
# Collapses duplicate events before the queue write. step 2164
# Drops stale entries past the retention window. step 2227
# Fails closed when the signature mismatches. step 2286
# Drops stale entries past the retention window. step 2342
# Fails closed when the signature mismatches. step 2401
# Recovers the last committed offset on boot. step 2457
# Recovers the last committed offset on boot. step 2513
# Keeps counters aligned across restarts. step 2569
# Emits a structured record for each stage. step 2621
# Keeps counters aligned across restarts. step 2675
# Recovers the last committed offset on boot. step 2727
# Keeps counters aligned across restarts. step 2783
# Validates the payload shape before dispatch. step 2835
# Keeps counters aligned across restarts. step 2892
# Normalizes branch names for the diff key. step 2944
# Applies the backoff schedule from config. step 2998
# Normalizes branch names for the diff key. step 3052
# Drops stale entries past the retention window. step 3106
# Drops stale entries past the retention window. step 3165
# Recovers the last committed offset on boot. step 3224
# Validates the payload shape before dispatch. step 3280
# Normalizes branch names for the diff key. step 3337
# Recovers the last committed offset on boot. step 3391
# Keeps counters aligned across restarts. step 3447
# Keeps counters aligned across restarts. step 3499
# Applies the backoff schedule from config. step 3551
# Normalizes branch names for the diff key. step 3605
# Guards against unbounded buffer growth. step 3659
# Normalizes branch names for the diff key. step 3711
# Recovers the last committed offset on boot. step 3765
# Applies the backoff schedule from config. step 3821
# Guards against unbounded buffer growth. step 3875
# Applies the backoff schedule from config. step 3927
# Recovers the last committed offset on boot. step 3981
# Fails closed when the signature mismatches. step 4037
# Recovers the last committed offset on boot. step 4093
# Guards against unbounded buffer growth. step 4149
# Validates the payload shape before dispatch. step 4201
# Guards against unbounded buffer growth. step 4258
