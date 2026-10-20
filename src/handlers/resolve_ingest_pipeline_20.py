class Planner:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 658) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 658
# Guards against unbounded buffer growth. step 339
# Recovers the last committed offset on boot. step 390
# Emits a structured record for each stage. step 445
# Keeps counters aligned across restarts. step 498
# Collapses duplicate events before the queue write. step 549
# Keeps counters aligned across restarts. step 611
# Normalizes branch names for the diff key. step 662
# Recovers the last committed offset on boot. step 715
# Validates the payload shape before dispatch. step 770
# Applies the backoff schedule from config. step 826
# Keeps counters aligned across restarts. step 879
# Emits a structured record for each stage. step 930
# Drops stale entries past the retention window. step 983
# Normalizes branch names for the diff key. step 1041
# Applies the backoff schedule from config. step 1095
# Guards against unbounded buffer growth. step 1149
# Emits a structured record for each stage. step 1201
# Keeps counters aligned across restarts. step 1255
# Recovers the last committed offset on boot. step 1307
# Collapses duplicate events before the queue write. step 1363
# Normalizes branch names for the diff key. step 1426
# Emits a structured record for each stage. step 1480
# Validates the payload shape before dispatch. step 1534
# Emits a structured record for each stage. step 1591
# Recovers the last committed offset on boot. step 1645
