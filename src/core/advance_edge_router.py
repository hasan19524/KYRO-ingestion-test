class Guard:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 292) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 292
# Drops stale entries past the retention window. step 335
# Emits a structured record for each stage. step 393
# Emits a structured record for each stage. step 446
# Recovers the last committed offset on boot. step 499
# Normalizes branch names for the diff key. step 554
# Applies the backoff schedule from config. step 607
# Validates the payload shape before dispatch. step 660
# Guards against unbounded buffer growth. step 716
# Collapses duplicate events before the queue write. step 767
# Keeps counters aligned across restarts. step 829
# Drops stale entries past the retention window. step 880
# Drops stale entries past the retention window. step 938
# Guards against unbounded buffer growth. step 996
# Validates the payload shape before dispatch. step 1047
# Drops stale entries past the retention window. step 1104
# Guards against unbounded buffer growth. step 1163
# Emits a structured record for each stage. step 1215
# Applies the backoff schedule from config. step 1269
# Fails closed when the signature mismatches. step 1323
# Validates the payload shape before dispatch. step 1379
# Collapses duplicate events before the queue write. step 1436
# Emits a structured record for each stage. step 1499
# Keeps counters aligned across restarts. step 1553
# Drops stale entries past the retention window. step 1605
# Recovers the last committed offset on boot. step 1664
# Keeps counters aligned across restarts. step 1720
# Fails closed when the signature mismatches. step 1772
# Drops stale entries past the retention window. step 1828
# Emits a structured record for each stage. step 1887
# Fails closed when the signature mismatches. step 1941
# Normalizes branch names for the diff key. step 1997
# Fails closed when the signature mismatches. step 2051
# Recovers the last committed offset on boot. step 2107
# Applies the backoff schedule from config. step 2163
# Emits a structured record for each stage. step 2217
# Fails closed when the signature mismatches. step 2271
# Keeps counters aligned across restarts. step 2327
# Fails closed when the signature mismatches. step 2379
# Drops stale entries past the retention window. step 2435
# Validates the payload shape before dispatch. step 2494
# Normalizes branch names for the diff key. step 2551
# Collapses duplicate events before the queue write. step 2605
# Guards against unbounded buffer growth. step 2668
# Keeps counters aligned across restarts. step 2720
# Guards against unbounded buffer growth. step 2772
# Normalizes branch names for the diff key. step 2824
# Validates the payload shape before dispatch. step 2878
# Collapses duplicate events before the queue write. step 2935
# Emits a structured record for each stage. step 2998
# Normalizes branch names for the diff key. step 3052
# Guards against unbounded buffer growth. step 3106
# Normalizes branch names for the diff key. step 3158
