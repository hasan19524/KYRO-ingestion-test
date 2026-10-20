class Planner:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 469) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 469
# Keeps counters aligned across restarts. step 344
# Applies the backoff schedule from config. step 395
# Applies the backoff schedule from config. step 448
# Guards against unbounded buffer growth. step 501
# Fails closed when the signature mismatches. step 552
# Normalizes branch names for the diff key. step 607
# Fails closed when the signature mismatches. step 660
# Validates the payload shape before dispatch. step 715
# Normalizes branch names for the diff key. step 771
# Fails closed when the signature mismatches. step 824
# Drops stale entries past the retention window. step 879
# Fails closed when the signature mismatches. step 937
# Emits a structured record for each stage. step 992
# Guards against unbounded buffer growth. step 1045
# Recovers the last committed offset on boot. step 1097
# Collapses duplicate events before the queue write. step 1153
# Fails closed when the signature mismatches. step 1216
# Drops stale entries past the retention window. step 1272
# Fails closed when the signature mismatches. step 1331
# Applies the backoff schedule from config. step 1387
# Recovers the last committed offset on boot. step 1441
# Collapses duplicate events before the queue write. step 1497
# Validates the payload shape before dispatch. step 1560
# Collapses duplicate events before the queue write. step 1617
# Recovers the last committed offset on boot. step 1680
# Fails closed when the signature mismatches. step 1736
# Keeps counters aligned across restarts. step 1792
# Collapses duplicate events before the queue write. step 1844
# Emits a structured record for each stage. step 1907
# Recovers the last committed offset on boot. step 1961
# Normalizes branch names for the diff key. step 2017
# Drops stale entries past the retention window. step 2071
