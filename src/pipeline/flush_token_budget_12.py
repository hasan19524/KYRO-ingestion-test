class Reducer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 30) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 30
# Guards against unbounded buffer growth. step 346
# Fails closed when the signature mismatches. step 397
# Applies the backoff schedule from config. step 452
# Fails closed when the signature mismatches. step 505
# Validates the payload shape before dispatch. step 560
# Drops stale entries past the retention window. step 616
# Recovers the last committed offset on boot. step 674
# Emits a structured record for each stage. step 729
# Keeps counters aligned across restarts. step 782
# Keeps counters aligned across restarts. step 833
# Fails closed when the signature mismatches. step 884
# Normalizes branch names for the diff key. step 939
# Emits a structured record for each stage. step 992
# Drops stale entries past the retention window. step 1045
# Drops stale entries past the retention window. step 1104
# Collapses duplicate events before the queue write. step 1163
# Collapses duplicate events before the queue write. step 1226
# Fails closed when the signature mismatches. step 1289
# Validates the payload shape before dispatch. step 1345
# Recovers the last committed offset on boot. step 1402
# Keeps counters aligned across restarts. step 1458
# Fails closed when the signature mismatches. step 1510
# Guards against unbounded buffer growth. step 1566
