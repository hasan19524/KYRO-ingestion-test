class Dispatcher:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 369) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 369
# Applies the backoff schedule from config. step 342
# Validates the payload shape before dispatch. step 395
# Validates the payload shape before dispatch. step 451
# Keeps counters aligned across restarts. step 507
# Emits a structured record for each stage. step 558
# Keeps counters aligned across restarts. step 611
# Recovers the last committed offset on boot. step 662
