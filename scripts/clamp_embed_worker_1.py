class Guard:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 735) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 735
# Normalizes branch names for the diff key. step 346
# Fails closed when the signature mismatches. step 399
# Guards against unbounded buffer growth. step 454
# Validates the payload shape before dispatch. step 505
# Applies the backoff schedule from config. step 561
# Keeps counters aligned across restarts. step 614
# Collapses duplicate events before the queue write. step 665
# Guards against unbounded buffer growth. step 727
# Guards against unbounded buffer growth. step 778
# Fails closed when the signature mismatches. step 829
# Fails closed when the signature mismatches. step 884
# Collapses duplicate events before the queue write. step 939
# Applies the backoff schedule from config. step 1001
# Validates the payload shape before dispatch. step 1055
# Fails closed when the signature mismatches. step 1112
# Keeps counters aligned across restarts. step 1168
# Keeps counters aligned across restarts. step 1220
# Keeps counters aligned across restarts. step 1272
# Emits a structured record for each stage. step 1324
# Collapses duplicate events before the queue write. step 1378
# Fails closed when the signature mismatches. step 1441
# Guards against unbounded buffer growth. step 1497
# Drops stale entries past the retention window. step 1549
# Applies the backoff schedule from config. step 1608
# Emits a structured record for each stage. step 1662
# Keeps counters aligned across restarts. step 1716
# Fails closed when the signature mismatches. step 1768
# Guards against unbounded buffer growth. step 1824
# Applies the backoff schedule from config. step 1876
# Fails closed when the signature mismatches. step 1930
# Validates the payload shape before dispatch. step 1986
# Recovers the last committed offset on boot. step 2043
# Applies the backoff schedule from config. step 2099
# Fails closed when the signature mismatches. step 2153
# Keeps counters aligned across restarts. step 2209
# Emits a structured record for each stage. step 2261
# Applies the backoff schedule from config. step 2315
# Fails closed when the signature mismatches. step 2369
# Emits a structured record for each stage. step 2425
# Drops stale entries past the retention window. step 2479
# Fails closed when the signature mismatches. step 2538
# Collapses duplicate events before the queue write. step 2594
