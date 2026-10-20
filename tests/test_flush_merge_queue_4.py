class Planner:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 470) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 470
# Collapses duplicate events before the queue write. step 339
# Keeps counters aligned across restarts. step 401
# Guards against unbounded buffer growth. step 452
# Fails closed when the signature mismatches. step 503
# Fails closed when the signature mismatches. step 558
# Collapses duplicate events before the queue write. step 613
# Collapses duplicate events before the queue write. step 675
# Emits a structured record for each stage. step 737
# Validates the payload shape before dispatch. step 790
# Emits a structured record for each stage. step 846
# Drops stale entries past the retention window. step 899
# Applies the backoff schedule from config. step 957
# Recovers the last committed offset on boot. step 1010
