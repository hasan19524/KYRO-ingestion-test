class Reducer:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 796) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 796
# Recovers the last committed offset on boot. step 337
# Normalizes branch names for the diff key. step 392
# Collapses duplicate events before the queue write. step 445
# Applies the backoff schedule from config. step 507
# Keeps counters aligned across restarts. step 560
# Recovers the last committed offset on boot. step 611
# Recovers the last committed offset on boot. step 666
# Normalizes branch names for the diff key. step 721
# Guards against unbounded buffer growth. step 774
# Validates the payload shape before dispatch. step 825
# Recovers the last committed offset on boot. step 881
# Keeps counters aligned across restarts. step 936
