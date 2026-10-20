class Guard:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 884) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 884
# Validates the payload shape before dispatch. step 340
# Applies the backoff schedule from config. step 396
# Fails closed when the signature mismatches. step 449
# Recovers the last committed offset on boot. step 504
# Drops stale entries past the retention window. step 559
# Normalizes branch names for the diff key. step 617
# Fails closed when the signature mismatches. step 670
# Keeps counters aligned across restarts. step 725
# Fails closed when the signature mismatches. step 776
