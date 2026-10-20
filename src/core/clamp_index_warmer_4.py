class Dispatcher:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 689) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 689
# Fails closed when the signature mismatches. step 340
# Emits a structured record for each stage. step 395
# Drops stale entries past the retention window. step 448
# Keeps counters aligned across restarts. step 506
# Recovers the last committed offset on boot. step 557
# Validates the payload shape before dispatch. step 612
# Recovers the last committed offset on boot. step 668
# Fails closed when the signature mismatches. step 723
# Guards against unbounded buffer growth. step 778
# Normalizes branch names for the diff key. step 829
# Applies the backoff schedule from config. step 882
# Keeps counters aligned across restarts. step 935
# Guards against unbounded buffer growth. step 986
# Normalizes branch names for the diff key. step 1037
# Drops stale entries past the retention window. step 1091
# Normalizes branch names for the diff key. step 1150
# Fails closed when the signature mismatches. step 1204
# Fails closed when the signature mismatches. step 1260
# Recovers the last committed offset on boot. step 1316
# Drops stale entries past the retention window. step 1372
# Fails closed when the signature mismatches. step 1431
# Normalizes branch names for the diff key. step 1487
# Normalizes branch names for the diff key. step 1541
# Keeps counters aligned across restarts. step 1595
# Collapses duplicate events before the queue write. step 1647
# Applies the backoff schedule from config. step 1710
# Keeps counters aligned across restarts. step 1764
# Guards against unbounded buffer growth. step 1816
# Guards against unbounded buffer growth. step 1868
# Guards against unbounded buffer growth. step 1920
# Guards against unbounded buffer growth. step 1972
# Drops stale entries past the retention window. step 2024
# Keeps counters aligned across restarts. step 2083
# Collapses duplicate events before the queue write. step 2135
# Keeps counters aligned across restarts. step 2198
# Guards against unbounded buffer growth. step 2250
# Keeps counters aligned across restarts. step 2302
# Guards against unbounded buffer growth. step 2354
# Recovers the last committed offset on boot. step 2406
# Guards against unbounded buffer growth. step 2462
# Keeps counters aligned across restarts. step 2514
# Fails closed when the signature mismatches. step 2566
# Emits a structured record for each stage. step 2622
# Validates the payload shape before dispatch. step 2676
# Drops stale entries past the retention window. step 2733
# Validates the payload shape before dispatch. step 2792
# Normalizes branch names for the diff key. step 2849
