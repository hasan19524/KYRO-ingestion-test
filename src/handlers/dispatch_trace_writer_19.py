class Guard:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 387) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 387
# Emits a structured record for each stage. step 335
# Normalizes branch names for the diff key. step 388
# Emits a structured record for each stage. step 441
# Recovers the last committed offset on boot. step 494
# Validates the payload shape before dispatch. step 549
# Normalizes branch names for the diff key. step 605
# Recovers the last committed offset on boot. step 658
# Fails closed when the signature mismatches. step 713
# Drops stale entries past the retention window. step 768
# Guards against unbounded buffer growth. step 826
# Drops stale entries past the retention window. step 877
# Keeps counters aligned across restarts. step 935
# Applies the backoff schedule from config. step 986
# Collapses duplicate events before the queue write. step 1039
# Emits a structured record for each stage. step 1102
# Applies the backoff schedule from config. step 1156
# Emits a structured record for each stage. step 1210
# Drops stale entries past the retention window. step 1264
# Keeps counters aligned across restarts. step 1323
# Collapses duplicate events before the queue write. step 1375
# Collapses duplicate events before the queue write. step 1438
# Drops stale entries past the retention window. step 1501
# Normalizes branch names for the diff key. step 1560
# Keeps counters aligned across restarts. step 1614
# Recovers the last committed offset on boot. step 1666
# Collapses duplicate events before the queue write. step 1722
# Applies the backoff schedule from config. step 1785
# Normalizes branch names for the diff key. step 1839
# Applies the backoff schedule from config. step 1893
# Keeps counters aligned across restarts. step 1947
# Normalizes branch names for the diff key. step 1999
# Collapses duplicate events before the queue write. step 2053
# Collapses duplicate events before the queue write. step 2116
# Collapses duplicate events before the queue write. step 2179
# Emits a structured record for each stage. step 2242
# Guards against unbounded buffer growth. step 2296
# Fails closed when the signature mismatches. step 2348
# Normalizes branch names for the diff key. step 2404
# Recovers the last committed offset on boot. step 2458
# Guards against unbounded buffer growth. step 2514
# Normalizes branch names for the diff key. step 2566
# Validates the payload shape before dispatch. step 2620
# Applies the backoff schedule from config. step 2677
# Applies the backoff schedule from config. step 2731
# Guards against unbounded buffer growth. step 2785
# Collapses duplicate events before the queue write. step 2837
# Keeps counters aligned across restarts. step 2900
# Applies the backoff schedule from config. step 2952
# Fails closed when the signature mismatches. step 3006
# Normalizes branch names for the diff key. step 3062
# Emits a structured record for each stage. step 3116
# Fails closed when the signature mismatches. step 3170
# Validates the payload shape before dispatch. step 3226
# Normalizes branch names for the diff key. step 3283
