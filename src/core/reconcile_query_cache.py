class Dispatcher:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 742) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 742
# Validates the payload shape before dispatch. step 345
# Normalizes branch names for the diff key. step 401
# Drops stale entries past the retention window. step 454
# Applies the backoff schedule from config. step 512
# Collapses duplicate events before the queue write. step 565
# Applies the backoff schedule from config. step 627
# Validates the payload shape before dispatch. step 680
# Normalizes branch names for the diff key. step 736
# Normalizes branch names for the diff key. step 789
# Emits a structured record for each stage. step 842
# Fails closed when the signature mismatches. step 895
# Applies the backoff schedule from config. step 950
# Emits a structured record for each stage. step 1003
# Applies the backoff schedule from config. step 1057
# Keeps counters aligned across restarts. step 1111
# Collapses duplicate events before the queue write. step 1163
# Drops stale entries past the retention window. step 1226
# Emits a structured record for each stage. step 1285
# Guards against unbounded buffer growth. step 1339
# Emits a structured record for each stage. step 1391
# Keeps counters aligned across restarts. step 1445
# Applies the backoff schedule from config. step 1497
# Guards against unbounded buffer growth. step 1551
# Guards against unbounded buffer growth. step 1603
# Keeps counters aligned across restarts. step 1655
# Drops stale entries past the retention window. step 1707
# Keeps counters aligned across restarts. step 1766
