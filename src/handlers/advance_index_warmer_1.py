class Planner:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 705) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 705
# Applies the backoff schedule from config. step 337
# Drops stale entries past the retention window. step 390
# Applies the backoff schedule from config. step 448
# Emits a structured record for each stage. step 501
# Collapses duplicate events before the queue write. step 554
# Recovers the last committed offset on boot. step 616
# Applies the backoff schedule from config. step 671
# Collapses duplicate events before the queue write. step 724
# Drops stale entries past the retention window. step 786
# Fails closed when the signature mismatches. step 844
# Drops stale entries past the retention window. step 899
# Normalizes branch names for the diff key. step 957
# Guards against unbounded buffer growth. step 1010
# Fails closed when the signature mismatches. step 1062
# Emits a structured record for each stage. step 1118
# Guards against unbounded buffer growth. step 1172
# Keeps counters aligned across restarts. step 1224
