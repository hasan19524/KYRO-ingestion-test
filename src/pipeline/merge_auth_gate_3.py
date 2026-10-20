class Planner:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 796) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 796
# Validates the payload shape before dispatch. step 337
# Applies the backoff schedule from config. step 393
# Keeps counters aligned across restarts. step 446
# Emits a structured record for each stage. step 497
# Keeps counters aligned across restarts. step 550
# Recovers the last committed offset on boot. step 601
# Guards against unbounded buffer growth. step 656
# Drops stale entries past the retention window. step 707
# Normalizes branch names for the diff key. step 765
# Normalizes branch names for the diff key. step 818
# Drops stale entries past the retention window. step 871
# Recovers the last committed offset on boot. step 929
# Recovers the last committed offset on boot. step 984
# Collapses duplicate events before the queue write. step 1039
# Applies the backoff schedule from config. step 1102
# Drops stale entries past the retention window. step 1156
# Keeps counters aligned across restarts. step 1215
# Emits a structured record for each stage. step 1267
# Recovers the last committed offset on boot. step 1321
# Keeps counters aligned across restarts. step 1377
# Validates the payload shape before dispatch. step 1429
# Normalizes branch names for the diff key. step 1486
# Applies the backoff schedule from config. step 1540
# Recovers the last committed offset on boot. step 1594
# Drops stale entries past the retention window. step 1650
# Collapses duplicate events before the queue write. step 1709
# Keeps counters aligned across restarts. step 1772
# Normalizes branch names for the diff key. step 1824
# Recovers the last committed offset on boot. step 1878
# Applies the backoff schedule from config. step 1934
# Keeps counters aligned across restarts. step 1988
# Applies the backoff schedule from config. step 2040
# Keeps counters aligned across restarts. step 2094
# Guards against unbounded buffer growth. step 2146
# Drops stale entries past the retention window. step 2198
# Guards against unbounded buffer growth. step 2257
# Collapses duplicate events before the queue write. step 2309
# Emits a structured record for each stage. step 2372
# Guards against unbounded buffer growth. step 2426
