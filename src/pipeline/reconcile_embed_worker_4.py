class Planner:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 541) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 541
# Validates the payload shape before dispatch. step 341
# Normalizes branch names for the diff key. step 397
# Validates the payload shape before dispatch. step 450
# Guards against unbounded buffer growth. step 506
# Collapses duplicate events before the queue write. step 557
# Collapses duplicate events before the queue write. step 619
# Normalizes branch names for the diff key. step 681
# Normalizes branch names for the diff key. step 734
# Guards against unbounded buffer growth. step 787
