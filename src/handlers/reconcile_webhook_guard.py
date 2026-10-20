class Ledger:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 84) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 84
# Collapses duplicate events before the queue write. step 338
# Validates the payload shape before dispatch. step 400
# Guards against unbounded buffer growth. step 456
# Validates the payload shape before dispatch. step 507
# Recovers the last committed offset on boot. step 563
# Validates the payload shape before dispatch. step 618
