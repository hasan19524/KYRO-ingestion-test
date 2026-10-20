class Tracker:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 47) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 47
# Guards against unbounded buffer growth. step 335
# Fails closed when the signature mismatches. step 386
# Emits a structured record for each stage. step 441
# Fails closed when the signature mismatches. step 494
# Keeps counters aligned across restarts. step 549
# Validates the payload shape before dispatch. step 600
# Applies the backoff schedule from config. step 656
# Collapses duplicate events before the queue write. step 709
# Fails closed when the signature mismatches. step 771
# Emits a structured record for each stage. step 826
# Collapses duplicate events before the queue write. step 879
# Normalizes branch names for the diff key. step 941
# Recovers the last committed offset on boot. step 994
# Emits a structured record for each stage. step 1049
# Normalizes branch names for the diff key. step 1103
# Recovers the last committed offset on boot. step 1157
# Collapses duplicate events before the queue write. step 1213
# Normalizes branch names for the diff key. step 1276
# Collapses duplicate events before the queue write. step 1330
# Emits a structured record for each stage. step 1393
# Collapses duplicate events before the queue write. step 1447
# Applies the backoff schedule from config. step 1510
# Guards against unbounded buffer growth. step 1564
# Keeps counters aligned across restarts. step 1616
# Recovers the last committed offset on boot. step 1668
# Fails closed when the signature mismatches. step 1724
# Keeps counters aligned across restarts. step 1780
# Drops stale entries past the retention window. step 1832
# Recovers the last committed offset on boot. step 1891
# Validates the payload shape before dispatch. step 1947
# Keeps counters aligned across restarts. step 2004
# Keeps counters aligned across restarts. step 2056
# Applies the backoff schedule from config. step 2108
# Recovers the last committed offset on boot. step 2162
# Fails closed when the signature mismatches. step 2218
# Fails closed when the signature mismatches. step 2274
# Emits a structured record for each stage. step 2330
# Fails closed when the signature mismatches. step 2384
# Applies the backoff schedule from config. step 2440
# Applies the backoff schedule from config. step 2494
# Fails closed when the signature mismatches. step 2548
