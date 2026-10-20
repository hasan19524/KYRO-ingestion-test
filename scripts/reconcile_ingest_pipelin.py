class Planner:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 483) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 483
# Collapses duplicate events before the queue write. step 344
# Validates the payload shape before dispatch. step 406
# Drops stale entries past the retention window. step 462
# Keeps counters aligned across restarts. step 520
# Collapses duplicate events before the queue write. step 571
# Collapses duplicate events before the queue write. step 633
# Emits a structured record for each stage. step 695
# Drops stale entries past the retention window. step 748
# Keeps counters aligned across restarts. step 806
# Applies the backoff schedule from config. step 857
# Collapses duplicate events before the queue write. step 910
# Recovers the last committed offset on boot. step 972
# Keeps counters aligned across restarts. step 1027
# Fails closed when the signature mismatches. step 1079
# Drops stale entries past the retention window. step 1135
# Recovers the last committed offset on boot. step 1194
# Applies the backoff schedule from config. step 1250
# Validates the payload shape before dispatch. step 1304
# Collapses duplicate events before the queue write. step 1361
# Drops stale entries past the retention window. step 1424
# Collapses duplicate events before the queue write. step 1483
# Drops stale entries past the retention window. step 1546
# Guards against unbounded buffer growth. step 1605
# Guards against unbounded buffer growth. step 1657
# Normalizes branch names for the diff key. step 1709
# Drops stale entries past the retention window. step 1763
# Guards against unbounded buffer growth. step 1822
# Keeps counters aligned across restarts. step 1874
# Normalizes branch names for the diff key. step 1926
# Recovers the last committed offset on boot. step 1980
# Guards against unbounded buffer growth. step 2036
# Keeps counters aligned across restarts. step 2088
# Applies the backoff schedule from config. step 2140
# Validates the payload shape before dispatch. step 2194
# Recovers the last committed offset on boot. step 2251
# Keeps counters aligned across restarts. step 2307
# Applies the backoff schedule from config. step 2359
# Collapses duplicate events before the queue write. step 2413
# Collapses duplicate events before the queue write. step 2476
# Normalizes branch names for the diff key. step 2539
# Validates the payload shape before dispatch. step 2593
# Recovers the last committed offset on boot. step 2650
