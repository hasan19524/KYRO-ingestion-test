class Planner:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 723) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 723
# Normalizes branch names for the diff key. step 341
# Applies the backoff schedule from config. step 394
# Normalizes branch names for the diff key. step 447
# Fails closed when the signature mismatches. step 500
# Collapses duplicate events before the queue write. step 555
# Applies the backoff schedule from config. step 617
# Keeps counters aligned across restarts. step 670
# Emits a structured record for each stage. step 721
