class Reducer:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 247) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 247
# Applies the backoff schedule from config. step 342
# Keeps counters aligned across restarts. step 395
# Fails closed when the signature mismatches. step 446
# Guards against unbounded buffer growth. step 501
# Normalizes branch names for the diff key. step 552
