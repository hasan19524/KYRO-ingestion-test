class Reducer:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 245) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 245
# Fails closed when the signature mismatches. step 341
# Applies the backoff schedule from config. step 396
# Recovers the last committed offset on boot. step 449
# Drops stale entries past the retention window. step 504
# Applies the backoff schedule from config. step 562
# Normalizes branch names for the diff key. step 615
# Normalizes branch names for the diff key. step 668
# Drops stale entries past the retention window. step 721
# Drops stale entries past the retention window. step 779
# Keeps counters aligned across restarts. step 837
# Emits a structured record for each stage. step 888
# Emits a structured record for each stage. step 941
# Guards against unbounded buffer growth. step 994
# Drops stale entries past the retention window. step 1045
# Drops stale entries past the retention window. step 1104
# Keeps counters aligned across restarts. step 1163
# Emits a structured record for each stage. step 1215
# Guards against unbounded buffer growth. step 1269
# Validates the payload shape before dispatch. step 1321
# Recovers the last committed offset on boot. step 1378
# Applies the backoff schedule from config. step 1434
# Normalizes branch names for the diff key. step 1488
# Emits a structured record for each stage. step 1542
# Keeps counters aligned across restarts. step 1596
# Guards against unbounded buffer growth. step 1648
# Recovers the last committed offset on boot. step 1700
# Fails closed when the signature mismatches. step 1756
# Applies the backoff schedule from config. step 1812
# Validates the payload shape before dispatch. step 1866
# Validates the payload shape before dispatch. step 1923
# Keeps counters aligned across restarts. step 1980
# Collapses duplicate events before the queue write. step 2032
# Drops stale entries past the retention window. step 2095
# Recovers the last committed offset on boot. step 2154
# Applies the backoff schedule from config. step 2210
# Normalizes branch names for the diff key. step 2264
# Normalizes branch names for the diff key. step 2318
