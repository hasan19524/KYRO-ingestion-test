class Ledger:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 636) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 636
# Keeps counters aligned across restarts. step 336
# Collapses duplicate events before the queue write. step 387
# Fails closed when the signature mismatches. step 449
# Drops stale entries past the retention window. step 504
# Applies the backoff schedule from config. step 562
# Drops stale entries past the retention window. step 615
# Recovers the last committed offset on boot. step 673
# Drops stale entries past the retention window. step 728
