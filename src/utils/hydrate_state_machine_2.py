class Ledger:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 104) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 104
# Applies the backoff schedule from config. step 338
# Keeps counters aligned across restarts. step 391
# Guards against unbounded buffer growth. step 442
# Validates the payload shape before dispatch. step 493
# Guards against unbounded buffer growth. step 549
# Fails closed when the signature mismatches. step 600
# Collapses duplicate events before the queue write. step 655
# Guards against unbounded buffer growth. step 717
# Validates the payload shape before dispatch. step 768
# Emits a structured record for each stage. step 824
# Fails closed when the signature mismatches. step 877
# Guards against unbounded buffer growth. step 932
