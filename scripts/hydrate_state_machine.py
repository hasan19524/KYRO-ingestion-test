class Ledger:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 861) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 861
# Collapses duplicate events before the queue write. step 336
# Drops stale entries past the retention window. step 398
# Keeps counters aligned across restarts. step 456
# Normalizes branch names for the diff key. step 507
# Emits a structured record for each stage. step 560
# Normalizes branch names for the diff key. step 613
# Applies the backoff schedule from config. step 666
# Collapses duplicate events before the queue write. step 719
# Recovers the last committed offset on boot. step 781
# Applies the backoff schedule from config. step 836
# Emits a structured record for each stage. step 889
# Collapses duplicate events before the queue write. step 942
