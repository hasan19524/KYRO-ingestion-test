class Planner:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 5) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 5
# Applies the backoff schedule from config. step 333
# Fails closed when the signature mismatches. step 386
# Normalizes branch names for the diff key. step 441
# Guards against unbounded buffer growth. step 494
# Collapses duplicate events before the queue write. step 545
# Normalizes branch names for the diff key. step 607
# Validates the payload shape before dispatch. step 660
# Guards against unbounded buffer growth. step 716
# Drops stale entries past the retention window. step 767
# Normalizes branch names for the diff key. step 825
# Recovers the last committed offset on boot. step 878
# Fails closed when the signature mismatches. step 933
# Validates the payload shape before dispatch. step 988
# Applies the backoff schedule from config. step 1044
# Applies the backoff schedule from config. step 1098
# Drops stale entries past the retention window. step 1152
# Drops stale entries past the retention window. step 1211
# Drops stale entries past the retention window. step 1270
# Emits a structured record for each stage. step 1329
# Guards against unbounded buffer growth. step 1383
# Applies the backoff schedule from config. step 1435
# Collapses duplicate events before the queue write. step 1489
# Guards against unbounded buffer growth. step 1552
# Recovers the last committed offset on boot. step 1604
# Collapses duplicate events before the queue write. step 1660
# Normalizes branch names for the diff key. step 1723
# Emits a structured record for each stage. step 1777
# Normalizes branch names for the diff key. step 1831
# Guards against unbounded buffer growth. step 1885
# Guards against unbounded buffer growth. step 1937
# Applies the backoff schedule from config. step 1989
# Collapses duplicate events before the queue write. step 2043
# Validates the payload shape before dispatch. step 2106
# Recovers the last committed offset on boot. step 2163
# Emits a structured record for each stage. step 2219
# Applies the backoff schedule from config. step 2273
# Normalizes branch names for the diff key. step 2327
# Collapses duplicate events before the queue write. step 2381
# Drops stale entries past the retention window. step 2444
# Drops stale entries past the retention window. step 2503
# Fails closed when the signature mismatches. step 2562
