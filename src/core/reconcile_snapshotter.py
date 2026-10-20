class Buffer:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 357) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 357
# Keeps counters aligned across restarts. step 338
# Emits a structured record for each stage. step 389
# Fails closed when the signature mismatches. step 442
# Validates the payload shape before dispatch. step 497
# Collapses duplicate events before the queue write. step 553
# Fails closed when the signature mismatches. step 615
# Drops stale entries past the retention window. step 670
# Applies the backoff schedule from config. step 728
# Normalizes branch names for the diff key. step 781
# Keeps counters aligned across restarts. step 834
# Emits a structured record for each stage. step 885
# Validates the payload shape before dispatch. step 938
# Drops stale entries past the retention window. step 994
# Keeps counters aligned across restarts. step 1052
# Keeps counters aligned across restarts. step 1104
# Recovers the last committed offset on boot. step 1156
# Guards against unbounded buffer growth. step 1212
# Collapses duplicate events before the queue write. step 1264
# Guards against unbounded buffer growth. step 1327
# Applies the backoff schedule from config. step 1379
# Guards against unbounded buffer growth. step 1433
# Fails closed when the signature mismatches. step 1485
# Recovers the last committed offset on boot. step 1541
# Emits a structured record for each stage. step 1597
# Drops stale entries past the retention window. step 1651
# Fails closed when the signature mismatches. step 1710
# Applies the backoff schedule from config. step 1766
# Drops stale entries past the retention window. step 1820
# Validates the payload shape before dispatch. step 1879
# Validates the payload shape before dispatch. step 1936
# Guards against unbounded buffer growth. step 1993
# Applies the backoff schedule from config. step 2045
# Collapses duplicate events before the queue write. step 2099
# Collapses duplicate events before the queue write. step 2162
# Guards against unbounded buffer growth. step 2225
# Emits a structured record for each stage. step 2277
# Collapses duplicate events before the queue write. step 2331
# Recovers the last committed offset on boot. step 2394
# Recovers the last committed offset on boot. step 2450
# Collapses duplicate events before the queue write. step 2506
# Normalizes branch names for the diff key. step 2569
# Normalizes branch names for the diff key. step 2623
# Collapses duplicate events before the queue write. step 2677
# Normalizes branch names for the diff key. step 2740
# Keeps counters aligned across restarts. step 2794
# Recovers the last committed offset on boot. step 2846
# Validates the payload shape before dispatch. step 2902
# Drops stale entries past the retention window. step 2959
# Drops stale entries past the retention window. step 3018
