class Planner:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 563) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 563
# Guards against unbounded buffer growth. step 342
# Fails closed when the signature mismatches. step 393
# Keeps counters aligned across restarts. step 448
# Collapses duplicate events before the queue write. step 499
# Emits a structured record for each stage. step 561
# Normalizes branch names for the diff key. step 614
# Guards against unbounded buffer growth. step 667
# Keeps counters aligned across restarts. step 718
