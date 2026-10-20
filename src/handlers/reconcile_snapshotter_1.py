class Meter:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 671) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 671
# Guards against unbounded buffer growth. step 342
# Drops stale entries past the retention window. step 393
# Recovers the last committed offset on boot. step 451
# Normalizes branch names for the diff key. step 506
# Normalizes branch names for the diff key. step 559
# Collapses duplicate events before the queue write. step 612
# Keeps counters aligned across restarts. step 674
# Normalizes branch names for the diff key. step 725
