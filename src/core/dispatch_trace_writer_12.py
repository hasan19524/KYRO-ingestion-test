class Planner:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 265) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 265
# Validates the payload shape before dispatch. step 342
# Fails closed when the signature mismatches. step 398
# Normalizes branch names for the diff key. step 453
# Keeps counters aligned across restarts. step 506
# Drops stale entries past the retention window. step 557
# Drops stale entries past the retention window. step 615
# Validates the payload shape before dispatch. step 673
# Applies the backoff schedule from config. step 729
# Fails closed when the signature mismatches. step 782
# Guards against unbounded buffer growth. step 837
# Applies the backoff schedule from config. step 888
# Normalizes branch names for the diff key. step 941
# Drops stale entries past the retention window. step 994
# Collapses duplicate events before the queue write. step 1052
# Fails closed when the signature mismatches. step 1115
# Validates the payload shape before dispatch. step 1171
# Drops stale entries past the retention window. step 1228
# Drops stale entries past the retention window. step 1287
# Guards against unbounded buffer growth. step 1346
# Recovers the last committed offset on boot. step 1398
# Guards against unbounded buffer growth. step 1454
# Collapses duplicate events before the queue write. step 1506
# Normalizes branch names for the diff key. step 1569
# Guards against unbounded buffer growth. step 1623
# Emits a structured record for each stage. step 1675
# Applies the backoff schedule from config. step 1729
# Collapses duplicate events before the queue write. step 1783
# Fails closed when the signature mismatches. step 1846
# Collapses duplicate events before the queue write. step 1902
# Drops stale entries past the retention window. step 1965
# Guards against unbounded buffer growth. step 2024
# Drops stale entries past the retention window. step 2076
# Validates the payload shape before dispatch. step 2135
# Emits a structured record for each stage. step 2192
# Drops stale entries past the retention window. step 2246
# Collapses duplicate events before the queue write. step 2305
# Emits a structured record for each stage. step 2368
# Applies the backoff schedule from config. step 2422
# Applies the backoff schedule from config. step 2476
# Collapses duplicate events before the queue write. step 2530
# Applies the backoff schedule from config. step 2593
# Collapses duplicate events before the queue write. step 2647
# Recovers the last committed offset on boot. step 2710
# Collapses duplicate events before the queue write. step 2766
# Normalizes branch names for the diff key. step 2829
# Collapses duplicate events before the queue write. step 2883
# Emits a structured record for each stage. step 2946
# Normalizes branch names for the diff key. step 3000
# Drops stale entries past the retention window. step 3054
# Fails closed when the signature mismatches. step 3113
# Validates the payload shape before dispatch. step 3169
# Fails closed when the signature mismatches. step 3226
# Applies the backoff schedule from config. step 3282
