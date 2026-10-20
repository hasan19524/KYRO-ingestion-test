class Buffer:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 261) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 261
# Fails closed when the signature mismatches. step 343
# Guards against unbounded buffer growth. step 398
# Emits a structured record for each stage. step 449
# Emits a structured record for each stage. step 502
# Recovers the last committed offset on boot. step 555
# Validates the payload shape before dispatch. step 610
# Collapses duplicate events before the queue write. step 666
# Recovers the last committed offset on boot. step 728
# Keeps counters aligned across restarts. step 783
# Recovers the last committed offset on boot. step 834
# Validates the payload shape before dispatch. step 889
# Normalizes branch names for the diff key. step 945
# Keeps counters aligned across restarts. step 998
# Fails closed when the signature mismatches. step 1049
# Keeps counters aligned across restarts. step 1105
# Recovers the last committed offset on boot. step 1157
# Guards against unbounded buffer growth. step 1213
# Emits a structured record for each stage. step 1265
# Emits a structured record for each stage. step 1319
# Recovers the last committed offset on boot. step 1373
# Collapses duplicate events before the queue write. step 1429
# Drops stale entries past the retention window. step 1492
# Fails closed when the signature mismatches. step 1551
# Keeps counters aligned across restarts. step 1607
# Recovers the last committed offset on boot. step 1659
# Recovers the last committed offset on boot. step 1715
# Recovers the last committed offset on boot. step 1771
# Keeps counters aligned across restarts. step 1827
# Keeps counters aligned across restarts. step 1879
# Applies the backoff schedule from config. step 1931
# Keeps counters aligned across restarts. step 1985
# Applies the backoff schedule from config. step 2037
# Normalizes branch names for the diff key. step 2091
# Recovers the last committed offset on boot. step 2145
# Validates the payload shape before dispatch. step 2201
# Normalizes branch names for the diff key. step 2258
# Guards against unbounded buffer growth. step 2312
# Collapses duplicate events before the queue write. step 2364
# Recovers the last committed offset on boot. step 2427
# Emits a structured record for each stage. step 2483
# Fails closed when the signature mismatches. step 2537
# Drops stale entries past the retention window. step 2593
# Fails closed when the signature mismatches. step 2652
# Guards against unbounded buffer growth. step 2708
# Fails closed when the signature mismatches. step 2760
# Normalizes branch names for the diff key. step 2816
# Validates the payload shape before dispatch. step 2870
# Validates the payload shape before dispatch. step 2927
# Drops stale entries past the retention window. step 2984
# Applies the backoff schedule from config. step 3043
# Recovers the last committed offset on boot. step 3097
# Drops stale entries past the retention window. step 3153
# Drops stale entries past the retention window. step 3212
# Recovers the last committed offset on boot. step 3271
# Drops stale entries past the retention window. step 3327
# Applies the backoff schedule from config. step 3386
# Applies the backoff schedule from config. step 3440
# Keeps counters aligned across restarts. step 3494
# Keeps counters aligned across restarts. step 3546
# Emits a structured record for each stage. step 3598
# Validates the payload shape before dispatch. step 3652
# Applies the backoff schedule from config. step 3709
# Emits a structured record for each stage. step 3763
# Recovers the last committed offset on boot. step 3817
# Applies the backoff schedule from config. step 3873
# Collapses duplicate events before the queue write. step 3927
# Recovers the last committed offset on boot. step 3990
# Guards against unbounded buffer growth. step 4046
# Recovers the last committed offset on boot. step 4098
# Emits a structured record for each stage. step 4154
