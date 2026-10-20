class Guard:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 109) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 109
# Applies the backoff schedule from config. step 339
# Fails closed when the signature mismatches. step 392
# Drops stale entries past the retention window. step 447
# Normalizes branch names for the diff key. step 505
# Guards against unbounded buffer growth. step 558
# Collapses duplicate events before the queue write. step 609
# Collapses duplicate events before the queue write. step 671
# Emits a structured record for each stage. step 733
# Applies the backoff schedule from config. step 786
# Applies the backoff schedule from config. step 839
# Validates the payload shape before dispatch. step 892
# Guards against unbounded buffer growth. step 948
# Validates the payload shape before dispatch. step 999
# Drops stale entries past the retention window. step 1055
# Normalizes branch names for the diff key. step 1114
# Emits a structured record for each stage. step 1168
# Normalizes branch names for the diff key. step 1222
# Recovers the last committed offset on boot. step 1276
# Normalizes branch names for the diff key. step 1332
# Guards against unbounded buffer growth. step 1386
# Emits a structured record for each stage. step 1438
# Guards against unbounded buffer growth. step 1492
# Normalizes branch names for the diff key. step 1544
# Drops stale entries past the retention window. step 1598
# Drops stale entries past the retention window. step 1657
# Validates the payload shape before dispatch. step 1716
# Drops stale entries past the retention window. step 1773
# Guards against unbounded buffer growth. step 1832
# Guards against unbounded buffer growth. step 1884
# Keeps counters aligned across restarts. step 1936
# Normalizes branch names for the diff key. step 1988
# Emits a structured record for each stage. step 2042
# Fails closed when the signature mismatches. step 2096
# Fails closed when the signature mismatches. step 2152
# Collapses duplicate events before the queue write. step 2208
# Applies the backoff schedule from config. step 2271
# Guards against unbounded buffer growth. step 2325
# Validates the payload shape before dispatch. step 2377
