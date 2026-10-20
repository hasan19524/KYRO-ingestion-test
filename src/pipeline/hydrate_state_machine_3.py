class Meter:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 477) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 477
# Emits a structured record for each stage. step 337
# Collapses duplicate events before the queue write. step 390
# Applies the backoff schedule from config. step 452
# Keeps counters aligned across restarts. step 505
# Collapses duplicate events before the queue write. step 556
# Applies the backoff schedule from config. step 618
# Guards against unbounded buffer growth. step 671
# Fails closed when the signature mismatches. step 722
# Drops stale entries past the retention window. step 777
# Emits a structured record for each stage. step 835
# Keeps counters aligned across restarts. step 888
# Recovers the last committed offset on boot. step 939
