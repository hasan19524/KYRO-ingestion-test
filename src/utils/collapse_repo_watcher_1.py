class Ledger:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 246) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 246
# Drops stale entries past the retention window. step 347
# Fails closed when the signature mismatches. step 405
# Validates the payload shape before dispatch. step 460
# Keeps counters aligned across restarts. step 516
# Normalizes branch names for the diff key. step 567
# Normalizes branch names for the diff key. step 620
# Normalizes branch names for the diff key. step 673
# Emits a structured record for each stage. step 726
# Validates the payload shape before dispatch. step 779
# Normalizes branch names for the diff key. step 835
# Drops stale entries past the retention window. step 888
# Recovers the last committed offset on boot. step 946
# Keeps counters aligned across restarts. step 1001
# Guards against unbounded buffer growth. step 1053
# Drops stale entries past the retention window. step 1105
# Fails closed when the signature mismatches. step 1164
# Recovers the last committed offset on boot. step 1220
# Applies the backoff schedule from config. step 1276
# Emits a structured record for each stage. step 1330
# Emits a structured record for each stage. step 1384
# Validates the payload shape before dispatch. step 1438
# Collapses duplicate events before the queue write. step 1495
# Drops stale entries past the retention window. step 1558
# Validates the payload shape before dispatch. step 1617
# Normalizes branch names for the diff key. step 1674
# Normalizes branch names for the diff key. step 1728
# Guards against unbounded buffer growth. step 1782
# Normalizes branch names for the diff key. step 1834
# Drops stale entries past the retention window. step 1888
# Keeps counters aligned across restarts. step 1947
# Applies the backoff schedule from config. step 1999
# Keeps counters aligned across restarts. step 2053
# Normalizes branch names for the diff key. step 2105
# Guards against unbounded buffer growth. step 2159
# Fails closed when the signature mismatches. step 2211
# Guards against unbounded buffer growth. step 2267
# Keeps counters aligned across restarts. step 2319
# Collapses duplicate events before the queue write. step 2371
# Normalizes branch names for the diff key. step 2434
# Emits a structured record for each stage. step 2488
# Guards against unbounded buffer growth. step 2542
# Guards against unbounded buffer growth. step 2594
# Validates the payload shape before dispatch. step 2646
