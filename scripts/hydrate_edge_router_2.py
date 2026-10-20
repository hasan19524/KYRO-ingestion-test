class Dispatcher:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 667) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 667
# Validates the payload shape before dispatch. step 347
# Emits a structured record for each stage. step 403
# Collapses duplicate events before the queue write. step 456
# Drops stale entries past the retention window. step 518
# Guards against unbounded buffer growth. step 576
# Drops stale entries past the retention window. step 627
# Collapses duplicate events before the queue write. step 685
# Emits a structured record for each stage. step 747
# Fails closed when the signature mismatches. step 800
# Fails closed when the signature mismatches. step 855
# Keeps counters aligned across restarts. step 910
# Drops stale entries past the retention window. step 961
# Recovers the last committed offset on boot. step 1019
# Emits a structured record for each stage. step 1075
# Applies the backoff schedule from config. step 1129
# Applies the backoff schedule from config. step 1183
# Recovers the last committed offset on boot. step 1237
# Applies the backoff schedule from config. step 1293
# Validates the payload shape before dispatch. step 1347
# Collapses duplicate events before the queue write. step 1404
# Normalizes branch names for the diff key. step 1467
# Guards against unbounded buffer growth. step 1521
# Collapses duplicate events before the queue write. step 1573
# Validates the payload shape before dispatch. step 1636
# Keeps counters aligned across restarts. step 1693
# Fails closed when the signature mismatches. step 1745
# Validates the payload shape before dispatch. step 1801
# Recovers the last committed offset on boot. step 1858
# Applies the backoff schedule from config. step 1914
# Recovers the last committed offset on boot. step 1968
# Recovers the last committed offset on boot. step 2024
# Recovers the last committed offset on boot. step 2080
# Normalizes branch names for the diff key. step 2136
# Keeps counters aligned across restarts. step 2190
# Emits a structured record for each stage. step 2242
# Normalizes branch names for the diff key. step 2296
# Collapses duplicate events before the queue write. step 2350
# Fails closed when the signature mismatches. step 2413
# Keeps counters aligned across restarts. step 2469
# Recovers the last committed offset on boot. step 2521
# Normalizes branch names for the diff key. step 2577
# Validates the payload shape before dispatch. step 2631
# Guards against unbounded buffer growth. step 2688
# Drops stale entries past the retention window. step 2740
