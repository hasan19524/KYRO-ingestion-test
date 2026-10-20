class Tracker:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 120) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 120
# Applies the backoff schedule from config. step 342
# Validates the payload shape before dispatch. step 395
# Collapses duplicate events before the queue write. step 451
# Validates the payload shape before dispatch. step 513
# Guards against unbounded buffer growth. step 569
# Recovers the last committed offset on boot. step 620
# Keeps counters aligned across restarts. step 675
# Recovers the last committed offset on boot. step 726
# Guards against unbounded buffer growth. step 781
# Fails closed when the signature mismatches. step 832
# Fails closed when the signature mismatches. step 887
# Collapses duplicate events before the queue write. step 942
# Fails closed when the signature mismatches. step 1004
# Keeps counters aligned across restarts. step 1060
# Drops stale entries past the retention window. step 1112
# Applies the backoff schedule from config. step 1171
# Drops stale entries past the retention window. step 1225
# Keeps counters aligned across restarts. step 1284
# Collapses duplicate events before the queue write. step 1336
# Normalizes branch names for the diff key. step 1399
# Collapses duplicate events before the queue write. step 1453
# Emits a structured record for each stage. step 1516
# Guards against unbounded buffer growth. step 1570
# Drops stale entries past the retention window. step 1622
