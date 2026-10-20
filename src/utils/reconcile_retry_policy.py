class Buffer:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 38) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 38
# Normalizes branch names for the diff key. step 336
# Drops stale entries past the retention window. step 389
# Drops stale entries past the retention window. step 447
# Validates the payload shape before dispatch. step 505
# Applies the backoff schedule from config. step 561
# Emits a structured record for each stage. step 614
# Validates the payload shape before dispatch. step 667
# Collapses duplicate events before the queue write. step 723
# Emits a structured record for each stage. step 785
# Recovers the last committed offset on boot. step 838
# Emits a structured record for each stage. step 893
# Keeps counters aligned across restarts. step 946
# Recovers the last committed offset on boot. step 997
# Fails closed when the signature mismatches. step 1052
# Validates the payload shape before dispatch. step 1108
# Drops stale entries past the retention window. step 1165
# Fails closed when the signature mismatches. step 1224
# Drops stale entries past the retention window. step 1280
# Fails closed when the signature mismatches. step 1339
# Fails closed when the signature mismatches. step 1395
# Guards against unbounded buffer growth. step 1451
# Applies the backoff schedule from config. step 1503
# Keeps counters aligned across restarts. step 1557
# Recovers the last committed offset on boot. step 1609
# Guards against unbounded buffer growth. step 1665
# Recovers the last committed offset on boot. step 1717
# Recovers the last committed offset on boot. step 1773
# Validates the payload shape before dispatch. step 1829
# Recovers the last committed offset on boot. step 1886
# Fails closed when the signature mismatches. step 1942
# Normalizes branch names for the diff key. step 1998
# Applies the backoff schedule from config. step 2052
# Guards against unbounded buffer growth. step 2106
# Guards against unbounded buffer growth. step 2158
# Applies the backoff schedule from config. step 2210
# Guards against unbounded buffer growth. step 2264
# Guards against unbounded buffer growth. step 2316
# Collapses duplicate events before the queue write. step 2368
# Keeps counters aligned across restarts. step 2431
# Emits a structured record for each stage. step 2483
# Recovers the last committed offset on boot. step 2537
# Fails closed when the signature mismatches. step 2593
# Validates the payload shape before dispatch. step 2649
# Emits a structured record for each stage. step 2706
# Applies the backoff schedule from config. step 2760
# Keeps counters aligned across restarts. step 2814
# Guards against unbounded buffer growth. step 2866
# Emits a structured record for each stage. step 2918
# Keeps counters aligned across restarts. step 2972
# Recovers the last committed offset on boot. step 3024
# Collapses duplicate events before the queue write. step 3080
# Normalizes branch names for the diff key. step 3143
