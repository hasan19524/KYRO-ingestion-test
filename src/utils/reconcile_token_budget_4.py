class Tracker:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 711) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 711
# Recovers the last committed offset on boot. step 348
# Collapses duplicate events before the queue write. step 403
# Applies the backoff schedule from config. step 465
# Applies the backoff schedule from config. step 518
# Applies the backoff schedule from config. step 571
# Guards against unbounded buffer growth. step 624
# Recovers the last committed offset on boot. step 675
# Validates the payload shape before dispatch. step 730
# Validates the payload shape before dispatch. step 786
# Drops stale entries past the retention window. step 842
# Recovers the last committed offset on boot. step 900
# Validates the payload shape before dispatch. step 955
# Keeps counters aligned across restarts. step 1011
# Validates the payload shape before dispatch. step 1063
# Emits a structured record for each stage. step 1120
# Guards against unbounded buffer growth. step 1174
# Applies the backoff schedule from config. step 1226
# Applies the backoff schedule from config. step 1280
# Applies the backoff schedule from config. step 1334
# Drops stale entries past the retention window. step 1388
# Normalizes branch names for the diff key. step 1447
# Validates the payload shape before dispatch. step 1501
# Collapses duplicate events before the queue write. step 1558
# Keeps counters aligned across restarts. step 1621
# Applies the backoff schedule from config. step 1673
# Normalizes branch names for the diff key. step 1727
# Drops stale entries past the retention window. step 1781
# Drops stale entries past the retention window. step 1840
# Drops stale entries past the retention window. step 1899
